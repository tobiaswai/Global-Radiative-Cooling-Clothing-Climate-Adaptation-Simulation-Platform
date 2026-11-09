"""Celery tasks (Stage 9).

Both task families share one reliability contract:

* a row-level lease is acquired atomically before any work; a redelivered
  message that cannot acquire it exits silently (idempotent);
* every write is guarded by ``lease_owner == owner`` and rolled back when the
  guard fails; after ``LeaseLostError`` nothing is written;
* cancellation is cooperative and checked at every heartbeat;
* status changes go through ``job_state``;
* re-queued work keeps its original Celery queue.
"""

from __future__ import annotations

import asyncio
import logging
import os
import socket
import time

from celery import Task
from sqlalchemy import func, select, update

from app.core.config import settings
from app.core.time import utc_now
from app.db.session import SessionLocal
from app.models.global_batch import GlobalBatchJob, GlobalCityResult
from app.models.simulation_job import SimulationJob
from app.schemas.global_batch import GlobalBatchCreate, MonthlyAdaptationResult
from app.schemas.simulation import WeatherSimulationRequest
from app.services.annual_sampling import estimate_sample_count
from app.services.checkpoints import (
    CheckpointProvenance,
    load_resume_state,
    upsert_month_checkpoint,
)
from app.services.climate_adaptation import analyze_city_climate_adaptation
from app.services.execution_profile import resolve_queue_name
from app.services.global_batch_service import refresh_batch_status
from app.services.job_state import (
    BatchStatus,
    CityStatus,
    JobStatus,
    assert_batch_transition,
    assert_city_transition,
    assert_job_transition,
)
from app.services.leases import (
    acquire_city_lease,
    acquire_job_lease,
    heartbeat_city_lease,
    heartbeat_job_lease,
    release_city_lease,
    release_job_lease,
)
from app.services.result_storage import save_simulation_result
from app.services.weather_simulation import execute_weather_simulation
from app.worker.celery_app import celery_app


logger = logging.getLogger(__name__)

SINGLE_JOB_QUEUE = "default"


class JobCancelledError(Exception):
    pass


class GlobalBatchCancelledError(Exception):
    pass


class LeaseLostError(Exception):
    """The lease was reaped or taken by another worker. Do not write anything."""


def _owner_id(task: Task) -> str:
    return f"{socket.gethostname()}:{os.getpid()}:{task.request.id}"


# ---------------------------------------------------------------------------
# Single simulation job helpers (kept for tests and ad-hoc tooling)
# ---------------------------------------------------------------------------

def update_job(job_id: str, **values: object) -> None:
    """Unconditional update. Not used by the task itself any more; the task
    writes through ``heartbeat_job_lease`` so writes are owner-guarded."""
    with SessionLocal() as session:
        job = session.get(SimulationJob, job_id)
        if job is None:
            raise RuntimeError(f"Simulation task not found:{job_id}")
        for field, value in values.items():
            setattr(job, field, value)
        session.commit()


def ensure_not_cancelled(job_id: str) -> None:
    with SessionLocal() as session:
        job = session.get(SimulationJob, job_id)
        if job is None:
            raise RuntimeError(f"Simulation task not found:{job_id}")
        if job.status in {JobStatus.CANCELLING, JobStatus.CANCELLED}:
            raise JobCancelledError()


def _finish_job_as_owner(session, job_id: str, owner: str, target: JobStatus, **values: object) -> bool:
    current = session.scalar(
        select(SimulationJob.status).where(
            SimulationJob.id == job_id, SimulationJob.lease_owner == owner
        )
    )
    if current is None:
        return False
    assert_job_transition(current, target)
    return heartbeat_job_lease(
        session, job_id, owner,
        status=target, stage=target, completed_at=func.now(), **values,
    )


