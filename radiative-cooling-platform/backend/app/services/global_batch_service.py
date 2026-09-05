from datetime import datetime, timezone

from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import Session

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    GlobalBatchDetail,
    GlobalBatchResponse,
    GlobalCityResultResponse,
)


TERMINAL_CITY_STATUSES = {
    "completed",
    "failed",
    "cancelled",
}


def city_result_to_response(
    result: GlobalCityResult,
) -> GlobalCityResultResponse:
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
        retry_count=result.retry_count,
        monthly_results=result.monthly_json,
        error_message=result.error_message,
        started_at=result.started_at,
        completed_at=result.completed_at,
    )


def batch_to_response(
    batch: GlobalBatchJob,
) -> GlobalBatchResponse:
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
    )


def batch_to_detail(
    batch: GlobalBatchJob,
) -> GlobalBatchDetail:
    return GlobalBatchDetail(
        **batch_to_response(batch).model_dump(),
        request=batch.request_json,
        city_results=[
            city_result_to_response(item)
            for item in batch.city_results
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

