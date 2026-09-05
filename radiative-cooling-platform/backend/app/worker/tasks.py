import asyncio
from datetime import datetime, timezone

from celery import Task

from app.db.session import SessionLocal
from app.models.simulation_job import (
    SimulationJob,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
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

            request = (
                WeatherSimulationRequest
                .model_validate(
                    job.request_json
                )
            )

        update_job(
            job_id,
            status="running",
            stage="initializing",
            progress=2,
            started_at=datetime.now(
                timezone.utc
            ),
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
            summary_json=(
                result.summary.model_dump(
                    mode="json"
                )
            ),
            result_path=str(result_path),
            completed_at=datetime.now(
                timezone.utc
            ),
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
            completed_at=datetime.now(
                timezone.utc
            ),
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
            completed_at=datetime.now(
                timezone.utc
            ),
        )

        raise

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.services.climate_adaptation import (
    analyze_city_climate_adaptation,
)
from app.services.global_batch_service import (
    refresh_batch_status,
)


class GlobalBatchCancelledError(Exception):
    pass


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

            city_result.status = "running"
            city_result.stage = "initializing"
            city_result.progress = 1
            city_result.started_at = datetime.now(
                timezone.utc
            )
            city_result.error_message = None

            if batch.status == "queued":
                batch.status = "running"
                batch.stage = "analyzing_cities"
                batch.started_at = datetime.now(
                    timezone.utc
                )

            session.commit()

        def report(
            progress: int,
            stage: str,
        ) -> None:
            ensure_global_batch_not_cancelled(
                batch_id
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

                result.status = "running"
                result.stage = stage
                result.progress = progress
                session.commit()

            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": (
                        city_result_id
                    ),
                    "city_id": city_id,
                    "progress": progress,
                    "stage": stage,
                },
            )

        analysis = asyncio.run(
            analyze_city_climate_adaptation(
                city_id=city_id,
                request=request,
                progress_callback=report,
            )
        )

        ensure_global_batch_not_cancelled(
            batch_id
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

            result.status = "completed"
            result.stage = "completed"
            result.progress = 100

            result.climate_adaptation_rate_percent = (
                analysis[
                    "climate_adaptation_rate_percent"
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

            result.maximum_skin_improvement_c = (
                analysis[
                    "maximum_skin_improvement_c"
                ]
            )

            result.effective_cooling_hours = (
                analysis[
                    "effective_cooling_hours"
                ]
            )

            result.evaluated_weighted_days = (
                analysis[
                    "evaluated_weighted_days"
                ]
            )

            result.beneficial_weighted_days = (
                analysis[
                    "beneficial_weighted_days"
                ]
            )

            result.monthly_json = analysis[
                "monthly_results"
            ]

            result.completed_at = datetime.now(
                timezone.utc
            )

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
                    result.status = "cancelled"
                    result.stage = "cancelled"
                    result.completed_at = (
                        datetime.now(timezone.utc)
                    )
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
                    result.status = "failed"
                    result.stage = "failed"
                    result.error_message = str(
                        error
                    )[:4000]
                    result.completed_at = (
                        datetime.now(timezone.utc)
                    )
                    session.commit()

                refresh_batch_status(
                    session,
                    batch_id,
                )

        raise