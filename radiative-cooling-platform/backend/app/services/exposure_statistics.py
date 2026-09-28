"""Exposure-window statistics (Stage 1, PR-3).

Scenario-level weather statistics are computed strictly over the exposure
window ``[requested_start_time, requested_end_time]`` using time-weighted
(trapezoidal) integration of the piecewise-linear hourly series. They are
therefore invariant to the interpolation padding attached to
``weather.points``.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime

import numpy as np

from app.schemas.weather import WeatherTimeSeries
from app.services.weather_quality import (
    WeatherInsufficientCoverageError,
)


@dataclass(frozen=True)
class ExposureWindowStatistics:
    window_start: datetime
    window_end: datetime
    mean_air_temperature_c: float
    maximum_air_temperature_c: float
    mean_solar_radiation_w_m2: float
    maximum_solar_radiation_w_m2: float


def time_weighted_mean(
    times: Sequence[float],
    values: Sequence[float],
) -> float:
    """Trapezoidal time average. Falls back to the arithmetic mean for a
    single point or a zero-length span."""
    t = np.asarray(times, dtype=float)
    y = np.asarray(values, dtype=float)

    if t.size == 0:
        raise ValueError("Cannot average an empty series")

    if t.size == 1 or t[-1] <= t[0]:
        return float(np.mean(y))

    return float(np.trapezoid(y, t) / (t[-1] - t[0]))


def _window_knots(
    relative_seconds: np.ndarray,
    start_s: float,
    end_s: float,
) -> np.ndarray:
    inside = relative_seconds[
        (relative_seconds > start_s) & (relative_seconds < end_s)
    ]
    return np.concatenate(([start_s], inside, [end_s]))


def compute_exposure_window_statistics(
    weather: WeatherTimeSeries,
    *,
    window_start: datetime | None = None,
    window_end: datetime | None = None,
) -> ExposureWindowStatistics:
    """Time-weighted mean / maximum over the exposure window only."""
    window_start = window_start or weather.requested_start_time
    window_end = window_end or weather.requested_end_time

    if window_end <= window_start:
        raise ValueError("window_end must be after window_start")

    origin = weather.points[0].timestamp

    relative_seconds = np.asarray(
        [(p.timestamp - origin).total_seconds() for p in weather.points],
        dtype=float,
    )

    start_s = (window_start - origin).total_seconds()
    end_s = (window_end - origin).total_seconds()

    if start_s < relative_seconds[0] - 1e-6 or end_s > relative_seconds[-1] + 1e-6:
        raise WeatherInsufficientCoverageError(
            "Weather series does not cover the requested statistics window "
            f"{window_start.isoformat()} to {window_end.isoformat()}"
        )

    knots = _window_knots(relative_seconds, start_s, end_s)

    temperatures = np.interp(
        knots,
        relative_seconds,
        [p.air_temperature_c for p in weather.points],
    )

    ghi = np.maximum(
        0.0,
        np.interp(
            knots,
            relative_seconds,
            [p.ghi_w_m2 for p in weather.points],
        ),
    )

    return ExposureWindowStatistics(
        window_start=window_start,
        window_end=window_end,
        mean_air_temperature_c=time_weighted_mean(knots, temperatures),
        maximum_air_temperature_c=float(temperatures.max()),
        mean_solar_radiation_w_m2=time_weighted_mean(knots, ghi),
        maximum_solar_radiation_w_m2=float(ghi.max()),
    )