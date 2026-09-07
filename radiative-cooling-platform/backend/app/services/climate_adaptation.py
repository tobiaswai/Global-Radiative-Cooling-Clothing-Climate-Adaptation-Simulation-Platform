import calendar

from collections.abc import Callable
from datetime import (
    datetime,
    timedelta,
)

from app.core.cities import get_city
from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services.annual_sampling import (
    build_annual_sampling_plan,
    build_month_sampling_plan,
    build_weighted_sample_days,
)
from app.services.weather import (
    get_historical_weather_range,
    slice_weather_time_series,
)
from app.services.weather_simulation import (
    execute_weather_simulation_with_weather,
)


ProgressCallback = Callable[
    [int, str],
    None,
]


def mean(
    values: list[float],
) -> float:
    if not values:
        raise RuntimeError(
            "Cannot calculate the mean "
            "of an empty list"
        )

    return sum(values) / len(values)


def is_exposure_eligible(
    *,
    mean_air_temperature_c: float,
    mean_solar_radiation_w_m2: float,
    request: GlobalBatchCreate,
) -> bool:
    conditions: list[bool] = []

    if (
        request.minimum_air_temperature_c
        is not None
    ):
        conditions.append(
            mean_air_temperature_c
            >= request.minimum_air_temperature_c
        )

    if (
        request.minimum_solar_radiation_w_m2
        is not None
    ):
        conditions.append(
            mean_solar_radiation_w_m2
            >= request
            .minimum_solar_radiation_w_m2
        )

    if not conditions:
        return True

    if request.exposure_match_mode == "any":
        return any(conditions)

    return all(conditions)


def get_next_month_start(
    *,
    year: int,
    month: int,
) -> datetime:
    if month == 12:
        return datetime(
            year + 1,
            1,
            1,
        )

    return datetime(
        year,
        month + 1,
        1,
    )


