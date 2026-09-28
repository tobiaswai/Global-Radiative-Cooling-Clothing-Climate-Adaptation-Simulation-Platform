"""Weather timeline validation (Stage 1, PR-1).

Every weather series that reaches the thermal model must pass through
``normalize_timeline`` (sort / de-duplicate / detect gaps). The exposure
window that is actually simulated must additionally pass
``ensure_window_covered``, which rejects any series that does not fully
bracket the window or that has a missing step inside it.

Design decisions
----------------
* Errors subclass ``ValueError`` so the existing API handlers map them to
  HTTP 422 without changes. Each error carries a stable ``code`` string.
* No interpolation across missing hours is performed silently. A gap inside
  the exposure window is always an error.
* Timestamps must be timezone-aware. Naive timestamps are rejected rather
  than guessed.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Sequence
from datetime import datetime, timedelta

from app.schemas.weather import (
    WeatherGap,
    WeatherPoint,
    WeatherQualityReport,
)


DEFAULT_STEP_SECONDS = 3600
STEP_TOLERANCE_FRACTION = 0.001


class WeatherDataError(ValueError):
    """Base class for weather-data problems that invalidate a simulation."""

    code: str = "WEATHER_DATA_ERROR"

    def __init__(
        self,
        message: str,
        *,
        context: dict[str, str] | None = None,
    ) -> None:
        super().__init__(message)
        self.context: dict[str, str] = dict(context or {})

    def to_detail(self) -> dict[str, str]:
        """Structured payload for HTTP error responses."""
        return {
            "code": self.code,
            "message": str(self),
            **self.context,
        }


class WeatherNaiveTimestampError(WeatherDataError):
    code = "WEATHER_NAIVE_TIMESTAMP"


class WeatherDuplicateConflictError(WeatherDataError):
    code = "WEATHER_DUPLICATE_CONFLICT"


class WeatherGapInWindowError(WeatherDataError):
    code = "WEATHER_GAP_IN_WINDOW"


class WeatherInsufficientCoverageError(WeatherDataError):
    code = "WEATHER_INSUFFICIENT_COVERAGE"


def payload_sha256(payload: dict) -> str:
    """Deterministic hash of a provider payload for reproducibility records."""
    serialized = json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=True,
        separators=(",", ":"),
        default=str,
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def infer_step_seconds(timestamps: Sequence[datetime]) -> int:
    """Return the most common positive spacing, defaulting to one hour."""
    if len(timestamps) < 2:
        return DEFAULT_STEP_SECONDS

    diffs = Counter(
        int((later - earlier).total_seconds())
        for earlier, later in zip(timestamps, timestamps[1:])
        if later > earlier
    )

    if not diffs:
        return DEFAULT_STEP_SECONDS

    return diffs.most_common(1)[0][0]


def _values_without_timestamp(point: WeatherPoint) -> dict:
    return point.model_dump(exclude={"timestamp"})


def detect_gaps(
    points: Sequence[WeatherPoint],
    step_seconds: int,
) -> list[WeatherGap]:
    """Find consecutive pairs spaced by more than one expected step."""
    step = timedelta(seconds=step_seconds)
    tolerance = timedelta(
        seconds=step_seconds * (1.0 + STEP_TOLERANCE_FRACTION)
    )

    gaps: list[WeatherGap] = []

    for previous, current in zip(points, points[1:]):
        delta = current.timestamp - previous.timestamp

        if delta > tolerance:
            missing_steps = int(round(delta / step)) - 1

            gaps.append(
                WeatherGap(
                    start=previous.timestamp,
                    end=current.timestamp,
                    missing_steps=max(1, missing_steps),
                )
            )

    return gaps


def normalize_timeline(
    points: Sequence[WeatherPoint],
    *,
    expected_step_seconds: int | None = None,
) -> tuple[list[WeatherPoint], WeatherQualityReport]:
    """Sort, de-duplicate and audit a raw weather timeline.

    Returns the cleaned points and a report. Raises on conditions that
    cannot be repaired safely (naive timestamps, conflicting duplicates).
    Gaps are recorded in the report but not raised here; use
    ``ensure_window_covered`` for the window that is actually simulated.
    """
    notes: list[str] = []

    if not points:
        return [], WeatherQualityReport(
            expected_step_seconds=(
                expected_step_seconds or DEFAULT_STEP_SECONDS
            ),
            point_count=0,
            notes=["input timeline is empty"],
        )

    for point in points:
        timestamp = point.timestamp

        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise WeatherNaiveTimestampError(
                "Weather timestamps must be timezone-aware; "
                f"received naive timestamp {timestamp.isoformat()}",
                context={"timestamp": timestamp.isoformat()},
            )

    timestamps = [point.timestamp for point in points]

    was_sorted = all(
        later >= earlier
        for earlier, later in zip(timestamps, timestamps[1:])
    )

    ordered = sorted(points, key=lambda point: point.timestamp)

    if not was_sorted:
        notes.append("input points were not sorted; sorted by timestamp")

    deduplicated: list[WeatherPoint] = []
    duplicates_removed = 0

    for point in ordered:
        if (
            deduplicated
            and deduplicated[-1].timestamp == point.timestamp
        ):
            if _values_without_timestamp(
                deduplicated[-1]
            ) == _values_without_timestamp(point):
                duplicates_removed += 1
                continue

            raise WeatherDuplicateConflictError(
                "Conflicting weather values share the same timestamp "
                f"{point.timestamp.isoformat()}",
                context={"timestamp": point.timestamp.isoformat()},
            )

        deduplicated.append(point)

    if duplicates_removed:
        notes.append(
            f"removed {duplicates_removed} identical duplicate timestamp(s)"
        )

    step_seconds = expected_step_seconds or infer_step_seconds(
        [point.timestamp for point in deduplicated]
    )

    gaps = detect_gaps(deduplicated, step_seconds)

    if gaps:
        notes.append(f"detected {len(gaps)} gap(s) in the timeline")

    report = WeatherQualityReport(
        expected_step_seconds=step_seconds,
        point_count=len(deduplicated),
        first_timestamp=deduplicated[0].timestamp,
        last_timestamp=deduplicated[-1].timestamp,
        was_sorted=was_sorted,
        duplicates_removed=duplicates_removed,
        gaps=gaps,
        notes=notes,
    )

    return deduplicated, report


def ensure_window_covered(
    points: Sequence[WeatherPoint],
    *,
    window_start: datetime,
    window_end: datetime,
    step_seconds: int = DEFAULT_STEP_SECONDS,
    label: str = "Weather series",
) -> None:
    """Raise unless ``points`` fully bracket ``[window_start, window_end]``.

    ``points`` must already be normalised (sorted, unique timestamps).
    Linear interpolation needs a point at or before the window start and a
    point at or after the window end, with no missing step in between.
    """
    if window_end <= window_start:
        raise ValueError("window_end must be after window_start")

    if len(points) < 2:
        raise WeatherInsufficientCoverageError(
            f"{label} has fewer than two points",
            context={
                "window_start": window_start.isoformat(),
                "window_end": window_end.isoformat(),
            },
        )

    first = points[0].timestamp
    last = points[-1].timestamp

    if first > window_start or last < window_end:
        raise WeatherInsufficientCoverageError(
            f"{label} does not cover the exposure window "
            f"{window_start.isoformat()} to {window_end.isoformat()}; "
            f"available data spans {first.isoformat()} to {last.isoformat()}",
            context={
                "window_start": window_start.isoformat(),
                "window_end": window_end.isoformat(),
                "available_start": first.isoformat(),
                "available_end": last.isoformat(),
            },
        )

    for gap in detect_gaps(points, step_seconds):
        overlaps_window = (
            gap.end > window_start and gap.start < window_end
        )

        if overlaps_window:
            raise WeatherGapInWindowError(
                f"{label} has a gap of {gap.missing_steps} missing step(s) "
                f"between {gap.start.isoformat()} and {gap.end.isoformat()} "
                "inside the exposure window",
                context={
                    "gap_start": gap.start.isoformat(),
                    "gap_end": gap.end.isoformat(),
                    "missing_steps": str(gap.missing_steps),
                },
            )