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
                f"找不到模擬任務：{job_id}"
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
                f"找不到模擬任務：{job_id}"
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
                    f"找不到模擬任務：{job_id}"
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