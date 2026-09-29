from collections.abc import Callable

from app.core.cities import get_city
from app.schemas.simulation import (
    SimulationSummary,
    WeatherSimulationRequest,
    WeatherSimulationResponse,
)
from app.schemas.weather import (
    WeatherTimeSeries,
)
from app.services.two_node import (
    simulate_material_with_weather,
)
from app.services.weather import (
    get_historical_weather,
)

from app.services.model_parameters import build_model_metadata

MODEL_NAME = "Weather-driven transient two-node prototype"
MODEL_VERSION = "0.5.0"  # Stage 2: explicit Re,cl, IR transmittance, assumptions
ProgressCallback = Callable[
    [int, str],
    None,
]

RESULT_WARNING = (
    "This result comes from a weather-driven simplified human thermal "
    "balance prototype. Verification through thermal manikin or human "
    "experiments is still required."
)

def execute_weather_simulation_with_weather(
    *,
    request: WeatherSimulationRequest,
    weather: WeatherTimeSeries,
    city_name: str | None = None,
    progress_callback: ProgressCallback | None = None,
) -> WeatherSimulationResponse:
    def report(progress: int, stage: str) -> None:
        if progress_callback is not None:
            progress_callback(progress, stage)

    if city_name is None:
        city_name = get_city(request.city_id).name

    assumptions = request.environment_assumptions

    report(30, "running_control_simulation")
    control_result = simulate_material_with_weather(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=request.output_interval_minutes,
        weather=weather,
        person=request.person,
        material=request.control_material,
        assumptions=assumptions,
    )

    report(65, "running_radiative_cooling_simulation")
    rc_result = simulate_material_with_weather(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=request.output_interval_minutes,
        weather=weather,
        person=request.person,
        material=request.rc_material,
        assumptions=assumptions,
    )

    report(90, "generating_summary")

    control_average = sum(
        p.skin_temperature_c for p in control_result.time_series
    ) / len(control_result.time_series)
    rc_average = sum(
        p.skin_temperature_c for p in rc_result.time_series
    ) / len(rc_result.time_series)

    return WeatherSimulationResponse(
        model_name=MODEL_NAME,
        model_version=MODEL_VERSION,
        city=city_name,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                control_result.final_skin_temperature_c
                - rc_result.final_skin_temperature_c, 4
            ),
            final_core_temperature_improvement_c=round(
                control_result.final_core_temperature_c
                - rc_result.final_core_temperature_c, 4
            ),
            average_skin_temperature_improvement_c=round(
                control_average - rc_average, 4
            ),
        ),
        warning=RESULT_WARNING,
        weather=weather,
        environment_model_note=" ".join(assumptions.describe()),
        environment_assumptions=assumptions,
        model_metadata=build_model_metadata(),
    )


async def execute_weather_simulation(
    request: WeatherSimulationRequest,
    progress_callback: ProgressCallback | None = None,
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

    return execute_weather_simulation_with_weather(
        request=request,
        weather=weather,
        city_name=city.name,
        progress_callback=progress_callback,
    )