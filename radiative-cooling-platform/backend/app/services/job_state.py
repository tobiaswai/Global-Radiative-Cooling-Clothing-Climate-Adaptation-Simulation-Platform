from enum import StrEnum


class BatchStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    CANCELLING = "cancelling"
    COMPLETED = "completed"      # ← 對齊 Step 1 盤點到的既有字串
    FAILED = "failed"
    CANCELLED = "cancelled"


class CityStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


BATCH_TRANSITIONS: dict[BatchStatus, frozenset[BatchStatus]] = {
    BatchStatus.QUEUED:     frozenset({BatchStatus.RUNNING, BatchStatus.CANCELLING, BatchStatus.CANCELLED, BatchStatus.FAILED}),
    BatchStatus.RUNNING:    frozenset({BatchStatus.COMPLETED, BatchStatus.FAILED, BatchStatus.CANCELLING}),
    BatchStatus.CANCELLING: frozenset({BatchStatus.CANCELLED, BatchStatus.FAILED}),
    BatchStatus.COMPLETED:  frozenset(),
    BatchStatus.FAILED:     frozenset(),
    BatchStatus.CANCELLED:  frozenset(),
}

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
    """所有 city 都 terminal 時回傳 batch 應收斂到的狀態，否則 None。"""
    done = counts.get("completed", 0) + counts.get("failed", 0) + counts.get("cancelled", 0)
    if done < total:
        return None
    if cancel_requested or counts.get("cancelled", 0):
        return BatchStatus.CANCELLED
    if counts.get("failed", 0):
        return BatchStatus.FAILED
    return BatchStatus.COMPLETED