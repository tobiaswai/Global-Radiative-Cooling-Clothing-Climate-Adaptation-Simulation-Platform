from __future__ import annotations

from dataclasses import dataclass
from math import exp, sqrt

import numpy as np
from scipy.integrate import solve_ivp

from app.schemas.weather import WeatherTimeSeries
from app.services.weather_interpolation import (
    WeatherInterpolator,
)

from app.schemas.simulation import (
    EnergyDiagnostics,
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    ScenarioResult,
    TimeSeriesPoint,
)


SIGMA = 5.670374419e-8

# 人體核心與皮膚的面積歸一化有效熱容量，J/(m²·K)
CORE_HEAT_CAPACITY = 245_000.0
SKIN_HEAT_CAPACITY = 35_000.0


@dataclass
class HeatFluxes:
    convection: float
    longwave_radiation: float
    evaporation: float
    absorbed_solar: float
    core_to_skin: float
    respiration: float
    metabolism: float


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def saturation_vapor_pressure_kpa(temperature_c: float) -> float:
    """
    Magnus 型近似飽和水汽壓，單位 kPa。
    """
    return 0.61078 * exp(
        17.2694 * temperature_c
        / (temperature_c + 237.3)
    )


def calculate_fluxes(
    core_temperature_c: float,
    skin_temperature_c: float,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
) -> HeatFluxes:
    air_temperature_c = environment.air_temperature_c
    radiant_temperature_c = (
        environment.mean_radiant_temperature_c
    )

    sky_temperature_c = environment.sky_temperature_c
    if sky_temperature_c is None:
        sky_temperature_c = air_temperature_c - 15.0

    relative_humidity = (
        environment.relative_humidity_percent / 100.0
    )
    wind_speed = environment.wind_speed_m_s

    clothing_resistance = (
        0.155 * material.clothing_insulation_clo
    )

    # 強制對流與自然對流中取較大者
    forced_convection = 8.3 * sqrt(max(wind_speed, 0.0))
    convection_coefficient = max(3.1, forced_convection)

    # 服裝熱阻造成皮膚熱量傳到外表面的衰減
    clothing_coupling = 1.0 / (
        1.0
        + clothing_resistance
        * (convection_coefficient + 5.5)
    )

    convection = (
        convection_coefficient
        * (skin_temperature_c - air_temperature_c)
        * clothing_coupling
    )

    skin_temperature_k = skin_temperature_c + 273.15
    sky_temperature_k = sky_temperature_c + 273.15
    radiant_temperature_k = radiant_temperature_c + 273.15

    sky_view_factor = environment.sky_view_factor
    surroundings_view_factor = 1.0 - sky_view_factor

    sky_radiation = (
        sky_view_factor
        * SIGMA
        * (
            skin_temperature_k**4
            - sky_temperature_k**4
        )
    )

    surroundings_radiation = (
        surroundings_view_factor
        * SIGMA
        * (
            skin_temperature_k**4
            - radiant_temperature_k**4
        )
    )

    longwave_radiation = (
        material.infrared_emissivity
        * (sky_radiation + surroundings_radiation)
        * clothing_coupling
    )

    solar_absorptance = (
        1.0
        - material.solar_reflectance
        - material.solar_transmittance
    )
    solar_absorptance = clamp(solar_absorptance, 0.0, 1.0)

    absorbed_solar = (
        solar_absorptance
        * environment.solar_radiation_w_m2
        * material.projected_solar_area_factor
        * material.absorbed_solar_to_body_fraction
    )

    ambient_vapor_pressure_kpa = (
        relative_humidity
        * saturation_vapor_pressure_kpa(
            air_temperature_c
        )
    )
    skin_vapor_pressure_kpa = (
        saturation_vapor_pressure_kpa(
            skin_temperature_c
        )
    )

    evaporative_coefficient = (
        16.5 * convection_coefficient
    )

    clothing_evaporative_efficiency = 1.0 / (
        1.0
        + 0.45
        * material.clothing_insulation_clo
        * convection_coefficient
    )

    maximum_evaporation = max(
        0.0,
        evaporative_coefficient
        * (
            skin_vapor_pressure_kpa
            - ambient_vapor_pressure_kpa
        )
        * clothing_evaporative_efficiency,
    )

    regulatory_sweating_g_h_m2 = clamp(
        170.0 * max(core_temperature_c - 36.8, 0.0)
        + 200.0 * max(skin_temperature_c - 33.7, 0.0),
        0.0,
        500.0,
    )

    regulatory_evaporation = (
        regulatory_sweating_g_h_m2 * 0.68
    )
    diffusion_evaporation = 0.06 * maximum_evaporation

    evaporation = min(
        maximum_evaporation,
        regulatory_evaporation + diffusion_evaporation,
    )

    skin_blood_flow = clamp(
        6.3
        + 75.0 * max(core_temperature_c - 36.8, 0.0)
        + 20.0 * max(skin_temperature_c - 33.7, 0.0),
        0.5,
        90.0,
    )

    core_skin_conductance = (
        5.28 + 1.163 * skin_blood_flow
    )

    core_to_skin = (
        core_skin_conductance
        * (core_temperature_c - skin_temperature_c)
    )

    metabolism = person.met * 58.15

    ambient_vapor_pressure_pa = (
        ambient_vapor_pressure_kpa * 1000.0
    )

    respiration_latent = max(
        0.0,
        1.7e-5
        * metabolism
        * (5867.0 - ambient_vapor_pressure_pa),
    )

    respiration_sensible = (
        0.0014
        * metabolism
        * (34.0 - air_temperature_c)
    )

    respiration = max(
        0.0,
        respiration_latent + respiration_sensible,
    )

    return HeatFluxes(
        convection=convection,
        longwave_radiation=longwave_radiation,
        evaporation=evaporation,
        absorbed_solar=absorbed_solar,
        core_to_skin=core_to_skin,
        respiration=respiration,
        metabolism=metabolism,
    )

