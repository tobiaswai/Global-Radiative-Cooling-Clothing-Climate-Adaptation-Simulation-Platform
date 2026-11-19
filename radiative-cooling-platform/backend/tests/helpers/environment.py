"""Test helpers for environment assumptions (Stage 12, ADR 0009).

* LEGACY / legacy(...): pin the Stage 1 proxy rules on synthetic weather that
  carries no cloud cover or soil temperature.
* with_physical_series(...): add constant cloud cover and soil temperature to a
  synthetic series so the physical default (open_ground_physical) can run.
* make_fake_fetch(...): replacement for get_historical_weather(_range) that
  asserts the right extra variables were requested.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from app.schemas.environment import LEGACY_PRESET, EnvironmentAssumptions, preset_assumptions
from app.schemas.weather import WeatherPoint, WeatherTimeSeries
from app.services.environment_model import required_weather_variables

LEGACY = preset_assumptions(LEGACY_PRESET)
PHYSICAL = EnvironmentAssumptions()
PHYSICAL_EXTRAS = required_weather_variables(PHYSICAL)

SYNTHETIC_CLOUD_COVER_PERCENT = 20.0
SYNTHETIC_SOIL_TEMPERATURE_C = 38.0


def legacy(**overrides: Any) -> EnvironmentAssumptions:
    """LEGACY with overrides, validated (model_copy(update=) would not validate)."""
    return EnvironmentAssumptions(**{**LEGACY.model_dump(), **overrides})


def physical(**overrides: Any) -> EnvironmentAssumptions:
    return EnvironmentAssumptions(**{**PHYSICAL.model_dump(), **overrides})


def with_physical_variables(
    points: Sequence[WeatherPoint],
    *,
    cloud_cover_percent: float = SYNTHETIC_CLOUD_COVER_PERCENT,
    soil_temperature_c: float = SYNTHETIC_SOIL_TEMPERATURE_C,
) -> list[WeatherPoint]:
    return [
        p.model_copy(update={
            "cloud_cover_percent": cloud_cover_percent,
            "soil_temperature_c": soil_temperature_c,
        })
        for p in points
    ]


def with_physical_series(weather: WeatherTimeSeries, **kwargs: Any) -> WeatherTimeSeries:
    return weather.model_copy(update={"points": with_physical_variables(weather.points, **kwargs)})


def make_fake_fetch(weather: WeatherTimeSeries, assumptions: EnvironmentAssumptions):
    """Async stand-in for get_historical_weather / get_historical_weather_range."""
    expected = tuple(required_weather_variables(assumptions))

    async def fake(*args: Any, extra_variables: Sequence[str] = (), **kwargs: Any) -> WeatherTimeSeries:
        assert tuple(extra_variables) == expected, (tuple(extra_variables), expected)
        return with_physical_series(weather) if extra_variables else weather

    return fake