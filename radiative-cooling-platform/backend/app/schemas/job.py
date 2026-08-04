from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from app.schemas.simulation import (
    WeatherSimulationRequest,
)


JobStatus = Literal[
    "queued",
    "running",
    "cancelling",
    "cancelled",
    "completed",
    "failed",
]


class SimulationJobResponse(BaseModel):
    id: str
    celery_task_id: str | None
    status: JobStatus
    stage: str
    progress: int
    city_id: str

    summary: dict | None
    error_message: str | None

    created_at: datetime
    updated_at: datetime
    started_at: datetime | None
    completed_at: datetime | None


class SimulationJobDetail(
    SimulationJobResponse
):
    request: WeatherSimulationRequest


class SimulationJobListResponse(BaseModel):
    items: list[SimulationJobResponse]
    total: int
    limit: int
    offset: int