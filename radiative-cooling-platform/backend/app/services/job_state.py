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


BATCH_TRANSITIONS: dict[BatchStatus, frozenset[BatchStatus]] = {
    BatchStatus.QUEUED: frozenset({
        BatchStatus.RUNNING, BatchStatus.CANCELLING, BatchStatus.CANCELLED, BatchStatus.FAILED,
    }),
    BatchStatus.RUNNING: frozenset({
        BatchStatus.COMPLETED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.FAILED,
        BatchStatus.CANCELLING, BatchStatus.CANCELLED,
    }),
    # Cancel requested while cities were already finishing: any terminal outcome is legal.
    BatchStatus.CANCELLING: frozenset({
        BatchStatus.CANCELLED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.COMPLETED, BatchStatus.FAILED,
    }),
    # Retry (POST /retry-failed) re-opens a batch.
    BatchStatus.FAILED: frozenset({BatchStatus.RUNNING}),
    BatchStatus.PARTIAL_COMPLETED: frozenset({BatchStatus.RUNNING}),
    BatchStatus.COMPLETED: frozenset(),
    BatchStatus.CANCELLED: frozenset(),
}

TERMINAL_BATCH = frozenset({
    BatchStatus.COMPLETED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.FAILED, BatchStatus.CANCELLED,
})

CITY_TRANSITIONS: dict[CityStatus, frozenset[CityStatus]] = {
    CityStatus.QUEUED:    frozenset({CityStatus.RUNNING, CityStatus.CANCELLED}),
    CityStatus.RUNNING:   frozenset({CityStatus.COMPLETED, CityStatus.FAILED, CityStatus.CANCELLED, CityStatus.QUEUED}),  # QUEUED = lease 過期重排
    CityStatus.COMPLETED: frozenset(),
    CityStatus.FAILED:    frozenset(),
    CityStatus.CANCELLED: frozenset(),
}

TERMINAL_CITY = frozenset({CityStatus.COMPLETED, CityStatus.FAILED, CityStatus.CANCELLED})


class IllegalTransition(Exception):
    pass


def assert_batch_transition(current: str, target: str) -> None:
    if BatchStatus(target) not in BATCH_TRANSITIONS[BatchStatus(current)]:
        raise IllegalTransition(f"batch {current} -> {target}")


def assert_city_transition(current: str, target: str) -> None:
    if CityStatus(target) not in CITY_TRANSITIONS[CityStatus(current)]:
        raise IllegalTransition(f"city {current} -> {target}")


def derive_batch_status(counts: dict[str, int], total: int, cancel_requested: bool) -> BatchStatus | None:
    """Same rule as global_batch_service.refresh_batch_status; None while cities are pending."""
    completed = counts.get("completed", 0)
    failed = counts.get("failed", 0)
    cancelled = counts.get("cancelled", 0)
    if completed + failed + cancelled < total:
        return None
    if cancelled == total:
        return BatchStatus.CANCELLED
    if completed == 0:
        return BatchStatus.FAILED
    if failed or cancelled:
        return BatchStatus.PARTIAL_COMPLETED
    return BatchStatus.COMPLETED