"""Two-node transient human thermal model.

Stage 5 changes (ADR 0005, ADR 0006)
------------------------------------
* Solar radiation absorbed by the textile is a source term in the clothing
  surface balance; the share reaching the skin is an outcome of that balance.
  ``MaterialInput.absorbed_solar_to_body_fraction`` is ignored.
* Solar transmitted through the textile is deposited on the skin node.
* Incident shortwave uses the beam/diffuse split when available
  (``services.solar``); ``PersonInput.position`` selects A_r/A_D.

Retained from Stage 3: body-mass heat capacities (ADR 0001), Gagge 1986
controllers (ADR 0002), explicit clothing surface temperature (ADR 0003).
Every numeric constant is bound from ``model_parameters``.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from math import exp, sqrt

import numpy as np
from scipy.integrate import solve_ivp

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import (
    BodyPosition,
    BodyThermalSummary,
    ClothingSummary,
    EnergyDiagnostics,
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    ScenarioResult,
    TimeSeriesPoint,
)
from app.schemas.weather import WeatherTimeSeries
from app.services.body import BodyHeatCapacities, body_heat_capacities
from app.services.clothing import (
    ClothingResistances,
    assumptions_applied,
    maximum_evaporation_w_m2,
    resolve_clothing,
)
from app.services.model_parameters import get_parameter_value as _param
from app.services.solar import solar_load
from app.services.weather_interpolation import WeatherInterpolator
from app.services.longwave import (
    LongwaveOptics,
    RadiantField,
    longwave_notes,
    net_exchange_k4,
    radiant_field,
    resolve_longwave_optics,
)

from app.services.psychrometrics import saturation_vapor_pressure_kpa

# Version of the physics engine written into every response. Bump together
# with MODEL_PARAMETER_SET_VERSION whenever results change.
MODEL_VERSION = "0.9.0"  # Stage 11: radiant environment v2 (ADR 0008)

# Bound once at import. The registry is the single source of truth.
SIGMA = _param("stefan_boltzmann_constant")
NATURAL_CONVECTION_MINIMUM = _param("natural_convection_minimum_coefficient")
FORCED_CONVECTION_COEFFICIENT = _param("forced_convection_coefficient")
SKIN_EMISSIVITY = _param("skin_emissivity")
RADIATION_AREA_RATIO_STANDING = _param("effective_radiation_area_ratio_standing")
RADIATION_AREA_RATIO_SITTING = _param("effective_radiation_area_ratio_sitting")
SKIN_MASS_FRACTION = _param("skin_mass_fraction")
CORE_SETPOINT = _param("core_setpoint_temperature")
SKIN_SETPOINT = _param("skin_setpoint_temperature")
SWEATING_GAIN_BODY = _param("sweating_gain_body")
SWEATING_SKIN_SIGNAL_SCALE = _param("sweating_skin_signal_scale")
MAXIMUM_SWEAT_RATE = _param("maximum_sweat_rate")
LATENT_HEAT_PER_GRAM_HOUR = _param("latent_heat_of_sweat")
SKIN_DIFFUSION_FRACTION = _param("skin_diffusion_fraction")
W_MAX_CLOTHED_COEFFICIENT = _param("maximum_wettedness_clothed_coefficient")
W_MAX_CLOTHED_EXPONENT = _param("maximum_wettedness_clothed_exponent")
W_MAX_NUDE_COEFFICIENT = _param("maximum_wettedness_nude_coefficient")
W_MAX_NUDE_EXPONENT = _param("maximum_wettedness_nude_exponent")
SKIN_BLOOD_FLOW_BASAL = _param("skin_blood_flow_basal")
VASODILATION_GAIN = _param("vasodilation_gain")
VASOCONSTRICTION_GAIN = _param("vasoconstriction_gain")
SKIN_BLOOD_FLOW_MINIMUM = _param("skin_blood_flow_minimum")
SKIN_BLOOD_FLOW_MAXIMUM = _param("skin_blood_flow_maximum")
CORE_SKIN_CONDUCTANCE_BASAL = _param("core_skin_conductance_basal")
BLOOD_HEAT_CAPACITY_PER_FLOW = _param("blood_heat_capacity_per_flow")
SHIVERING_COEFFICIENT = _param("shivering_coefficient")
METABOLIC_RATE_PER_MET = _param("metabolic_rate_per_met")
RESPIRATORY_LATENT_COEFFICIENT = _param("respiratory_latent_coefficient")
RESPIRATORY_REFERENCE_PRESSURE = _param("respiratory_reference_vapor_pressure")
RESPIRATORY_SENSIBLE_COEFFICIENT = _param("respiratory_sensible_coefficient")
EXHALED_AIR_TEMPERATURE = _param("exhaled_air_temperature")
FALLBACK_SKY_OFFSET = _param("fallback_sky_temperature_offset")


KELVIN_OFFSET = 273.15
BODY_SETPOINT = (
    SKIN_MASS_FRACTION * SKIN_SETPOINT + (1.0 - SKIN_MASS_FRACTION) * CORE_SETPOINT
)

# Numerical (not physical) settings.
SOLVER_METHOD = "RK45"
SOLVER_RTOL = 1e-6
SOLVER_ATOL = 1e-8
SOLVER_MAX_STEP_SECONDS = 60.0
SURFACE_TEMPERATURE_TOLERANCE_K = 1e-5
SURFACE_TEMPERATURE_MAX_ITERATIONS = 30
NUDE_RESISTANCE_THRESHOLD_M2K_W = 1e-6
# Gagge's w_max correlations were fitted for v >= 0.1 m/s.
MINIMUM_WIND_FOR_WETTEDNESS_M_S = 0.1

EnvironmentAt = Callable[[float], EnvironmentInput]


@dataclass
class HeatFluxes:
    convection: float
    longwave_radiation: float
    longwave_transmitted: float
    evaporation: float
    maximum_evaporation: float
    skin_wettedness: float
    maximum_skin_wettedness: float
    solar_incident: float
    solar_absorbed_by_textile: float
    solar_transmitted: float
    absorbed_solar: float  # solar entering the clothing-body system
    core_to_skin: float
    respiration: float
    metabolism: float
    skin_blood_flow: float
    clothing_surface_temperature_c: float
    radiation_area_ratio: float
    # Stage 10 (selective emitters only)
    longwave_window: float | None = None
    sky_window_emissivity: float | None = None

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


def effective_radiation_area_ratio(position: BodyPosition) -> float:
    """A_r / A_D for the given posture (ADR 0006)."""
    if position == "sitting":
        return RADIATION_AREA_RATIO_SITTING
    return RADIATION_AREA_RATIO_STANDING



def convection_coefficient_w_m2k(wind_speed_m_s: float) -> float:
    return max(
        NATURAL_CONVECTION_MINIMUM,
        FORCED_CONVECTION_COEFFICIENT * sqrt(max(wind_speed_m_s, 0.0)),
    )


def environment_radiant_fourth_power_k4(environment: EnvironmentInput) -> float:
    """F_sky * T_sky^4 + (1 - F_sky) * T_mrt^4 in K^4."""
    sky_temperature_c = environment.sky_temperature_c
    if sky_temperature_c is None:
        sky_temperature_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET

    sky_k = sky_temperature_c + KELVIN_OFFSET
    radiant_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    f = environment.sky_view_factor

    return f * sky_k**4 + (1.0 - f) * radiant_k**4

def clothing_surface_temperature_c(
    *,
    skin_temperature_c: float,
    air_temperature_c: float,
    environment_fourth_k4: float,
    clothing: ClothingResistances,
    convection_coefficient: float,
    emissivity: float,
    radiation_area_ratio: float,
    absorbed_solar_w_m2: float = 0.0,
    optics: LongwaveOptics | None = None,
    field: RadiantField | None = None,
) -> float:
    """Solve the clothing surface balance (ADR 0003 + 0005 + 0007).

    Gray path: (A_r/A_D) eps sigma (T_cl^4 - T_env^4). Selective path: the
    same balance with window and out-of-window bands. Both emission terms
    increase with T_cl, so the residual stays strictly decreasing.
    """
    if clothing.dry_resistance_m2k_w < NUDE_RESISTANCE_THRESHOLD_M2K_W:
        return skin_temperature_c

    selective = optics is not None and optics.selective and field is not None

    resistance = clothing.dry_resistance_m2k_w
    area_factor = clothing.area_factor
    skin_k = skin_temperature_c + KELVIN_OFFSET
    air_k = air_temperature_c + KELVIN_OFFSET
    gray_factor = radiation_area_ratio * emissivity * SIGMA

    t = skin_k

    for _ in range(SURFACE_TEMPERATURE_MAX_ITERATIONS):
        if selective:
            net, net_slope, _ = net_exchange_k4(optics, field, t)
            emission = radiation_area_ratio * SIGMA * net
            emission_slope = radiation_area_ratio * SIGMA * net_slope
        else:
            emission = gray_factor * (t**4 - environment_fourth_k4)
            emission_slope = 4.0 * gray_factor * t**3

        residual = (
            (skin_k - t) / resistance
            + absorbed_solar_w_m2
            - area_factor * (convection_coefficient * (t - air_k) + emission)
        )
        derivative = -1.0 / resistance - area_factor * (
            convection_coefficient + emission_slope
        )
        step = residual / derivative
        t -= step

        if abs(step) < SURFACE_TEMPERATURE_TOLERANCE_K:
            return t - KELVIN_OFFSET

    raise RuntimeError(
        "Clothing surface temperature iteration did not converge "
        f"(T_sk = {skin_temperature_c:.3f} C, T_a = {air_temperature_c:.3f} C, "
        f"S_abs = {absorbed_solar_w_m2:.1f} W/m^2)"
    )

def maximum_skin_wettedness(wind_speed_m_s: float, clothing: ClothingResistances) -> float:
    v = max(wind_speed_m_s, MINIMUM_WIND_FOR_WETTEDNESS_M_S)
    if clothing.is_nude:
        w_max = W_MAX_NUDE_COEFFICIENT * v**W_MAX_NUDE_EXPONENT
    else:
        w_max = W_MAX_CLOTHED_COEFFICIENT * v**W_MAX_CLOTHED_EXPONENT
    return clamp(w_max, SKIN_DIFFUSION_FRACTION, 1.0)


def calculate_fluxes(
    core_temperature_c: float,
    skin_temperature_c: float,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
    clothing: ClothingResistances | None = None,
    optics: LongwaveOptics | None = None,
) -> HeatFluxes:
    if clothing is None:
        clothing = resolve_clothing(material)
    if optics is None:
        optics = resolve_longwave_optics(material)

    air_temperature_c = environment.air_temperature_c
    area_ratio = effective_radiation_area_ratio(person.position)

    # --- thermoregulatory signals (Gagge 1986) ------------------------------
    warm_skin = max(skin_temperature_c - SKIN_SETPOINT, 0.0)
    cold_skin = max(SKIN_SETPOINT - skin_temperature_c, 0.0)
    warm_core = max(core_temperature_c - CORE_SETPOINT, 0.0)
    cold_core = max(CORE_SETPOINT - core_temperature_c, 0.0)

    body_temperature_c = (
        SKIN_MASS_FRACTION * skin_temperature_c
        + (1.0 - SKIN_MASS_FRACTION) * core_temperature_c
    )
    warm_body = max(body_temperature_c - BODY_SETPOINT, 0.0)

    # --- solar (ADR 0005 / 0006) --------------------------------------------
    solar = solar_load(environment, material, area_ratio)

    # --- dry heat: clothing surface balance with the solar source -----------
    convection_coefficient = convection_coefficient_w_m2k(environment.wind_speed_m_s)

    if optics.selective:
        field = radiant_field(environment)
        environment_fourth = field.total_k4
    else:
        field = None
        environment_fourth = environment_radiant_fourth_power_k4(environment)

    surface_c = clothing_surface_temperature_c(
        skin_temperature_c=skin_temperature_c,
        air_temperature_c=air_temperature_c,
        environment_fourth_k4=environment_fourth,
        clothing=clothing,
        convection_coefficient=convection_coefficient,
        emissivity=material.infrared_emissivity,
        radiation_area_ratio=area_ratio,
        absorbed_solar_w_m2=solar.absorbed_by_textile_w_m2,
        optics=optics,
        field=field,
    )
    surface_k = surface_c + KELVIN_OFFSET
    skin_k = skin_temperature_c + KELVIN_OFFSET

    convection = clothing.area_factor * convection_coefficient * (
        surface_c - air_temperature_c
    )

    longwave_window: float | None = None
    if field is not None:
        net, _, net_window = net_exchange_k4(optics, field, surface_k)
        longwave_surface = clothing.area_factor * area_ratio * SIGMA * net
        longwave_window = clothing.area_factor * area_ratio * SIGMA * net_window
    else:
        longwave_surface = (
            clothing.area_factor
            * area_ratio
            * material.infrared_emissivity
            * SIGMA
            * (surface_k**4 - environment_fourth)
        )

    # Skin emission transmitted directly through an IR-transparent textile
    # (skin and transmittance are gray).
    longwave_transmitted = (
        area_ratio
        * clothing.infrared_transmittance
        * SKIN_EMISSIVITY
        * SIGMA
        * (skin_k**4 - environment_fourth)
    )

    longwave_radiation = longwave_surface + longwave_transmitted

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

    regulatory_sweating_g_h_m2 = min(
        SWEATING_GAIN_BODY * warm_body * exp(warm_skin / SWEATING_SKIN_SIGNAL_SCALE),
        MAXIMUM_SWEAT_RATE,
    )
    regulatory_evaporation = regulatory_sweating_g_h_m2 * LATENT_HEAT_PER_GRAM_HOUR

    w_max = maximum_skin_wettedness(environment.wind_speed_m_s, clothing)

    if maximum_evaporation <= 0.0:
        skin_wettedness = w_max
        evaporation = 0.0
    else:
        sweat_ratio = regulatory_evaporation / maximum_evaporation
        skin_wettedness = min(
            SKIN_DIFFUSION_FRACTION + (1.0 - SKIN_DIFFUSION_FRACTION) * sweat_ratio,
            w_max,
        )
        evaporation = skin_wettedness * maximum_evaporation

    # --- core <-> skin ------------------------------------------------------
    skin_blood_flow = clamp(
        (SKIN_BLOOD_FLOW_BASAL + VASODILATION_GAIN * warm_core)
        / (1.0 + VASOCONSTRICTION_GAIN * cold_skin),
        SKIN_BLOOD_FLOW_MINIMUM,
        SKIN_BLOOD_FLOW_MAXIMUM,
    )

    core_skin_conductance = (
        CORE_SKIN_CONDUCTANCE_BASAL + BLOOD_HEAT_CAPACITY_PER_FLOW * skin_blood_flow
    )

    core_to_skin = core_skin_conductance * (core_temperature_c - skin_temperature_c)

    # --- metabolism and respiration -----------------------------------------
    metabolism = (
        person.met * METABOLIC_RATE_PER_MET
        + SHIVERING_COEFFICIENT * cold_skin * cold_core
    )

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
        longwave_transmitted=longwave_transmitted,
        evaporation=evaporation,
        maximum_evaporation=maximum_evaporation,
        skin_wettedness=skin_wettedness,
        maximum_skin_wettedness=w_max,
        solar_incident=solar.incident_w_m2,
        solar_absorbed_by_textile=solar.absorbed_by_textile_w_m2,
        solar_transmitted=solar.transmitted_to_skin_w_m2,
        absorbed_solar=solar.entering_system_w_m2,
        core_to_skin=core_to_skin,
        respiration=respiration,
        metabolism=metabolism,
        skin_blood_flow=skin_blood_flow,
        clothing_surface_temperature_c=surface_c,
        radiation_area_ratio=area_ratio,
        longwave_window=longwave_window,
        sky_window_emissivity=None if field is None else field.sky_window_emissivity,
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
    capacities: BodyHeatCapacities,
) -> EnergyDiagnostics:
    integrated_net_heat = float(np.trapezoid(net_heat_fluxes, times_seconds))

    stored_energy_change = float(
        capacities.core_j_m2k * (core_temperatures[-1] - core_temperatures[0])
        + capacities.skin_j_m2k * (skin_temperatures[-1] - skin_temperatures[0])
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
        diagnostic_interval_seconds=DIAGNOSTIC_INTERVAL_SECONDS,
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
    optics = resolve_longwave_optics(material)
    capacities = body_heat_capacities(person)
    area_ratio = effective_radiation_area_ratio(person.position)
    solar_split_available = environment_at(0.0).has_solar_split

    duration_seconds = duration_minutes * 60.0
    output_times = _output_times(duration_seconds, output_interval_minutes * 60.0)
    eval_times = _diagnostic_times(duration_seconds, output_times)

    def derivatives(time_seconds: float, state: np.ndarray) -> list[float]:
        fluxes = calculate_fluxes(
            core_temperature_c=float(state[0]),
            skin_temperature_c=float(state[1]),
            environment=environment_at(float(time_seconds)),
            person=person,
            material=material,
            clothing=clothing,
            optics=optics,
        )

        core_storage = fluxes.metabolism - fluxes.respiration - fluxes.core_to_skin
        # absorbed_solar = textile absorption (routed through the surface
        # balance, which already raised convection/longwave) + transmission.
        skin_storage = (
            fluxes.core_to_skin
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        return [
            core_storage / capacities.core_j_m2k,
            skin_storage / capacities.skin_j_m2k,
        ]
        
    solution = solve_ivp(
        fun=derivatives,
        t_span=(0.0, duration_seconds),
        y0=[person.initial_core_temperature_c, person.initial_skin_temperature_c],
        t_eval=eval_times,
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
    is_output = np.isin(times, output_times)

    time_series: list[TimeSeriesPoint] = []
    net_heat: list[float] = []

    for time_seconds, core_c, skin_c, emit in zip(times, core_array, skin_array, is_output, strict=True):
        environment = environment_at(float(time_seconds))
        fluxes = calculate_fluxes(
            core_temperature_c=float(core_c),
            skin_temperature_c=float(skin_c),
            environment=environment,
            person=person,
            material=material,
            clothing=clothing,
            optics=optics,
        )
        net_heat.append(fluxes.net_body_gain)

        if not emit:
            continue

        sky_c = environment.sky_temperature_c
        if sky_c is None:
            sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET

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
                clothing_surface_temperature_c=round(fluxes.clothing_surface_temperature_c, 4),
                skin_blood_flow_kg_h_m2=round(fluxes.skin_blood_flow, 4),
                solar_incident_w_m2=round(fluxes.solar_incident, 4),
                solar_absorbed_by_textile_w_m2=round(fluxes.solar_absorbed_by_textile, 4),
                solar_transmitted_w_m2=round(fluxes.solar_transmitted, 4),
                longwave_window_w_m2=(
                    None if fluxes.longwave_window is None else round(fluxes.longwave_window, 4)
                ),
                sky_temperature_c=round(sky_c, 4),
                surround_temperature_c=round(environment.mean_radiant_temperature_c, 4),
            )
        )

    diagnostics = _energy_diagnostics(
        times, core_array, skin_array, np.asarray(net_heat), solution.nfev, capacities
    )

    return ScenarioResult(
        material_name=material.name,
        time_series=time_series,
        final_core_temperature_c=time_series[-1].core_temperature_c,
        final_skin_temperature_c=time_series[-1].skin_temperature_c,
        peak_core_temperature_c=round(float(core_array.max()), 4),
        peak_skin_temperature_c=round(float(skin_array.max()), 4),
        diagnostics=diagnostics,
        clothing=ClothingSummary(
            dry_resistance_m2k_w=round(clothing.dry_resistance_m2k_w, 6),
            evaporative_resistance_m2pa_w=round(clothing.evaporative_resistance_m2pa_w, 4),
            evaporative_resistance_source=clothing.evaporative_resistance_source,
            infrared_transmittance=clothing.infrared_transmittance,
            clothing_area_factor=round(clothing.area_factor, 6),
            clothing_area_factor_source=clothing.area_factor_source,
            infrared_emissivity_window=round(optics.window, 6) if optics.selective else None,
            infrared_emissivity_outside_window=round(optics.outside, 6) if optics.selective else None,
        ),
        assumptions_applied=(
            assumptions_applied(clothing, solar_split_available=solar_split_available)
            + longwave_notes(optics)
        ),
        body=BodyThermalSummary(
            body_mass_kg=person.body_mass_kg,
            body_surface_area_m2=person.body_surface_area_m2,
            core_heat_capacity_j_m2k=round(capacities.core_j_m2k, 2),
            skin_heat_capacity_j_m2k=round(capacities.skin_j_m2k, 2),
            position=person.position,
            effective_radiation_area_ratio=area_ratio,
        ),
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

def simulate_material_with_interpolator(
    duration_minutes: int,
    output_interval_minutes: int,
    interpolator: WeatherInterpolator,
    person: PersonInput,
    material: MaterialInput,
) -> ScenarioResult:
    """Same physics as simulate_material_with_weather, but reuses a prebuilt
    interpolator (optimization evaluates thousands of garments per window)."""
    interpolator.ensure_covers(0.0, duration_minutes * 60.0)

    return _integrate(
        duration_minutes=duration_minutes,
        output_interval_minutes=output_interval_minutes,
        environment_at=interpolator.environment_at,
        person=person,
        material=material,
        failure_label="Weather-driven numerical solution failed",
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
    return simulate_material_with_interpolator(
        duration_minutes, output_interval_minutes, interpolator, person, material
    )
    
# Numerical (not physical) settings.
DIAGNOSTIC_INTERVAL_SECONDS = 60.0  # energy audit grid, independent of output interval


def _diagnostic_times(duration_seconds: float, output_times: np.ndarray) -> np.ndarray:
    """Union of a fixed 60 s audit grid and the requested output times.

    solve_ivp chooses its steps independently of t_eval, so evaluating on a
    denser grid does not change the trajectory at the output times; it only
    makes the energy-balance integral independent of output_interval_minutes.
    """
    fine = np.arange(0.0, duration_seconds + 0.1, DIAGNOSTIC_INTERVAL_SECONDS)
    if fine[-1] < duration_seconds:
        fine = np.append(fine, duration_seconds)
    return np.unique(np.concatenate([fine, output_times]))