@celery_app.task(
    bind=True,
    name="simulation.run_weather",
    acks_late=True,
    reject_on_worker_lost=True,
)
def run_weather_simulation_task(self: Task, job_id: str) -> dict:
    owner = _owner_id(self)
    lease_lost = False

    with SessionLocal() as session:
        if not acquire_job_lease(session, job_id, owner):
            return {"job_id": job_id, "status": "skipped", "reason": "lease_not_acquired"}

    try:
        with SessionLocal() as session:
            job = session.get(SimulationJob, job_id)
            if job is None:
                raise RuntimeError(f"Simulation task not found:{job_id}")
            request = WeatherSimulationRequest.model_validate(job.request_json)

            ok = heartbeat_job_lease(
                session, job_id, owner,
                stage="initializing", progress=2, error_message=None,
                attempt=SimulationJob.attempt + 1,
            )
        if not ok:
            lease_lost = True
            raise LeaseLostError()

        def report(progress: int, stage: str) -> None:
            nonlocal lease_lost
            ensure_not_cancelled(job_id)

            self.update_state(
                state="PROGRESS",
                meta={"job_id": job_id, "progress": progress, "stage": stage},
            )
            with SessionLocal() as session:
                beat_ok = heartbeat_job_lease(session, job_id, owner, stage=stage, progress=progress)
            if not beat_ok:
                lease_lost = True
                raise LeaseLostError()

        result = asyncio.run(execute_weather_simulation(request=request, progress_callback=report))

        report(95, "saving_result")
        result_path = save_simulation_result(job_id=job_id, result=result)

        with SessionLocal() as session:
            ensure_not_cancelled(job_id)
            ok = _finish_job_as_owner(
                session, job_id, owner, JobStatus.COMPLETED,
                progress=100,
                summary_json=result.summary.model_dump(mode="json"),
                result_path=str(result_path),
                error_message=None,
            )
        if not ok:
            lease_lost = True
            raise LeaseLostError()

        return {"job_id": job_id, "status": "completed"}

    except LeaseLostError:
        return {"job_id": job_id, "status": "lease_lost"}

    except JobCancelledError:
        with SessionLocal() as session:
            _finish_job_as_owner(session, job_id, owner, JobStatus.CANCELLED)
        return {"job_id": job_id, "status": "cancelled"}

    except Exception as error:
        logger.exception("simulation job %s failed", job_id)
        with SessionLocal() as session:
            _finish_job_as_owner(
                session, job_id, owner, JobStatus.FAILED,
                error_message=str(error)[:4000],
            )
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_job_lease(session, job_id, owner)


@celery_app.task(name="simulation.reap_expired_leases")
def reap_expired_job_leases() -> dict:
    """Re-queue (or fail) single jobs whose worker died without releasing."""
    requeued: list[str] = []
    failed: list[str] = []

    with SessionLocal() as session:
        stale = session.scalars(
            select(SimulationJob)
            .where(
                SimulationJob.status.in_([JobStatus.RUNNING, JobStatus.CANCELLING]),
                SimulationJob.lease_expires_at < func.now(),
            )
            .with_for_update(skip_locked=True)
        ).all()

        for job in stale:
            if job.status == JobStatus.CANCELLING:
                assert_job_transition(job.status, JobStatus.CANCELLED)
                job.status = JobStatus.CANCELLED
                job.stage = "cancelled"
                job.completed_at = utc_now()
            elif job.attempt < settings.CITY_MAX_RETRIES:
                assert_job_transition(job.status, JobStatus.QUEUED)
                job.status = JobStatus.QUEUED
                job.stage = "retry_scheduled"
                requeued.append(job.id)
            else:
                assert_job_transition(job.status, JobStatus.FAILED)
                job.status = JobStatus.FAILED
                job.stage = "failed"
                job.error_message = f"lease expired after {job.attempt} attempt(s)"
                job.completed_at = utc_now()
                failed.append(job.id)
            job.lease_owner = None
            job.lease_expires_at = None

        session.commit()

    for job_id in requeued:
        run_weather_simulation_task.apply_async(args=[job_id], queue=SINGLE_JOB_QUEUE)

    return {"requeued": requeued, "failed": failed}


# ---------------------------------------------------------------------------
# Global batch city task
# ---------------------------------------------------------------------------

def _batch_cancel_requested(session, batch_id: str) -> bool:
    row = session.execute(
        select(GlobalBatchJob.status, GlobalBatchJob.cancel_requested_at)
        .where(GlobalBatchJob.id == batch_id)
    ).one_or_none()
    if row is None:
        raise RuntimeError(f"Global batch not found: {batch_id}")
    status, cancel_requested_at = row
    return cancel_requested_at is not None or status in {BatchStatus.CANCELLING, BatchStatus.CANCELLED}


