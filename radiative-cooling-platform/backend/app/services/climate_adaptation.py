import calendar

from collections.abc import Callable
from datetime import datetime

from app.core.cities import get_city
from app.schemas.global_batch import (
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services.weather_simulation import (
    execute_weather_simulation,
)


ProgressCallback = Callable[
    [int, str],
    None,
]


async def analyze_city_climate_adaptation(
    *,
    city_id: str,
    request: GlobalBatchCreate,
    progress_callback: ProgressCallback | None = None,
) -> dict:
    city = get_city(city_id)

    months = list(
        range(
            request.start_month,
            request.end_month + 1,
        )
    )

    monthly_results: list[
        MonthlyAdaptationResult
    ] = []

    weighted_skin_total = 0.0
    weighted_core_total = 0.0
    evaluated_weighted_days = 0
    beneficial_weighted_days = 0
    maximum_skin_improvement = float("-inf")

    def report(
        progress: int,
        stage: str,
    ) -> None:
        if progress_callback is not None:
            progress_callback(
                progress,
                stage,
            )

    for index, month in enumerate(months):
        report(
            max(
                1,
                round(
                    index
                    / max(len(months), 1)
                    * 90
                ),
            ),
            f"analyzing_month_{month:02d}",
        )

        days_in_month = calendar.monthrange(
            request.year,
            month,
        )[1]

        representative_day = min(
            request.representative_day,
            days_in_month,
        )

        start_time_local = datetime(
            request.year,
            month,
            representative_day,
            request.local_start_hour,
            0,
            0,
        )

        simulation_request = (
            WeatherSimulationRequest(
                city_id=city.id,
                start_time_local=start_time_local,
                duration_minutes=(
                    request.duration_minutes
                ),
                output_interval_minutes=(
                    request.output_interval_minutes
                ),
                person=request.person,
                control_material=(
                    request.control_material
                ),
                rc_material=request.rc_material,
            )
        )

        simulation = await execute_weather_simulation(
            request=simulation_request,
        )

        paired_points = list(
            zip(
                simulation.control.time_series,
                simulation.radiative_cooling.time_series,
                strict=True,
            )
        )

        skin_improvements = [
            control.skin_temperature_c
            - radiative.skin_temperature_c
            for control, radiative in paired_points
        ]

        core_improvements = [
            control.core_temperature_c
            - radiative.core_temperature_c
            for control, radiative in paired_points
        ]

        average_skin_improvement = (
            sum(skin_improvements)
            / len(skin_improvements)
        )

        average_core_improvement = (
            sum(core_improvements)
            / len(core_improvements)
        )

        month_maximum_skin_improvement = max(
            skin_improvements
        )

        beneficial = (
            average_skin_improvement
            >= request.minimum_skin_improvement_c
        )

        monthly_result = MonthlyAdaptationResult(
            month=month,
            representative_date_local=(
                start_time_local
            ),
            weight_days=days_in_month,
            average_skin_improvement_c=round(
                average_skin_improvement,
                4,
            ),
            final_skin_improvement_c=round(
                simulation.summary
                .final_skin_temperature_improvement_c,
                4,
            ),
            average_core_improvement_c=round(
                average_core_improvement,
                4,
            ),
            maximum_skin_improvement_c=round(
                month_maximum_skin_improvement,
                4,
            ),
            beneficial=beneficial,
        )

        monthly_results.append(monthly_result)

        evaluated_weighted_days += days_in_month

        weighted_skin_total += (
            average_skin_improvement
            * days_in_month
        )

        weighted_core_total += (
            average_core_improvement
            * days_in_month
        )

        if beneficial:
            beneficial_weighted_days += days_in_month

        maximum_skin_improvement = max(
            maximum_skin_improvement,
            month_maximum_skin_improvement,
        )

    if evaluated_weighted_days == 0:
        raise RuntimeError(
            "No valid monthly analysis result"
        )

    adaptation_rate = (
        beneficial_weighted_days
        / evaluated_weighted_days
        * 100
    )

    duration_hours = (
        request.duration_minutes / 60
    )

    effective_cooling_hours = (
        beneficial_weighted_days
        * duration_hours
    )

    report(
        95,
        "generating_city_summary",
    )

    return {
        "city_id": city.id,
        "city_name": city.name,
        "country": city.country,
        "latitude": city.latitude,
        "longitude": city.longitude,
        "climate_adaptation_rate_percent": round(
            adaptation_rate,
            4,
        ),
        "annual_average_skin_improvement_c": round(
            weighted_skin_total
            / evaluated_weighted_days,
            4,
        ),
        "annual_average_core_improvement_c": round(
            weighted_core_total
            / evaluated_weighted_days,
            4,
        ),
        "maximum_skin_improvement_c": round(
            maximum_skin_improvement,
            4,
        ),
        "effective_cooling_hours": round(
            effective_cooling_hours,
            2,
        ),
        "evaluated_weighted_days": (
            evaluated_weighted_days
        ),
        "beneficial_weighted_days": (
            beneficial_weighted_days
        ),
        "monthly_results": [
            item.model_dump(mode="json")
            for item in monthly_results
        ],
    }