"""Two-node transient human thermal model.

Stage 2 changes
---------------
* Evaporation is limited by an explicit clothing evaporative resistance
  (``MaterialInput.evaporative_resistance_m2pa_w``). If the material does not
  supply one it is derived from clo (see ``clothing.py``) and reported in
  ``ScenarioResult.assumptions_applied``.
* ``infrared_transmittance`` participates in the longwave term: transmitted
  skin emission bypasses the clothing coupling factor (first-order model).
* Every numeric constant is bound from ``model_parameters`` (unit + source).
* Fixed-environment and weather-driven runs share ``_integrate``; the
  weather-driven path takes explicit ``EnvironmentAssumptions``.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from math import exp, sqrt

import numpy as np
from scipy.integrate import solve_ivp

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import (
    ClothingSummary,
    EnergyDiagnostics,
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    ScenarioResult,
    TimeSeriesPoint,
)
from app.schemas.weather import WeatherTimeSeries
from app.services.clothing import (
    ClothingResistances,
    assumptions_applied,
    maximum_evaporation_w_m2,
    resolve_clothing,
)
from app.services.model_parameters import get_parameter_value as _param
from app.services.weather_interpolation import WeatherInterpolator


# Bound once at import. The registry is the single source of truth.
SIGMA = _param("stefan_boltzmann_constant")
CORE_HEAT_CAPACITY = _param("core_heat_capacity")
SKIN_HEAT_CAPACITY = _param("skin_heat_capacity")
NATURAL_CONVECTION_MINIMUM = _param("natural_convection_minimum_coefficient")
FORCED_CONVECTION_COEFFICIENT = _param("forced_convection_coefficient")
LINEARIZED_RADIATIVE_COEFFICIENT = _param("linearized_radiative_coefficient")
SKIN_EMISSIVITY = _param("skin_emissivity")
CORE_SETPOINT = _param("core_setpoint_temperature")
SKIN_SETPOINT = _param("skin_setpoint_temperature")
SWEATING_GAIN_CORE = _param("sweating_gain_core")
SWEATING_GAIN_SKIN = _param("sweating_gain_skin")
MAXIMUM_SWEAT_RATE = _param("maximum_sweat_rate")
LATENT_HEAT_PER_GRAM_HOUR = _param("latent_heat_of_sweat")
SKIN_DIFFUSION_FRACTION = _param("skin_diffusion_fraction")
SKIN_BLOOD_FLOW_BASAL = _param("skin_blood_flow_basal")
SKIN_BLOOD_FLOW_CORE_GAIN = _param("skin_blood_flow_core_gain")
SKIN_BLOOD_FLOW_SKIN_GAIN = _param("skin_blood_flow_skin_gain")
SKIN_BLOOD_FLOW_MINIMUM = _param("skin_blood_flow_minimum")
SKIN_BLOOD_FLOW_MAXIMUM = _param("skin_blood_flow_maximum")
CORE_SKIN_CONDUCTANCE_BASAL = _param("core_skin_conductance_basal")
BLOOD_HEAT_CAPACITY_PER_FLOW = _param("blood_heat_capacity_per_flow")
METABOLIC_RATE_PER_MET = _param("metabolic_rate_per_met")
RESPIRATORY_LATENT_COEFFICIENT = _param("respiratory_latent_coefficient")
RESPIRATORY_REFERENCE_PRESSURE = _param("respiratory_reference_vapor_pressure")
RESPIRATORY_SENSIBLE_COEFFICIENT = _param("respiratory_sensible_coefficient")
EXHALED_AIR_TEMPERATURE = _param("exhaled_air_temperature")
FALLBACK_SKY_OFFSET = _param("fallback_sky_temperature_offset")
MAGNUS_A = _param("magnus_a")
MAGNUS_B = _param("magnus_b")
MAGNUS_C = _param("magnus_c")

KELVIN_OFFSET = 273.15

# Numerical (not physical) settings.
SOLVER_METHOD = "RK45"
SOLVER_RTOL = 1e-6
SOLVER_ATOL = 1e-8
SOLVER_MAX_STEP_SECONDS = 60.0

EnvironmentAt = Callable[[float], EnvironmentInput]


@dataclass
class HeatFluxes:
    convection: float
    longwave_radiation: float
    evaporation: float
    maximum_evaporation: float
    skin_wettedness: float
    absorbed_solar: float
    core_to_skin: float
    respiration: float
    metabolism: float

    @property
    def net_body_gain(self) -> float:
        """Whole-body net heat gain; core_to_skin is internal and cancels."""
        return (
            self.metabolism
            - self.respiration
            + self.absorbed_solar
            - self.convection
            - self.longwave_radiation
            - self.evaporation
        )


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def saturation_vapor_pressure_kpa(temperature_c: float) -> float:
    return MAGNUS_A * exp(MAGNUS_B * temperature_c / (temperature_c + MAGNUS_C))


def calculate_fluxes(
    core_temperature_c: float,
    skin_temperature_c: float,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
    clothing: ClothingResistances | None = None,
) -> HeatFluxes:
    if clothing is None:
        clothing = resolve_clothing(material)

    air_temperature_c = environment.air_temperature_c

    sky_temperature_c = environment.sky_temperature_c
    if sky_temperature_c is None:
        sky_temperature_c = air_temperature_c - FALLBACK_SKY_OFFSET

    # --- convection ---------------------------------------------------------
    convection_coefficient = max(
        NATURAL_CONVECTION_MINIMUM,
        FORCED_CONVECTION_COEFFICIENT * sqrt(max(environment.wind_speed_m_s, 0.0)),
    )

    clothing_coupling = 1.0 / (
        1.0
        + clothing.dry_resistance_m2k_w
        * (convection_coefficient + LINEARIZED_RADIATIVE_COEFFICIENT)
    )

    convection = (
        convection_coefficient
        * (skin_temperature_c - air_temperature_c)
        * clothing_coupling
    )

    # --- longwave radiation -------------------------------------------------
    skin_k = skin_temperature_c + KELVIN_OFFSET
    sky_k = sky_temperature_c + KELVIN_OFFSET
    radiant_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET

    sky_view_factor = environment.sky_view_factor

    net_radiation = SIGMA * (
        sky_view_factor * (skin_k**4 - sky_k**4)
        + (1.0 - sky_view_factor) * (skin_k**4 - radiant_k**4)
    )

    # Emission from the textile surface (attenuated by the clothing coupling)
    # plus skin emission transmitted directly through an IR-transparent textile.
    effective_emitter = (
        material.infrared_emissivity * clothing_coupling
        + clothing.infrared_transmittance * SKIN_EMISSIVITY
    )

    longwave_radiation = effective_emitter * net_radiation

    # --- solar --------------------------------------------------------------
    solar_absorptance = clamp(
        1.0 - material.solar_reflectance - material.solar_transmittance, 0.0, 1.0
    )

    absorbed_solar = (
        solar_absorptance
        * environment.solar_radiation_w_m2
        * material.projected_solar_area_factor
        * material.absorbed_solar_to_body_fraction
    )

    # --- evaporation --------------------------------------------------------
    ambient_vapor_pressure_kpa = (
        environment.relative_humidity_percent / 100.0
        * saturation_vapor_pressure_kpa(air_temperature_c)
    )
    skin_vapor_pressure_kpa = saturation_vapor_pressure_kpa(skin_temperature_c)

    maximum_evaporation = maximum_evaporation_w_m2(
        clothing,
        convection_coefficient,
        skin_vapor_pressure_kpa,
        ambient_vapor_pressure_kpa,
    )

    regulatory_sweating_g_h_m2 = clamp(
        SWEATING_GAIN_CORE * max(core_temperature_c - CORE_SETPOINT, 0.0)
        + SWEATING_GAIN_SKIN * max(skin_temperature_c - SKIN_SETPOINT, 0.0),
        0.0,
        MAXIMUM_SWEAT_RATE,
    )

    regulatory_evaporation = regulatory_sweating_g_h_m2 * LATENT_HEAT_PER_GRAM_HOUR
    diffusion_evaporation = SKIN_DIFFUSION_FRACTION * maximum_evaporation

    evaporation = min(maximum_evaporation, regulatory_evaporation + diffusion_evaporation)

    skin_wettedness = (
        evaporation / maximum_evaporation if maximum_evaporation > 0.0 else 1.0
    )

    # --- core <-> skin ------------------------------------------------------
    skin_blood_flow = clamp(
        SKIN_BLOOD_FLOW_BASAL
        + SKIN_BLOOD_FLOW_CORE_GAIN * max(core_temperature_c - CORE_SETPOINT, 0.0)
        + SKIN_BLOOD_FLOW_SKIN_GAIN * max(skin_temperature_c - SKIN_SETPOINT, 0.0),
        SKIN_BLOOD_FLOW_MINIMUM,
        SKIN_BLOOD_FLOW_MAXIMUM,
    )

    core_skin_conductance = (
        CORE_SKIN_CONDUCTANCE_BASAL + BLOOD_HEAT_CAPACITY_PER_FLOW * skin_blood_flow
    )

    core_to_skin = core_skin_conductance * (core_temperature_c - skin_temperature_c)

    # --- metabolism and respiration -----------------------------------------
    metabolism = person.met * METABOLIC_RATE_PER_MET

    respiration_latent = max(
        0.0,
        RESPIRATORY_LATENT_COEFFICIENT
        * metabolism
        * (RESPIRATORY_REFERENCE_PRESSURE - ambient_vapor_pressure_kpa * 1000.0),
    )

    respiration_sensible = (
        RESPIRATORY_SENSIBLE_COEFFICIENT
        * metabolism
        * (EXHALED_AIR_TEMPERATURE - air_temperature_c)
    )

    respiration = max(0.0, respiration_latent + respiration_sensible)

    return HeatFluxes(
        convection=convection,
        longwave_radiation=longwave_radiation,
        evaporation=evaporation,
        maximum_evaporation=maximum_evaporation,
        skin_wettedness=skin_wettedness,
        absorbed_solar=absorbed_solar,
        core_to_skin=core_to_skin,
        respiration=respiration,
        metabolism=metabolism,
    )


def _output_times(duration_seconds: float, interval_seconds: float) -> np.ndarray:
    times = np.arange(0.0, duration_seconds + 0.1, interval_seconds)
    if times[-1] < duration_seconds:
        times = np.append(times, duration_seconds)
    return times


def _energy_diagnostics(
    times_seconds: np.ndarray,
    core_temperatures: np.ndarray,
    skin_temperatures: np.ndarray,
    net_heat_fluxes: np.ndarray,
    solver_function_evaluations: int,
) -> EnergyDiagnostics:
    integrated_net_heat = float(np.trapezoid(net_heat_fluxes, times_seconds))

    stored_energy_change = float(
        CORE_HEAT_CAPACITY * (core_temperatures[-1] - core_temperatures[0])
        + SKIN_HEAT_CAPACITY * (skin_temperatures[-1] - skin_temperatures[0])
    )

    residual = stored_energy_change - integrated_net_heat
    denominator = max(abs(stored_energy_change), abs(integrated_net_heat), 1.0)

    def max_step(values: np.ndarray) -> float:
        return float(np.max(np.abs(np.diff(values)))) if len(values) > 1 else 0.0

    return EnergyDiagnostics(
        stored_energy_change_j_m2=round(stored_energy_change, 4),
        integrated_net_heat_j_m2=round(integrated_net_heat, 4),
        energy_residual_j_m2=round(residual, 4),
        normalized_residual_percent=round(abs(residual) / denominator * 100.0, 6),
        maximum_core_step_c=round(max_step(core_temperatures), 6),
        maximum_skin_step_c=round(max_step(skin_temperatures), 6),
        solver_function_evaluations=int(solver_function_evaluations),
    )


def _integrate(
    *,
    duration_minutes: int,
    output_interval_minutes: int,
    environment_at: EnvironmentAt,
    person: PersonInput,
    material: MaterialInput,
    failure_label: str,
) -> ScenarioResult:
    clothing = resolve_clothing(material)

    duration_seconds = duration_minutes * 60.0
    output_times = _output_times(duration_seconds, output_interval_minutes * 60.0)

    def derivatives(time_seconds: float, state: np.ndarray) -> list[float]:
        fluxes = calculate_fluxes(
            core_temperature_c=float(state[0]),
            skin_temperature_c=float(state[1]),
            environment=environment_at(float(time_seconds)),
            person=person,
            material=material,
            clothing=clothing,
        )

        core_storage = fluxes.metabolism - fluxes.respiration - fluxes.core_to_skin
        skin_storage = (
            fluxes.core_to_skin
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        return [core_storage / CORE_HEAT_CAPACITY, skin_storage / SKIN_HEAT_CAPACITY]

    solution = solve_ivp(
        fun=derivatives,
        t_span=(0.0, duration_seconds),
        y0=[person.initial_core_temperature_c, person.initial_skin_temperature_c],
        t_eval=output_times,
        method=SOLVER_METHOD,
        rtol=SOLVER_RTOL,
        atol=SOLVER_ATOL,
        max_step=SOLVER_MAX_STEP_SECONDS,
    )

    if not solution.success:
        raise RuntimeError(f"{failure_label}: {solution.message}")

    times = np.asarray(solution.t, dtype=float)
    core_array = np.asarray(solution.y[0], dtype=float)
    skin_array = np.asarray(solution.y[1], dtype=float)

    time_series: list[TimeSeriesPoint] = []
    net_heat: list[float] = []

    for time_seconds, core_c, skin_c in zip(times, core_array, skin_array, strict=True):
        fluxes = calculate_fluxes(
            core_temperature_c=float(core_c),
            skin_temperature_c=float(skin_c),
            environment=environment_at(float(time_seconds)),
            person=person,
            material=material,
            clothing=clothing,
        )

        net_heat.append(fluxes.net_body_gain)

        time_series.append(
            TimeSeriesPoint(
                minute=round(float(time_seconds) / 60.0, 4),
                core_temperature_c=round(float(core_c), 4),
                skin_temperature_c=round(float(skin_c), 4),
                convection_w_m2=round(fluxes.convection, 4),
                longwave_radiation_w_m2=round(fluxes.longwave_radiation, 4),
                evaporation_w_m2=round(fluxes.evaporation, 4),
                absorbed_solar_w_m2=round(fluxes.absorbed_solar, 4),
                core_to_skin_w_m2=round(fluxes.core_to_skin, 4),
                maximum_evaporation_w_m2=round(fluxes.maximum_evaporation, 4),
                skin_wettedness=round(fluxes.skin_wettedness, 4),
            )
        )

    diagnostics = _energy_diagnostics(
        times, core_array, skin_array, np.asarray(net_heat), solution.nfev
    )

    core_temperatures = [p.core_temperature_c for p in time_series]
    skin_temperatures = [p.skin_temperature_c for p in time_series]

    return ScenarioResult(
        material_name=material.name,
        time_series=time_series,
        final_core_temperature_c=core_temperatures[-1],
        final_skin_temperature_c=skin_temperatures[-1],
        peak_core_temperature_c=max(core_temperatures),
        peak_skin_temperature_c=max(skin_temperatures),
        diagnostics=diagnostics,
        clothing=ClothingSummary(
            dry_resistance_m2k_w=round(clothing.dry_resistance_m2k_w, 6),
            evaporative_resistance_m2pa_w=round(clothing.evaporative_resistance_m2pa_w, 4),
            evaporative_resistance_source=clothing.evaporative_resistance_source,
            infrared_transmittance=clothing.infrared_transmittance,
        ),
        assumptions_applied=assumptions_applied(clothing),
    )


def simulate_material(
    duration_minutes: int,
    output_interval_minutes: int,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
) -> ScenarioResult:
    return _integrate(
        duration_minutes=duration_minutes,
        output_interval_minutes=output_interval_minutes,
        environment_at=lambda _time_seconds: environment,
        person=person,
        material=material,
        failure_label="Fixed-environment numerical solution failed",
    )


def simulate_material_with_weather(
    duration_minutes: int,
    output_interval_minutes: int,
    weather: WeatherTimeSeries,
    person: PersonInput,
    material: MaterialInput,
    assumptions: EnvironmentAssumptions | None = None,
) -> ScenarioResult:
    interpolator = WeatherInterpolator.from_series(
        weather, assumptions=assumptions or EnvironmentAssumptions()
    )

    # Fail before solving if the requested duration exceeds the weather data.
    interpolator.ensure_covers(0.0, duration_minutes * 60.0)

    return _integrate(
        duration_minutes=duration_minutes,
        output_interval_minutes=output_interval_minutes,
        environment_at=interpolator.environment_at,
        person=person,
        material=material,
        failure_label="Weather-driven numerical solution failed",
    )