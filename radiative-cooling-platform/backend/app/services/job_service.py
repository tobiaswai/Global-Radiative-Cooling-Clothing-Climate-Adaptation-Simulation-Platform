from sqlalchemy.orm import Session
from datetime import datetime
from app.services.leases import derive_lease_state

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



def job_to_response(job: SimulationJob, *, now: datetime | None = None) -> SimulationJobResponse:
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
        control_material_version_id=getattr(job, "control_material_version_id", None),
        rc_material_version_id=getattr(job, "rc_material_version_id", None),
        attempt=getattr(job, "attempt", 0) or 0,
        lease_owner=getattr(job, "lease_owner", None),
        lease_expires_at=getattr(job, "lease_expires_at", None),
        last_heartbeat_at=getattr(job, "last_heartbeat_at", None),
        lease_state=derive_lease_state(
            getattr(job, "lease_owner", None), getattr(job, "lease_expires_at", None), now
        ),
    )


def job_to_detail(job: SimulationJob, *, now: datetime | None = None) -> SimulationJobDetail:
    return SimulationJobDetail(
        **job_to_response(job, now=now).model_dump(),
        request=WeatherSimulationRequest.model_validate(job.request_json),
    )


def get_job_or_none(
    session: Session,
    job_id: str,
) -> SimulationJob | None:
    return session.get(
        SimulationJob,
        job_id,
    )