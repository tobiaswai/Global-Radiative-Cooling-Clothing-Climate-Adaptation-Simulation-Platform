from datetime import datetime, timezone

from celery import group
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from requests import session
from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.core.cities import (
    get_city,
    list_cities,
)
from app.db.session import get_db
from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    GlobalBatchCreate,
    GlobalBatchDetail,
    GlobalBatchListResponse,
    GlobalBatchResponse,
)
from fastapi.responses import Response

from app.services.global_batch_export import (
    build_batch_export_zip,
    build_batch_geojson,
)
from app.services.global_batch_service import (
    batch_to_detail,
    batch_to_response,
    refresh_batch_status,
)
from app.worker.celery_app import celery_app
from app.worker.tasks import (
    run_global_city_analysis_task,
)


router = APIRouter(
    prefix="/api/v1/global-batches",
    tags=["global-batches"],
)


def load_batch(
    session: Session,
    batch_id: str,
) -> GlobalBatchJob | None:
    return session.scalar(
        select(GlobalBatchJob)
        .options(
            selectinload(
                GlobalBatchJob.city_results
            )
        )
        .where(
            GlobalBatchJob.id == batch_id
        )
    )


@router.get("/cities")
def get_supported_cities() -> dict:
    return {
        "items": [
            {
                "id": city.id,
                "name": city.name,
                "country": city.country,
                "latitude": city.latitude,
                "longitude": city.longitude,
                "elevation_m": city.elevation_m,
                "timezone": city.timezone,
                "climate_type": (
                    city.climate_type
                ),
            }
            for city in list_cities()
        ]
    }


@router.post(
    "",
    response_model=GlobalBatchResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def create_global_batch(
    request: GlobalBatchCreate,
    session: Session = Depends(get_db),
) -> GlobalBatchResponse:
    cities = []

    for city_id in request.city_ids:
        try:
            cities.append(
                get_city(city_id)
            )
        except ValueError as error:
            raise HTTPException(
                status_code=422,
                detail=str(error),
            ) from error

    batch = GlobalBatchJob(
        status="queued",
        stage="creating_city_tasks",
        progress=0,
        total_city_count=len(cities),
        request_json=request.model_dump(
            mode="json"
        ),
    )

    session.add(batch)
    session.flush()

    city_results = []

    for city in cities:
        city_result = GlobalCityResult(
            batch_id=batch.id,
            city_id=city.id,
            city_name=city.name,
            country=city.country,
            latitude=city.latitude,
            longitude=city.longitude,
            status="queued",
            stage="queued",
            progress=0,
        )

        session.add(city_result)
        city_results.append(city_result)

    session.commit()

    try:
        celery_group = group(
            run_global_city_analysis_task.s(
                result.id
            )
            for result in city_results
        )

        group_result = celery_group.apply_async()

        batch.celery_group_id = group_result.id
        batch.stage = "queued"

        for city_result, async_result in zip(
            city_results,
            group_result.results,
            strict=True,
        ):
            city_result.celery_task_id = (
                async_result.id
            )

        session.commit()
        session.refresh(batch)

    except Exception as error:
        batch.status = "failed"
        batch.stage = "queue_submission_failed"
        batch.error_message = str(error)[:4000]
        batch.completed_at = datetime.now(
            timezone.utc
        )

        for result in city_results:
            result.status = "failed"
            result.stage = (
                "queue_submission_failed"
            )
            result.error_message = str(
                error
            )[:4000]

        session.commit()

        raise HTTPException(
            status_code=503,
            detail=(
                "Unable to submit global batch "
                f"to Celery: {error}"
            ),
        ) from error

    return batch_to_response(batch)


@router.get(
    "",
    response_model=GlobalBatchListResponse,
)
def list_global_batches(
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
    offset: int = Query(
        default=0,
        ge=0,
    ),
    session: Session = Depends(get_db),
) -> GlobalBatchListResponse:
    total = session.scalar(
        select(func.count())
        .select_from(GlobalBatchJob)
    ) or 0

    batches = session.scalars(
        select(GlobalBatchJob)
        .order_by(
            GlobalBatchJob.created_at.desc()
        )
        .offset(offset)
        .limit(limit)
    ).all()

    return GlobalBatchListResponse(
        items=[
            batch_to_response(batch)
            for batch in batches
        ],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{batch_id}",
    response_model=GlobalBatchDetail,
)
def get_global_batch(
    batch_id: str,
    session: Session = Depends(get_db),
) -> GlobalBatchDetail:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=404,
            detail="Global batch not found",
        )

    return batch_to_detail(batch)


