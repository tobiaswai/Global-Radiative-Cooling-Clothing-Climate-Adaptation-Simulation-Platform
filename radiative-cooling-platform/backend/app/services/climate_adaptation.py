import calendar

from collections.abc import Callable
from datetime import datetime

from app.core.cities import get_city
from app.schemas.global_batch import (
    DailyAdaptationResult,
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


def build_weighted_sample_days(
    *,
    days_in_month: int,
    sample_count: int,
    legacy_representative_day: int | None = None,
) -> list[tuple[int, int]]:
    """
    Return [(representing day, representing number of days), ...].

    Example:
    31 days, 3 samples, approximately generating days 5, 16, and 26;
    Each sample's weight is the number of days in the month closest to it.
    """
    sample_count = max(
        1,
        min(sample_count, days_in_month),
    )

    if (
        sample_count == 1
        and legacy_representative_day is not None
    ):
        sample_days = [
            min(
                legacy_representative_day,
                days_in_month,
            )
        ]
    else:
        sample_days = []

        for index in range(sample_count):
            day = round(
                (index + 0.5)
                * days_in_month
                / sample_count
            )

            day = max(
                1,
                min(days_in_month, day),
            )

            if day not in sample_days:
                sample_days.append(day)

        # 防止 round 導致少於要求數量。
        candidate = 1

        while len(sample_days) < sample_count:
            if candidate not in sample_days:
                sample_days.append(candidate)

            candidate += 1

        sample_days.sort()

    weights = {
        day: 0
        for day in sample_days
    }

    for calendar_day in range(
        1,
        days_in_month + 1,
    ):
        nearest_sample = min(
            sample_days,
            key=lambda sample_day: (
                abs(sample_day - calendar_day),
                sample_day,
            ),
        )

        weights[nearest_sample] += 1

    return [
        (
            sample_day,
            weights[sample_day],
        )
        for sample_day in sample_days
    ]


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

    if (
        request.minimum_solar_radiation_w_m2
        is not None
    ):
        conditions.append(
            mean_solar_radiation_w_m2
            >= request.minimum_solar_radiation_w_m2
        )

    if not conditions:
        return True

    if request.exposure_match_mode == "any":
        return any(conditions)

    return all(conditions)


def mean(values: list[float]) -> float:
    if not values:
        raise RuntimeError(
            "Cannot calculate the mean of an empty list"
        )

    return sum(values) / len(values)


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

    sampling_plan: list[
        tuple[int, int, int]
    ] = []

    for month in months:
        days_in_month = calendar.monthrange(
            request.year,
            month,
        )[1]

        weighted_days = build_weighted_sample_days(
            days_in_month=days_in_month,
            sample_count=request.sample_days_per_month,
            legacy_representative_day=(
                request.representative_day
            ),
        )

        for sample_day, weight_days in weighted_days:
            sampling_plan.append(
                (
                    month,
                    sample_day,
                    weight_days,
                )
            )

    total_sample_count = len(sampling_plan)

    if total_sample_count == 0:
        raise RuntimeError(
            "No sampling dates were generated"
        )

    all_sample_count = 0
    eligible_sample_count = 0

    total_weighted_days = 0
    evaluated_weighted_days = 0
    beneficial_weighted_days = 0

    weighted_skin_total = 0.0
    weighted_core_total = 0.0

    maximum_skin_improvement: float | None = None

    def report(
        progress: int,
        stage: str,
    ) -> None:
        if progress_callback is not None:
            progress_callback(
                progress,
                stage,
            )

    current_plan_index = 0

    for month in months:
        days_in_month = calendar.monthrange(
            request.year,
            month,
        )[1]

        weighted_days = build_weighted_sample_days(
            days_in_month=days_in_month,
            sample_count=request.sample_days_per_month,
            legacy_representative_day=(
                request.representative_day
            ),
        )

        month_samples: list[
            DailyAdaptationResult
        ] = []

        month_total_weighted_days = 0
        month_evaluated_weighted_days = 0
        month_beneficial_weighted_days = 0

        month_weighted_skin_total = 0.0
        month_weighted_core_total = 0.0
        month_maximum_skin: float | None = None

        month_eligible_count = 0

        for sample_day, weight_days in weighted_days:
            progress = max(
                1,
                round(
                    current_plan_index
                    / total_sample_count
                    * 92
                ),
            )

            report(
                progress,
                (
                    f"analyzing_{request.year}-"
                    f"{month:02d}-{sample_day:02d}"
                ),
            )

            start_time_local = datetime(
                request.year,
                month,
                sample_day,
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
                    simulation
                    .radiative_cooling
                    .time_series,
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

            sample_maximum_skin = max(
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
                >= request.minimum_skin_improvement_c
            )

            sample_result = DailyAdaptationResult(
                sample_date_local=start_time_local,
                weight_days=weight_days,
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
                exposure_eligible=exposure_eligible,
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
                    sample_maximum_skin,
                    4,
                ),
                weather_from_cache=(
                    simulation.weather.source.from_cache
                ),
            )

            month_samples.append(sample_result)

            all_sample_count += 1
            total_weighted_days += weight_days
            month_total_weighted_days += weight_days

            if exposure_eligible:
                eligible_sample_count += 1
                month_eligible_count += 1

                evaluated_weighted_days += weight_days
                month_evaluated_weighted_days += (
                    weight_days
                )

                weighted_skin_total += (
                    average_skin_improvement
                    * weight_days
                )

                weighted_core_total += (
                    average_core_improvement
                    * weight_days
                )

                month_weighted_skin_total += (
                    average_skin_improvement
                    * weight_days
                )

                month_weighted_core_total += (
                    average_core_improvement
                    * weight_days
                )

                maximum_skin_improvement = (
                    sample_maximum_skin
                    if maximum_skin_improvement is None
                    else max(
                        maximum_skin_improvement,
                        sample_maximum_skin,
                    )
                )

                month_maximum_skin = (
                    sample_maximum_skin
                    if month_maximum_skin is None
                    else max(
                        month_maximum_skin,
                        sample_maximum_skin,
                    )
                )

            if beneficial:
                beneficial_weighted_days += weight_days
                month_beneficial_weighted_days += (
                    weight_days
                )

            current_plan_index += 1

        month_exposure_coverage = (
            month_evaluated_weighted_days
            / month_total_weighted_days
            * 100
            if month_total_weighted_days
            else 0.0
        )

        month_adaptation_rate = (
            month_beneficial_weighted_days
            / month_evaluated_weighted_days
            * 100
            if month_evaluated_weighted_days
            else None
        )

        monthly_results.append(
            MonthlyAdaptationResult(
                month=month,
                sampled_day_count=len(
                    month_samples
                ),
                eligible_sample_count=(
                    month_eligible_count
                ),
                total_weighted_days=(
                    month_total_weighted_days
                ),
                evaluated_weighted_days=(
                    month_evaluated_weighted_days
                ),
                beneficial_weighted_days=(
                    month_beneficial_weighted_days
                ),
                exposure_coverage_percent=round(
                    month_exposure_coverage,
                    4,
                ),
                climate_adaptation_rate_percent=(
                    round(
                        month_adaptation_rate,
                        4,
                    )
                    if month_adaptation_rate
                    is not None
                    else None
                ),
                average_skin_improvement_c=(
                    round(
                        month_weighted_skin_total
                        / month_evaluated_weighted_days,
                        4,
                    )
                    if month_evaluated_weighted_days
                    else None
                ),
                average_core_improvement_c=(
                    round(
                        month_weighted_core_total
                        / month_evaluated_weighted_days,
                        4,
                    )
                    if month_evaluated_weighted_days
                    else None
                ),
                maximum_skin_improvement_c=(
                    round(
                        month_maximum_skin,
                        4,
                    )
                    if month_maximum_skin is not None
                    else None
                ),
                samples=month_samples,
            )
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

    duration_hours = (
        request.duration_minutes / 60
    )

    effective_cooling_hours = (
        beneficial_weighted_days
        * duration_hours
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
                weighted_skin_total
                / evaluated_weighted_days,
                4,
            )
            if evaluated_weighted_days
            else None
        ),
        "annual_average_core_improvement_c": (
            round(
                weighted_core_total
                / evaluated_weighted_days,
                4,
            )
            if evaluated_weighted_days
            else None
        ),
        "maximum_skin_improvement_c": (
            round(
                maximum_skin_improvement,
                4,
            )
            if maximum_skin_improvement is not None
            else None
        ),
        "effective_cooling_hours": round(
            effective_cooling_hours,
            2,
        ),
        "sampled_day_count": all_sample_count,
        "eligible_sample_count": (
            eligible_sample_count
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