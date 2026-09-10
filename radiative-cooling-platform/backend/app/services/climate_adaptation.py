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
)
from app.services.climate_analytics import (
    build_city_analytics,
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

CheckpointCallback = Callable[
    [
        list[MonthlyAdaptationResult],
        int,
        int,
    ],
    None,
]

def build_weighted_sample_days(
    *,
    days_in_month: int,
    sample_count: int,
    legacy_representative_day: int | None = None,
) -> list[tuple[int, int]]:
    """
    Build representative sample days for one month.

    Each returned tuple contains:

        (representative_day, represented_day_count)

    The represented-day weights always add up to
    ``days_in_month``. If the requested sample count is larger
    than the number of days, one sample is generated per day.

    ``legacy_representative_day`` preserves the original
    single-sample behavior.
    """
    if days_in_month <= 0:
        raise ValueError(
            "days_in_month must be greater than zero"
        )

    if sample_count <= 0:
        raise ValueError(
            "sample_count must be greater than zero"
        )

    effective_sample_count = min(
        sample_count,
        days_in_month,
    )

    if effective_sample_count == 1:
        if legacy_representative_day is None:
            representative_day = (
                days_in_month + 1
            ) // 2
        else:
            # Keep the configured legacy day inside the month.
            representative_day = min(
                max(legacy_representative_day, 1),
                days_in_month,
            )

        return [
            (
                representative_day,
                days_in_month,
            ),
        ]

    base_weight, remainder = divmod(
        days_in_month,
        effective_sample_count,
    )

    samples: list[tuple[int, int]] = []
    interval_start_day = 1

    for index in range(effective_sample_count):
        weight_days = (
            base_weight
            + (1 if index < remainder else 0)
        )

        interval_end_day = (
            interval_start_day
            + weight_days
            - 1
        )

        representative_day = (
            interval_start_day
            + interval_end_day
        ) // 2

        samples.append(
            (
                representative_day,
                weight_days,
            )
        )

        interval_start_day = interval_end_day + 1

    return samples

def mean(values: list[float]) -> float:
    if not values:
        raise RuntimeError(
            "Cannot calculate the mean of an empty list"
        )

    return sum(values) / len(values)


def round_optional(
    value: float | None,
    digits: int = 4,
) -> float | None:
    if value is None:
        return None

    return round(value, digits)


def is_exposure_eligible(
    *,
    mean_air_temperature_c: float,
    mean_solar_radiation_w_m2: float,
    request: GlobalBatchCreate,
) -> bool:
    conditions: list[bool] = []

    if request.minimum_air_temperature_c is not None:
        conditions.append(
            mean_air_temperature_c
            >= request.minimum_air_temperature_c
        )

    if request.minimum_solar_radiation_w_m2 is not None:
        conditions.append(
            mean_solar_radiation_w_m2
            >= request.minimum_solar_radiation_w_m2
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

    exposure_coverage_percent = (
        evaluated_weighted_days
        / total_weighted_days
        * 100.0
        if total_weighted_days
        else 0.0
    )

    climate_adaptation_rate_percent = (
        beneficial_weighted_days
        / evaluated_weighted_days
        * 100.0
        if evaluated_weighted_days
        else None
    )

    average_skin_improvement_c = (
        sum(
            sample.average_skin_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    average_core_improvement_c = (
        sum(
            sample.average_core_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement_c = (
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
        eligible_sample_count=len(eligible_samples),
        total_weighted_days=total_weighted_days,
        evaluated_weighted_days=evaluated_weighted_days,
        beneficial_weighted_days=beneficial_weighted_days,
        exposure_coverage_percent=round(
            exposure_coverage_percent,
            4,
        ),
        climate_adaptation_rate_percent=round_optional(
            climate_adaptation_rate_percent
        ),
        average_skin_improvement_c=round_optional(
            average_skin_improvement_c
        ),
        average_core_improvement_c=round_optional(
            average_core_improvement_c
        ),
        maximum_skin_improvement_c=round_optional(
            maximum_skin_improvement_c
        ),
        samples=samples,
    )


def normalize_initial_monthly_results(
    *,
    request: GlobalBatchCreate,
    results: list[MonthlyAdaptationResult] | None,
) -> list[MonthlyAdaptationResult]:
    if not results:
        return []

    results_by_month: dict[int, MonthlyAdaptationResult] = {}

    for result in results:
        if (
            request.start_month
            <= result.month
            <= request.end_month
        ):
            results_by_month[result.month] = result

    return [
        results_by_month[month]
        for month in sorted(results_by_month)
    ]


async def analyze_city_climate_adaptation(
    *,
    city_id: str,
    request: GlobalBatchCreate,
    progress_callback: ProgressCallback | None = None,
    checkpoint_callback: CheckpointCallback | None = None,
    initial_monthly_results: (
        list[MonthlyAdaptationResult] | None
    ) = None,
) -> dict:
    city = get_city(city_id)

    annual_plan = build_annual_sampling_plan(request)

    if not annual_plan:
        raise RuntimeError(
            "No sampling dates were generated"
        )

    total_sample_count = len(annual_plan)

    monthly_results = normalize_initial_monthly_results(
        request=request,
        results=initial_monthly_results,
    )

    completed_months = {
        result.month
        for result in monthly_results
    }

    completed_sample_count = sum(
        result.sampled_day_count
        for result in monthly_results
    )

    def report(
        progress: int,
        stage: str,
    ) -> None:
        if progress_callback is not None:
            progress_callback(
                max(0, min(progress, 100)),
                stage,
            )

    for month in range(
        request.start_month,
        request.end_month + 1,
    ):
        if month in completed_months:
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
                    f"restored_checkpoint_"
                    f"{request.year}-{month:02d}"
                ),
            )
            continue

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

        next_month_start = get_next_month_start(
            year=request.year,
            month=month,
        )

        # The final simulation day may continue into the next month.
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

        month_weather = await get_historical_weather_range(
            city=city,
            start_time_local=month_start,
            end_time_local=prefetch_end,
            padding_hours=1,
        )

        month_samples: list[DailyAdaptationResult] = []

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
                f"analyzing_{start_time_local:%Y-%m-%d}",
            )

            sample_weather = slice_weather_time_series(
                weather=month_weather,
                start_time_local=start_time_local,
                duration_minutes=request.duration_minutes,
                padding_hours=1,
            )

            simulation_request = WeatherSimulationRequest(
                city_id=city.id,
                start_time_local=start_time_local,
                duration_minutes=request.duration_minutes,
                output_interval_minutes=(
                    request.output_interval_minutes
                ),
                person=request.person,
                control_material=request.control_material,
                rc_material=request.rc_material,
            )

            simulation = execute_weather_simulation_with_weather(
                request=simulation_request,
                weather=sample_weather,
            )

            paired_points = list(
                zip(
                    simulation.control.time_series,
                    simulation.radiative_cooling.time_series,
                    strict=True,
                )
            )

            if not paired_points:
                raise RuntimeError(
                    "Simulation returned no paired points"
                )

            skin_improvements = [
                (
                    control.skin_temperature_c
                    - radiative.skin_temperature_c
                )
                for control, radiative in paired_points
            ]

            core_improvements = [
                (
                    control.core_temperature_c
                    - radiative.core_temperature_c
                )
                for control, radiative in paired_points
            ]

            weather_points = simulation.weather.points

            if not weather_points:
                raise RuntimeError(
                    "Simulation returned no weather points"
                )

            mean_air_temperature_c = mean(
                [
                    point.air_temperature_c
                    for point in weather_points
                ]
            )

            maximum_air_temperature_c = max(
                point.air_temperature_c
                for point in weather_points
            )

            mean_solar_radiation_w_m2 = mean(
                [
                    point.ghi_w_m2
                    for point in weather_points
                ]
            )

            maximum_solar_radiation_w_m2 = max(
                point.ghi_w_m2
                for point in weather_points
            )

            average_skin_improvement_c = mean(
                skin_improvements
            )

            average_core_improvement_c = mean(
                core_improvements
            )

            maximum_skin_improvement_c = max(
                skin_improvements
            )

            exposure_eligible = is_exposure_eligible(
                mean_air_temperature_c=(
                    mean_air_temperature_c
                ),
                mean_solar_radiation_w_m2=(
                    mean_solar_radiation_w_m2
                ),
                request=request,
            )

            beneficial = (
                exposure_eligible
                and average_skin_improvement_c
                >= request.minimum_skin_improvement_c
            )

            month_samples.append(
                DailyAdaptationResult(
                    sample_date_local=start_time_local,
                    weight_days=sample_day.weight_days,
                    mean_air_temperature_c=round(
                        mean_air_temperature_c,
                        4,
                    ),
                    maximum_air_temperature_c=round(
                        maximum_air_temperature_c,
                        4,
                    ),
                    mean_solar_radiation_w_m2=round(
                        mean_solar_radiation_w_m2,
                        4,
                    ),
                    maximum_solar_radiation_w_m2=round(
                        maximum_solar_radiation_w_m2,
                        4,
                    ),
                    exposure_eligible=exposure_eligible,
                    beneficial=beneficial,
                    average_skin_improvement_c=round(
                        average_skin_improvement_c,
                        4,
                    ),
                    final_skin_improvement_c=round(
                        simulation.summary
                        .final_skin_temperature_improvement_c,
                        4,
                    ),
                    average_core_improvement_c=round(
                        average_core_improvement_c,
                        4,
                    ),
                    maximum_skin_improvement_c=round(
                        maximum_skin_improvement_c,
                        4,
                    ),
                    weather_from_cache=(
                        month_weather.source.from_cache
                    ),
                )
            )

            completed_sample_count += 1

        monthly_result = summarize_month(
            month=month,
            samples=month_samples,
        )

        monthly_results.append(monthly_result)
        monthly_results.sort(
            key=lambda result: result.month
        )

        completed_months.add(month)

        if checkpoint_callback is not None:
            checkpoint_callback(
                list(monthly_results),
                month,
                completed_sample_count,
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

    exposure_coverage_percent = (
        evaluated_weighted_days
        / total_weighted_days
        * 100.0
        if total_weighted_days
        else 0.0
    )

    climate_adaptation_rate_percent = (
        beneficial_weighted_days
        / evaluated_weighted_days
        * 100.0
        if evaluated_weighted_days
        else None
    )

    annual_average_skin_improvement_c = (
        sum(
            sample.average_skin_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    annual_average_core_improvement_c = (
        sum(
            sample.average_core_improvement_c
            * sample.weight_days
            for sample in eligible_samples
        )
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement_c = (
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
        / 60.0
    )

    analytics = build_city_analytics(
        samples=all_samples,
        request=request,
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
        "climate_adaptation_rate_percent": round_optional(
            climate_adaptation_rate_percent
        ),
        "exposure_coverage_percent": round(
            exposure_coverage_percent,
            4,
        ),
        "annual_average_skin_improvement_c": round_optional(
            annual_average_skin_improvement_c
        ),
        "annual_average_core_improvement_c": round_optional(
            annual_average_core_improvement_c
        ),
        "maximum_skin_improvement_c": round_optional(
            maximum_skin_improvement_c
        ),
        "effective_cooling_hours": round(
            effective_cooling_hours,
            2,
        ),
        "sampled_day_count": len(all_samples),
        "eligible_sample_count": len(eligible_samples),
        "evaluated_weighted_days": evaluated_weighted_days,
        "beneficial_weighted_days": beneficial_weighted_days,
        "completed_month_count": len(monthly_results),
        "skin_improvement_p50_c": analytics[
            "skin_improvement_p50_c"
        ],
        "skin_improvement_p90_c": analytics[
            "skin_improvement_p90_c"
        ],
        "skin_improvement_p95_c": analytics[
            "skin_improvement_p95_c"
        ],
        "core_improvement_p50_c": analytics[
            "core_improvement_p50_c"
        ],
        "core_improvement_p90_c": analytics[
            "core_improvement_p90_c"
        ],
        "core_improvement_p95_c": analytics[
            "core_improvement_p95_c"
        ],
        "heatwave_analysis_available": analytics[
            "heatwave_analysis_available"
        ],
        "heatwave_event_count": analytics[
            "heatwave_event_count"
        ],
        "longest_heatwave_days": analytics[
            "longest_heatwave_days"
        ],
        "heatwave_events": analytics[
            "heatwave_events"
        ],
        "monthly_results": [
            result.model_dump(mode="json")
            for result in monthly_results
        ],
    }