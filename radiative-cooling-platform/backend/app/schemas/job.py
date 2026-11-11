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

LeaseState = Literal["none", "live", "expired"]


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
    # Stage 4. Set when the request referenced material library versions.
    control_material_version_id: str | None = None
    rc_material_version_id: str | None = None
    # Stage 9
    attempt: int = 0
    lease_owner: str | None = None
    lease_expires_at: datetime | None = None
    last_heartbeat_at: datetime | None = None
    lease_state: LeaseState = "none"
    
class SimulationJobDetail(
    SimulationJobResponse
):
    request: WeatherSimulationRequest


class SimulationJobListResponse(BaseModel):
    items: list[SimulationJobResponse]
    total: int
    limit: int
    offset: int