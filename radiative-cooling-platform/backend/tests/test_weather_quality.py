from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from app.schemas.weather import WeatherPoint
from app.services.weather_quality import (
    WeatherDuplicateConflictError,
    WeatherGapInWindowError,
    WeatherInsufficientCoverageError,
    WeatherNaiveTimestampError,
    ensure_window_covered,
    normalize_timeline,
)


TZ = ZoneInfo("Asia/Dubai")
BASE = datetime(2023, 7, 15, 9, tzinfo=TZ)


def make_point(timestamp: datetime, temperature: float = 30.0) -> WeatherPoint:
    return WeatherPoint(
        timestamp=timestamp,
        air_temperature_c=temperature,
        relative_humidity_percent=40.0,
        wind_speed_m_s=2.0,
        ghi_w_m2=600.0,
        direct_radiation_w_m2=450.0,
        diffuse_radiation_w_m2=150.0,
        dni_w_m2=700.0,
    )


def hourly(count: int, *, skip: set[int] = frozenset()) -> list[WeatherPoint]:
    return [
        make_point(BASE + timedelta(hours=index), 30.0 + index)
        for index in range(count)
        if index not in skip
    ]


@pytest.mark.unit
def test_unsorted_input_is_sorted_and_noted():
    points = list(reversed(hourly(4)))

    cleaned, report = normalize_timeline(points)

    assert [p.timestamp for p in cleaned] == sorted(p.timestamp for p in points)
    assert report.was_sorted is False
    assert any("not sorted" in note for note in report.notes)


@pytest.mark.unit
def test_identical_duplicate_is_removed():
    points = hourly(3) + [make_point(BASE + timedelta(hours=1), 31.0)]

    cleaned, report = normalize_timeline(points)

    assert len(cleaned) == 3
    assert report.duplicates_removed == 1


@pytest.mark.unit
def test_conflicting_duplicate_is_rejected():
    points = hourly(3) + [make_point(BASE + timedelta(hours=1), 99.0)]

    with pytest.raises(WeatherDuplicateConflictError):
        normalize_timeline(points)


@pytest.mark.unit
def test_naive_timestamp_is_rejected():
    naive = make_point(datetime(2023, 7, 15, 9))

    with pytest.raises(WeatherNaiveTimestampError):
        normalize_timeline([naive])


@pytest.mark.unit
def test_gap_is_reported_but_not_raised_by_normalize():
    cleaned, report = normalize_timeline(hourly(6, skip={3}))

    assert len(cleaned) == 5
    assert len(report.gaps) == 1
    assert report.gaps[0].missing_steps == 1
    assert report.expected_step_seconds == 3600


@pytest.mark.unit
def test_window_with_gap_inside_is_rejected():
    cleaned, report = normalize_timeline(hourly(6, skip={3}))

    with pytest.raises(WeatherGapInWindowError):
        ensure_window_covered(
            cleaned,
            window_start=BASE + timedelta(hours=1),
            window_end=BASE + timedelta(hours=4),
            step_seconds=report.expected_step_seconds,
        )


@pytest.mark.unit
def test_window_outside_gap_is_accepted():
    cleaned, report = normalize_timeline(hourly(6, skip={5}))

    ensure_window_covered(
        cleaned,
        window_start=BASE + timedelta(hours=1),
        window_end=BASE + timedelta(hours=3),
        step_seconds=report.expected_step_seconds,
    )


@pytest.mark.unit
def test_missing_tail_is_rejected():
    cleaned, report = normalize_timeline(hourly(4))  # 09:00 .. 12:00

    with pytest.raises(WeatherInsufficientCoverageError, match="does not cover"):
        ensure_window_covered(
            cleaned,
            window_start=BASE + timedelta(hours=1),
            window_end=BASE + timedelta(hours=3, minutes=1),
            step_seconds=report.expected_step_seconds,
        )


@pytest.mark.unit
def test_exact_boundaries_are_accepted():
    cleaned, report = normalize_timeline(hourly(4))

    ensure_window_covered(
        cleaned,
        window_start=BASE,
        window_end=BASE + timedelta(hours=3),
        step_seconds=report.expected_step_seconds,
    )