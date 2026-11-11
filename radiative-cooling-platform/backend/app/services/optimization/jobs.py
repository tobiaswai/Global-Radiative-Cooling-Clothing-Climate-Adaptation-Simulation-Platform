from datetime import datetime

from app.models.optimization_job import OptimizationJob
from app.schemas.optimization import (
    GenerationRecord,
    OptimizationCreate,
    OptimizationJobDetail,
    OptimizationJobResponse,
    OptimizationResult,
)
from app.services.leases import derive_lease_state


def optimization_to_response(job: OptimizationJob, *, now: datetime | None = None) -> OptimizationJobResponse:
    return OptimizationJobResponse(
        id=job.id, celery_task_id=job.celery_task_id, name=job.name, city_id=job.city_id,
        status=job.status, stage=job.stage, progress=job.progress,
        evaluation_count=job.evaluation_count or 0, error_message=job.error_message,
        created_at=job.created_at, updated_at=job.updated_at,
        started_at=job.started_at, completed_at=job.completed_at,
        attempt=job.attempt or 0, lease_owner=job.lease_owner,
        lease_expires_at=job.lease_expires_at, last_heartbeat_at=job.last_heartbeat_at,
        lease_state=derive_lease_state(job.lease_owner, job.lease_expires_at, now),
        cancel_requested_at=job.cancel_requested_at,
        control_material_version_id=job.control_material_version_id,
        base_material_version_id=job.base_material_version_id,
    )


def optimization_to_detail(job: OptimizationJob, *, now: datetime | None = None) -> OptimizationJobDetail:
    return OptimizationJobDetail(
        **optimization_to_response(job, now=now).model_dump(),
        request=OptimizationCreate.model_validate(job.request_json),
        history=[GenerationRecord.model_validate(r) for r in (job.history_json or [])],
        result=None if job.result_json is None else OptimizationResult.model_validate(job.result_json),
    )