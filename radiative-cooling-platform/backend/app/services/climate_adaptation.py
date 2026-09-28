"""Per-city annual climate adaptation analysis.

Stage 1 changes
---------------
* Exposure statistics (mean / max air temperature and GHI) are computed over
  the exposure window only via ``compute_exposure_window_statistics``, never
  over the padded ``weather.points`` buffer.
* Skin/core improvement averages use time-weighted integration.
* Sample days whose weather fails validation are recorded as skipped instead
  of aborting the whole city.
* The duplicate ``build_weighted_sample_days`` was removed; the canonical
  implementation lives in ``annual_sampling`` and is re-exported here.
* ``effective_cooling_hours`` keeps its numeric field (DB column, CSV) but
  an explicit definition is emitted in ``metric_definitions``.
"""

from collections.abc import Callable
from datetime import datetime, timedelta

from app.core.cities import get_city
from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    MonthlyAdaptationResult,
    SkippedSample,
)
from app.schemas.simulation import WeatherSimulationRequest
from app.services.annual_sampling import (  # noqa: F401 (re-export)
    build_annual_sampling_plan,
    build_month_sampling_plan,
    build_weighted_sample_days,
)
from app.services.climate_analytics import build_city_analytics
from app.services.exposure_statistics import (
    compute_exposure_window_statistics,
    time_weighted_mean,
)
from app.services.weather import (
    get_historical_weather_range,
    slice_weather_time_series,
)
from app.services.weather_quality import WeatherDataError
from app.services.weather_simulation import (
    execute_weather_simulation_with_weather,
)


__all__ = [
    "analyze_city_climate_adaptation",
    "build_metric_definitions",
    "build_weighted_sample_days",
    "is_exposure_eligible",
    "summarize_month",
]


ProgressCallback = Callable[[int, str], None]

CheckpointCallback = Callable[
    [list[MonthlyAdaptationResult], int, int],
    None,
]


def build_metric_definitions(request: GlobalBatchCreate) -> dict:
    """Machine-readable definitions of derived metrics (see docs/metrics.md)."""
    return {
        "effective_cooling_hours": {
            "display_name": (
                "Estimated beneficial exposure hours under the configured "
                "daily exposure scenario"
            ),
            "formula": "beneficial_weighted_days * duration_minutes / 60",
            "interpretation": (
                "Sum over sampled days (weighted by the calendar days each "
                "sample represents) of the configured daily exposure "
                "duration, counted only when the sample is exposure-eligible "
                "and its time-weighted mean skin-temperature improvement is "
                ">= minimum_skin_improvement_c. It is not a measurement of "
                "hours during which cooling physically occurred."
            ),
            "inputs": {
                "local_start_hour": request.local_start_hour,
                "duration_minutes": request.duration_minutes,
                "minimum_skin_improvement_c": (
                    request.minimum_skin_improvement_c
                ),
                "minimum_air_temperature_c": (
                    request.minimum_air_temperature_c
                ),
                "minimum_solar_radiation_w_m2": (
                    request.minimum_solar_radiation_w_m2
                ),
                "exposure_match_mode": request.exposure_match_mode,
            },
            "statistics_window": (
                "[local_start_hour, local_start_hour + duration_minutes]; "
                "padding hours are excluded"
            ),
        }
    }


def round_optional(value: float | None, digits: int = 4) -> float | None:
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
            mean_air_temperature_c >= request.minimum_air_temperature_c
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


def get_next_month_start(*, year: int, month: int) -> datetime:
    if month == 12:
        return datetime(year + 1, 1, 1)
    return datetime(year, month + 1, 1)


def summarize_skip_reasons(
    skipped: list[SkippedSample],
) -> dict[str, int]:
    reasons: dict[str, int] = {}
    for item in skipped:
        reasons[item.reason_code] = reasons.get(item.reason_code, 0) + 1
    return reasons


