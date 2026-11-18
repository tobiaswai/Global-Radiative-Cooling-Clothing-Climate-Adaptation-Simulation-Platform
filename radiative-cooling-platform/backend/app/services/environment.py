"""Explicit rules for deriving boundary conditions that ERA5 does not provide
(Stage 2; Stage 5 ground albedo; Stage 11 physical sky and ground, ADR 0008).

Defaults reproduce the Stage 1 estimates exactly.

``mean_radiant_temperature`` in EnvironmentInput is used by the model only as
the longwave temperature of the NON-SKY part of the view. The legacy rule
``air_plus_solar_linear`` raises it with GHI although body shortwave is
computed explicitly since Stage 5, i.e. it counts the sun twice (ADR 0008).
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


MeanRadiantTemperatureMethod = Literal[
    "air_plus_solar_linear",   # legacy: T_air + min(cap, gain * GHI)
    "equal_to_air",            # shaded / indoor-like
    "ground_energy_balance",   # Stage 11: steady ground surface balance
]

SkyTemperatureMethod = Literal[
    "humidity_offset",   # T_sky = T_air - (base + range * (1 - RH))
    "fixed_offset",      # T_sky = T_air - fixed_offset
    "swinbank",          # T_sky[K] = 0.0552 * T_air[K]^1.5 (clear sky)
    "brutsaert_cloud",   # Stage 11: Brutsaert + cloud fraction
]

RadiationTimeConvention = Literal[
    "instantaneous_linear",
    "preceding_hour_mean_step",
]

_STAGE1 = {"source_type": "assumed", "reference": "Stage 1 prototype"}


class EnvironmentAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mean_radiant_temperature_method: MeanRadiantTemperatureMethod = Field(
        default="air_plus_solar_linear", json_schema_extra=_STAGE1,
    )
    solar_mrt_gain_k_per_w_m2: float = Field(
        default=0.012, ge=0.0, le=0.05,
        description="MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
        json_schema_extra=_STAGE1,
    )
    solar_mrt_gain_cap_k: float = Field(
        default=15.0, ge=0.0, le=40.0,
        description="Upper bound of the solar MRT rise",
        json_schema_extra=_STAGE1,
    )

    sky_temperature_method: SkyTemperatureMethod = Field(
        default="humidity_offset", json_schema_extra=_STAGE1,
    )
    sky_offset_base_k: float = Field(
        default=5.0, ge=0.0, le=40.0,
        description="humidity_offset: depression at 100 % RH", json_schema_extra=_STAGE1,
    )
    sky_offset_humidity_range_k: float = Field(
        default=10.0, ge=0.0, le=40.0,
        description="humidity_offset: additional depression at 0 % RH", json_schema_extra=_STAGE1,
    )
    fixed_sky_offset_k: float = Field(
        default=15.0, ge=0.0, le=50.0,
        description="fixed_offset: T_air - T_sky", json_schema_extra=_STAGE1,
    )

    sky_view_factor: float = Field(
        default=0.5, ge=0.0, le=1.0,
        description="Fraction of the body's radiative view occupied by sky",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Standing person on an open, unobstructed site",
        },
    )

    wind_speed_scaling_factor: float = Field(
        default=1.0, gt=0.0, le=1.5,
        description=(
            "Multiplier from ERA5 10 m wind to body-height wind. 1.0 keeps "
            "Stage 1 behaviour; ~0.67 approximates 1.1 m height via a "
            "logarithmic profile over open terrain."
        ),
        json_schema_extra=_STAGE1,
    )

    ground_albedo: float = Field(
        default=0.2, ge=0.0, le=1.0,
        description="Shortwave reflectance of the ground surface",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Typical dry soil / urban pavement (0.15-0.25)",
        },
    )

    radiation_time_convention: RadiationTimeConvention = Field(
        default="instantaneous_linear",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Open-Meteo hourly parameter definition (preceding hour mean)",
        },
    )

    # Stage 11 (ADR 0008), ground_energy_balance only.
    ground_emissivity: float = Field(
        default=0.95, ge=0.8, le=1.0,
        description="Longwave emissivity of the ground surface",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Typical soil, asphalt and concrete (0.92-0.97)",
        },
    )
    ground_soil_conductance_w_m2k: float = Field(
        default=15.0, ge=2.0, le=200.0,
        description=(
            "Effective conductance between the ground surface and the ERA5 "
            "0-7 cm soil layer (k/d)"
        ),
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Order of magnitude for dry soil to pavement; not measured",
        },
    )

    def describe(self) -> list[str]:
        """Human-readable summary written into ``environment_model_note``."""
        if self.mean_radiant_temperature_method == "air_plus_solar_linear":
            mrt = (
                f"T_mrt = T_air + min({self.solar_mrt_gain_cap_k} K, "
                f"{self.solar_mrt_gain_k_per_w_m2} K/(W/m^2) * GHI)"
            )
        elif self.mean_radiant_temperature_method == "ground_energy_balance":
            mrt = (
                "Non-sky surroundings = ground surface temperature from "
                "(1 - rho_g) GHI + eps_g sigma T_sky^4 = eps_g sigma T_g^4 "
                "+ h_g (T_g - T_air) + K (T_g - T_soil,0-7cm), "
                f"eps_g = {self.ground_emissivity}, "
                f"K = {self.ground_soil_conductance_w_m2k} W/(m^2 K)"
            )
        else:
            mrt = "T_mrt = T_air"

        if self.sky_temperature_method == "humidity_offset":
            sky = (
                f"T_sky = T_air - ({self.sky_offset_base_k} K + "
                f"{self.sky_offset_humidity_range_k} K * (1 - RH))"
            )
        elif self.sky_temperature_method == "fixed_offset":
            sky = f"T_sky = T_air - {self.fixed_sky_offset_k} K"
        elif self.sky_temperature_method == "brutsaert_cloud":
            sky = (
                "T_sky = eps_sky^0.25 T_air, eps_sky = c + (1 - c) * 1.24 "
                "(e_a/T_air)^(1/7), c = ERA5 total cloud cover "
                "(Brutsaert 1975; Crawford & Duchon 1999 form)"
            )
        else:
            sky = "T_sky[K] = 0.0552 * T_air[K]^1.5 (Swinbank 1963, clear sky)"

        if self.radiation_time_convention == "preceding_hour_mean_step":
            radiation = (
                "GHI/DNI/DHI are treated as preceding-hour means held constant "
                "over (t-1h, t] (energy-conserving)."
            )
        else:
            radiation = (
                "GHI/DNI/DHI hourly means are treated as instantaneous values at "
                "the stamped hour and interpolated linearly (approximation; "
                "shifts the solar profile by up to 30 min)."
            )

        return [
            "Air temperature, relative humidity, 10 m wind speed and GHI are "
            "taken from ERA5 via Open-Meteo.",
            mrt,
            sky,
            f"Sky view factor = {self.sky_view_factor}",
            f"Body-height wind = {self.wind_speed_scaling_factor} * ERA5 10 m wind",
            "Direct normal and diffuse horizontal irradiance are taken from "
            "ERA5; the body-incident shortwave follows ASHRAE 55 Appendix C "
            "geometry (ADR 0006).",
            f"Ground albedo = {self.ground_albedo}",
            radiation,
        ]