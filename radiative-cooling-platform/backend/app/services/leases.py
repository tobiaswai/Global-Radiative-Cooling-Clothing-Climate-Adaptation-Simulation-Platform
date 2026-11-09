"""Row-level leases for GlobalCityResult (Stage 7) and SimulationJob (Stage 9).

Contract
--------
* ``acquire_*`` is one atomic UPDATE ... RETURNING. A caller that gets False
  must exit without writing anything: another worker owns the row, or the row
  is terminal.
* ``heartbeat_*`` is the only way a worker writes to its row. It is guarded by
  ``lease_owner == owner``; when the guard fails the whole transaction is
  rolled back (so anything staged in the same session, e.g. a checkpoint
  upsert, is discarded too) and False is returned.
* All time comparisons use the database clock (``func.now()``) so that the
  API, the workers and the reaper agree regardless of host clock drift.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

from sqlalchemy import func, or_, select, update
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.time import utc_now
from app.models.global_batch import GlobalCityResult
from app.models.simulation_job import SimulationJob
from app.services.job_state import CityStatus, JobStatus


LeaseState = str  # "none" | "live" | "expired"


def db_now(session: Session) -> datetime:
    """Database clock; the reference for every lease comparison."""
    return session.scalar(select(func.now()))


def derive_lease_state(
    owner: str | None,
    expires_at: datetime | None,
    now: datetime | None = None,
) -> LeaseState:
    if owner is None or expires_at is None:
        return "none"
    now = now or utc_now()
    return "live" if expires_at > now else "expired"


def _ttl() -> timedelta:
    return timedelta(seconds=settings.CITY_LEASE_TTL_SECONDS)


def _acquire(
    session: Session,
    model: Any,
    row_id: str,
    owner: str,
    active_statuses: tuple[str, ...],
    running_status: str,
) -> bool:
    stmt = (
        update(model)
        .where(
            model.id == row_id,
            model.status.in_(active_statuses),
            or_(
                model.lease_owner.is_(None),
                model.lease_expires_at < func.now(),
                model.lease_owner == owner,  # re-entrant for the same owner
            ),
        )
        .values(
            lease_owner=owner,
            lease_expires_at=func.now() + _ttl(),
            last_heartbeat_at=func.now(),
            status=running_status,
            started_at=func.coalesce(model.started_at, func.now()),
        )
        .returning(model.id)
    )
    got = session.execute(stmt).scalar_one_or_none()
    session.commit()
    return got is not None


def _heartbeat(session: Session, model: Any, row_id: str, owner: str, values: dict[str, Any]) -> bool:
    payload: dict[str, Any] = {
        "last_heartbeat_at": func.now(),
        "lease_expires_at": func.now() + _ttl(),
    }
    payload.update(values)  # caller values win

    result = session.execute(
        update(model)
        .where(model.id == row_id, model.lease_owner == owner)
        .values(**payload)
    )

    if result.rowcount == 1:
        session.commit()
        return True

    # Lease lost: discard everything staged in this transaction.
    session.rollback()
    return False


def _release(session: Session, model: Any, row_id: str, owner: str) -> None:
    session.execute(
        update(model)
        .where(model.id == row_id, model.lease_owner == owner)
        .values(lease_owner=None, lease_expires_at=None)
    )
    session.commit()


# --- cities -----------------------------------------------------------------

def acquire_city_lease(session: Session, city_result_id: str, owner: str) -> bool:
    return _acquire(
        session, GlobalCityResult, city_result_id, owner,
        (CityStatus.QUEUED, CityStatus.RUNNING), CityStatus.RUNNING,
    )


def heartbeat_city_lease(session: Session, city_result_id: str, owner: str, **values: Any) -> bool:
    return _heartbeat(session, GlobalCityResult, city_result_id, owner, values)


def release_city_lease(session: Session, city_result_id: str, owner: str) -> None:
    _release(session, GlobalCityResult, city_result_id, owner)


# --- single simulation jobs -------------------------------------------------

def acquire_job_lease(session: Session, job_id: str, owner: str) -> bool:
    return _acquire(
        session, SimulationJob, job_id, owner,
        (JobStatus.QUEUED, JobStatus.RUNNING), JobStatus.RUNNING,
    )


def heartbeat_job_lease(session: Session, job_id: str, owner: str, **values: Any) -> bool:
    return _heartbeat(session, SimulationJob, job_id, owner, values)


def release_job_lease(session: Session, job_id: str, owner: str) -> None:
    _release(session, SimulationJob, job_id, owner)