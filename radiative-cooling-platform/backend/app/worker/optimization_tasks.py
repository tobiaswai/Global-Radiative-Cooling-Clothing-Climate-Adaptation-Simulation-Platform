"""Inverse optimization task. Same lease/cancel contract as the other tasks.

Heartbeats are emitted from inside evaluate() (throttled), so a single long
generation can never outlive the lease TTL. Cancellation latency is bounded
by CITY_HEARTBEAT_SECONDS. No checkpoints: a reaped job restarts from scratch.
"""

from __future__ import annotations

import asyncio
import logging
import time

from celery import Task
from sqlalchemy import func, select

from app.core.config import settings
from app.core.time import utc_now
from app.db.session import SessionLocal
from app.models.optimization_job import OptimizationJob
from app.schemas.optimization import GenerationRecord, OptimizationCreate
from app.services.job_state import JobStatus, assert_job_transition
from app.services.leases import (
    acquire_optimization_lease,
    heartbeat_optimization_lease,
    release_optimization_lease,
)
from app.services.optimization.evaluator import MaterialEvaluator, prepare_samples
from app.services.optimization.runner import OptimizationCancelled
from app.services.optimization.service import execute_optimization
from app.worker.celery_app import celery_app
from app.worker.tasks import LeaseLostError, _owner_id


logger = logging.getLogger(__name__)

OPTIMIZATION_QUEUE = "optimization"


class OptimizationReporter:
    """Throttled, owner-guarded writes of progress, history and cancel checks."""

    def __init__(self, job_id: str, owner: str) -> None:
        self.job_id = job_id
        self.owner = owner
        self.interval = settings.CITY_HEARTBEAT_SECONDS
        self.last = 0.0
        self.progress = 0
        self.stage = "initializing"
        self.history: list[dict] = []
        self.evaluations = 0

    def __call__(
        self,
        *,
        progress: int | None = None,
        stage: str | None = None,
        history_record: GenerationRecord | None = None,
        evaluations: int | None = None,
        force: bool = False,
    ) -> None:
        if progress is not None:
            self.progress = max(self.progress, min(99, int(progress)))
        if stage is not None:
            self.stage = stage
        if history_record is not None:
            self.history.append(history_record.model_dump(mode="json"))
            self.evaluations = history_record.evaluation_count
        if evaluations is not None:
            self.evaluations = evaluations

        if not force and time.monotonic() - self.last < self.interval:
            return
        self.flush()

    def flush(self) -> None:
        with SessionLocal() as session:
            row = session.execute(
                select(OptimizationJob.status, OptimizationJob.cancel_requested_at)
                .where(OptimizationJob.id == self.job_id)
            ).one_or_none()
            if row is None:
                raise RuntimeError(f"Optimization job not found: {self.job_id}")
            if row.cancel_requested_at is not None or row.status in {JobStatus.CANCELLING, JobStatus.CANCELLED}:
                raise OptimizationCancelled()

            ok = heartbeat_optimization_lease(
                session, self.job_id, self.owner,
                stage=self.stage[:100], progress=self.progress,
                history_json=list(self.history), evaluation_count=self.evaluations,
            )
        if not ok:
            raise LeaseLostError()
        self.last = time.monotonic()


def _finish(session, job_id: str, owner: str, target: JobStatus, **values) -> bool:
    current = session.scalar(
        select(OptimizationJob.status).where(
            OptimizationJob.id == job_id, OptimizationJob.lease_owner == owner
        )
    )
    if current is None:
        return False
    assert_job_transition(current, target)
    return heartbeat_optimization_lease(
        session, job_id, owner, status=target, stage=target, completed_at=func.now(), **values
    )


@celery_app.task(bind=True, name="optimization.run", acks_late=True, reject_on_worker_lost=True)
def run_optimization_task(self: Task, job_id: str) -> dict:
    owner = _owner_id(self)
    lease_lost = False

    with SessionLocal() as session:
        if not acquire_optimization_lease(session, job_id, owner):
            return {"job_id": job_id, "status": "skipped", "reason": "lease_not_acquired"}

    try:
        with SessionLocal() as session:
            job = session.get(OptimizationJob, job_id)
            if job is None:
                raise RuntimeError(f"Optimization job not found: {job_id}")
            request = OptimizationCreate.model_validate(job.request_json)
            ok = heartbeat_optimization_lease(
                session, job_id, owner,
                stage="preparing_samples", progress=1, error_message=None,
                history_json=[], evaluation_count=0, result_json=None,
                attempt=OptimizationJob.attempt + 1,
            )
        if not ok:
            raise LeaseLostError()

        reporter = OptimizationReporter(job_id, owner)

        preparation = asyncio.run(
            prepare_samples(request, progress=lambda p, s: reporter(progress=p, stage=s))
        )
        evaluator = MaterialEvaluator(
            request, preparation.samples,
            on_evaluation=lambda count: reporter(evaluations=count),
        )
        result = execute_optimization(request, evaluator, preparation, report=reporter)
        reporter(force=True)  # last cancel check, flush history

        with SessionLocal() as session:
            ok = _finish(
                session, job_id, owner, JobStatus.COMPLETED,
                progress=100, error_message=None,
                evaluation_count=result.evaluation_count,
                history_json=reporter.history,
                result_json=result.model_dump(mode="json"),
            )
        if not ok:
            raise LeaseLostError()
        return {"job_id": job_id, "status": "completed", "verdict": result.verdict}

    except LeaseLostError:
        lease_lost = True
        return {"job_id": job_id, "status": "lease_lost"}

    except OptimizationCancelled:
        with SessionLocal() as session:
            _finish(session, job_id, owner, JobStatus.CANCELLED)
        return {"job_id": job_id, "status": "cancelled"}

    except Exception as error:
        logger.exception("optimization job %s failed", job_id)
        with SessionLocal() as session:
            _finish(session, job_id, owner, JobStatus.FAILED, error_message=str(error)[:4000])
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_optimization_lease(session, job_id, owner)


@celery_app.task(name="optimization.reap_expired_leases")
def reap_expired_optimization_leases() -> dict:
    requeued: list[str] = []
    failed: list[str] = []

    with SessionLocal() as session:
        stale = session.scalars(
            select(OptimizationJob)
            .where(
                OptimizationJob.status.in_([JobStatus.RUNNING, JobStatus.CANCELLING]),
                OptimizationJob.lease_expires_at < func.now(),
            )
            .with_for_update(skip_locked=True)
        ).all()

        for job in stale:
            if job.status == JobStatus.CANCELLING:
                assert_job_transition(job.status, JobStatus.CANCELLED)
                job.status, job.stage, job.completed_at = JobStatus.CANCELLED, "cancelled", utc_now()
            elif job.attempt < settings.CITY_MAX_RETRIES:
                assert_job_transition(job.status, JobStatus.QUEUED)
                job.status, job.stage = JobStatus.QUEUED, "retry_scheduled"
                requeued.append(job.id)
            else:
                assert_job_transition(job.status, JobStatus.FAILED)
                job.status, job.stage = JobStatus.FAILED, "failed"
                job.error_message = f"lease expired after {job.attempt} attempt(s)"
                job.completed_at = utc_now()
                failed.append(job.id)
            job.lease_owner = None
            job.lease_expires_at = None

        session.commit()

    for job_id in requeued:
        run_optimization_task.apply_async(args=[job_id], queue=OPTIMIZATION_QUEUE)

    return {"requeued": requeued, "failed": failed}