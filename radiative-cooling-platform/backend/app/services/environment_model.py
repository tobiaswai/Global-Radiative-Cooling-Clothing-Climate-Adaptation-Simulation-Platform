"""Derive model boundary conditions from ERA5 variables (Stage 2, 11)."""

from __future__ import annotations

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import EnvironmentInput
from app.services.ground_surface import (
    brutsaert_cloud_sky_temperature_c,
    solve_ground_surface_temperature_c,
)
from app.services.model_parameters import get_parameter_value
from app.services.weather_quality import WeatherMissingVariableError


SWINBANK_COEFFICIENT = get_parameter_value("swinbank_coefficient")
KELVIN_OFFSET = 273.15

CLOUD_COVER = "cloud_cover"
SOIL_TEMPERATURE = "soil_temperature_0_to_7cm"


def required_weather_variables(assumptions: EnvironmentAssumptions) -> tuple[str, ...]:
    """Open-Meteo hourly variables needed beyond the Stage 10 set. Empty for defaults,
    so default requests, caches and payload hashes are unchanged."""
    needed: list[str] = []
    if assumptions.sky_temperature_method == "brutsaert_cloud":
        needed.append(CLOUD_COVER)
    if assumptions.mean_radiant_temperature_method == "ground_energy_balance":
        needed.append(SOIL_TEMPERATURE)
    return tuple(needed)


def _require(value: float | None, name: str) -> float:
    if value is None:
        raise WeatherMissingVariableError(
            f"Weather variable {name} is required by the selected environment "
            "assumptions but is missing",
            context={"variable": name},
        )
    return float(value)


def _sky_temperature_c(
    air: float, relative_humidity: float, cloud: float | None, a: EnvironmentAssumptions
) -> float:
    if a.sky_temperature_method == "humidity_offset":
        return air - (
            a.sky_offset_base_k + a.sky_offset_humidity_range_k * (1.0 - relative_humidity / 100.0)
        )
    if a.sky_temperature_method == "fixed_offset":
        return air - a.fixed_sky_offset_k
    if a.sky_temperature_method == "brutsaert_cloud":
        return brutsaert_cloud_sky_temperature_c(air, relative_humidity, _require(cloud, CLOUD_COVER))
    return SWINBANK_COEFFICIENT * (air + KELVIN_OFFSET) ** 1.5 - KELVIN_OFFSET


def derive_environment(
    *,
    air_temperature_c: float,
    relative_humidity_percent: float,
    wind_speed_m_s: float,
    ghi_w_m2: float,
    assumptions: EnvironmentAssumptions,
    direct_normal_irradiance_w_m2: float | None = None,
    diffuse_horizontal_irradiance_w_m2: float | None = None,
    cloud_cover_percent: float | None = None,
    soil_temperature_c: float | None = None,
) -> EnvironmentInput:
    air = float(air_temperature_c)
    ghi = max(0.0, float(ghi_w_m2))
    relative_humidity = min(100.0, max(0.0, float(relative_humidity_percent)))
    wind = max(0.0, float(wind_speed_m_s)) * assumptions.wind_speed_scaling_factor

    sky = _sky_temperature_c(air, relative_humidity, cloud_cover_percent, assumptions)

    method = assumptions.mean_radiant_temperature_method
    if method == "air_plus_solar_linear":
        mean_radiant = air + min(
            assumptions.solar_mrt_gain_cap_k,
            assumptions.solar_mrt_gain_k_per_w_m2 * ghi,
        )
    elif method == "ground_energy_balance":
        mean_radiant = solve_ground_surface_temperature_c(
            air_c=air,
            sky_c=sky,
            ghi_w_m2=ghi,
            albedo=assumptions.ground_albedo,
            wind_speed_m_s=wind,
            soil_c=_require(soil_temperature_c, SOIL_TEMPERATURE),
            emissivity=assumptions.ground_emissivity,
            conductance_w_m2k=assumptions.ground_soil_conductance_w_m2k,
        )
    else:
        mean_radiant = air

    dni = None if direct_normal_irradiance_w_m2 is None else max(0.0, float(direct_normal_irradiance_w_m2))
    dhi = None if diffuse_horizontal_irradiance_w_m2 is None else max(0.0, float(diffuse_horizontal_irradiance_w_m2))
    if (dni is None) != (dhi is None):
        raise ValueError("DNI and DHI must be supplied together")

    return EnvironmentInput(
        air_temperature_c=air,
        mean_radiant_temperature_c=mean_radiant,
        sky_temperature_c=sky,
        relative_humidity_percent=relative_humidity,
        wind_speed_m_s=wind,
        solar_radiation_w_m2=ghi,
        sky_view_factor=assumptions.sky_view_factor,
        direct_normal_irradiance_w_m2=dni,
        diffuse_horizontal_irradiance_w_m2=dhi,
        ground_albedo=assumptions.ground_albedo,
    )