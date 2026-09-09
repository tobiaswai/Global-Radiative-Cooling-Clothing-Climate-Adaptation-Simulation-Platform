from celery import Celery
from kombu import Queue

from app.core.config import settings


celery_app = Celery(
    "radiative_cooling_worker",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    include=[
        "app.worker.tasks",
    ],
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    worker_prefetch_multiplier=1,
    broker_connection_retry_on_startup=True,
    result_expires=3600,
    task_queues=(
        Queue("default"),
        Queue("global_standard"),
        Queue("global_large"),
    ),
    task_default_queue="default",
    task_routes={
        "simulation.run_weather": {
            "queue": "default",
        },
        "global_batch.run_city": {
            "queue": "global_standard",
        },
    },
)