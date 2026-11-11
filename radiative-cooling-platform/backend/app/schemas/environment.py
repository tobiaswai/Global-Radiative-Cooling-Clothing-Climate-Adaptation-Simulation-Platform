"""Explicit rules for deriving boundary conditions that ERA5 does not
provide: mean radiant temperature, sky temperature, sky view factor and
body-height wind (Stage 2).

Defaults reproduce the Stage 1 empirical estimates exactly, so introducing
this model does not change existing results.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


MeanRadiantTemperatureMethod = Literal[
    "air_plus_solar_linear",  # T_mrt = T_air + min(cap, gain * GHI)
    "equal_to_air",           # T_mrt = T_air (shaded / indoor-like)
]

SkyTemperatureMethod = Literal[
    "humidity_offset",  # T_sky = T_air - (base + range * (1 - RH))
    "fixed_offset",     # T_sky = T_air - fixed_offset
    "swinbank",         # T_sky[K] = 0.0552 * T_air[K]^1.5 (clear sky)
]

RadiationTimeConvention = Literal[
    "instantaneous_linear",     # legacy: treat hourly means as instants, interpolate linearly
    "preceding_hour_mean_step", # Open-Meteo definition: value = mean over (t-1h, t], piecewise constant
]

class EnvironmentAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mean_radiant_temperature_method: MeanRadiantTemperatureMethod = Field(
        default="air_plus_solar_linear",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    solar_mrt_gain_k_per_w_m2: float = Field(
        default=0.012, ge=0.0, le=0.05,
        description="MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    solar_mrt_gain_cap_k: float = Field(
        default=15.0, ge=0.0, le=40.0,
        description="Upper bound of the solar MRT rise",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )

    sky_temperature_method: SkyTemperatureMethod = Field(
        default="humidity_offset",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    sky_offset_base_k: float = Field(
        default=5.0, ge=0.0, le=40.0,
        description="humidity_offset: depression at 100 % RH",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    sky_offset_humidity_range_k: float = Field(
        default=10.0, ge=0.0, le=40.0,
        description="humidity_offset: additional depression at 0 % RH",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    fixed_sky_offset_k: float = Field(
        default=15.0, ge=0.0, le=50.0,
        description="fixed_offset: T_air - T_sky",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
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
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )

    # Stage 5 (ADR 0006). Ground-reflected shortwave = 0.5 f_eff rho_g GHI.
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

    def describe(self) -> list[str]:
        """Human-readable summary written into ``environment_model_note``."""
        if self.mean_radiant_temperature_method == "air_plus_solar_linear":
            mrt = (
                f"T_mrt = T_air + min({self.solar_mrt_gain_cap_k} K, "
                f"{self.solar_mrt_gain_k_per_w_m2} K/(W/m^2) * GHI)"
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