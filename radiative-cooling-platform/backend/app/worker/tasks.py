import asyncio
from datetime import (
    datetime,
    timezone,
)

from celery import Task

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


class JobCancelledError(Exception):
    pass


class GlobalBatchCancelledError(Exception):
    pass


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def update_job(
    job_id: str,
    **values: object,
) -> None:
    with SessionLocal() as session:
        job = session.get(
            SimulationJob,
            job_id,
        )

        if job is None:
            raise RuntimeError(
                f"Simulation task not found:{job_id}"
            )

        for field, value in values.items():
            setattr(job, field, value)

        session.commit()


def ensure_not_cancelled(
    job_id: str,
) -> None:
    with SessionLocal() as session:
        job = session.get(
            SimulationJob,
            job_id,
        )

        if job is None:
            raise RuntimeError(
                f"Simulation task not found:{job_id}"
            )

        if job.status in {
            "cancelling",
            "cancelled",
        }:
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


def ensure_global_batch_not_cancelled(
    batch_id: str,
) -> None:
    with SessionLocal() as session:
        batch = session.get(
            GlobalBatchJob,
            batch_id,
        )

        if batch is None:
            raise RuntimeError(
                f"Global batch not found: {batch_id}"
            )

        if batch.status in {
            "cancelling",
            "cancelled",
        }:
            raise GlobalBatchCancelledError()


