from collections.abc import Callable

from app.core.cities import get_city
from app.schemas.simulation import (
    SimulationSummary,
    WeatherSimulationRequest,
    WeatherSimulationResponse,
)
from app.services.two_node import (
    simulate_material_with_weather,
)
from app.services.weather import (
    get_historical_weather,
)


ProgressCallback = Callable[
    [int, str],
    None,
]


async def execute_weather_simulation(
    request: WeatherSimulationRequest,
    progress_callback: ProgressCallback
    | None = None,
) -> WeatherSimulationResponse:
    def report(
        progress: int,
        stage: str,
    ) -> None:
        if progress_callback is not None:
            progress_callback(
                progress,
                stage,
            )

    city = get_city(request.city_id)

    report(
        10,
        "downloading_weather",
    )

    weather = await get_historical_weather(
        city=city,
        start_time_local=(
            request.start_time_local
        ),
        duration_minutes=(
            request.duration_minutes
        ),
    )

    report(
        30,
        "running_control_simulation",
    )

    control_result = (
        simulate_material_with_weather(
            duration_minutes=(
                request.duration_minutes
            ),
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            weather=weather,
            person=request.person,
            material=request.control_material,
        )
    )

    report(
        65,
        "running_radiative_cooling_simulation",
    )

    rc_result = (
        simulate_material_with_weather(
            duration_minutes=(
                request.duration_minutes
            ),
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            weather=weather,
            person=request.person,
            material=request.rc_material,
        )
    )

    report(
        90,
        "generating_summary",
    )

    control_average = sum(
        point.skin_temperature_c
        for point in control_result.time_series
    ) / len(control_result.time_series)

    rc_average = sum(
        point.skin_temperature_c
        for point in rc_result.time_series
    ) / len(rc_result.time_series)

    return WeatherSimulationResponse(
        model_name=(
            "Weather-driven transient "
            "two-node prototype"
        ),
        model_version="0.4.0",
        city=city.name,
        duration_minutes=(
            request.duration_minutes
        ),
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                control_result
                .final_skin_temperature_c
                - rc_result
                .final_skin_temperature_c,
                4,
            ),
            final_core_temperature_improvement_c=round(
                control_result
                .final_core_temperature_c
                - rc_result
                .final_core_temperature_c,
                4,
            ),
            average_skin_temperature_improvement_c=round(
                control_average - rc_average,
                4,
            ),
        ),
        warning=(
            "This result comes from a weather-driven simplified human model."
            "Thermal equilibrium prototype, not yet completed in JOS-3."
            "Verification through thermal doll or human experiments."
        ),
        weather=weather,
        environment_model_note=(
            "Air temperature, humidity, wind speed, and shortwave radiation"
            "From ERA5; mean radiant temperature and effective radiant temperature"
            "Sky temperature is currently estimated using empirical formulas."
        ),
    )
    
