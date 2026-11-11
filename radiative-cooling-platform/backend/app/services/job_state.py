"""Status enums and legal transitions for batches, cities and single jobs.

Every status write in the worker and the API goes through ``assert_*``;
an illegal transition is a programming error, not a runtime condition.
"""

from enum import StrEnum


class BatchStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    CANCELLING = "cancelling"
    COMPLETED = "completed"
    PARTIAL_COMPLETED = "partial_completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class CityStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"


BATCH_TRANSITIONS: dict[BatchStatus, frozenset[BatchStatus]] = {
    BatchStatus.QUEUED: frozenset({
        BatchStatus.RUNNING, BatchStatus.CANCELLING, BatchStatus.CANCELLED, BatchStatus.FAILED,
    }),
    BatchStatus.RUNNING: frozenset({
        BatchStatus.COMPLETED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.FAILED,
        BatchStatus.CANCELLING, BatchStatus.CANCELLED,
    }),
    BatchStatus.CANCELLING: frozenset({
        BatchStatus.CANCELLED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.COMPLETED, BatchStatus.FAILED,
    }),
    # POST /retry-failed re-opens a batch.
    BatchStatus.FAILED: frozenset({BatchStatus.RUNNING}),
    BatchStatus.PARTIAL_COMPLETED: frozenset({BatchStatus.RUNNING}),
    BatchStatus.COMPLETED: frozenset(),
    BatchStatus.CANCELLED: frozenset(),
}

TERMINAL_BATCH = frozenset({
    BatchStatus.COMPLETED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.FAILED, BatchStatus.CANCELLED,
})

CITY_TRANSITIONS: dict[CityStatus, frozenset[CityStatus]] = {
    CityStatus.QUEUED: frozenset({CityStatus.RUNNING, CityStatus.CANCELLED}),
    # RUNNING -> QUEUED: lease expired (reaper) or retryable failure.
    CityStatus.RUNNING: frozenset({
        CityStatus.COMPLETED, CityStatus.FAILED, CityStatus.CANCELLED, CityStatus.QUEUED,
    }),
    CityStatus.COMPLETED: frozenset(),
    # FAILED -> QUEUED: explicit POST /retry-failed (Stage 9; was missing).
    CityStatus.FAILED: frozenset({CityStatus.QUEUED}),
    CityStatus.CANCELLED: frozenset(),
}

TERMINAL_CITY = frozenset({CityStatus.COMPLETED, CityStatus.FAILED, CityStatus.CANCELLED})

JOB_TRANSITIONS: dict[JobStatus, frozenset[JobStatus]] = {
    JobStatus.QUEUED: frozenset({JobStatus.RUNNING, JobStatus.CANCELLED, JobStatus.FAILED}),
    # RUNNING -> QUEUED: lease expired, re-queued by the reaper.
    JobStatus.RUNNING: frozenset({
        JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLING, JobStatus.CANCELLED, JobStatus.QUEUED,
    }),
    # Cancel requested while the worker was finishing: any terminal outcome is legal.
    JobStatus.CANCELLING: frozenset({JobStatus.CANCELLED, JobStatus.COMPLETED, JobStatus.FAILED}),
    JobStatus.COMPLETED: frozenset(),
    JobStatus.FAILED: frozenset(),
    JobStatus.CANCELLED: frozenset(),
}

TERMINAL_JOB = frozenset({JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED})


class IllegalTransition(Exception):
    pass


def assert_batch_transition(current: str, target: str) -> None:
    if BatchStatus(target) not in BATCH_TRANSITIONS[BatchStatus(current)]:
        raise IllegalTransition(f"batch {current} -> {target}")


def assert_city_transition(current: str, target: str) -> None:
    if CityStatus(target) not in CITY_TRANSITIONS[CityStatus(current)]:
        raise IllegalTransition(f"city {current} -> {target}")


def assert_job_transition(current: str, target: str) -> None:
    if JobStatus(target) not in JOB_TRANSITIONS[JobStatus(current)]:
        raise IllegalTransition(f"job {current} -> {target}")


def derive_batch_status(
    counts: dict[str, int],
    total: int,
    cancel_requested: bool = False,
) -> BatchStatus | None:
    """Same rule as global_batch_service.refresh_batch_status.

    Returns None while any city is still pending. ``cancel_requested`` makes
    a batch that produced nothing report CANCELLED rather than FAILED.
    """
    completed = counts.get("completed", 0)
    failed = counts.get("failed", 0)
    cancelled = counts.get("cancelled", 0)

    if completed + failed + cancelled < total:
        return None
    if cancelled == total:
        return BatchStatus.CANCELLED
    if completed == 0:
        return BatchStatus.CANCELLED if cancel_requested else BatchStatus.FAILED
    if failed or cancelled:
        return BatchStatus.PARTIAL_COMPLETED
    return BatchStatus.COMPLETED