from fastapi import APIRouter, HTTPException

from app.core.cities import get_city
from app.schemas.simulation import (
    WeatherSimulationRequest,
    WeatherSimulationResponse,
)
from app.services.two_node import (
    simulate_material,
    simulate_material_with_weather,
)
from app.services.weather import (
    get_historical_weather,
)

from app.schemas.simulation import (
    SimulationRequest,
    SimulationResponse,
    SimulationSummary,
)
from app.services.two_node import simulate_material

from app.api.routes import simulation_events
from app.api.routes import simulation_jobs

router = APIRouter(
    prefix="/api/v1/simulations",
    tags=["simulations"],
)


@router.post(
    "/run",
    response_model=SimulationResponse,
)
def run_simulation(
    request: SimulationRequest,
) -> SimulationResponse:
    try:
        control_result = simulate_material(
            duration_minutes=request.duration_minutes,
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            environment=request.environment,
            person=request.person,
            material=request.control_material,
        )

        rc_result = simulate_material(
            duration_minutes=request.duration_minutes,
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            environment=request.environment,
            person=request.person,
            material=request.rc_material,
        )
    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error

    final_skin_improvement = (
        control_result.final_skin_temperature_c
        - rc_result.final_skin_temperature_c
    )

    final_core_improvement = (
        control_result.final_core_temperature_c
        - rc_result.final_core_temperature_c
    )

    control_skin_average = sum(
        point.skin_temperature_c
        for point in control_result.time_series
    ) / len(control_result.time_series)

    rc_skin_average = sum(
        point.skin_temperature_c
        for point in rc_result.time_series
    ) / len(rc_result.time_series)

    return SimulationResponse(
        model_name="RC transient two-node prototype",
        model_version="0.1.0",
        city=request.city,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                final_skin_improvement,
                4,
            ),
            final_core_temperature_improvement_c=round(
                final_core_improvement,
                4,
            ),
            average_skin_temperature_improvement_c=round(
                control_skin_average - rc_skin_average,
                4,
            ),
        ),
        warning=(
                    "These results are from a simplified transient prototype "
                    "and have not yet been validated using thermal dolls, human trials, "
                    "or JOS-3 benchmarks. They are not suitable for medical, occupational safety, "
                    "or product certification purposes."
        ),
    )
    
@router.post(
    "/run-weather",
    response_model=WeatherSimulationResponse,
)
async def run_weather_simulation(
    request: WeatherSimulationRequest,
) -> WeatherSimulationResponse:
    try:
        city = get_city(request.city_id)

        weather = await get_historical_weather(
            city=city,
            start_time_local=(
                request.start_time_local
            ),
            duration_minutes=(
                request.duration_minutes
            ),
        )

        control_result = (
            simulate_material_with_weather(
                duration_minutes=(
                    request.duration_minutes
                ),
                output_interval_minutes=(
                    request.output_interval_minutes
                ),
                weather=weather,
                person=request.person,
                material=request.control_material,
            )
        )

        rc_result = (
            simulate_material_with_weather(
                duration_minutes=(
                    request.duration_minutes
                ),
                output_interval_minutes=(
                    request.output_interval_minutes
                ),
                weather=weather,
                person=request.person,
                material=request.rc_material,
            )
        )
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error
    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error),
        ) from error

    control_average = sum(
        point.skin_temperature_c
        for point in control_result.time_series
    ) / len(control_result.time_series)

    rc_average = sum(
        point.skin_temperature_c
        for point in rc_result.time_series
    ) / len(rc_result.time_series)

    return WeatherSimulationResponse(
        model_name=(
            "Weather-driven transient "
            "two-node prototype"
        ),
        model_version="0.3.0",
        city=city.name,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                control_result
                .final_skin_temperature_c
                - rc_result
                .final_skin_temperature_c,
                4,
            ),
            final_core_temperature_improvement_c=round(
                control_result
                .final_core_temperature_c
                - rc_result
                .final_core_temperature_c,
                4,
            ),
            average_skin_temperature_improvement_c=round(
                control_average - rc_average,
                4,
            ),
        ),
        warning=(
            "These results are from a simplified transient prototype "
            "and have not yet been validated using thermal dolls, human trials, "
            "or JOS-3 benchmarks. They are not suitable for medical, "
            "occupational safety, or product certification purposes."
        ),
        weather=weather,
        environment_model_note=(
            "Air temperature, humidity, wind speed, and shortwave radiation are from ERA5;"
            "the average radiative temperature and effective sky temperature are currently "
            "estimated using empirical formulas."
        ),
    )

import asyncio
import json

import anyio
from fastapi import (
    Depends,
    HTTPException,
    Query,
    Request,
    status,
)
from fastapi.responses import (
    StreamingResponse,
)
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.session import (
    SessionLocal,
    get_db,
)
from app.models.simulation_job import (
    SimulationJob,
)
from app.schemas.job import (
    SimulationJobDetail,
    SimulationJobListResponse,
    SimulationJobResponse,
)
from app.services.job_service import (
    get_job_or_none,
    job_to_detail,
    job_to_response,
)
from app.services.result_storage import (
    load_simulation_result,
)
from app.worker.celery_app import (
    celery_app,
)
from app.worker.tasks import (
    run_weather_simulation_task,
)