def _finish_city_as_owner(session, city_result_id: str, owner: str, target: CityStatus, **values: object) -> bool:
    assert_city_transition(CityStatus.RUNNING, target)
    return heartbeat_city_lease(
        session, city_result_id, owner,
        status=target, stage=target, completed_at=func.now(), **values,
    )


def _fail_or_requeue_city(session, city_result_id: str, owner: str, error: Exception) -> bool:
    """True -> set back to queued and must be re-submitted; False -> terminal failed."""
    retry_count = session.scalar(
        select(GlobalCityResult.retry_count).where(
            GlobalCityResult.id == city_result_id, GlobalCityResult.lease_owner == owner
        )
    )
    if retry_count is None:
        return False  # not ours any more

    message = str(error)[:4000]

    if retry_count < settings.CITY_MAX_RETRIES:
        assert_city_transition(CityStatus.RUNNING, CityStatus.QUEUED)
        return heartbeat_city_lease(
            session, city_result_id, owner,
            status=CityStatus.QUEUED,
            stage="retry_scheduled",
            error_message=message,
            retry_count=GlobalCityResult.retry_count + 1,
        )

    _finish_city_as_owner(session, city_result_id, owner, CityStatus.FAILED, error_message=message)
    return False


@celery_app.task(
    bind=True,
    name="global_batch.run_city",
    acks_late=True,
    reject_on_worker_lost=True,
)
def run_global_city_analysis_task(self: Task, city_result_id: str) -> dict:
    owner = _owner_id(self)
    batch_id: str | None = None
    queue_name = "global_standard"
    lease_lost = False

    with SessionLocal() as session:
        if not acquire_city_lease(session, city_result_id, owner):
            return {"city_result_id": city_result_id, "status": "skipped", "reason": "lease_not_acquired"}

    try:
        with SessionLocal() as session:
            city_result = session.get(GlobalCityResult, city_result_id)
            if city_result is None:
                raise RuntimeError(f"Global city result not found: {city_result_id}")
            batch = session.get(GlobalBatchJob, city_result.batch_id)
            if batch is None:
                raise RuntimeError(f"Global batch not found: {city_result.batch_id}")

            batch_id = batch.id
            request = GlobalBatchCreate.model_validate(batch.request_json)
            queue_name = resolve_queue_name(request)
            city_id = city_result.city_id
            provenance = CheckpointProvenance.for_request(request)

            if _batch_cancel_requested(session, batch_id):
                raise GlobalBatchCancelledError()

            # The API decides whether checkpoints exist (it deletes them when
            # the user opts out of resuming); the worker always trusts the
            # provenance-checked contiguous prefix that remains.
            resume = load_resume_state(
                session, city_result_id,
                start_month=request.start_month, provenance=provenance,
            )
            initial_monthly_results = [
                MonthlyAdaptationResult.model_validate(item) for item in resume.payloads
            ]
            checkpoints_discarded = list(resume.discarded)

            city_result.stage = "initializing"
            city_result.progress = 1
            city_result.completed_at = None
            city_result.error_message = None
            city_result.resumed_from_checkpoint = bool(initial_monthly_results)

            if batch.status != BatchStatus.RUNNING:
                assert_batch_transition(batch.status, BatchStatus.RUNNING)
                batch.status = BatchStatus.RUNNING
                batch.stage = "analyzing_cities"
                batch.started_at = batch.started_at or utc_now()
                batch.completed_at = None

            session.commit()

        total_sample_count = max(1, estimate_sample_count(request))
        heartbeat_interval = settings.CITY_HEARTBEAT_SECONDS
        last_beat = time.monotonic()
        last_stage: str | None = None

        def report(progress: int, stage: str) -> None:
            nonlocal last_beat, last_stage, lease_lost
            progress = max(0, min(progress, 100))
            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id, "city_result_id": city_result_id,
                    "city_id": city_id, "progress": progress, "stage": stage,
                },
            )
            if time.monotonic() - last_beat < heartbeat_interval and stage == last_stage:
                return

            with SessionLocal() as session:
                if _batch_cancel_requested(session, batch_id):
                    raise GlobalBatchCancelledError()
                ok = heartbeat_city_lease(session, city_result_id, owner, stage=stage, progress=progress)
            if not ok:
                lease_lost = True
                raise LeaseLostError()

            last_beat = time.monotonic()
            last_stage = stage

        def save_checkpoint(
            monthly_results: list[MonthlyAdaptationResult],
            completed_month: int,
            completed_sample_count: int,
        ) -> None:
            nonlocal last_beat, lease_lost

            checkpoint_progress = max(1, min(92, round(completed_sample_count / total_sample_count * 92)))
            stage = f"checkpoint_saved_{request.year}-{completed_month:02d}"

            month_payload = next(
                (m.model_dump(mode="json") for m in monthly_results if m.month == completed_month),
                monthly_results[-1].model_dump(mode="json"),
            )
            all_payloads = [m.model_dump(mode="json") for m in monthly_results]

            with SessionLocal() as session:
                if _batch_cancel_requested(session, batch_id):
                    raise GlobalBatchCancelledError()

                retry_count = session.scalar(
                    select(GlobalCityResult.retry_count).where(GlobalCityResult.id == city_result_id)
                )

                # (a) checkpoint row staged, owner-guarded ...
                staged = upsert_month_checkpoint(
                    session,
                    city_result_id=city_result_id, owner=owner,
                    month=completed_month, attempt=retry_count or 0,
                    payload=month_payload, provenance=provenance,
                )
                if not staged:
                    session.rollback()
                    ok = False
                else:
                    # (b) ... and committed together with the heartbeat; a lost
                    # lease rolls (a) back as well.
                    ok = heartbeat_city_lease(
                        session, city_result_id, owner,
                        monthly_json=all_payloads,
                        completed_month_count=len(monthly_results),
                        last_checkpoint_month=completed_month,
                        stage=stage,
                        progress=func.greatest(GlobalCityResult.progress, checkpoint_progress),
                    )

            if not ok:
                lease_lost = True
                raise LeaseLostError()

            last_beat = time.monotonic()
            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id, "city_result_id": city_result_id, "city_id": city_id,
                    "progress": checkpoint_progress, "stage": stage, "completed_month": completed_month,
                },
            )

        analysis = asyncio.run(
            analyze_city_climate_adaptation(
                city_id=city_id,
                request=request,
                progress_callback=report,
                checkpoint_callback=save_checkpoint,
                initial_monthly_results=initial_monthly_results,
            )
        )

        monthly_json = analysis["monthly_results"]
        last_month = max(item["month"] for item in monthly_json) if monthly_json else None

        data_quality = dict(analysis.get("data_quality", {}))
        data_quality["checkpoints_discarded"] = checkpoints_discarded
        data_quality["checkpoint_provenance"] = {
            "model_version": provenance.model_version,
            "parameter_fingerprint": provenance.parameter_fingerprint,
            "request_sha256": provenance.request_sha256,
        }

        with SessionLocal() as session:
            if _batch_cancel_requested(session, batch_id):
                raise GlobalBatchCancelledError()

            ok = _finish_city_as_owner(
                session, city_result_id, owner, CityStatus.COMPLETED,
                progress=100,
                error_message=None,
                climate_adaptation_rate_percent=analysis["climate_adaptation_rate_percent"],
                exposure_coverage_percent=analysis["exposure_coverage_percent"],
                annual_average_skin_improvement_c=analysis["annual_average_skin_improvement_c"],
                annual_average_core_improvement_c=analysis["annual_average_core_improvement_c"],
                maximum_skin_improvement_c=analysis["maximum_skin_improvement_c"],
                effective_cooling_hours=analysis["effective_cooling_hours"],
                sampled_day_count=analysis["sampled_day_count"],
                eligible_sample_count=analysis["eligible_sample_count"],
                evaluated_weighted_days=analysis["evaluated_weighted_days"],
                beneficial_weighted_days=analysis["beneficial_weighted_days"],
                skin_improvement_p50_c=analysis["skin_improvement_p50_c"],
                skin_improvement_p90_c=analysis["skin_improvement_p90_c"],
                skin_improvement_p95_c=analysis["skin_improvement_p95_c"],
                core_improvement_p50_c=analysis["core_improvement_p50_c"],
                core_improvement_p90_c=analysis["core_improvement_p90_c"],
                core_improvement_p95_c=analysis["core_improvement_p95_c"],
                heatwave_event_count=analysis["heatwave_event_count"],
                longest_heatwave_days=analysis["longest_heatwave_days"],
                analytics_json={
                    "heatwave_analysis_available": analysis.get("heatwave_analysis_available", False),
                    "heatwave_unavailable_reason": analysis.get("heatwave_unavailable_reason"),
                    "heatwave_temperature_basis": analysis.get("heatwave_temperature_basis"),
                    "heatwave_events": analysis.get("heatwave_events", []),
                    "data_quality": data_quality,
                    "metric_definitions": analysis.get("metric_definitions", {}),
                },
                monthly_json=monthly_json,
                completed_month_count=analysis["completed_month_count"],
                last_checkpoint_month=last_month,
            )
            if not ok:
                lease_lost = True
                raise LeaseLostError()

            refresh_batch_status(session, batch_id)

        return {"batch_id": batch_id, "city_result_id": city_result_id, "status": "completed"}

    except LeaseLostError:
        return {"batch_id": batch_id, "city_result_id": city_result_id, "status": "lease_lost"}

    except GlobalBatchCancelledError:
        if batch_id is not None:
            with SessionLocal() as session:
                _finish_city_as_owner(session, city_result_id, owner, CityStatus.CANCELLED, progress=100)
                refresh_batch_status(session, batch_id)
        return {"batch_id": batch_id, "city_result_id": city_result_id, "status": "cancelled"}

    except Exception as error:
        logger.exception("city %s failed", city_result_id)
        requeue = False
        if batch_id is not None:
            with SessionLocal() as session:
                requeue = _fail_or_requeue_city(session, city_result_id, owner, error)
                refresh_batch_status(session, batch_id)

        if requeue:
            run_global_city_analysis_task.apply_async(
                args=[city_result_id],
                countdown=settings.CITY_HEARTBEAT_SECONDS,
                queue=queue_name,  # keep the original queue
            )
            return {
                "batch_id": batch_id, "city_result_id": city_result_id,
                "status": "requeued", "error": str(error)[:500],
            }
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_city_lease(session, city_result_id, owner)


