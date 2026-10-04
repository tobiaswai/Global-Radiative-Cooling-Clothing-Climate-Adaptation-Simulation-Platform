import asyncio
from datetime import (
    datetime,
    timezone,
)

from celery import Task
import logging

from app.core.time import utc_now
from app.db.session import SessionLocal
from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.models.simulation_job import (
    SimulationJob,
)
from app.schemas.global_batch import (
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services.annual_sampling import (
    estimate_sample_count,
)
from app.services.climate_adaptation import (
    analyze_city_climate_adaptation,
)
from app.services.global_batch_service import (
    reconcile_batch,
    refresh_batch_status,
)
from app.services.result_storage import (
    save_simulation_result,
)
from app.services.weather_simulation import (
    execute_weather_simulation,
)
from app.worker.celery_app import (
    celery_app,
)
import os
import socket
import time

from sqlalchemy import func, select, update

from app.core.config import settings
from app.services.checkpoints import (
    load_resume_state,
    upsert_month_checkpoint,
)
from app.services.job_state import (
    BatchStatus,
    CityStatus,
    assert_batch_transition,
    assert_city_transition,
)
from app.services.leases import (
    acquire_city_lease,
    heartbeat_city_lease,
    release_city_lease,
)

logger = logging.getLogger(__name__)   # replaces: from fastapi import logger

class JobCancelledError(Exception):
    pass

class GlobalBatchCancelledError(Exception):
    pass

def update_job(
    job_id: str,
    **values: object,
) -> None:
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
        if job.status in {"cancelling", "cancelled"}:
            raise JobCancelledError()

@celery_app.task(
    bind=True,
    name="simulation.run_weather",
    acks_late=True,
)
def run_weather_simulation_task(
    self: Task,
    job_id: str,
) -> dict:
    try:
        with SessionLocal() as session:
            job = session.get(
                SimulationJob,
                job_id,
            )

            if job is None:
                raise RuntimeError(
                    f"Simulation task not found:{job_id}"
                )

            request = WeatherSimulationRequest.model_validate(
                job.request_json
            )

        update_job(
            job_id,
            status="running",
            stage="initializing",
            progress=2,
            started_at=utc_now(),
            error_message=None,
        )

        def report(
            progress: int,
            stage: str,
        ) -> None:
            ensure_not_cancelled(job_id)

            update_job(
                job_id,
                status="running",
                stage=stage,
                progress=progress,
            )

            self.update_state(
                state="PROGRESS",
                meta={
                    "job_id": job_id,
                    "progress": progress,
                    "stage": stage,
                },
            )

        result = asyncio.run(
            execute_weather_simulation(
                request=request,
                progress_callback=report,
            )
        )

        ensure_not_cancelled(job_id)

        update_job(
            job_id,
            stage="saving_result",
            progress=95,
        )

        result_path = save_simulation_result(
            job_id=job_id,
            result=result,
        )

        update_job(
            job_id,
            status="completed",
            stage="completed",
            progress=100,
            summary_json=result.summary.model_dump(
                mode="json"
            ),
            result_path=str(result_path),
            completed_at=utc_now(),
        )

        return {
            "job_id": job_id,
            "status": "completed",
        }

    except JobCancelledError:
        update_job(
            job_id,
            status="cancelled",
            stage="cancelled",
            completed_at=utc_now(),
        )

        return {
            "job_id": job_id,
            "status": "cancelled",
        }

    except Exception as error:
        
        update_job(
            job_id,
            status="failed",
            stage="failed",
            error_message=str(error)[:4000],
            completed_at=utc_now(),
        )
        raise
class LeaseLostError(Exception):
    """租約被 reaper 收回或被別的 worker 接手。收到後不得再寫任何 DB。"""


def _owner_id(task: Task) -> str:
    return f"{socket.gethostname()}:{os.getpid()}:{task.request.id}"


def _batch_cancel_requested(session, batch_id: str) -> bool:
    row = session.execute(
        select(
            GlobalBatchJob.status,
            GlobalBatchJob.cancel_requested_at,
        ).where(GlobalBatchJob.id == batch_id)
    ).one_or_none()

    if row is None:
        raise RuntimeError(f"Global batch not found: {batch_id}")

    status, cancel_requested_at = row
    return (
        cancel_requested_at is not None
        or status in {BatchStatus.CANCELLING, BatchStatus.CANCELLED}
    )


def _finish_city_as_owner(
    session,
    city_result_id: str,
    owner: str,
    target: CityStatus,
    **values: object,
) -> bool:
    """running -> terminal 的寫入，只有租約持有者能成功。"""
    assert_city_transition(CityStatus.RUNNING, target)
    now = utc_now()
    return heartbeat_city_lease(
        session,
        city_result_id,
        owner,
        status=target,
        stage=target,
        completed_at=now,
        **values,
    )


def _fail_or_requeue_city(
    session,
    city_result_id: str,
    owner: str,
    error: Exception,
) -> bool:
    """回傳 True 代表已改回 queued、需要重新投遞；False 代表已終態 failed。"""
    retry_count = session.execute(
        select(GlobalCityResult.retry_count).where(
            GlobalCityResult.id == city_result_id,
            GlobalCityResult.lease_owner == owner,
        )
    ).scalar_one_or_none()

    if retry_count is None:
        return False  # 租約早已不是我們的，什麼都不做

    message = str(error)[:4000]

    if retry_count < settings.CITY_MAX_RETRIES:
        assert_city_transition(CityStatus.RUNNING, CityStatus.QUEUED)
        result = session.execute(
            update(GlobalCityResult)
            .where(GlobalCityResult.id == city_result_id,
                GlobalCityResult.lease_owner == owner)
            .values(
                status=CityStatus.QUEUED,
                stage="retry_scheduled",
                error_message=message,
                retry_count=GlobalCityResult.retry_count + 1,
                last_heartbeat_at=utc_now(),
            )
        )
        session.commit()
        return result.rowcount == 1

    _finish_city_as_owner(
        session,
        city_result_id,
        owner,
        CityStatus.FAILED,
        error_message=message,
    )
    return False


@celery_app.task(
    bind=True,
    name="global_batch.run_city",
    acks_late=True,
    reject_on_worker_lost=True,
)
def run_global_city_analysis_task(
    self: Task,
    city_result_id: str,
) -> dict:
    owner = _owner_id(self)
    batch_id: str | None = None
    lease_lost = False

    # ---- 1. 原子性取租約；拿不到就靜默退出（冪等） ----
    with SessionLocal() as session:
        if not acquire_city_lease(session, city_result_id, owner):
            return {
                "city_result_id": city_result_id,
                "status": "skipped",
                "reason": "lease_not_acquired",
            }

    try:
        # ---- 2. 讀 context + 續跑狀態 ----
        with SessionLocal() as session:
            city_result = session.get(GlobalCityResult, city_result_id)
            if city_result is None:
                raise RuntimeError(
                    f"Global city result not found: {city_result_id}"
                )

            batch = session.get(GlobalBatchJob, city_result.batch_id)
            if batch is None:
                raise RuntimeError(
                    f"Global batch not found: {city_result.batch_id}"
                )

            batch_id = batch.id
            request = GlobalBatchCreate.model_validate(batch.request_json)
            city_id = city_result.city_id

            if _batch_cancel_requested(session, batch_id):
                raise GlobalBatchCancelledError()

            # 續跑來源優先順序：checkpoint 表 > 舊 monthly_json（相容舊資料）
            # reaper 重排（retry_count > 0）一律續跑，不看 request 的旗標
            should_resume = (
                request.resume_from_checkpoint or city_result.retry_count > 0
            )
            payloads: list[dict] = []
            if should_resume:
                _, payloads = load_resume_state(
                    session, city_result_id, start_month=request.start_month
                )
                if not payloads and city_result.monthly_json:
                    payloads = list(city_result.monthly_json)

            initial_monthly_results = [
                MonthlyAdaptationResult.model_validate(item)
                for item in payloads
            ]

            # 補 checkpoint 表（舊資料第一次續跑時把 monthly_json 回填進去）
            for item in payloads:
                upsert_month_checkpoint(
                    session,
                    city_result_id,
                    month=item["month"],
                    attempt=city_result.retry_count,
                    payload=item,
                )

            # status/started_at/lease 已由 acquire_city_lease 寫好，這裡只補其餘欄位
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

        # ---- 3. callbacks：心跳 + 取消檢查 + checkpoint ----
        def report(progress: int, stage: str) -> None:
            nonlocal last_beat, last_stage, lease_lost

            progress = max(0, min(progress, 100))
            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": city_result_id,
                    "city_id": city_id,
                    "progress": progress,
                    "stage": stage,
                },
            )

            # 節流：沒到心跳週期且 stage 沒變就不打 DB
            if (
                time.monotonic() - last_beat < heartbeat_interval
                and stage == last_stage
            ):
                return

            with SessionLocal() as session:
                if _batch_cancel_requested(session, batch_id):
                    raise GlobalBatchCancelledError()

                ok = heartbeat_city_lease(
                    session,
                    city_result_id,
                    owner,
                    stage=stage,
                    progress=progress,
                )

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

            checkpoint_progress = max(
                1,
                min(92, round(completed_sample_count / total_sample_count * 92)),
            )
            stage = f"checkpoint_saved_{request.year}-{completed_month:02d}"

            month_payload = next(
                (
                    m.model_dump(mode="json")
                    for m in monthly_results
                    if m.month == completed_month
                ),
                monthly_results[-1].model_dump(mode="json"),
            )
            all_payloads = [m.model_dump(mode="json") for m in monthly_results]

            with SessionLocal() as session:
                if _batch_cancel_requested(session, batch_id):
                    raise GlobalBatchCancelledError()

                retry_count = session.execute(
                    select(GlobalCityResult.retry_count).where(
                        GlobalCityResult.id == city_result_id
                    )
                ).scalar_one()

                # (a) durable checkpoint：真相來源
                upsert_month_checkpoint(
                    session,
                    city_result_id,
                    month=completed_month,
                    attempt=retry_count,
                    payload=month_payload,
                )

                # (b) city 衍生欄位 + 心跳，同一 transaction、租約保護
                ok = heartbeat_city_lease(
                    session,
                    city_result_id,
                    owner,
                    monthly_json=all_payloads,
                    completed_month_count=len(monthly_results),
                    last_checkpoint_month=completed_month,
                    stage=stage,
                    progress=func.greatest(
                        GlobalCityResult.progress, checkpoint_progress
                    ),
                )
                # heartbeat_city_lease 內部 commit，(a)(b) 一起落地

            if not ok:
                lease_lost = True
                raise LeaseLostError()

            last_beat = time.monotonic()

            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": city_result_id,
                    "city_id": city_id,
                    "progress": checkpoint_progress,
                    "stage": stage,
                    "completed_month": completed_month,
                },
            )

        # ---- 4. 跑分析 ----
        analysis = asyncio.run(
            analyze_city_climate_adaptation(
                city_id=city_id,
                request=request,
                progress_callback=report,
                checkpoint_callback=save_checkpoint,
                initial_monthly_results=initial_monthly_results,
            )
        )

        # ---- 5. 完成寫入（租約保護） ----
        monthly_json = analysis["monthly_results"]
        last_month = (
            max(item["month"] for item in monthly_json) if monthly_json else None
        )

        with SessionLocal() as session:
            if _batch_cancel_requested(session, batch_id):
                raise GlobalBatchCancelledError()

            ok = _finish_city_as_owner(
                session,
                city_result_id,
                owner,
                CityStatus.COMPLETED,
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
                    "data_quality": analysis.get("data_quality", {}),
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

        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "completed",
        }

    except LeaseLostError:
        # 租約已被收回：別人在跑或 reaper 已處理。絕對不要再寫 DB。
        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "lease_lost",
        }

    except GlobalBatchCancelledError:
        if batch_id is not None:
            with SessionLocal() as session:
                _finish_city_as_owner(
                    session,
                    city_result_id,
                    owner,
                    CityStatus.CANCELLED,
                    progress=100,
                )
                refresh_batch_status(session, batch_id)

        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "cancelled",
        }

    except Exception as error:
        logger.exception("city %s failed", city_result_id)
        requeue = False
        if batch_id is not None:
            with SessionLocal() as session:
                requeue = _fail_or_requeue_city(
                    session, city_result_id, owner, error
                )
                refresh_batch_status(session, batch_id)

        if requeue:
            run_global_city_analysis_task.apply_async(
                args=[city_result_id],
                countdown=settings.CITY_HEARTBEAT_SECONDS,
            )
            return {
                "batch_id": batch_id,
                "city_result_id": city_result_id,
                "status": "requeued",
                "error": str(error)[:500],
            }
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_city_lease(session, city_result_id, owner)

@celery_app.task(name="global_batch.reap_expired_leases")
def reap_expired_leases():
    with SessionLocal() as db:
        stale = db.execute(
            select(GlobalCityResult)
            .where(GlobalCityResult.status == CityStatus.RUNNING,
                   GlobalCityResult.lease_expires_at < func.now())
            .with_for_update(skip_locked=True)
        ).scalars().all()

        touched_batches = set()
        for city in stale:
            if city.retry_count < settings.CITY_MAX_RETRIES:
                assert_city_transition(city.status, CityStatus.QUEUED)
                city.status = CityStatus.QUEUED
                city.retry_count += 1
                city.lease_owner = None
                city.lease_expires_at = None
                db.commit()
                run_global_city_analysis_task.delay(city.id)                 # 重新投遞
            else:
                assert_city_transition(city.status, CityStatus.FAILED)
                city.status = CityStatus.FAILED
                city.error_message = f"lease expired after {city.retry_count} retries"
                city.lease_owner = None
                db.commit()
            touched_batches.add(city.batch_id)

        for bid in touched_batches:
            reconcile_batch(db, bid)