def summarize_month(
    *,
    month: int,
    samples: list[DailyAdaptationResult],
) -> MonthlyAdaptationResult:
    total_weighted_days = sum(
        sample.weight_days
        for sample in samples
    )

    eligible_samples = [
        sample
        for sample in samples
        if sample.exposure_eligible
    ]

    evaluated_weighted_days = sum(
        sample.weight_days
        for sample in eligible_samples
    )

    beneficial_weighted_days = sum(
        sample.weight_days
        for sample in samples
        if sample.beneficial
    )

    exposure_coverage = (
        evaluated_weighted_days
        / total_weighted_days
        * 100
        if total_weighted_days
        else 0.0
    )

    adaptation_rate = (
        beneficial_weighted_days
        / evaluated_weighted_days
        * 100
        if evaluated_weighted_days
        else None
    )

    average_skin_improvement = (
        sum(
            sample.average_skin_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    average_core_improvement = (
        sum(
            sample.average_core_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement = (
        max(
            sample.maximum_skin_improvement_c
            for sample in eligible_samples
        )
        if eligible_samples
        else None
    )

    return MonthlyAdaptationResult(
        month=month,
        sampled_day_count=len(samples),
        eligible_sample_count=len(
            eligible_samples
        ),
        total_weighted_days=(
            total_weighted_days
        ),
        evaluated_weighted_days=(
            evaluated_weighted_days
        ),
        beneficial_weighted_days=(
            beneficial_weighted_days
        ),
        exposure_coverage_percent=round(
            exposure_coverage,
            4,
        ),
        climate_adaptation_rate_percent=(
            round(
                adaptation_rate,
                4,
            )
            if adaptation_rate is not None
            else None
        ),
        average_skin_improvement_c=(
            round(
                average_skin_improvement,
                4,
            )
            if average_skin_improvement
            is not None
            else None
        ),
        average_core_improvement_c=(
            round(
                average_core_improvement,
                4,
            )
            if average_core_improvement
            is not None
            else None
        ),
        maximum_skin_improvement_c=(
            round(
                maximum_skin_improvement,
                4,
            )
            if maximum_skin_improvement
            is not None
            else None
        ),
        samples=samples,
    )


async def analyze_city_climate_adaptation(
    *,
    city_id: str,
    request: GlobalBatchCreate,
    progress_callback: ProgressCallback | None = None,
) -> dict:
    city = get_city(city_id)

    annual_plan = build_annual_sampling_plan(
        request
    )

    if not annual_plan:
        raise RuntimeError(
            "No sampling dates were generated"
        )

    total_sample_count = len(
        annual_plan
    )

    completed_sample_count = 0

    monthly_results: list[
        MonthlyAdaptationResult
    ] = []

    def report(
        progress: int,
        stage: str,
    ) -> None:
        if progress_callback is not None:
            progress_callback(
                progress,
                stage,
            )

    for month in range(
        request.start_month,
        request.end_month + 1,
    ):
        month_plan = build_month_sampling_plan(
            request=request,
            month=month,
        )

        month_start = datetime(
            request.year,
            month,
            1,
            0,
            0,
            0,
        )

        next_month_start = (
            get_next_month_start(
                year=request.year,
                month=month,
            )
        )

        # 最後一天的分析可能延伸到下個月，
        # 因此預取範圍加入開始小時及模擬長度。
        prefetch_end = (
            next_month_start
            + timedelta(
                hours=request.local_start_hour,
                minutes=request.duration_minutes,
            )
        )

        report(
            max(
                1,
                round(
                    completed_sample_count
                    / total_sample_count
                    * 92
                ),
            ),
            (
                f"prefetching_weather_"
                f"{request.year}-{month:02d}"
            ),
        )

        month_weather = (
            await get_historical_weather_range(
                city=city,
                start_time_local=month_start,
                end_time_local=prefetch_end,
                padding_hours=1,
            )
        )

        month_samples: list[
            DailyAdaptationResult
        ] = []

        for sample_day in month_plan:
            start_time_local = datetime(
                sample_day.date_local.year,
                sample_day.date_local.month,
                sample_day.date_local.day,
                request.local_start_hour,
                0,
                0,
            )

            progress = max(
                1,
                round(
                    completed_sample_count
                    / total_sample_count
                    * 92
                ),
            )

            report(
                progress,
                (
                    f"analyzing_"
                    f"{start_time_local:%Y-%m-%d}"
                ),
            )

            sample_weather = (
                slice_weather_time_series(
                    weather=month_weather,
                    start_time_local=(
                        start_time_local
                    ),
                    duration_minutes=(
                        request.duration_minutes
                    ),
                    padding_hours=1,
                )
            )

            simulation_request = (
                WeatherSimulationRequest(
                    city_id=city.id,
                    start_time_local=(
                        start_time_local
                    ),
                    duration_minutes=(
                        request.duration_minutes
                    ),
                    output_interval_minutes=(
                        request
                        .output_interval_minutes
                    ),
                    person=request.person,
                    control_material=(
                        request.control_material
                    ),
                    rc_material=(
                        request.rc_material
                    ),
                )
            )

            simulation = (
                execute_weather_simulation_with_weather(
                    request=simulation_request,
                    weather=sample_weather,
                )
            )

            paired_points = list(
                zip(
                    simulation.control.time_series,
                    simulation
                    .radiative_cooling
                    .time_series,
                    strict=True,
                )
            )

            if not paired_points:
                raise RuntimeError(
                    "Simulation returned no "
                    "paired points"
                )

            skin_improvements = [
                (
                    control.skin_temperature_c
                    - radiative
                    .skin_temperature_c
                )
                for control, radiative
                in paired_points
            ]

            core_improvements = [
                (
                    control.core_temperature_c
                    - radiative
                    .core_temperature_c
                )
                for control, radiative
                in paired_points
            ]

            weather_points = (
                simulation.weather.points
            )

            mean_air_temperature = mean(
                [
                    point.air_temperature_c
                    for point in weather_points
                ]
            )

            maximum_air_temperature = max(
                point.air_temperature_c
                for point in weather_points
            )

            mean_solar_radiation = mean(
                [
                    point.ghi_w_m2
                    for point in weather_points
                ]
            )

            maximum_solar_radiation = max(
                point.ghi_w_m2
                for point in weather_points
            )

            average_skin_improvement = mean(
                skin_improvements
            )

            average_core_improvement = mean(
                core_improvements
            )

            maximum_skin_improvement = max(
                skin_improvements
            )

            exposure_eligible = (
                is_exposure_eligible(
                    mean_air_temperature_c=(
                        mean_air_temperature
                    ),
                    mean_solar_radiation_w_m2=(
                        mean_solar_radiation
                    ),
                    request=request,
                )
            )

            beneficial = (
                exposure_eligible
                and average_skin_improvement
                >= request
                .minimum_skin_improvement_c
            )

            month_samples.append(
                DailyAdaptationResult(
                    sample_date_local=(
                        start_time_local
                    ),
                    weight_days=(
                        sample_day.weight_days
                    ),
                    mean_air_temperature_c=round(
                        mean_air_temperature,
                        4,
                    ),
                    maximum_air_temperature_c=round(
                        maximum_air_temperature,
                        4,
                    ),
                    mean_solar_radiation_w_m2=round(
                        mean_solar_radiation,
                        4,
                    ),
                    maximum_solar_radiation_w_m2=round(
                        maximum_solar_radiation,
                        4,
                    ),
                    exposure_eligible=(
                        exposure_eligible
                    ),
                    beneficial=beneficial,
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
                        maximum_skin_improvement,
                        4,
                    ),
                    weather_from_cache=(
                        month_weather
                        .source
                        .from_cache
                    ),
                )
            )

            completed_sample_count += 1

        monthly_results.append(
            summarize_month(
                month=month,
                samples=month_samples,
            )
        )

    all_samples = [
        sample
        for monthly_result in monthly_results
        for sample in monthly_result.samples
    ]

    eligible_samples = [
        sample
        for sample in all_samples
        if sample.exposure_eligible
    ]

    total_weighted_days = sum(
        sample.weight_days
        for sample in all_samples
    )

    evaluated_weighted_days = sum(
        sample.weight_days
        for sample in eligible_samples
    )

    beneficial_weighted_days = sum(
        sample.weight_days
        for sample in all_samples
        if sample.beneficial
    )

    exposure_coverage = (
        evaluated_weighted_days
        / total_weighted_days
        * 100
        if total_weighted_days
        else 0.0
    )

    adaptation_rate = (
        beneficial_weighted_days
        / evaluated_weighted_days
        * 100
        if evaluated_weighted_days
        else None
    )

    average_skin_improvement = (
        sum(
            sample.average_skin_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    average_core_improvement = (
        sum(
            sample.average_core_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement = (
        max(
            sample.maximum_skin_improvement_c
            for sample in eligible_samples
        )
        if eligible_samples
        else None
    )

    effective_cooling_hours = (
        beneficial_weighted_days
        * request.duration_minutes
        / 60
    )

    report(
        96,
        "generating_city_summary",
    )

    return {
        "city_id": city.id,
        "city_name": city.name,
        "country": city.country,
        "latitude": city.latitude,
        "longitude": city.longitude,
        "climate_adaptation_rate_percent": (
            round(
                adaptation_rate,
                4,
            )
            if adaptation_rate is not None
            else None
        ),
        "exposure_coverage_percent": round(
            exposure_coverage,
            4,
        ),
        "annual_average_skin_improvement_c": (
            round(
                average_skin_improvement,
                4,
            )
            if average_skin_improvement
            is not None
            else None
        ),
        "annual_average_core_improvement_c": (
            round(
                average_core_improvement,
                4,
            )
            if average_core_improvement
            is not None
            else None
        ),
        "maximum_skin_improvement_c": (
            round(
                maximum_skin_improvement,
                4,
            )
            if maximum_skin_improvement
            is not None
            else None
        ),
        "effective_cooling_hours": round(
            effective_cooling_hours,
            2,
        ),
        "sampled_day_count": len(
            all_samples
        ),
        "eligible_sample_count": len(
            eligible_samples
        ),
        "evaluated_weighted_days": (
            evaluated_weighted_days
        ),
        "beneficial_weighted_days": (
            beneficial_weighted_days
        ),
        "monthly_results": [
            result.model_dump(
                mode="json"
            )
            for result in monthly_results
        ],
    }