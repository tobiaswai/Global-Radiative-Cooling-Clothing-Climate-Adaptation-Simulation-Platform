"""Sky emissivity with cloud and steady ground surface temperature (ADR 0008).

Ground balance per unit horizontal area (positive terms leave the surface):

    (1 - rho_g) GHI + eps_g sigma T_sky^4
        = eps_g sigma T_g^4 + h_g (T_g - T_a) + K (T_g - T_soil)

f(T_g) = left - right is strictly decreasing and concave, so Newton from any
start converges monotonically after the first step.
"""

from __future__ import annotations

from app.services.model_parameters import get_parameter_value as _param
from app.services.psychrometrics import vapor_pressure_kpa


SIGMA = _param("stefan_boltzmann_constant")
BRUTSAERT_COEFFICIENT = _param("brutsaert_coefficient")
BRUTSAERT_EXPONENT = _param("brutsaert_exponent")
GROUND_H0 = _param("ground_convection_still_air_coefficient")
GROUND_H1 = _param("ground_convection_wind_coefficient")

KELVIN_OFFSET = 273.15

# Numerical (not physical) settings.
MINIMUM_VAPOR_PRESSURE_HPA = 0.1
NEWTON_TOLERANCE_K = 1e-6
NEWTON_MAX_ITERATIONS = 50


def brutsaert_cloud_sky_emissivity(
    air_temperature_c: float,
    relative_humidity_percent: float,
    cloud_cover_percent: float,
) -> float:
    air_k = air_temperature_c + KELVIN_OFFSET
    e_hpa = max(
        MINIMUM_VAPOR_PRESSURE_HPA,
        vapor_pressure_kpa(air_temperature_c, relative_humidity_percent) * 10.0,
    )
    clear = min(1.0, BRUTSAERT_COEFFICIENT * (e_hpa / air_k) ** BRUTSAERT_EXPONENT)
    cloud = min(1.0, max(0.0, cloud_cover_percent / 100.0))
    return cloud + (1.0 - cloud) * clear


def brutsaert_cloud_sky_temperature_c(
    air_temperature_c: float,
    relative_humidity_percent: float,
    cloud_cover_percent: float,
) -> float:
    emissivity = brutsaert_cloud_sky_emissivity(
        air_temperature_c, relative_humidity_percent, cloud_cover_percent
    )
    return emissivity ** 0.25 * (air_temperature_c + KELVIN_OFFSET) - KELVIN_OFFSET


def ground_convection_coefficient(wind_speed_m_s: float) -> float:
    return GROUND_H0 + GROUND_H1 * max(0.0, wind_speed_m_s)


def ground_energy_residual(
    ground_c: float,
    *,
    air_c: float,
    sky_c: float,
    ghi_w_m2: float,
    albedo: float,
    wind_speed_m_s: float,
    soil_c: float,
    emissivity: float,
    conductance_w_m2k: float,
) -> float:
    t = ground_c + KELVIN_OFFSET
    gains = (1.0 - albedo) * max(0.0, ghi_w_m2) + emissivity * SIGMA * (sky_c + KELVIN_OFFSET) ** 4
    losses = (
        emissivity * SIGMA * t**4
        + ground_convection_coefficient(wind_speed_m_s) * (ground_c - air_c)
        + conductance_w_m2k * (ground_c - soil_c)
    )
    return gains - losses


def solve_ground_surface_temperature_c(
    *,
    air_c: float,
    sky_c: float,
    ghi_w_m2: float,
    albedo: float,
    wind_speed_m_s: float,
    soil_c: float,
    emissivity: float,
    conductance_w_m2k: float,
) -> float:
    h = ground_convection_coefficient(wind_speed_m_s)
    kwargs = dict(
        air_c=air_c, sky_c=sky_c, ghi_w_m2=ghi_w_m2, albedo=albedo,
        wind_speed_m_s=wind_speed_m_s, soil_c=soil_c,
        emissivity=emissivity, conductance_w_m2k=conductance_w_m2k,
    )

    t = max(air_c, soil_c)
    for _ in range(NEWTON_MAX_ITERATIONS):
        f = ground_energy_residual(t, **kwargs)
        slope = -4.0 * emissivity * SIGMA * (t + KELVIN_OFFSET) ** 3 - h - conductance_w_m2k
        step = f / slope
        t -= step
        if abs(step) < NEWTON_TOLERANCE_K:
            return t

    raise RuntimeError(
        f"Ground surface balance did not converge (T_a = {air_c:.2f} C, GHI = {ghi_w_m2:.0f})"
    )
