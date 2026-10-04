from datetime import datetime, timezone

from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import Session
from app.core.time import utc_now
from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult

from app.schemas.global_batch import (
    CityCheckpointListResponse,
    CityCheckpointResponse,
    GlobalBatchDetail,
    GlobalBatchProgressEvent,
    GlobalBatchResponse,
    GlobalCityProgress,
    GlobalCityResultResponse,
    LeaseState,
)
from app.services.checkpoints import load_resume_state

from app.services.job_state import assert_batch_transition, derive_batch_status

from collections import defaultdict
import hashlib
import json

TERMINAL_CITY_STATUSES = {
    "completed",
    "failed",
    "cancelled",
}

def derive_lease_state(
    owner: str | None,
    expires_at: datetime | None,
    now: datetime | None = None,
) -> LeaseState:
    if owner is None or expires_at is None:
        return "none"
    now = now or utc_now()
    return "live" if expires_at > now else "expired"


def load_checkpoint_months(session: Session, batch_id: str) -> dict[str, list[int]]:
    """city_result_id -> sorted months with a durable checkpoint. Months only;
    payloads are never loaded here."""
    rows = session.execute(
        select(GlobalCityCheckpoint.city_result_id, GlobalCityCheckpoint.month)
        .join(GlobalCityResult, GlobalCityResult.id == GlobalCityCheckpoint.city_result_id)
        .where(GlobalCityResult.batch_id == batch_id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()
    months: dict[str, list[int]] = defaultdict(list)
    for city_result_id, month in rows:
        months[city_result_id].append(month)
    return dict(months)

def city_result_to_response(
    result: GlobalCityResult,
    *,
    checkpoint_months: list[int] | None = None,
    now: datetime | None = None,
) -> GlobalCityResultResponse:
    analytics = result.analytics_json or {}
    return GlobalCityResultResponse(
        id=result.id,
        batch_id=result.batch_id,
        celery_task_id=result.celery_task_id,
        city_id=result.city_id,
        city_name=result.city_name,
        country=result.country,
        latitude=result.latitude,
        longitude=result.longitude,
        status=result.status,
        stage=result.stage,
        progress=result.progress,
        climate_adaptation_rate_percent=(
            result.climate_adaptation_rate_percent
        ),
        exposure_coverage_percent=(
            result.exposure_coverage_percent
        ),
        annual_average_skin_improvement_c=(
            result.annual_average_skin_improvement_c
        ),
        annual_average_core_improvement_c=(
            result.annual_average_core_improvement_c
        ),
        maximum_skin_improvement_c=(
            result.maximum_skin_improvement_c
        ),
        effective_cooling_hours=(
            result.effective_cooling_hours
        ),
        sampled_day_count=result.sampled_day_count,
        eligible_sample_count=(
            result.eligible_sample_count
        ),
        evaluated_weighted_days=(
            result.evaluated_weighted_days
        ),
        beneficial_weighted_days=(
            result.beneficial_weighted_days
        ),
        completed_month_count=(
            result.completed_month_count
        ),
        last_checkpoint_month=(
            result.last_checkpoint_month
        ),
        resumed_from_checkpoint=(
            result.resumed_from_checkpoint
        ),
        last_heartbeat_at=(
            result.last_heartbeat_at
        ),
        skin_improvement_p50_c=(
            result.skin_improvement_p50_c
        ),
        skin_improvement_p90_c=(
            result.skin_improvement_p90_c
        ),
        skin_improvement_p95_c=(
            result.skin_improvement_p95_c
        ),
        core_improvement_p50_c=(
            result.core_improvement_p50_c
        ),
        core_improvement_p90_c=(
            result.core_improvement_p90_c
        ),
        core_improvement_p95_c=(
            result.core_improvement_p95_c
        ),
        heatwave_event_count=(
            result.heatwave_event_count
        ),
        longest_heatwave_days=(
            result.longest_heatwave_days
        ),
        heatwave_events=(
            (
                result.analytics_json or {}
            ).get(
                "heatwave_events"
            )
        ),
        retry_count=result.retry_count,
        monthly_results=result.monthly_json,
        error_message=result.error_message,
        started_at=result.started_at,
        completed_at=result.completed_at,
        data_quality=analytics.get("data_quality"),
        metric_definitions=analytics.get("metric_definitions"),
        # Stage 8
        lease_owner=getattr(result, "lease_owner", None),
        lease_expires_at=getattr(result, "lease_expires_at", None),
        lease_state=derive_lease_state(
            getattr(result, "lease_owner", None),
            getattr(result, "lease_expires_at", None),
            now,
        ),
        checkpoint_months=list(checkpoint_months or []),
    )


def batch_to_response(batch: GlobalBatchJob) -> GlobalBatchResponse:
    return GlobalBatchResponse(
        id=batch.id,
        celery_group_id=batch.celery_group_id,
        status=batch.status,
        stage=batch.stage,
        progress=batch.progress,
        total_city_count=batch.total_city_count,
        completed_city_count=(
            batch.completed_city_count
        ),
        failed_city_count=batch.failed_city_count,
        cancelled_city_count=(
            batch.cancelled_city_count
        ),
        summary=batch.summary_json,
        error_message=batch.error_message,
        created_at=batch.created_at,
        updated_at=batch.updated_at,
        started_at=batch.started_at,
        completed_at=batch.completed_at,
        control_material_version_id=getattr(batch, "control_material_version_id", None),
        rc_material_version_id=getattr(batch, "rc_material_version_id", None),
        # Stage 8
        attempt=getattr(batch, "attempt", 0) or 0,
        lease_owner=getattr(batch, "lease_owner", None),
        lease_expires_at=getattr(batch, "lease_expires_at", None),
        last_heartbeat_at=getattr(batch, "last_heartbeat_at", None),
        cancel_requested_at=getattr(batch, "cancel_requested_at", None),
    )


def batch_to_detail(
    batch: GlobalBatchJob,
    *,
    checkpoint_months: dict[str, list[int]] | None = None,
) -> GlobalBatchDetail:
    now = utc_now()
    months = checkpoint_months or {}
    return GlobalBatchDetail(
        **batch_to_response(batch).model_dump(),
        request=batch.request_json,
        city_results=[
            city_result_to_response(item, checkpoint_months=months.get(item.id), now=now)
            for item in batch.city_results
        ],
    )

def batch_progress_event(
    batch: GlobalBatchJob,
    checkpoint_months: dict[str, list[int]] | None = None,
) -> GlobalBatchProgressEvent:
    now = utc_now()
    months = checkpoint_months or {}
    return GlobalBatchProgressEvent(
        batch=batch_to_response(batch),
        cities=[
            GlobalCityProgress(
                id=item.id,
                city_id=item.city_id,
                status=item.status,
                stage=item.stage,
                progress=item.progress,
                retry_count=item.retry_count,
                completed_month_count=item.completed_month_count,
                last_checkpoint_month=item.last_checkpoint_month,
                last_heartbeat_at=item.last_heartbeat_at,
                lease_owner=getattr(item, "lease_owner", None),
                lease_expires_at=getattr(item, "lease_expires_at", None),
                lease_state=derive_lease_state(
                    getattr(item, "lease_owner", None),
                    getattr(item, "lease_expires_at", None),
                    now,
                ),
                checkpoint_months=list(months.get(item.id, [])),
                error_message=item.error_message,
            )
            for item in batch.city_results
        ],
    )

def _payload_sha256(payload: dict) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def city_checkpoints_to_response(
    session: Session,
    *,
    batch: GlobalBatchJob,
    city_result: GlobalCityResult,
) -> CityCheckpointListResponse:
    request = batch.request_json or {}
    start_month = int(request.get("start_month", 1))
    end_month = int(request.get("end_month", 12))

    rows = session.scalars(
        select(GlobalCityCheckpoint)
        .where(GlobalCityCheckpoint.city_result_id == city_result.id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()

    resume_from_month, _ = load_resume_state(
        session, city_result.id, start_month=start_month
    )

    return CityCheckpointListResponse(
        batch_id=batch.id,
        city_result_id=city_result.id,
        city_id=city_result.city_id,
        start_month=start_month,
        end_month=end_month,
        resume_from_month=resume_from_month,
        items=[
            CityCheckpointResponse(
                id=row.id,
                month=row.month,
                attempt=row.attempt,
                created_at=row.created_at,
                payload_sha256=_payload_sha256(row.payload_json),
                sampled_day_count=int((row.payload_json or {}).get("sampled_day_count", 0)),
                skipped_sample_count=len((row.payload_json or {}).get("skipped_samples", [])),
            )
            for row in rows
        ],
    )
    
    
def refresh_batch_status(
    session: Session,
    batch_id: str,
) -> None:
    batch = session.scalar(
        select(GlobalBatchJob)
        .where(GlobalBatchJob.id == batch_id)
        .with_for_update()
    )

    if batch is None:
        return

    status_counts = dict(
        session.execute(
            select(
                GlobalCityResult.status,
                func.count(GlobalCityResult.id),
            )
            .where(
                GlobalCityResult.batch_id == batch_id
            )
            .group_by(GlobalCityResult.status)
        ).all()
    )

    completed = status_counts.get(
        "completed",
        0,
    )
    failed = status_counts.get(
        "failed",
        0,
    )
    cancelled = status_counts.get(
        "cancelled",
        0,
    )
    running = status_counts.get(
        "running",
        0,
    )

    processed = (
        completed
        + failed
        + cancelled
    )

    batch.completed_city_count = completed
    batch.failed_city_count = failed
    batch.cancelled_city_count = cancelled

    if batch.total_city_count > 0:
        batch.progress = round(
            processed
            / batch.total_city_count
            * 100
        )

    if running > 0 and batch.status == "queued":
        batch.status = "running"
        batch.stage = "analyzing_cities"
        batch.started_at = datetime.now(
            timezone.utc
        )

    if processed < batch.total_city_count:
        session.commit()
        return

    batch.progress = 100
    batch.completed_at = datetime.now(
        timezone.utc
    )

    if cancelled == batch.total_city_count:
        batch.status = "cancelled"
        batch.stage = "cancelled"

    elif completed == 0:
        batch.status = "failed"
        batch.stage = "failed"

    elif failed > 0 or cancelled > 0:
        batch.status = "partial_completed"
        batch.stage = "partial_completed"

    else:
        batch.status = "completed"
        batch.stage = "completed"

    completed_results = session.scalars(
        select(GlobalCityResult).where(
            GlobalCityResult.batch_id == batch_id,
            GlobalCityResult.status == "completed",
        )
    ).all()

    if completed_results:
        rates = [
            item.climate_adaptation_rate_percent
            for item in completed_results
            if (
                item.climate_adaptation_rate_percent
                is not None
            )
        ]

        skin_values = [
            item.annual_average_skin_improvement_c
            for item in completed_results
            if (
                item.annual_average_skin_improvement_c
                is not None
            )
        ]

        coverage_values = [
            item.exposure_coverage_percent
            for item in completed_results
            if item.exposure_coverage_percent is not None
        ]
        
        batch.summary_json = {
            "completed_city_count": len(
                completed_results
            ),
            "mean_climate_adaptation_rate_percent": (
                round(
                    sum(rates) / len(rates),
                    4,
                )
                if rates
                else None
            ),
            "mean_exposure_coverage_percent": (
                round(
                    sum(coverage_values)
                    / len(coverage_values),
                    4,
                )
                if coverage_values
                else None
            ),
            "mean_annual_skin_improvement_c": (
                round(
                    sum(skin_values)
                    / len(skin_values),
                    4,
                )
                if skin_values
                else None
            ),
        }

    session.commit()

def reconcile_batch(db: Session, batch_id: str) -> None:
    counts = dict(
        db.execute(
            select(GlobalCityResult.status, func.count())
            .where(GlobalCityResult.batch_id == batch_id)
            .group_by(GlobalCityResult.status)
        ).all()
    )
    batch = db.get(GlobalBatchJob, batch_id)
    batch.completed_city_count = counts.get("completed", 0)
    batch.failed_city_count = counts.get("failed", 0)
    batch.cancelled_city_count = counts.get("cancelled", 0)
    done = sum(counts.get(s, 0) for s in ("completed", "failed", "cancelled"))
    batch.progress = int(100 * done / max(batch.total_city_count, 1))

    target = derive_batch_status(counts, batch.total_city_count, batch.cancel_requested_at is not None)
    if target and batch.status != target:
        assert_batch_transition(batch.status, target)
        batch.status = target
        batch.completed_at = func.now()
    db.commit()