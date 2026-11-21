"""Feature extraction for surrogate models (ADR 0011).

Weather features describe the environment the physics engine actually used
(derived T_sky and T_surround included), averaged over the exposure window.
"""

from __future__ import annotations

import math

import numpy as np

from app.services.exposure_statistics import time_weighted_mean
from app.services.psychrometrics import vapor_pressure_kpa
from app.services.weather_interpolation import WeatherInterpolator

WEATHER_FEATURES: tuple[str, ...] = (
    "air_temperature_mean_c",
    "air_temperature_max_c",
    "relative_humidity_mean_percent",
    "vapor_pressure_mean_kpa",
    "wind_speed_mean_m_s",
    "ghi_mean_w_m2",
    "ghi_max_w_m2",
    "dni_mean_w_m2",
    "dhi_mean_w_m2",
    "sky_temperature_mean_c",
    "surround_temperature_mean_c",
    "surround_temperature_max_c",
)

FEATURE_STEP_SECONDS = 300.0


def window_times(duration_minutes: int) -> np.ndarray:
    end = duration_minutes * 60.0
    times = np.arange(0.0, end + 0.1, FEATURE_STEP_SECONDS)
    if times[-1] < end:
        times = np.append(times, end)
    return times


def weather_features(interpolator: WeatherInterpolator, duration_minutes: int) -> dict[str, float]:
    times = window_times(duration_minutes)
    environments = [interpolator.environment_at(float(t)) for t in times]

    def series(getter) -> list[float]:
        return [float(getter(e)) for e in environments]

    def mean(values: list[float]) -> float:
        if any(math.isnan(v) for v in values):
            return math.nan
        return time_weighted_mean(times, values)

    air = series(lambda e: e.air_temperature_c)
    rh = series(lambda e: e.relative_humidity_percent)
    ghi = series(lambda e: e.solar_radiation_w_m2)
    surround = series(lambda e: e.mean_radiant_temperature_c)
    nan = math.nan

    return {
        "air_temperature_mean_c": mean(air),
        "air_temperature_max_c": max(air),
        "relative_humidity_mean_percent": mean(rh),
        "vapor_pressure_mean_kpa": mean([vapor_pressure_kpa(a, r) for a, r in zip(air, rh)]),
        "wind_speed_mean_m_s": mean(series(lambda e: e.wind_speed_m_s)),
        "ghi_mean_w_m2": mean(ghi),
        "ghi_max_w_m2": max(ghi),
        "dni_mean_w_m2": mean(series(lambda e: nan if e.direct_normal_irradiance_w_m2 is None
                                     else e.direct_normal_irradiance_w_m2)),
        "dhi_mean_w_m2": mean(series(lambda e: nan if e.diffuse_horizontal_irradiance_w_m2 is None
                                     else e.diffuse_horizontal_irradiance_w_m2)),
        "sky_temperature_mean_c": mean(series(lambda e: nan if e.sky_temperature_c is None
                                              else e.sky_temperature_c)),
        "surround_temperature_mean_c": mean(surround),
        "surround_temperature_max_c": max(surround),
    }