@router.post(
    "/{batch_id}/cancel",
    response_model=GlobalBatchResponse,
)
def cancel_global_batch(
    batch_id: str,
    session: Session = Depends(get_db),
) -> GlobalBatchResponse:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=404,
            detail="Global batch not found",
        )

    if batch.status in {
        "completed",
        "partial_completed",
        "failed",
        "cancelled",
    }:
        raise HTTPException(
            status_code=409,
            detail=(
                "Batch in terminal state "
                "cannot be cancelled"
            ),
        )

    batch.status = "cancelling"
    batch.stage = (
        "waiting_for_cooperative_cancel"
    )

    for result in batch.city_results:
        if result.status == "queued":
            result.status = "cancelled"
            result.stage = "cancelled"
            result.progress = 100
            result.completed_at = datetime.now(
                timezone.utc
            )

        if (
            result.celery_task_id
            and result.status != "completed"
        ):
            celery_app.control.revoke(
                result.celery_task_id,
                terminate=False,
            )

    session.commit()

    refresh_batch_status(
        session,
        batch.id,
    )

    session.refresh(batch)

    return batch_to_response(batch)


@router.get(
    "/{batch_id}/geojson",
)
def get_global_batch_geojson(
    batch_id: str,
    session: Session = Depends(get_db),
) -> dict:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=404,
            detail="Global batch not found",
        )

    return build_batch_geojson(batch)

@router.get(
    "/{batch_id}/export",
)
def export_global_batch(
    batch_id: str,
    session: Session = Depends(get_db),
) -> Response:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=404,
            detail="Global batch not found",
        )

    export_content = build_batch_export_zip(
        batch
    )

    filename = (
        f"global-climate-adaptation-"
        f"{batch.id}.zip"
    )

    return Response(
        content=export_content,
        media_type="application/zip",
        headers={
            "Content-Disposition": (
                f'attachment; filename="{filename}"'
            ),
        },
    )
    
@router.post(
    "/{batch_id}/retry-failed",
    response_model=GlobalBatchResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def retry_failed_cities(
    batch_id: str,
    session: Session = Depends(get_db),
) -> GlobalBatchResponse:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=404,
            detail="Global batch not found",
        )

    if batch.status not in {
        "failed",
        "partial_completed",
    }:
        raise HTTPException(
            status_code=409,
            detail=(
                "Only failed or partially completed "
                "batches can be retried"
            ),
        )

    failed_results = [
        result
        for result in batch.city_results
        if result.status == "failed"
    ]

    if not failed_results:
        raise HTTPException(
            status_code=409,
            detail=(
                "The batch contains no failed cities"
            ),
        )

    now = datetime.now(
        timezone.utc
    )

    for result in failed_results:
        result.status = "queued"
        result.stage = "queued_for_retry"
        result.progress = 0
        result.retry_count += 1

        result.error_message = None
        result.started_at = None
        result.completed_at = None

        result.climate_adaptation_rate_percent = None
        result.exposure_coverage_percent = None
        result.annual_average_skin_improvement_c = None
        result.annual_average_core_improvement_c = None
        result.maximum_skin_improvement_c = None
        result.effective_cooling_hours = None

        result.sampled_day_count = None
        result.eligible_sample_count = None
        result.evaluated_weighted_days = None
        result.beneficial_weighted_days = None
        result.monthly_json = None

    batch.status = "running"
    batch.stage = "retrying_failed_cities"
    batch.progress = round(
        (
            batch.total_city_count
            - len(failed_results)
        )
        / batch.total_city_count
        * 100
    )

    batch.failed_city_count = 0
    batch.completed_at = None
    batch.error_message = None

    if batch.started_at is None:
        batch.started_at = now

    session.commit()

    try:
        retry_group = group(
            run_global_city_analysis_task.s(
                result.id
            )
            for result in failed_results
        )

        group_result = retry_group.apply_async()

        batch.celery_group_id = group_result.id

        for result, async_result in zip(
            failed_results,
            group_result.results,
            strict=True,
        ):
            result.celery_task_id = (
                async_result.id
            )

        session.commit()
        session.refresh(batch)

    except Exception as error:
        batch.status = "partial_completed"
        batch.stage = "retry_submission_failed"
        batch.error_message = str(
            error
        )[:4000]

        for result in failed_results:
            result.status = "failed"
            result.stage = (
                "retry_submission_failed"
            )
            result.error_message = str(
                error
            )[:4000]
            result.completed_at = now

        session.commit()

        raise HTTPException(
            status_code=503,
            detail=(
                "Unable to submit retry tasks: "
                f"{error}"
            ),
        ) from error

    return batch_to_response(batch)