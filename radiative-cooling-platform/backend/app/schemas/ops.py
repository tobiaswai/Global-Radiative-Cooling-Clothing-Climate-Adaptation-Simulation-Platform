"""Operational health of the asynchronous pipeline (Stage 8)."""

from datetime import datetime

from pydantic import BaseModel, Field


class WorkerStatus(BaseModel):
    name: str
    active_task_count: int
    reserved_task_count: int


class LeaseSummary(BaseModel):
    running_cities: int
    queued_cities: int
    live_leases: int
    expired_leases: int
    running_batches: int
    cancelling_batches: int


class OpsStatusResponse(BaseModel):
    checked_at: datetime
    broker_reachable: bool
    worker_count: int
    workers: list[WorkerStatus] = Field(default_factory=list)
    leases: LeaseSummary
    lease_ttl_seconds: int
    heartbeat_interval_seconds: int
    reaper_interval_seconds: int
    # Upper bound on time-to-recovery after a hard worker kill.
    worst_case_recovery_seconds: int