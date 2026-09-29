"""Derive model boundary conditions from ERA5 variables (Stage 2)."""

from __future__ import annotations

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import EnvironmentInput
from app.services.model_parameters import get_parameter_value


SWINBANK_COEFFICIENT = get_parameter_value("swinbank_coefficient")
KELVIN_OFFSET = 273.15


def derive_environment(
    *,
    air_temperature_c: float,
    relative_humidity_percent: float,
    wind_speed_m_s: float,
    ghi_w_m2: float,
    assumptions: EnvironmentAssumptions,
) -> EnvironmentInput:
    air = float(air_temperature_c)
    ghi = max(0.0, float(ghi_w_m2))
    relative_humidity = min(100.0, max(0.0, float(relative_humidity_percent)))
    wind = max(0.0, float(wind_speed_m_s)) * assumptions.wind_speed_scaling_factor

    if assumptions.mean_radiant_temperature_method == "air_plus_solar_linear":
        mean_radiant = air + min(
            assumptions.solar_mrt_gain_cap_k,
            assumptions.solar_mrt_gain_k_per_w_m2 * ghi,
        )
    else:
        mean_radiant = air

    if assumptions.sky_temperature_method == "humidity_offset":
        sky = air - (
            assumptions.sky_offset_base_k
            + assumptions.sky_offset_humidity_range_k
            * (1.0 - relative_humidity / 100.0)
        )
    elif assumptions.sky_temperature_method == "fixed_offset":
        sky = air - assumptions.fixed_sky_offset_k
    else:
        sky = SWINBANK_COEFFICIENT * (air + KELVIN_OFFSET) ** 1.5 - KELVIN_OFFSET

    return EnvironmentInput(
        air_temperature_c=air,
        mean_radiant_temperature_c=mean_radiant,
        sky_temperature_c=sky,
        relative_humidity_percent=relative_humidity,
        wind_speed_m_s=wind,
        solar_radiation_w_m2=ghi,
        sky_view_factor=assumptions.sky_view_factor,
    )