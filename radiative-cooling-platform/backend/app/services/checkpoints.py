"""Durable monthly checkpoints with provenance (Stage 9).

A checkpoint row is only trusted when it was produced by the same model
version, the same parameter fingerprint and the same physics-relevant request
as the batch being resumed. Anything else is reported in ``discarded`` and
recomputed. Rows written before Stage 9 carry NULL provenance and are never
resumed from.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from app.models.global_batch import GlobalCityCheckpoint, GlobalCityResult
from app.schemas.global_batch import GlobalBatchCreate
from app.services.reproducibility import canonical_json, parameter_fingerprint
from app.services.two_node import MODEL_VERSION


# Fields that do not change the per-city physics and must not invalidate a
# checkpoint when a batch is retried.
REQUEST_HASH_EXCLUDED_FIELDS = frozenset(
    {"name", "city_ids", "execution_profile", "resume_from_checkpoint"}
)


def request_sha256(request: GlobalBatchCreate) -> str:
    payload = request.model_dump(mode="json", exclude=set(REQUEST_HASH_EXCLUDED_FIELDS))
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CheckpointProvenance:
    model_version: str
    parameter_fingerprint: str
    request_sha256: str

    @classmethod
    def for_request(cls, request: GlobalBatchCreate) -> "CheckpointProvenance":
        return cls(
            model_version=MODEL_VERSION,
            parameter_fingerprint=parameter_fingerprint(request.environment_assumptions),
            request_sha256=request_sha256(request),
        )

    def mismatch_reason(self, row: GlobalCityCheckpoint) -> str | None:
        if row.model_version is None or row.parameter_fingerprint is None or row.request_sha256 is None:
            return "legacy checkpoint without provenance (written before Stage 9)"
        if row.model_version != self.model_version:
            return f"model_version {row.model_version} != {self.model_version}"
        if row.parameter_fingerprint != self.parameter_fingerprint:
            return "parameter_fingerprint differs"
        if row.request_sha256 != self.request_sha256:
            return "request parameters differ"
        return None


@dataclass
class ResumeState:
    next_month: int
    payloads: list[dict] = field(default_factory=list)
    discarded: list[dict] = field(default_factory=list)  # {"month": int, "reason": str}


def upsert_month_checkpoint(
    session: Session,
    *,
    city_result_id: str,
    owner: str,
    month: int,
    attempt: int,
    payload: dict,
    provenance: CheckpointProvenance,
) -> bool:
    """Stage the checkpoint row in the current transaction.

    Returns False (and stages nothing) when ``owner`` does not hold the city
    lease. The caller must commit via ``heartbeat_city_lease`` in the same
    session so that row and heartbeat land (or roll back) together.
    """
    owns = session.scalar(
        select(GlobalCityResult.id).where(
            GlobalCityResult.id == city_result_id,
            GlobalCityResult.lease_owner == owner,
        )
    )
    if owns is None:
        return False

    values = {
        "city_result_id": city_result_id,
        "month": month,
        "attempt": attempt,
        "payload_json": payload,
        "model_version": provenance.model_version,
        "parameter_fingerprint": provenance.parameter_fingerprint,
        "request_sha256": provenance.request_sha256,
    }
    session.execute(
        pg_insert(GlobalCityCheckpoint)
        .values(**values)
        .on_conflict_do_update(
            constraint="uq_global_city_checkpoint_month",
            set_={k: v for k, v in values.items() if k not in ("city_result_id", "month")},
        )
    )
    return True


def load_resume_state(
    session: Session,
    city_result_id: str,
    *,
    start_month: int,
    provenance: CheckpointProvenance,
) -> ResumeState:
    """Trusted contiguous prefix of checkpoints starting at ``start_month``.

    The prefix ends at the first hole or provenance mismatch. Every row after
    that is discarded; each one reports its *own* reason (provenance first,
    then contiguity) so the operator sees why a month was recomputed instead
    of a cascade of "hole" messages.
    """
    rows = session.scalars(
        select(GlobalCityCheckpoint)
        .where(GlobalCityCheckpoint.city_result_id == city_result_id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()

    state = ResumeState(next_month=start_month)
    prefix_open = True

    for row in rows:
        if row.month < start_month:
            state.discarded.append({"month": row.month, "reason": "outside requested range"})
            continue

        reason = provenance.mismatch_reason(row)
        if reason is not None:
            state.discarded.append({"month": row.month, "reason": reason})
            prefix_open = False
            continue

        if not prefix_open or row.month > state.next_month:
            state.discarded.append({
                "month": row.month,
                "reason": f"not contiguous with the resumable prefix (resume restarts at month {state.next_month})",
            })
            prefix_open = False
            continue

        state.payloads.append(row.payload_json)
        state.next_month += 1

    return state