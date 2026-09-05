from datetime import datetime, timezone

from celery import group
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
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
from app.services.global_batch_service import (
    batch_to_detail,
    batch_to_response,
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

    features = []

    for result in batch.city_results:
        if result.status != "completed":
            continue

        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        result.longitude,
                        result.latitude,
                    ],
                },
                "properties": {
                    "city_id": result.city_id,
                    "city_name": result.city_name,
                    "country": result.country,
                    "status": result.status,
                    "climate_adaptation_rate_percent": (
                        result
                        .climate_adaptation_rate_percent
                    ),
                    "annual_average_skin_improvement_c": (
                        result
                        .annual_average_skin_improvement_c
                    ),
                    "annual_average_core_improvement_c": (
                        result
                        .annual_average_core_improvement_c
                    ),
                    "maximum_skin_improvement_c": (
                        result
                        .maximum_skin_improvement_c
                    ),
                    "effective_cooling_hours": (
                        result
                        .effective_cooling_hours
                    ),
                },
            }
        )

    return {
        "type": "FeatureCollection",
        "metadata": {
            "batch_id": batch.id,
            "status": batch.status,
            "year": batch.request_json.get(
                "year"
            ),
            "method": (
                "monthly_representative_day"
            ),
        },
        "features": features,
    }