"""Linear interpolation of hourly weather to solver time (Stage 1, PR-2).

Boundary policy: queries outside ``[t_min, t_max]`` raise instead of being
clamped. ``from_series`` additionally verifies that the series brackets the
requested exposure window, so an under-covered series fails before the ODE
solver starts.

The empirical environment estimates (mean radiant temperature, sky
temperature, sky view factor) are intentionally left unchanged here; they
belong to Stage 2 (model completion).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from app.schemas.simulation import EnvironmentInput
from app.schemas.weather import WeatherTimeSeries
from app.services.weather_quality import (
    WeatherInsufficientCoverageError,
)


BOUNDS_TOLERANCE_SECONDS = 1e-6


class InterpolationOutOfRangeError(WeatherInsufficientCoverageError):
    code = "WEATHER_INTERPOLATION_OUT_OF_RANGE"


@dataclass
class WeatherInterpolator:
    relative_seconds: np.ndarray
    temperatures: np.ndarray
    humidities: np.ndarray
    wind_speeds: np.ndarray
    ghi_values: np.ndarray

    def __post_init__(self) -> None:
        arrays = (
            self.relative_seconds,
            self.temperatures,
            self.humidities,
            self.wind_speeds,
            self.ghi_values,
        )

        lengths = {len(array) for array in arrays}

        if len(lengths) != 1:
            raise ValueError(
                "All interpolation arrays must have the same length"
            )

        if len(self.relative_seconds) < 2:
            raise WeatherInsufficientCoverageError(
                "Interpolation requires at least two weather points"
            )

        if not np.all(np.diff(self.relative_seconds) > 0):
            raise ValueError(
                "relative_seconds must be strictly increasing"
            )

    @property
    def t_min(self) -> float:
        return float(self.relative_seconds[0])

    @property
    def t_max(self) -> float:
        return float(self.relative_seconds[-1])

    def ensure_covers(
        self,
        start_seconds: float,
        end_seconds: float,
    ) -> None:
        """Raise unless ``[start_seconds, end_seconds]`` lies inside the data."""
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

    @classmethod
    def from_series(
        cls,
        weather: WeatherTimeSeries,
        *,
        check_requested_window: bool = True,
    ) -> "WeatherInterpolator":
        start_time = weather.requested_start_time

        relative_seconds = np.asarray(
            [
                (point.timestamp - start_time).total_seconds()
                for point in weather.points
            ],
            dtype=float,
        )

        interpolator = cls(
            relative_seconds=relative_seconds,
            temperatures=np.asarray(
                [p.air_temperature_c for p in weather.points], dtype=float
            ),
            humidities=np.asarray(
                [p.relative_humidity_percent for p in weather.points],
                dtype=float,
            ),
            wind_speeds=np.asarray(
                [p.wind_speed_m_s for p in weather.points], dtype=float
            ),
            ghi_values=np.asarray(
                [p.ghi_w_m2 for p in weather.points], dtype=float
            ),
        )

        if check_requested_window:
            required_end = (
                weather.requested_end_time - start_time
            ).total_seconds()

            interpolator.ensure_covers(0.0, required_end)

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

    def _interpolate(
        self,
        values: np.ndarray,
        elapsed_seconds: float,
    ) -> float:
        return float(
            np.interp(
                elapsed_seconds,
                self.relative_seconds,
                values,
            )
        )

    def environment_at(
        self,
        elapsed_seconds: float,
    ) -> EnvironmentInput:
        self._check_bounds(elapsed_seconds)

        air_temperature = self._interpolate(
            self.temperatures, elapsed_seconds
        )
        relative_humidity = self._interpolate(
            self.humidities, elapsed_seconds
        )
        wind_speed = self._interpolate(
            self.wind_speeds, elapsed_seconds
        )
        ghi = max(
            0.0,
            self._interpolate(self.ghi_values, elapsed_seconds),
        )

        # Stage 2 will replace these empirical estimates. Do not change here.
        mean_radiant_temperature = air_temperature + min(15.0, 0.012 * ghi)

        sky_temperature = air_temperature - (
            5.0 + 10.0 * (1.0 - relative_humidity / 100.0)
        )

        return EnvironmentInput(
            air_temperature_c=air_temperature,
            mean_radiant_temperature_c=mean_radiant_temperature,
            sky_temperature_c=sky_temperature,
            relative_humidity_percent=relative_humidity,
            wind_speed_m_s=max(0.0, wind_speed),
            solar_radiation_w_m2=ghi,
            sky_view_factor=0.5,
        )