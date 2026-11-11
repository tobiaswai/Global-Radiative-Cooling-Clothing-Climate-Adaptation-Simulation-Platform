"""Operational health (Stage 8). Read-only; safe to poll every few seconds."""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.time import utc_now
from app.db.session import get_db
from app.models.global_batch import GlobalBatchJob, GlobalCityResult
from app.schemas.ops import LeaseSummary, OpsStatusResponse, WorkerStatus
from app.worker.celery_app import celery_app


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/ops", tags=["ops"])

INSPECT_TIMEOUT_SECONDS = 1.0


def inspect_workers(timeout: float = INSPECT_TIMEOUT_SECONDS) -> tuple[bool, list[WorkerStatus]]:
    """Ping Celery workers. Broker failures are reported, never raised."""
    try:
        inspector = celery_app.control.inspect(timeout=timeout)
        pong = inspector.ping() or {}
        active = inspector.active() or {}
        reserved = inspector.reserved() or {}
    except Exception as error:  # noqa: BLE001 - kombu raises many transport-specific types
        logger.warning("Celery inspect failed: %s", error)
        return False, []

    workers = [
        WorkerStatus(
            name=name,
            active_task_count=len(active.get(name, []) or []),
            reserved_task_count=len(reserved.get(name, []) or []),
        )
        for name in sorted(pong)
    ]
    return True, workers


def summarize_leases(session: Session) -> LeaseSummary:
    now = utc_now()

    city_counts = dict(
        session.execute(
            select(GlobalCityResult.status, func.count())
            .group_by(GlobalCityResult.status)
        ).all()
    )

    live = session.scalar(
        select(func.count()).select_from(GlobalCityResult).where(
            GlobalCityResult.lease_owner.is_not(None),
            GlobalCityResult.lease_expires_at > now,
        )
    ) or 0

    expired = session.scalar(
        select(func.count()).select_from(GlobalCityResult).where(
            GlobalCityResult.status == "running",
            GlobalCityResult.lease_expires_at.is_not(None),
            GlobalCityResult.lease_expires_at <= now,
        )
    ) or 0

    batch_counts = dict(
        session.execute(
            select(GlobalBatchJob.status, func.count()).group_by(GlobalBatchJob.status)
        ).all()
    )

    return LeaseSummary(
        running_cities=city_counts.get("running", 0),
        queued_cities=city_counts.get("queued", 0),
        live_leases=live,
        expired_leases=expired,
        running_batches=batch_counts.get("running", 0),
        cancelling_batches=batch_counts.get("cancelling", 0),
    )


@router.get("/status", response_model=OpsStatusResponse)
def ops_status(session: Session = Depends(get_db)) -> OpsStatusResponse:
    broker_reachable, workers = inspect_workers()

    return OpsStatusResponse(
        checked_at=utc_now(),
        broker_reachable=broker_reachable,
        worker_count=len(workers),
        workers=workers,
        leases=summarize_leases(session),
        lease_ttl_seconds=settings.CITY_LEASE_TTL_SECONDS,
        heartbeat_interval_seconds=settings.CITY_HEARTBEAT_SECONDS,
        reaper_interval_seconds=settings.LEASE_REAPER_INTERVAL_SECONDS,
        worst_case_recovery_seconds=(
            settings.CITY_LEASE_TTL_SECONDS + settings.LEASE_REAPER_INTERVAL_SECONDS
        ),
    )