@celery_app.task(
    bind=True,
    name="global_batch.run_city",
    acks_late=True,
)
def run_global_city_analysis_task(
    self: Task,
    city_result_id: str,
) -> dict:
    batch_id: str | None = None

    try:
        with SessionLocal() as session:
            city_result = session.get(
                GlobalCityResult,
                city_result_id,
            )

            if city_result is None:
                raise RuntimeError(
                    "Global city result not found: "
                    f"{city_result_id}"
                )

            batch = session.get(
                GlobalBatchJob,
                city_result.batch_id,
            )

            if batch is None:
                raise RuntimeError(
                    "Global batch not found: "
                    f"{city_result.batch_id}"
                )

            batch_id = batch.id

            request = GlobalBatchCreate.model_validate(
                batch.request_json
            )

            city_id = city_result.city_id

            initial_monthly_results: list[
                MonthlyAdaptationResult
            ] = []

            if (
                request.resume_from_checkpoint
                and city_result.monthly_json
            ):
                initial_monthly_results = [
                    MonthlyAdaptationResult.model_validate(
                        item
                    )
                    for item in city_result.monthly_json
                ]

            now = utc_now()

            city_result.status = "running"
            city_result.stage = "initializing"
            city_result.progress = 1
            city_result.started_at = (
                city_result.started_at or now
            )
            city_result.completed_at = None
            city_result.last_heartbeat_at = now
            city_result.error_message = None
            city_result.resumed_from_checkpoint = bool(
                initial_monthly_results
            )

            if batch.status in {
                "queued",
                "failed",
                "partial_completed",
            }:
                batch.status = "running"
                batch.stage = "analyzing_cities"
                batch.started_at = (
                    batch.started_at or now
                )
                batch.completed_at = None

            session.commit()

        if batch_id is None:
            raise RuntimeError(
                "Global batch ID was not initialized"
            )

        total_sample_count = max(
            1,
            estimate_sample_count(request),
        )

        def report(
            progress: int,
            stage: str,
        ) -> None:
            ensure_global_batch_not_cancelled(
                batch_id
            )

            heartbeat = utc_now()

            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is None:
                    raise RuntimeError(
                        "Global city result disappeared"
                    )

                result.status = "running"
                result.stage = stage
                result.progress = max(
                    0,
                    min(progress, 100),
                )
                result.last_heartbeat_at = heartbeat

                session.commit()

            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": city_result_id,
                    "city_id": city_id,
                    "progress": progress,
                    "stage": stage,
                    "last_heartbeat_at": (
                        heartbeat.isoformat()
                    ),
                },
            )

        def save_checkpoint(
            monthly_results: list[
                MonthlyAdaptationResult
            ],
            completed_month: int,
            completed_sample_count: int,
        ) -> None:
            ensure_global_batch_not_cancelled(
                batch_id
            )

            heartbeat = utc_now()

            checkpoint_progress = max(
                1,
                min(
                    92,
                    round(
                        completed_sample_count
                        / total_sample_count
                        * 92
                    ),
                ),
            )

            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is None:
                    raise RuntimeError(
                        "Global city result disappeared"
                    )

                result.monthly_json = [
                    monthly_result.model_dump(
                        mode="json"
                    )
                    for monthly_result in monthly_results
                ]

                result.completed_month_count = len(
                    monthly_results
                )
                result.last_checkpoint_month = (
                    completed_month
                )
                result.last_heartbeat_at = heartbeat
                result.stage = (
                    f"checkpoint_saved_"
                    f"{request.year}-"
                    f"{completed_month:02d}"
                )
                result.progress = max(
                    result.progress,
                    checkpoint_progress,
                )

                session.commit()

            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": city_result_id,
                    "city_id": city_id,
                    "progress": checkpoint_progress,
                    "stage": (
                        f"checkpoint_saved_"
                        f"{request.year}-"
                        f"{completed_month:02d}"
                    ),
                    "completed_month": completed_month,
                },
            )

        analysis = asyncio.run(
            analyze_city_climate_adaptation(
                city_id=city_id,
                request=request,
                progress_callback=report,
                checkpoint_callback=save_checkpoint,
                initial_monthly_results=(
                    initial_monthly_results
                ),
            )
        )

        ensure_global_batch_not_cancelled(
            batch_id
        )

        completed_at = utc_now()

        with SessionLocal() as session:
            result = session.get(
                GlobalCityResult,
                city_result_id,
            )

            if result is None:
                raise RuntimeError(
                    "Global city result disappeared"
                )

            result.status = "completed"
            result.stage = "completed"
            result.progress = 100

            result.climate_adaptation_rate_percent = (
                analysis[
                    "climate_adaptation_rate_percent"
                ]
            )

            result.exposure_coverage_percent = (
                analysis[
                    "exposure_coverage_percent"
                ]
            )

            result.annual_average_skin_improvement_c = (
                analysis[
                    "annual_average_skin_improvement_c"
                ]
            )

            result.annual_average_core_improvement_c = (
                analysis[
                    "annual_average_core_improvement_c"
                ]
            )

            result.maximum_skin_improvement_c = analysis[
                "maximum_skin_improvement_c"
            ]

            result.effective_cooling_hours = analysis[
                "effective_cooling_hours"
            ]

            result.sampled_day_count = analysis[
                "sampled_day_count"
            ]

            result.eligible_sample_count = analysis[
                "eligible_sample_count"
            ]

            result.evaluated_weighted_days = analysis[
                "evaluated_weighted_days"
            ]

            result.beneficial_weighted_days = analysis[
                "beneficial_weighted_days"
            ]

            result.skin_improvement_p50_c = analysis[
                "skin_improvement_p50_c"
            ]

            result.skin_improvement_p90_c = analysis[
                "skin_improvement_p90_c"
            ]

            result.skin_improvement_p95_c = analysis[
                "skin_improvement_p95_c"
            ]

            result.core_improvement_p50_c = analysis[
                "core_improvement_p50_c"
            ]

            result.core_improvement_p90_c = analysis[
                "core_improvement_p90_c"
            ]

            result.core_improvement_p95_c = analysis[
                "core_improvement_p95_c"
            ]

            result.heatwave_event_count = analysis[
                "heatwave_event_count"
            ]

            result.longest_heatwave_days = analysis[
                "longest_heatwave_days"
            ]

            result.analytics_json = {
                "heatwave_analysis_available": analysis[
                    "heatwave_analysis_available"
                ],
                "heatwave_events": analysis[
                    "heatwave_events"
                ],
            }

            result.monthly_json = analysis[
                "monthly_results"
            ]

            result.completed_month_count = analysis[
                "completed_month_count"
            ]

            if result.monthly_json:
                result.last_checkpoint_month = max(
                    item["month"]
                    for item in result.monthly_json
                )

            result.error_message = None
            result.last_heartbeat_at = completed_at
            result.completed_at = completed_at

            session.commit()

            refresh_batch_status(
                session,
                batch_id,
            )

        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "completed",
        }

    except GlobalBatchCancelledError:
        if batch_id is not None:
            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is not None:
                    now = utc_now()

                    result.status = "cancelled"
                    result.stage = "cancelled"
                    result.progress = 100
                    result.last_heartbeat_at = now
                    result.completed_at = now

                    session.commit()

                refresh_batch_status(
                    session,
                    batch_id,
                )

        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "cancelled",
        }

    except Exception as error:
        if batch_id is not None:
            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is not None:
                    now = utc_now()

                    result.status = "failed"
                    result.stage = "failed"
                    result.error_message = str(
                        error
                    )[:4000]
                    result.last_heartbeat_at = now
                    result.completed_at = now

                    session.commit()

                refresh_batch_status(
                    session,
                    batch_id,
                )

        raise