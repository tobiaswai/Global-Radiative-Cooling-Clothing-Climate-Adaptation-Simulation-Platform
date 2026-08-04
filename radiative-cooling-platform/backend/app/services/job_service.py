from sqlalchemy.orm import Session

from app.models.simulation_job import (
    SimulationJob,
)
from app.schemas.job import (
    SimulationJobDetail,
    SimulationJobResponse,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
)


def job_to_response(
    job: SimulationJob,
) -> SimulationJobResponse:
    return SimulationJobResponse(
        id=job.id,
        celery_task_id=job.celery_task_id,
        status=job.status,
        stage=job.stage,
        progress=job.progress,
        city_id=job.city_id,
        summary=job.summary_json,
        error_message=job.error_message,
        created_at=job.created_at,
        updated_at=job.updated_at,
        started_at=job.started_at,
        completed_at=job.completed_at,
    )


def job_to_detail(
    job: SimulationJob,
) -> SimulationJobDetail:
    return SimulationJobDetail(
        **job_to_response(job).model_dump(),
        request=WeatherSimulationRequest.model_validate(
            job.request_json
        ),
    )


def get_job_or_none(
    session: Session,
    job_id: str,
) -> SimulationJob | None:
    return session.get(
        SimulationJob,
        job_id,
    )