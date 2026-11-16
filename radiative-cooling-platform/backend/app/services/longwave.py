"""Two-band longwave exchange: atmospheric window (8-13 um) vs. rest (ADR 0007).

Gray materials (infrared_emissivity_window is None) never use this module's
band arithmetic: two_node keeps the single-band formula for them, so every
existing result is unchanged.

Sky model: outside the window the near-surface atmosphere is treated as
opaque at air temperature; inside the window its emissivity eps_sky,W is
chosen so that the broadband sky radiance equals sigma T_sky^4 from the
configured sky-temperature method.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import EnvironmentInput, MaterialInput
from app.services.model_parameters import get_parameter_value as _param
from app.services.planck import (
    WINDOW_LOWER_UM,
    WINDOW_UPPER_UM,
    band_fraction,
    band_power_k4,
    outside_window_emissivity,
)


KELVIN_OFFSET = 273.15
FALLBACK_SKY_OFFSET = _param("fallback_sky_temperature_offset")


@dataclass(frozen=True)
class LongwaveOptics:
    broadband: float
    window: float
    outside: float
    selective: bool


def resolve_longwave_optics(material: MaterialInput) -> LongwaveOptics:
    emissivity = material.infrared_emissivity
    window = material.infrared_emissivity_window

    if window is None:
        return LongwaveOptics(emissivity, emissivity, emissivity, False)

    # The schema has already rejected values outside [0, 1] beyond 1e-6.
    outside = min(1.0, max(0.0, outside_window_emissivity(emissivity, window)))
    return LongwaveOptics(emissivity, window, outside, True)


@dataclass(frozen=True)
class RadiantField:
    """Incoming longwave per band, divided by sigma (K^4)."""

    window_k4: float
    outside_k4: float
    sky_window_emissivity: float

    @property
    def total_k4(self) -> float:
        return self.window_k4 + self.outside_k4


def sky_window_emissivity(air_k: float, sky_k: float) -> float:
    fw = band_fraction(air_k)
    total = (sky_k / air_k) ** 4
    return min(1.0, max(0.0, (total - (1.0 - fw)) / fw))


def radiant_field(environment: EnvironmentInput) -> RadiantField:
    air_k = environment.air_temperature_c + KELVIN_OFFSET
    sky_c = environment.sky_temperature_c
    if sky_c is None:
        sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET
    sky_k = sky_c + KELVIN_OFFSET
    surround_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    f_sky = environment.sky_view_factor

    fw_air = band_fraction(air_k)
    eps_sky_w = sky_window_emissivity(air_k, sky_k)
    sky_window = eps_sky_w * fw_air * air_k**4
    sky_outside = (1.0 - fw_air) * air_k**4

    surround_window, _ = band_power_k4(surround_k)
    surround_total = surround_k**4

    return RadiantField(
        window_k4=f_sky * sky_window + (1.0 - f_sky) * surround_window,
        outside_k4=f_sky * sky_outside + (1.0 - f_sky) * (surround_total - surround_window),
        sky_window_emissivity=eps_sky_w,
    )


def net_exchange_k4(
    optics: LongwaveOptics,
    field: RadiantField,
    temperature_k: float,
) -> tuple[float, float, float]:
    """(net emission - absorption, its T-derivative, window-band part), / sigma."""
    window_emission, window_slope = band_power_k4(temperature_k)
    total_emission = temperature_k**4
    total_slope = 4.0 * temperature_k**3

    net_window = optics.window * (window_emission - field.window_k4)
    net_outside = optics.outside * (
        (total_emission - window_emission) - field.outside_k4
    )
    derivative = (
        optics.window * window_slope
        + optics.outside * (total_slope - window_slope)
    )
    return net_window + net_outside, derivative, net_window


def longwave_notes(optics: LongwaveOptics) -> list[str]:
    if not optics.selective:
        return []
    return [
        "selective longwave emitter: eps_W = "
        f"{optics.window:.3f} ({WINDOW_LOWER_UM:g}-{WINDOW_UPPER_UM:g} um), "
        f"eps_N = {optics.outside:.3f} (derived from broadband "
        f"{optics.broadband:.3f}); sky outside the window is treated as opaque "
        "at air temperature (ADR 0007)"
    ]