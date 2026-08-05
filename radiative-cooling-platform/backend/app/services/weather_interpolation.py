from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from app.schemas.simulation import EnvironmentInput
from app.schemas.weather import WeatherTimeSeries


@dataclass
class WeatherInterpolator:
    relative_seconds: np.ndarray
    temperatures: np.ndarray
    humidities: np.ndarray
    wind_speeds: np.ndarray
    ghi_values: np.ndarray

    @classmethod
    def from_series(
        cls,
        weather: WeatherTimeSeries,
    ) -> "WeatherInterpolator":
        start_time = weather.requested_start_time

        relative_seconds = np.asarray(
            [
                (
                    point.timestamp - start_time
                ).total_seconds()
                for point in weather.points
            ],
            dtype=float,
        )

        return cls(
            relative_seconds=relative_seconds,
            temperatures=np.asarray(
                [
                    point.air_temperature_c
                    for point in weather.points
                ],
                dtype=float,
            ),
            humidities=np.asarray(
                [
                    point.relative_humidity_percent
                    for point in weather.points
                ],
                dtype=float,
            ),
            wind_speeds=np.asarray(
                [
                    point.wind_speed_m_s
                    for point in weather.points
                ],
                dtype=float,
            ),
            ghi_values=np.asarray(
                [
                    point.ghi_w_m2
                    for point in weather.points
                ],
                dtype=float,
            ),
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
        air_temperature = self._interpolate(
            self.temperatures,
            elapsed_seconds,
        )

        relative_humidity = self._interpolate(
            self.humidities,
            elapsed_seconds,
        )

        wind_speed = self._interpolate(
            self.wind_speeds,
            elapsed_seconds,
        )

        ghi = max(
            0.0,
            self._interpolate(
                self.ghi_values,
                elapsed_seconds,
            ),
        )

        # MVP 經驗估計：
        # 戶外平均輻射溫度會因短波太陽輻射上升。
        mean_radiant_temperature = (
            air_temperature
            + min(15.0, 0.012 * ghi)
        )

        # Open-Meteo 歷史接口未直接提供有效天空溫度，
        # 第一版按濕度估計天空相對空氣的溫差。
        sky_temperature = (
            air_temperature
            - (
                5.0
                + 10.0
                * (
                    1.0
                    - relative_humidity / 100.0
                )
            )
        )

        return EnvironmentInput(
            air_temperature_c=air_temperature,
            mean_radiant_temperature_c=(
                mean_radiant_temperature
            ),
            sky_temperature_c=sky_temperature,
            relative_humidity_percent=(
                relative_humidity
            ),
            wind_speed_m_s=max(
                0.0,
                wind_speed,
            ),
            solar_radiation_w_m2=ghi,
            sky_view_factor=0.5,
        )