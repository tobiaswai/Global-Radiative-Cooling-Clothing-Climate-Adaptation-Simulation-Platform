from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import EnvironmentInput
from app.schemas.weather import WeatherTimeSeries
from app.services.environment_model import (
    CLOUD_COVER,
    SOIL_TEMPERATURE,
    derive_environment,
    required_weather_variables,
)
from app.services.weather_quality import (
    WeatherInsufficientCoverageError,
    WeatherMissingVariableError,
)


BOUNDS_TOLERANCE_SECONDS = 1e-6

_POINT_FIELD = {CLOUD_COVER: "cloud_cover_percent", SOIL_TEMPERATURE: "soil_temperature_c"}


class InterpolationOutOfRangeError(WeatherInsufficientCoverageError):
    code = "WEATHER_INTERPOLATION_OUT_OF_RANGE"


@dataclass
class WeatherInterpolator:
    relative_seconds: np.ndarray
    temperatures: np.ndarray
    humidities: np.ndarray
    wind_speeds: np.ndarray
    ghi_values: np.ndarray
    assumptions: EnvironmentAssumptions = field(default_factory=EnvironmentAssumptions)
    dni_values: np.ndarray | None = None
    dhi_values: np.ndarray | None = None
    # Stage 11 (instantaneous variables, linear interpolation)
    cloud_values: np.ndarray | None = None
    soil_values: np.ndarray | None = None

    def __post_init__(self) -> None:
        arrays = [self.relative_seconds, self.temperatures, self.humidities, self.wind_speeds, self.ghi_values]
        arrays += [a for a in (self.dni_values, self.dhi_values, self.cloud_values, self.soil_values) if a is not None]

        if len({len(a) for a in arrays}) != 1:
            raise ValueError("All interpolation arrays must have the same length")
        if len(self.relative_seconds) < 2:
            raise WeatherInsufficientCoverageError("Interpolation requires at least two weather points")
        if not np.all(np.diff(self.relative_seconds) > 0):
            raise ValueError("relative_seconds must be strictly increasing")

        required = required_weather_variables(self.assumptions)
        if CLOUD_COVER in required and self.cloud_values is None:
            raise WeatherMissingVariableError("cloud_cover is required but was not provided",
                                              context={"variable": CLOUD_COVER})
        if SOIL_TEMPERATURE in required and self.soil_values is None:
            raise WeatherMissingVariableError("soil temperature is required but was not provided",
                                              context={"variable": SOIL_TEMPERATURE})

    @property
    def t_min(self) -> float:
        return float(self.relative_seconds[0])

    @property
    def t_max(self) -> float:
        return float(self.relative_seconds[-1])

    def ensure_covers(self, start_seconds: float, end_seconds: float) -> None:
        if (
            start_seconds < self.t_min - BOUNDS_TOLERANCE_SECONDS
            or end_seconds > self.t_max + BOUNDS_TOLERANCE_SECONDS
        ):
            raise WeatherInsufficientCoverageError(
                "Weather data cover "
                f"[{self.t_min:.0f} s, {self.t_max:.0f} s] relative to the "
                "requested start, but the simulation requires "
                f"[{start_seconds:.0f} s, {end_seconds:.0f} s]",
                context={
                    "available_start_seconds": f"{self.t_min:.0f}",
                    "available_end_seconds": f"{self.t_max:.0f}",
                    "required_start_seconds": f"{start_seconds:.0f}",
                    "required_end_seconds": f"{end_seconds:.0f}",
                },
            )

    @staticmethod
    def _optional_array(weather: WeatherTimeSeries, variable: str, required: bool) -> np.ndarray | None:
        name = _POINT_FIELD[variable]
        values = [getattr(p, name) for p in weather.points]
        if all(v is None for v in values):
            return None
        if any(v is None for v in values):
            if required:
                raise WeatherMissingVariableError(
                    f"{variable} has missing values inside the simulated window",
                    context={"variable": variable},
                )
            return None
        return np.asarray(values, dtype=float)

    @classmethod
    def from_series(
        cls,
        weather: WeatherTimeSeries,
        *,
        check_requested_window: bool = True,
        assumptions: EnvironmentAssumptions | None = None,
    ) -> "WeatherInterpolator":
        assumptions = assumptions or EnvironmentAssumptions()
        required = required_weather_variables(assumptions)
        start_time = weather.requested_start_time

        interpolator = cls(
            relative_seconds=np.asarray(
                [p.timestamp.timestamp() - start_time.timestamp() for p in weather.points], dtype=float
            ),
            temperatures=np.asarray([p.air_temperature_c for p in weather.points], dtype=float),
            humidities=np.asarray([p.relative_humidity_percent for p in weather.points], dtype=float),
            wind_speeds=np.asarray([p.wind_speed_m_s for p in weather.points], dtype=float),
            ghi_values=np.asarray([p.ghi_w_m2 for p in weather.points], dtype=float),
            assumptions=assumptions,
            dni_values=np.asarray([p.dni_w_m2 for p in weather.points], dtype=float),
            dhi_values=np.asarray([p.diffuse_radiation_w_m2 for p in weather.points], dtype=float),
            cloud_values=cls._optional_array(weather, CLOUD_COVER, CLOUD_COVER in required),
            soil_values=cls._optional_array(weather, SOIL_TEMPERATURE, SOIL_TEMPERATURE in required),
        )

        if check_requested_window:
            interpolator.ensure_covers(
                0.0, weather.requested_end_time.timestamp() - start_time.timestamp()
            )
        return interpolator

    def _check_bounds(self, elapsed_seconds: float) -> None:
        if (
            elapsed_seconds < self.t_min - BOUNDS_TOLERANCE_SECONDS
            or elapsed_seconds > self.t_max + BOUNDS_TOLERANCE_SECONDS
        ):
            raise InterpolationOutOfRangeError(
                f"Requested time {elapsed_seconds:.3f} s is outside the "
                f"weather data range [{self.t_min:.0f} s, {self.t_max:.0f} s]",
                context={
                    "requested_seconds": f"{elapsed_seconds:.3f}",
                    "available_start_seconds": f"{self.t_min:.0f}",
                    "available_end_seconds": f"{self.t_max:.0f}",
                },
            )

    def _interpolate(self, values: np.ndarray, elapsed_seconds: float) -> float:
        return float(np.interp(elapsed_seconds, self.relative_seconds, values))

    def _interpolate_optional(self, values: np.ndarray | None, elapsed_seconds: float) -> float | None:
        return None if values is None else self._interpolate(values, elapsed_seconds)

    def _interpolate_radiation(self, values: np.ndarray, elapsed_seconds: float) -> float:
        if self.assumptions.radiation_time_convention == "instantaneous_linear":
            return self._interpolate(values, elapsed_seconds)
        index = int(np.searchsorted(self.relative_seconds, elapsed_seconds, side="left"))
        index = min(max(index, 0), len(values) - 1)
        return float(values[index])

    def environment_at(self, elapsed_seconds: float) -> EnvironmentInput:
        self._check_bounds(elapsed_seconds)
        return derive_environment(
            air_temperature_c=self._interpolate(self.temperatures, elapsed_seconds),
            relative_humidity_percent=self._interpolate(self.humidities, elapsed_seconds),
            wind_speed_m_s=self._interpolate(self.wind_speeds, elapsed_seconds),
            ghi_w_m2=self._interpolate_radiation(self.ghi_values, elapsed_seconds),
            direct_normal_irradiance_w_m2=(
                None if self.dni_values is None
                else self._interpolate_radiation(self.dni_values, elapsed_seconds)
            ),
            diffuse_horizontal_irradiance_w_m2=(
                None if self.dhi_values is None
                else self._interpolate_radiation(self.dhi_values, elapsed_seconds)
            ),
            cloud_cover_percent=self._interpolate_optional(self.cloud_values, elapsed_seconds),
            soil_temperature_c=self._interpolate_optional(self.soil_values, elapsed_seconds),
            assumptions=self.assumptions,
        )