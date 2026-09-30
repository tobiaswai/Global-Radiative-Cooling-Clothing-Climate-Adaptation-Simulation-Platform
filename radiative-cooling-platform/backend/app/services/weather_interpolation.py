from __future__ import annotations

from dataclasses import dataclass, field  # Stage 2: `field` added

import numpy as np

from app.schemas.environment import EnvironmentAssumptions  # Stage 2
from app.schemas.simulation import EnvironmentInput
from app.schemas.weather import WeatherTimeSeries
from app.services.environment_model import derive_environment  # Stage 2
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

    # Stage 2. Must stay the last field: dataclass fields with defaults
    # cannot precede fields without defaults. Existing keyword-based
    # constructions (see tests/test_weather_interpolation.py) remain valid.
    assumptions: EnvironmentAssumptions = field(
        default_factory=EnvironmentAssumptions
    )
    # Stage 5. Optional so keyword constructions without the split keep working.
    dni_values: np.ndarray | None = None
    dhi_values: np.ndarray | None = None

    def __post_init__(self) -> None:
        arrays = [
            self.relative_seconds,
            self.temperatures,
            self.humidities,
            self.wind_speeds,
            self.ghi_values,
        ]
        if self.dni_values is not None:
            arrays.append(self.dni_values)
        if self.dhi_values is not None:
            arrays.append(self.dhi_values)

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
        assumptions: EnvironmentAssumptions | None = None,  # Stage 2
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
            assumptions=assumptions or EnvironmentAssumptions(),  # Stage 2
            dni_values=np.asarray(
                [p.dni_w_m2 for p in weather.points], dtype=float
            ),
            dhi_values=np.asarray(
                [p.diffuse_radiation_w_m2 for p in weather.points], dtype=float
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
        """Interpolate the ERA5 variables and derive the model boundary
        conditions according to ``self.assumptions``.

        Stage 2: the mean radiant temperature, sky temperature, sky view
        factor and wind scaling rules live in ``environment_model``; this
        method only interpolates.
        """
        self._check_bounds(elapsed_seconds)

        return derive_environment(
            air_temperature_c=self._interpolate(self.temperatures, elapsed_seconds),
            relative_humidity_percent=self._interpolate(self.humidities, elapsed_seconds),
            wind_speed_m_s=self._interpolate(self.wind_speeds, elapsed_seconds),
            ghi_w_m2=self._interpolate(self.ghi_values, elapsed_seconds),
            direct_normal_irradiance_w_m2=(
                None
                if self.dni_values is None
                else self._interpolate(self.dni_values, elapsed_seconds)
            ),
            diffuse_horizontal_irradiance_w_m2=(
                None
                if self.dhi_values is None
                else self._interpolate(self.dhi_values, elapsed_seconds)
            ),
            assumptions=self.assumptions,
        )