def summarize_month(
    *,
    month: int,
    samples: list[DailyAdaptationResult],
    skipped: list[SkippedSample] | None = None,
) -> MonthlyAdaptationResult:
    skipped = list(skipped or [])

    total_weighted_days = sum(s.weight_days for s in samples)

    eligible_samples = [s for s in samples if s.exposure_eligible]

    evaluated_weighted_days = sum(s.weight_days for s in eligible_samples)

    beneficial_weighted_days = sum(
        s.weight_days for s in samples if s.beneficial
    )

    exposure_coverage_percent = (
        evaluated_weighted_days / total_weighted_days * 100.0
        if total_weighted_days
        else 0.0
    )

    climate_adaptation_rate_percent = (
        beneficial_weighted_days / evaluated_weighted_days * 100.0
        if evaluated_weighted_days
        else None
    )

    average_skin_improvement_c = (
        sum(s.average_skin_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    average_core_improvement_c = (
        sum(s.average_core_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement_c = (
        max(s.maximum_skin_improvement_c for s in eligible_samples)
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
        exposure_coverage_percent=round(exposure_coverage_percent, 4),
        climate_adaptation_rate_percent=round_optional(
            climate_adaptation_rate_percent
        ),
        average_skin_improvement_c=round_optional(average_skin_improvement_c),
        average_core_improvement_c=round_optional(average_core_improvement_c),
        maximum_skin_improvement_c=round_optional(maximum_skin_improvement_c),
        samples=samples,
        skipped_samples=skipped,
        skipped_weighted_days=sum(s.weight_days for s in skipped),
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
        if request.start_month <= result.month <= request.end_month:
            results_by_month[result.month] = result

    return [results_by_month[m] for m in sorted(results_by_month)]


async def analyze_city_climate_adaptation(
    *,
    city_id: str,
    request: GlobalBatchCreate,
    progress_callback: ProgressCallback | None = None,
    checkpoint_callback: CheckpointCallback | None = None,
    initial_monthly_results: list[MonthlyAdaptationResult] | None = None,
) -> dict:
    city = get_city(city_id)

    annual_plan = build_annual_sampling_plan(request)

    if not annual_plan:
        raise RuntimeError("No sampling dates were generated")

    total_sample_count = len(annual_plan)

    monthly_results = normalize_initial_monthly_results(
        request=request,
        results=initial_monthly_results,
    )

    completed_months = {r.month for r in monthly_results}

    completed_sample_count = sum(
        r.sampled_day_count + len(r.skipped_samples)
        for r in monthly_results
    )

    monthly_weather_payload_sha256: dict[str, str | None] = {}

    def report(progress: int, stage: str) -> None:
        if progress_callback is not None:
            progress_callback(max(0, min(progress, 100)), stage)

    def progress_now() -> int:
        return max(
            1,
            round(completed_sample_count / total_sample_count * 92),
        )

    for month in range(request.start_month, request.end_month + 1):
        if month in completed_months:
            report(
                progress_now(),
                f"restored_checkpoint_{request.year}-{month:02d}",
            )
            continue

        month_plan = build_month_sampling_plan(request=request, month=month)

        month_start = datetime(request.year, month, 1, 0, 0, 0)

        next_month_start = get_next_month_start(
            year=request.year, month=month
        )

        # The final simulation day may continue into the next month.
        prefetch_end = next_month_start + timedelta(
            hours=request.local_start_hour,
            minutes=request.duration_minutes,
        )

        report(
            progress_now(),
            f"prefetching_weather_{request.year}-{month:02d}",
        )

        # Monthly prefetch: do not require whole-month coverage here; each
        # sample slice enforces coverage for its own exposure window.
        month_weather = await get_historical_weather_range(
            city=city,
            start_time_local=month_start,
            end_time_local=prefetch_end,
            padding_hours=1,
            require_window_coverage=False,
        )

        monthly_weather_payload_sha256[f"{month:02d}"] = (
            month_weather.source.payload_sha256
        )

        month_samples: list[DailyAdaptationResult] = []
        month_skipped: list[SkippedSample] = []

        for sample_day in month_plan:
            start_time_local = datetime(
                sample_day.date_local.year,
                sample_day.date_local.month,
                sample_day.date_local.day,
                request.local_start_hour,
                0,
                0,
            )

            report(
                progress_now(),
                f"analyzing_{start_time_local:%Y-%m-%d}",
            )

            try:
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
                    output_interval_minutes=request.output_interval_minutes,
                    person=request.person,
                    control_material=request.control_material,
                    rc_material=request.rc_material,
                )

                simulation = execute_weather_simulation_with_weather(
                    request=simulation_request,
                    weather=sample_weather,
                )

            except WeatherDataError as error:
                month_skipped.append(
                    SkippedSample(
                        sample_date_local=start_time_local,
                        weight_days=sample_day.weight_days,
                        reason_code=error.code,
                        message=str(error)[:500],
                    )
                )
                completed_sample_count += 1
                continue

            paired_points = list(
                zip(
                    simulation.control.time_series,
                    simulation.radiative_cooling.time_series,
                    strict=True,
                )
            )

            if not paired_points:
                raise RuntimeError("Simulation returned no paired points")

            minutes = [control.minute for control, _ in paired_points]

            skin_improvements = [
                control.skin_temperature_c - radiative.skin_temperature_c
                for control, radiative in paired_points
            ]

            core_improvements = [
                control.core_temperature_c - radiative.core_temperature_c
                for control, radiative in paired_points
            ]

            # Exposure statistics strictly over [start, start + duration].
            exposure = compute_exposure_window_statistics(sample_weather)

            average_skin_improvement_c = time_weighted_mean(
                minutes, skin_improvements
            )
            average_core_improvement_c = time_weighted_mean(
                minutes, core_improvements
            )
            maximum_skin_improvement_c = max(skin_improvements)

            exposure_eligible = is_exposure_eligible(
                mean_air_temperature_c=exposure.mean_air_temperature_c,
                mean_solar_radiation_w_m2=exposure.mean_solar_radiation_w_m2,
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
                        exposure.mean_air_temperature_c, 4
                    ),
                    maximum_air_temperature_c=round(
                        exposure.maximum_air_temperature_c, 4
                    ),
                    mean_solar_radiation_w_m2=round(
                        exposure.mean_solar_radiation_w_m2, 4
                    ),
                    maximum_solar_radiation_w_m2=round(
                        exposure.maximum_solar_radiation_w_m2, 4
                    ),
                    exposure_eligible=exposure_eligible,
                    beneficial=beneficial,
                    average_skin_improvement_c=round(
                        average_skin_improvement_c, 4
                    ),
                    final_skin_improvement_c=round(
                        simulation.summary.final_skin_temperature_improvement_c,
                        4,
                    ),
                    average_core_improvement_c=round(
                        average_core_improvement_c, 4
                    ),
                    maximum_skin_improvement_c=round(
                        maximum_skin_improvement_c, 4
                    ),
                    weather_from_cache=month_weather.source.from_cache,
                )
            )

            completed_sample_count += 1

        monthly_result = summarize_month(
            month=month,
            samples=month_samples,
            skipped=month_skipped,
        )

        monthly_results.append(monthly_result)
        monthly_results.sort(key=lambda r: r.month)
        completed_months.add(month)

        if checkpoint_callback is not None:
            checkpoint_callback(
                list(monthly_results),
                month,
                completed_sample_count,
            )

    all_samples = [s for m in monthly_results for s in m.samples]
    all_skipped = [s for m in monthly_results for s in m.skipped_samples]

    eligible_samples = [s for s in all_samples if s.exposure_eligible]

    total_weighted_days = sum(s.weight_days for s in all_samples)

    evaluated_weighted_days = sum(s.weight_days for s in eligible_samples)

    beneficial_weighted_days = sum(
        s.weight_days for s in all_samples if s.beneficial
    )

    exposure_coverage_percent = (
        evaluated_weighted_days / total_weighted_days * 100.0
        if total_weighted_days
        else 0.0
    )

    climate_adaptation_rate_percent = (
        beneficial_weighted_days / evaluated_weighted_days * 100.0
        if evaluated_weighted_days
        else None
    )

    annual_average_skin_improvement_c = (
        sum(s.average_skin_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    annual_average_core_improvement_c = (
        sum(s.average_core_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement_c = (
        max(s.maximum_skin_improvement_c for s in eligible_samples)
        if eligible_samples
        else None
    )

    effective_cooling_hours = (
        beneficial_weighted_days * request.duration_minutes / 60.0
    )

    analytics = build_city_analytics(samples=all_samples, request=request)

    report(96, "generating_city_summary")

    return {
        "city_id": city.id,
        "city_name": city.name,
        "country": city.country,
        "latitude": city.latitude,
        "longitude": city.longitude,
        "climate_adaptation_rate_percent": round_optional(
            climate_adaptation_rate_percent
        ),
        "exposure_coverage_percent": round(exposure_coverage_percent, 4),
        "annual_average_skin_improvement_c": round_optional(
            annual_average_skin_improvement_c
        ),
        "annual_average_core_improvement_c": round_optional(
            annual_average_core_improvement_c
        ),
        "maximum_skin_improvement_c": round_optional(
            maximum_skin_improvement_c
        ),
        "effective_cooling_hours": round(effective_cooling_hours, 2),
        "sampled_day_count": len(all_samples),
        "eligible_sample_count": len(eligible_samples),
        "evaluated_weighted_days": evaluated_weighted_days,
        "beneficial_weighted_days": beneficial_weighted_days,
        "completed_month_count": len(monthly_results),
        "skin_improvement_p50_c": analytics["skin_improvement_p50_c"],
        "skin_improvement_p90_c": analytics["skin_improvement_p90_c"],
        "skin_improvement_p95_c": analytics["skin_improvement_p95_c"],
        "core_improvement_p50_c": analytics["core_improvement_p50_c"],
        "core_improvement_p90_c": analytics["core_improvement_p90_c"],
        "core_improvement_p95_c": analytics["core_improvement_p95_c"],
        "heatwave_analysis_available": analytics["heatwave_analysis_available"],
        "heatwave_event_count": analytics["heatwave_event_count"],
        "longest_heatwave_days": analytics["longest_heatwave_days"],
        "heatwave_events": analytics["heatwave_events"],
        "data_quality": {
            "skipped_sample_count": len(all_skipped),
            "skipped_weighted_days": sum(s.weight_days for s in all_skipped),
            "skip_reasons": summarize_skip_reasons(all_skipped),
            "monthly_weather_payload_sha256": monthly_weather_payload_sha256,
        },
        "metric_definitions": build_metric_definitions(request),
        "monthly_results": [
            r.model_dump(mode="json") for r in monthly_results
        ],
    }