@router.post(
    "/jobs",
    response_model=SimulationJobResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def create_simulation_job(
    request: WeatherSimulationRequest,
    session: Session = Depends(get_db),
) -> SimulationJobResponse:
    job = SimulationJob(
        city_id=request.city_id,
        status="queued",
        stage="queued",
        progress=0,
        request_json=request.model_dump(
            mode="json"
        ),
    )

    session.add(job)
    session.commit()
    session.refresh(job)

    try:
        celery_result = (
            run_weather_simulation_task.delay(
                job.id
            )
        )

        job.celery_task_id = celery_result.id
        session.commit()
        session.refresh(job)

    except Exception as error:
        job.status = "failed"
        job.stage = "queue_submission_failed"
        job.error_message = str(error)
        session.commit()

        raise HTTPException(
            status_code=503,
            detail=(
                "Unable to submit task to Celery:"
                f"{error}"
            ),
        ) from error

    return job_to_response(job)

@router.get(
    "/jobs",
    response_model=SimulationJobListResponse,
)
def list_simulation_jobs(
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
) -> SimulationJobListResponse:
    total = session.scalar(
        select(func.count())
        .select_from(SimulationJob)
    ) or 0

    jobs = session.scalars(
        select(SimulationJob)
        .order_by(
            SimulationJob.created_at.desc()
        )
        .offset(offset)
        .limit(limit)
    ).all()

    return SimulationJobListResponse(
        items=[
            job_to_response(job)
            for job in jobs
        ],
        total=total,
        limit=limit,
        offset=offset,
    )
    
@router.get(
    "/jobs/{job_id}",
    response_model=SimulationJobDetail,
)
def get_simulation_job(
    job_id: str,
    session: Session = Depends(get_db),
) -> SimulationJobDetail:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    return job_to_detail(job)

@router.get(
    "/jobs/{job_id}/result",
    response_model=WeatherSimulationResponse,
)
def get_simulation_result(
    job_id: str,
    session: Session = Depends(get_db),
) -> WeatherSimulationResponse:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    if job.status != "completed":
        raise HTTPException(
            status_code=409,
            detail=(
                "Simulation not yet completed, "
                f"current status: {job.status}"
            ),
        )

    if not job.result_path:
        raise HTTPException(
            status_code=500,
            detail="Simulation completed but missing result path",
        )

    try:
        return load_simulation_result(
            job.result_path
        )
    except FileNotFoundError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error
        
@router.post(
    "/jobs/{job_id}/cancel",
    response_model=SimulationJobResponse,
)
def cancel_simulation_job(
    job_id: str,
    session: Session = Depends(get_db),
) -> SimulationJobResponse:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    if job.status in {
        "completed",
        "failed",
        "cancelled",
    }:
        raise HTTPException(
            status_code=409,
            detail=(
                "Simulation job in terminal state cannot be cancelled"
            ),
        )

    if job.celery_task_id:
        celery_app.control.revoke(
            job.celery_task_id,
            terminate=False,
        )

    if job.status == "queued":
        job.status = "cancelled"
        job.stage = "cancelled"
    else:
        job.status = "cancelling"
        job.stage = (
            "waiting_for_cooperative_cancel"
        )

    session.commit()
    session.refresh(job)

    return job_to_response(job)

TERMINAL_JOB_STATUSES = {
    "completed",
    "failed",
    "cancelled",
}


def load_job_snapshot(
    job_id: str,
) -> SimulationJobResponse | None:
    with SessionLocal() as session:
        job = session.get(
            SimulationJob,
            job_id,
        )

        if job is None:
            return None

        return job_to_response(job)


@router.get(
    "/jobs/{job_id}/events",
)
async def simulation_job_events(
    job_id: str,
    request: Request,
) -> StreamingResponse:
    initial = await anyio.to_thread.run_sync(
        load_job_snapshot,
        job_id,
    )

    if initial is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    async def event_generator():
        previous_payload: str | None = None

        while True:
            if await request.is_disconnected():
                break

            snapshot = (
                await anyio.to_thread.run_sync(
                    load_job_snapshot,
                    job_id,
                )
            )

            if snapshot is None:
                yield (
                    "event: error\n"
                    'data: {"detail":"job not found"}\n\n'
                )
                break

            payload = json.dumps(
                snapshot.model_dump(
                    mode="json"
                ),
                ensure_ascii=False,
            )

            if payload != previous_payload:
                yield (
                    "event: progress\n"
                    f"data: {payload}\n\n"
                )

                previous_payload = payload

            if snapshot.status in (
                TERMINAL_JOB_STATUSES
            ):
                yield (
                    "event: terminal\n"
                    f"data: {payload}\n\n"
                )
                break

            await asyncio.sleep(1)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
    
from fastapi.responses import Response

from app.services.result_export import (
    export_result_csv,
    export_result_json,
)

@router.get(
    "/jobs/{job_id}/export",
)
def export_simulation_result(
    job_id: str,
    format: str = Query(
        default="csv",
        pattern="^(csv|json)$",
    ),
    session: Session = Depends(get_db),
) -> Response:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    if job.status != "completed":
        raise HTTPException(
            status_code=409,
            detail="Simulation not yet completed",
        )

    if not job.result_path:
        raise HTTPException(
            status_code=500,
            detail="Simulation completed but missing result path",
        )

    try:
        result = load_simulation_result(
            job.result_path
        )
    except FileNotFoundError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error

    if format == "json":
        content = export_result_json(result)
        media_type = "application/json"
        filename = f"simulation-{job_id}.json"
    else:
        content = export_result_csv(result)
        media_type = "text/csv"
        filename = f"simulation-{job_id}.csv"

    return Response(
        content=content.encode("utf-8-sig"),
        media_type=media_type,
        headers={
            "Content-Disposition": (
                f'attachment; filename="{filename}"'
            )
        },
    )

router.include_router(simulation_jobs.router)
router.include_router(simulation_events.router)