@celery_app.task(name="global_batch.reap_expired_leases")
def reap_expired_leases() -> dict:
    requeued: list[tuple[str, str]] = []  # (city_result_id, queue)
    touched_batches: set[str] = set()

    with SessionLocal() as db:
        stale = db.scalars(
            select(GlobalCityResult)
            .where(
                GlobalCityResult.status == CityStatus.RUNNING,
                GlobalCityResult.lease_expires_at < func.now(),
            )
            .with_for_update(skip_locked=True)
        ).all()

        queue_by_batch: dict[str, str] = {}

        for city in stale:
            if city.batch_id not in queue_by_batch:
                batch = db.get(GlobalBatchJob, city.batch_id)
                queue_by_batch[city.batch_id] = resolve_queue_name(
                    GlobalBatchCreate.model_validate(batch.request_json)
                )

            if city.retry_count < settings.CITY_MAX_RETRIES:
                assert_city_transition(city.status, CityStatus.QUEUED)
                city.status = CityStatus.QUEUED
                city.stage = "lease_expired_requeued"
                city.retry_count += 1
                requeued.append((city.id, queue_by_batch[city.batch_id]))
            else:
                assert_city_transition(city.status, CityStatus.FAILED)
                city.status = CityStatus.FAILED
                city.stage = "failed"
                city.error_message = f"lease expired after {city.retry_count} retries"
                city.completed_at = utc_now()

            city.lease_owner = None
            city.lease_expires_at = None
            touched_batches.add(city.batch_id)

        db.commit()

        for batch_id in touched_batches:
            refresh_batch_status(db, batch_id)

    for city_result_id, queue in requeued:
        run_global_city_analysis_task.apply_async(args=[city_result_id], queue=queue)

    return {"requeued": [c for c, _ in requeued], "batches": sorted(touched_batches)}