def calculate_energy_diagnostics(
    times_seconds: np.ndarray,
    core_temperatures: np.ndarray,
    skin_temperatures: np.ndarray,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
    solver_function_evaluations: int,
) -> EnergyDiagnostics:
    """
    計算整個模擬期間的人體總能量守恆殘差。

    人體核心與皮膚之間的熱交換 core_to_skin 是內部熱流，
    在人體總能量平衡中會互相抵消，因此不放入總淨熱流。
    """

    net_heat_fluxes: list[float] = []

    for core_temperature, skin_temperature in zip(
        core_temperatures,
        skin_temperatures,
        strict=True,
    ):
        fluxes = calculate_fluxes(
            core_temperature_c=float(core_temperature),
            skin_temperature_c=float(skin_temperature),
            environment=environment,
            person=person,
            material=material,
        )

        net_heat_flux = (
            fluxes.metabolism
            - fluxes.respiration
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        net_heat_fluxes.append(net_heat_flux)

    net_heat_array = np.asarray(
        net_heat_fluxes,
        dtype=float,
    )

    integrated_net_heat = float(
        np.trapezoid(
            y=net_heat_array,
            x=times_seconds,
        )
    )

    stored_energy_change = float(
        CORE_HEAT_CAPACITY
        * (
            core_temperatures[-1]
            - core_temperatures[0]
        )
        + SKIN_HEAT_CAPACITY
        * (
            skin_temperatures[-1]
            - skin_temperatures[0]
        )
    )

    energy_residual = (
        stored_energy_change
        - integrated_net_heat
    )

    normalization_denominator = max(
        abs(stored_energy_change),
        abs(integrated_net_heat),
        1.0,
    )

    normalized_residual_percent = (
        abs(energy_residual)
        / normalization_denominator
        * 100.0
    )

    maximum_core_step = (
        float(np.max(np.abs(np.diff(core_temperatures))))
        if len(core_temperatures) > 1
        else 0.0
    )

    maximum_skin_step = (
        float(np.max(np.abs(np.diff(skin_temperatures))))
        if len(skin_temperatures) > 1
        else 0.0
    )

    return EnergyDiagnostics(
        stored_energy_change_j_m2=round(
            stored_energy_change,
            4,
        ),
        integrated_net_heat_j_m2=round(
            integrated_net_heat,
            4,
        ),
        energy_residual_j_m2=round(
            energy_residual,
            4,
        ),
        normalized_residual_percent=round(
            normalized_residual_percent,
            6,
        ),
        maximum_core_step_c=round(
            maximum_core_step,
            6,
        ),
        maximum_skin_step_c=round(
            maximum_skin_step,
            6,
        ),
        solver_function_evaluations=int(
            solver_function_evaluations
        ),
    )

def simulate_material(
    duration_minutes: int,
    output_interval_minutes: int,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
) -> ScenarioResult:
    duration_seconds = duration_minutes * 60.0

    output_times = np.arange(
        0.0,
        duration_seconds + 0.1,
        output_interval_minutes * 60.0,
    )

    if output_times[-1] < duration_seconds:
        output_times = np.append(
            output_times,
            duration_seconds,
        )

    initial_state = [
        person.initial_core_temperature_c,
        person.initial_skin_temperature_c,
    ]

    def derivatives(
        _time_seconds: float,
        state: np.ndarray,
    ) -> list[float]:
        core_temperature_c = float(state[0])
        skin_temperature_c = float(state[1])

        fluxes = calculate_fluxes(
            core_temperature_c=core_temperature_c,
            skin_temperature_c=skin_temperature_c,
            environment=environment,
            person=person,
            material=material,
        )

        core_storage = (
            fluxes.metabolism
            - fluxes.respiration
            - fluxes.core_to_skin
        )

        skin_storage = (
            fluxes.core_to_skin
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        core_rate = (
            core_storage / CORE_HEAT_CAPACITY
        )
        skin_rate = (
            skin_storage / SKIN_HEAT_CAPACITY
        )

        return [core_rate, skin_rate]

    solution = solve_ivp(
        fun=derivatives,
        t_span=(0.0, duration_seconds),
        y0=initial_state,
        t_eval=output_times,
        method="RK45",
        rtol=1e-6,
        atol=1e-8,
        max_step=60.0,
    )

    if not solution.success:
        raise RuntimeError(
            f"數值求解失敗：{solution.message}"
        )

    core_temperature_array = np.asarray(
    solution.y[0],
    dtype=float,
    )

    skin_temperature_array = np.asarray(
    solution.y[1],
    dtype=float,
    )

    diagnostics = calculate_energy_diagnostics(
    times_seconds=np.asarray(
        solution.t,
        dtype=float,
    ),
    core_temperatures=core_temperature_array,
    skin_temperatures=skin_temperature_array,
    environment=environment,
    person=person,
    material=material,
    solver_function_evaluations=solution.nfev,
    )
    
    time_series: list[TimeSeriesPoint] = []

    for index, time_seconds in enumerate(solution.t):
        core_temperature_c = float(solution.y[0, index])
        skin_temperature_c = float(solution.y[1, index])

        fluxes = calculate_fluxes(
            core_temperature_c=core_temperature_c,
            skin_temperature_c=skin_temperature_c,
            environment=environment,
            person=person,
            material=material,
        )

        time_series.append(
            TimeSeriesPoint(
                minute=round(time_seconds / 60.0, 4),
                core_temperature_c=round(
                    core_temperature_c,
                    4,
                ),
                skin_temperature_c=round(
                    skin_temperature_c,
                    4,
                ),
                convection_w_m2=round(
                    fluxes.convection,
                    4,
                ),
                longwave_radiation_w_m2=round(
                    fluxes.longwave_radiation,
                    4,
                ),
                evaporation_w_m2=round(
                    fluxes.evaporation,
                    4,
                ),
                absorbed_solar_w_m2=round(
                    fluxes.absorbed_solar,
                    4,
                ),
                core_to_skin_w_m2=round(
                    fluxes.core_to_skin,
                    4,
                ),
            )
        )

    core_temperatures = [
        point.core_temperature_c
        for point in time_series
    ]
    skin_temperatures = [
        point.skin_temperature_c
        for point in time_series
    ]

    return ScenarioResult(
        material_name=material.name,
        time_series=time_series,
        final_core_temperature_c=core_temperatures[-1],
        final_skin_temperature_c=skin_temperatures[-1],
        peak_core_temperature_c=max(core_temperatures),
        peak_skin_temperature_c=max(skin_temperatures),
        diagnostics=diagnostics,
    )
    
def simulate_material_with_weather(
    duration_minutes: int,
    output_interval_minutes: int,
    weather: WeatherTimeSeries,
    person: PersonInput,
    material: MaterialInput,
) -> ScenarioResult:
    interpolator = (
        WeatherInterpolator.from_series(weather)
    )

    duration_seconds = duration_minutes * 60.0

    output_times = np.arange(
        0.0,
        duration_seconds + 0.1,
        output_interval_minutes * 60.0,
    )

    if output_times[-1] < duration_seconds:
        output_times = np.append(
            output_times,
            duration_seconds,
        )

    initial_state = [
        person.initial_core_temperature_c,
        person.initial_skin_temperature_c,
    ]

    def derivatives(
        time_seconds: float,
        state: np.ndarray,
    ) -> list[float]:
        environment = interpolator.environment_at(
            time_seconds
        )

        core_temperature_c = float(state[0])
        skin_temperature_c = float(state[1])

        fluxes = calculate_fluxes(
            core_temperature_c=core_temperature_c,
            skin_temperature_c=skin_temperature_c,
            environment=environment,
            person=person,
            material=material,
        )

        core_storage = (
            fluxes.metabolism
            - fluxes.respiration
            - fluxes.core_to_skin
        )

        skin_storage = (
            fluxes.core_to_skin
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        return [
            core_storage / CORE_HEAT_CAPACITY,
            skin_storage / SKIN_HEAT_CAPACITY,
        ]

    solution = solve_ivp(
        fun=derivatives,
        t_span=(0.0, duration_seconds),
        y0=initial_state,
        t_eval=output_times,
        method="RK45",
        rtol=1e-6,
        atol=1e-8,
        max_step=60.0,
    )

    if not solution.success:
        raise RuntimeError(
            f"動態氣象數值求解失敗："
            f"{solution.message}"
        )

    time_series: list[TimeSeriesPoint] = []
    net_heat_fluxes: list[float] = []

    for index, time_seconds in enumerate(
        solution.t
    ):
        core_temperature = float(
            solution.y[0, index]
        )
        skin_temperature = float(
            solution.y[1, index]
        )

        environment = interpolator.environment_at(
            float(time_seconds)
        )

        fluxes = calculate_fluxes(
            core_temperature_c=core_temperature,
            skin_temperature_c=skin_temperature,
            environment=environment,
            person=person,
            material=material,
        )

        net_heat_fluxes.append(
            fluxes.metabolism
            - fluxes.respiration
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        time_series.append(
            TimeSeriesPoint(
                minute=round(
                    float(time_seconds) / 60.0,
                    4,
                ),
                core_temperature_c=round(
                    core_temperature,
                    4,
                ),
                skin_temperature_c=round(
                    skin_temperature,
                    4,
                ),
                convection_w_m2=round(
                    fluxes.convection,
                    4,
                ),
                longwave_radiation_w_m2=round(
                    fluxes.longwave_radiation,
                    4,
                ),
                evaporation_w_m2=round(
                    fluxes.evaporation,
                    4,
                ),
                absorbed_solar_w_m2=round(
                    fluxes.absorbed_solar,
                    4,
                ),
                core_to_skin_w_m2=round(
                    fluxes.core_to_skin,
                    4,
                ),
            )
        )

    core_array = np.asarray(
        solution.y[0],
        dtype=float,
    )
    skin_array = np.asarray(
        solution.y[1],
        dtype=float,
    )
    time_array = np.asarray(
        solution.t,
        dtype=float,
    )

    integrated_net_heat = float(
        np.trapezoid(
            np.asarray(net_heat_fluxes),
            time_array,
        )
    )

    stored_energy_change = float(
        CORE_HEAT_CAPACITY
        * (core_array[-1] - core_array[0])
        + SKIN_HEAT_CAPACITY
        * (skin_array[-1] - skin_array[0])
    )

    residual = (
        stored_energy_change
        - integrated_net_heat
    )

    denominator = max(
        abs(stored_energy_change),
        abs(integrated_net_heat),
        1.0,
    )

    diagnostics = EnergyDiagnostics(
        stored_energy_change_j_m2=round(
            stored_energy_change,
            4,
        ),
        integrated_net_heat_j_m2=round(
            integrated_net_heat,
            4,
        ),
        energy_residual_j_m2=round(
            residual,
            4,
        ),
        normalized_residual_percent=round(
            abs(residual)
            / denominator
            * 100.0,
            6,
        ),
        maximum_core_step_c=round(
            float(
                np.max(
                    np.abs(np.diff(core_array))
                )
            ),
            6,
        ),
        maximum_skin_step_c=round(
            float(
                np.max(
                    np.abs(np.diff(skin_array))
                )
            ),
            6,
        ),
        solver_function_evaluations=int(
            solution.nfev
        ),
    )

    core_temperatures = [
        point.core_temperature_c
        for point in time_series
    ]
    skin_temperatures = [
        point.skin_temperature_c
        for point in time_series
    ]

    return ScenarioResult(
        material_name=material.name,
        time_series=time_series,
        final_core_temperature_c=(
            core_temperatures[-1]
        ),
        final_skin_temperature_c=(
            skin_temperatures[-1]
        ),
        peak_core_temperature_c=max(
            core_temperatures
        ),
        peak_skin_temperature_c=max(
            skin_temperatures
        ),
        diagnostics=diagnostics,
    )