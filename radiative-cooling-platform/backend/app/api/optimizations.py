from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.cities import get_city
from app.core.time import utc_now
from app.db.session import get_db
from app.models.optimization_job import OptimizationJob
from app.schemas.optimization import (
    OptimizationCreate,
    OptimizationEstimate,
    OptimizationJobDetail,
    OptimizationJobListResponse,
    OptimizationJobResponse,
)
from app.services.leases import db_now
from app.services.material_resolution import resolve_request_materials
from app.services.optimization.jobs import optimization_to_detail, optimization_to_response
from app.services.optimization.search_space import build_search_space
from app.services.optimization.service import estimate_optimization
from app.worker.celery_app import celery_app
from app.worker.optimization_tasks import run_optimization_task


router = APIRouter(prefix="/api/v1/optimizations", tags=["optimizations"])

TERMINAL = {"completed", "failed", "cancelled"}
MATERIAL_FIELDS = ("control_material", "base_material")


def _validate(request: OptimizationCreate) -> None:
    try:
        get_city(request.city_id)
        build_search_space(request)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(error)) from error


@router.post("/estimate", response_model=OptimizationEstimate)
def estimate(request: OptimizationCreate, session: Session = Depends(get_db)) -> OptimizationEstimate:
    request = resolve_request_materials(session, request, fields=MATERIAL_FIELDS)
    _validate(request)
    return estimate_optimization(request)


@router.post("", response_model=OptimizationJobResponse, status_code=status.HTTP_202_ACCEPTED)
def create_optimization(request: OptimizationCreate, session: Session = Depends(get_db)) -> OptimizationJobResponse:
    request = resolve_request_materials(session, request, fields=MATERIAL_FIELDS)
    _validate(request)

    job = OptimizationJob(
        name=request.name, city_id=request.city_id,
        status="queued", stage="queued", progress=0,
        request_json=request.model_dump(mode="json"),
        control_material_version_id=request.control_material.material_version_id,
        base_material_version_id=request.base_material.material_version_id,
    )
    session.add(job)
    session.commit()
    session.refresh(job)

    try:
        job.celery_task_id = run_optimization_task.delay(job.id).id
        session.commit()
        session.refresh(job)
    except Exception as error:
        job.status, job.stage = "failed", "queue_submission_failed"
        job.error_message = str(error)[:4000]
        session.commit()
        raise HTTPException(status_code=503, detail=f"Unable to submit optimization: {error}") from error

    return optimization_to_response(job, now=db_now(session))


@router.get("", response_model=OptimizationJobListResponse)
def list_optimizations(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: Session = Depends(get_db),
) -> OptimizationJobListResponse:
    total = session.scalar(select(func.count()).select_from(OptimizationJob)) or 0
    jobs = session.scalars(
        select(OptimizationJob).order_by(OptimizationJob.created_at.desc()).offset(offset).limit(limit)
    ).all()
    now = db_now(session)
    return OptimizationJobListResponse(
        items=[optimization_to_response(j, now=now) for j in jobs], total=total, limit=limit, offset=offset
    )


@router.get("/{job_id}", response_model=OptimizationJobDetail)
def get_optimization(job_id: str, session: Session = Depends(get_db)) -> OptimizationJobDetail:
    job = session.get(OptimizationJob, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Optimization job not found")
    return optimization_to_detail(job, now=db_now(session))


@router.post("/{job_id}/cancel", response_model=OptimizationJobResponse)
def cancel_optimization(job_id: str, session: Session = Depends(get_db)) -> OptimizationJobResponse:
    job = session.get(OptimizationJob, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Optimization job not found")
    if job.status in TERMINAL:
        raise HTTPException(status_code=409, detail="Optimization job in terminal state cannot be cancelled")

    now = utc_now()
    job.cancel_requested_at = job.cancel_requested_at or now
    if job.status == "queued":
        job.status, job.stage, job.completed_at = "cancelled", "cancelled", now
    else:
        job.status, job.stage = "cancelling", "waiting_for_cooperative_cancel"

    if job.celery_task_id:
        celery_app.control.revoke(job.celery_task_id, terminate=False)

    session.commit()
    session.refresh(job)
    return optimization_to_response(job, now=db_now(session))