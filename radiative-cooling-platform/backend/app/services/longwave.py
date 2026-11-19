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


def radiant_field(
    environment: EnvironmentInput,
    sky_view_factor: float | None = None,
) -> RadiantField:
    air_k = environment.air_temperature_c + KELVIN_OFFSET
    sky_c = environment.sky_temperature_c
    if sky_c is None:
        sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET
    sky_k = sky_c + KELVIN_OFFSET
    surround_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    f_sky = environment.sky_view_factor if sky_view_factor is None else sky_view_factor

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

# --------------------------------------------------------------------------
# Two-zone garment (Stage 12, ADR 0010)
# --------------------------------------------------------------------------

def surroundings_fourth_power_k4(
    environment: EnvironmentInput,
    sky_view_factor: float | None = None,
) -> float:
    """F T_sky^4 + (1 - F) T_surround^4 for a given sky view (K^4)."""
    f = environment.sky_view_factor if sky_view_factor is None else sky_view_factor
    sky_c = environment.sky_temperature_c
    if sky_c is None:
        sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET
    sky_k = sky_c + KELVIN_OFFSET
    surround_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    return f * sky_k**4 + (1.0 - f) * surround_k**4


def zone_sky_views(sky_view_factor: float, separation: float) -> tuple[float, float]:
    """(sky view of the sky-facing zone, of the ground-facing zone).

    Zone areas are F and 1 - F, so F * up + (1 - F) * down == F for every s.
    """
    f, s = sky_view_factor, separation
    return f + s * (1.0 - f), f * (1.0 - s)


@dataclass(frozen=True)
class PreparedZone:
    name: str
    area_fraction: float
    sky_view_factor: float
    optics: LongwaveOptics
    field: RadiantField | None     # selective zones only
    surroundings_k4: float         # gray zones (and diagnostics)


def prepare_longwave_zones(
    material: MaterialInput,
    environment: EnvironmentInput,
    optics: LongwaveOptics,
) -> tuple[PreparedZone, ...] | None:
    """None for a uniform garment, so the Stage 11 code path is used unchanged."""
    ground = material.infrared_emissivity_ground_facing
    if ground is None:
        return None

    f = environment.sky_view_factor
    up_view, down_view = zone_sky_views(f, environment.zone_view_separation)
    ground_optics = LongwaveOptics(ground, ground, ground, False)

    zones: list[PreparedZone] = []
    for name, area, view, zone_optics in (
        ("sky_facing", f, up_view, optics),
        ("ground_facing", 1.0 - f, down_view, ground_optics),
    ):
        if area <= 0.0:
            continue
        zones.append(
            PreparedZone(
                name=name,
                area_fraction=area,
                sky_view_factor=view,
                optics=zone_optics,
                field=radiant_field(environment, sky_view_factor=view) if zone_optics.selective else None,
                surroundings_k4=surroundings_fourth_power_k4(environment, view),
            )
        )
    return tuple(zones)


def zoned_exchange_k4(
    zones: tuple[PreparedZone, ...],
    temperature_k: float,
) -> tuple[float, float, float | None]:
    """Area-weighted (net, d net/dT, window part) over zones, / sigma."""
    net = slope = 0.0
    window: float | None = None
    for zone in zones:
        if zone.field is not None:
            n, s, w = net_exchange_k4(zone.optics, zone.field, temperature_k)
            window = (window or 0.0) + zone.area_fraction * w
        else:
            eps = zone.optics.broadband
            n = eps * (temperature_k**4 - zone.surroundings_k4)
            s = 4.0 * eps * temperature_k**3
        net += zone.area_fraction * n
        slope += zone.area_fraction * s
    return net, slope, window


def zone_notes(zones: tuple[PreparedZone, ...] | None) -> list[str]:
    if not zones:
        return []
    parts = "; ".join(
        f"{z.name}: area {z.area_fraction:.2f}, sky view {z.sky_view_factor:.2f}, "
        f"eps {z.optics.broadband:.2f}{' (selective)' if z.optics.selective else ''}"
        for z in zones
    )
    return [
        f"two-zone garment (ADR 0010): {parts}. Both zones share one clothing "
        "surface temperature; the ground-facing zone is gray."
    ]