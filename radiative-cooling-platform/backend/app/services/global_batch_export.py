import csv
import io
import json
import zipfile
from typing import Any

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)

def get_attribute(
    obj: Any,
    name: str,
    default: Any = None,
) -> Any:
    return getattr(
        obj,
        name,
        default,
    )

def get_heatwave_events(
    result: GlobalCityResult,
) -> list[dict[str, Any]]:
    analytics = get_attribute(
        result,
        "analytics_json",
        {},
    ) or {}

    if not isinstance(analytics, dict):
        return []

    events = analytics.get(
        "heatwave_events",
        [],
    )

    if not isinstance(events, list):
        return []

    return [
        event
        for event in events
        if isinstance(event, dict)
    ]

def build_geojson_properties(
    result: GlobalCityResult,
) -> dict[str, Any]:
    return {
        "city_id": get_attribute(
            result,
            "city_id",
        ),
        "city_name": get_attribute(
            result,
            "city_name",
        ),
        "country": get_attribute(
            result,
            "country",
        ),
        "status": get_attribute(
            result,
            "status",
        ),
        "climate_adaptation_rate_percent": (
            get_attribute(
                result,
                "climate_adaptation_rate_percent",
            )
        ),
        "exposure_coverage_percent": (
            get_attribute(
                result,
                "exposure_coverage_percent",
            )
        ),
        "annual_average_skin_improvement_c": (
            get_attribute(
                result,
                "annual_average_skin_improvement_c",
            )
        ),
        "annual_average_core_improvement_c": (
            get_attribute(
                result,
                "annual_average_core_improvement_c",
            )
        ),
        "maximum_skin_improvement_c": (
            get_attribute(
                result,
                "maximum_skin_improvement_c",
            )
        ),
        "effective_cooling_hours": (
            get_attribute(
                result,
                "effective_cooling_hours",
            )
        ),
        "sampled_day_count": get_attribute(
            result,
            "sampled_day_count",
            0,
        ),
        "eligible_sample_count": get_attribute(
            result,
            "eligible_sample_count",
            0,
        ),
        "evaluated_weighted_days": get_attribute(
            result,
            "evaluated_weighted_days",
            0,
        ),
        "beneficial_weighted_days": get_attribute(
            result,
            "beneficial_weighted_days",
            0,
        ),
        "skin_improvement_p50_c": get_attribute(
            result,
            "skin_improvement_p50_c",
        ),
        "skin_improvement_p90_c": get_attribute(
            result,
            "skin_improvement_p90_c",
        ),
        "skin_improvement_p95_c": get_attribute(
            result,
            "skin_improvement_p95_c",
        ),
        "core_improvement_p50_c": get_attribute(
            result,
            "core_improvement_p50_c",
        ),
        "core_improvement_p90_c": get_attribute(
            result,
            "core_improvement_p90_c",
        ),
        "core_improvement_p95_c": get_attribute(
            result,
            "core_improvement_p95_c",
        ),
        "heatwave_event_count": get_attribute(
            result,
            "heatwave_event_count",
            0,
        ),
        "longest_heatwave_days": get_attribute(
            result,
            "longest_heatwave_days",
            0,
        ),
    }

def build_batch_geojson(
    batch: GlobalBatchJob,
) -> dict[str, Any]:
    request = batch.request_json or {}

    analysis_resolution = request.get(
        "analysis_resolution",
        "representative",
    )

    heatwave_analysis_available = (
        request.get(
            "enable_heatwave_analysis",
            True,
        )
        and analysis_resolution == "daily"
        and request.get(
            "daily_stride_days",
            1,
        ) == 1
    )

    features = []

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        if result.status != "completed":
            continue

        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        result.longitude,
                        result.latitude,
                    ],
                },
                "properties": (
                    build_geojson_properties(
                        result
                    )
                ),
            }
        )

    return {
        "type": "FeatureCollection",
        "metadata": {
            "batch_id": batch.id,
            "status": batch.status,
            "year": request.get("year"),
            "method": (
                "daily_heat_exposure_weighted"
                if analysis_resolution == "daily"
                else (
                    "representative_day_"
                    "heat_exposure_weighted"
                )
            ),
            "analysis_resolution": (
                analysis_resolution
            ),
            "sample_days_per_month": (
                request.get(
                    "sample_days_per_month",
                    1,
                )
            ),
            "daily_stride_days": (
                request.get(
                    "daily_stride_days",
                    1,
                )
            ),
            "execution_profile": (
                request.get(
                    "execution_profile",
                    "auto",
                )
            ),
            "heatwave_analysis_available": (
                heatwave_analysis_available
            ),
        },
        "features": features,
    }


def build_city_summary_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_result_id",
            "city_id",
            "city_name",
            "country",
            "status",
            "stage",
            "progress",
            "latitude",
            "longitude",
            "climate_adaptation_rate_percent",
            "exposure_coverage_percent",
            "annual_average_skin_improvement_c",
            "annual_average_core_improvement_c",
            "maximum_skin_improvement_c",
            "effective_cooling_hours",
            "sampled_day_count",
            "eligible_sample_count",
            "evaluated_weighted_days",
            "beneficial_weighted_days",
            "skin_improvement_p50_c",
            "skin_improvement_p90_c",
            "skin_improvement_p95_c",
            "core_improvement_p50_c",
            "core_improvement_p90_c",
            "core_improvement_p95_c",
            "heatwave_event_count",
            "longest_heatwave_days",
            "completed_month_count",
            "last_checkpoint_month",
            "resumed_from_checkpoint",
            "last_heartbeat_at",
            "retry_count",
            "started_at",
            "completed_at",
            "error_message",
        ]
    )

    city_results = get_attribute(
        batch,
        "city_results",
        [],
    ) or []

    batch_id = get_attribute(
        batch,
        "id",
    )

    for result in city_results:
        status = get_attribute(
            result,
            "status",
        )

        writer.writerow(
            [
                batch_id,
                get_attribute(
                    result,
                    "id",
                ),
                get_attribute(
                    result,
                    "city_id",
                ),
                get_attribute(
                    result,
                    "city_name",
                ),
                get_attribute(
                    result,
                    "country",
                ),
                status,
                get_attribute(
                    result,
                    "stage",
                    status,
                ),
                get_attribute(
                    result,
                    "progress",
                    (
                        100
                        if status == "completed"
                        else 0
                    ),
                ),
                get_attribute(
                    result,
                    "latitude",
                ),
                get_attribute(
                    result,
                    "longitude",
                ),
                get_attribute(
                    result,
                    (
                        "climate_adaptation_"
                        "rate_percent"
                    ),
                ),
                get_attribute(
                    result,
                    "exposure_coverage_percent",
                ),
                get_attribute(
                    result,
                    (
                        "annual_average_skin_"
                        "improvement_c"
                    ),
                ),
                get_attribute(
                    result,
                    (
                        "annual_average_core_"
                        "improvement_c"
                    ),
                ),
                get_attribute(
                    result,
                    "maximum_skin_improvement_c",
                ),
                get_attribute(
                    result,
                    "effective_cooling_hours",
                    0,
                ),
                get_attribute(
                    result,
                    "sampled_day_count",
                    0,
                ),
                get_attribute(
                    result,
                    "eligible_sample_count",
                    0,
                ),
                get_attribute(
                    result,
                    "evaluated_weighted_days",
                    0,
                ),
                get_attribute(
                    result,
                    "beneficial_weighted_days",
                    0,
                ),
                get_attribute(
                    result,
                    "skin_improvement_p50_c",
                ),
                get_attribute(
                    result,
                    "skin_improvement_p90_c",
                ),
                get_attribute(
                    result,
                    "skin_improvement_p95_c",
                ),
                get_attribute(
                    result,
                    "core_improvement_p50_c",
                ),
                get_attribute(
                    result,
                    "core_improvement_p90_c",
                ),
                get_attribute(
                    result,
                    "core_improvement_p95_c",
                ),
                get_attribute(
                    result,
                    "heatwave_event_count",
                    0,
                ),
                get_attribute(
                    result,
                    "longest_heatwave_days",
                    0,
                ),
                get_attribute(
                    result,
                    "completed_month_count",
                    0,
                ),
                get_attribute(
                    result,
                    "last_checkpoint_month",
                ),
                get_attribute(
                    result,
                    "resumed_from_checkpoint",
                    False,
                ),
                get_attribute(
                    result,
                    "last_heartbeat_at",
                ),
                get_attribute(
                    result,
                    "retry_count",
                    0,
                ),
                get_attribute(
                    result,
                    "started_at",
                ),
                get_attribute(
                    result,
                    "completed_at",
                ),
                get_attribute(
                    result,
                    "error_message",
                ),
            ]
        )

    return output.getvalue()


def build_monthly_results_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_id",
            "city_name",
            "country",
            "month",
            "sampled_day_count",
            "eligible_sample_count",
            "total_weighted_days",
            "evaluated_weighted_days",
            "beneficial_weighted_days",
            "exposure_coverage_percent",
            "climate_adaptation_rate_percent",
            "average_skin_improvement_c",
            "average_core_improvement_c",
            "maximum_skin_improvement_c",
        ]
    )

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        monthly_results = (
            result.monthly_json or []
        )

        for monthly_result in monthly_results:
            if not isinstance(
                monthly_result,
                dict,
            ):
                continue

            writer.writerow(
                [
                    batch.id,
                    result.city_id,
                    result.city_name,
                    result.country,
                    monthly_result.get(
                        "month"
                    ),
                    monthly_result.get(
                        "sampled_day_count"
                    ),
                    monthly_result.get(
                        "eligible_sample_count"
                    ),
                    monthly_result.get(
                        "total_weighted_days"
                    ),
                    monthly_result.get(
                        "evaluated_weighted_days"
                    ),
                    monthly_result.get(
                        "beneficial_weighted_days"
                    ),
                    monthly_result.get(
                        "exposure_coverage_percent"
                    ),
                    monthly_result.get(
                        (
                            "climate_adaptation_"
                            "rate_percent"
                        )
                    ),
                    monthly_result.get(
                        (
                            "average_skin_"
                            "improvement_c"
                        )
                    ),
                    monthly_result.get(
                        (
                            "average_core_"
                            "improvement_c"
                        )
                    ),
                    monthly_result.get(
                        (
                            "maximum_skin_"
                            "improvement_c"
                        )
                    ),
                ]
            )

    return output.getvalue()


def normalize_month_samples(
    monthly_result: dict[str, Any],
) -> list[dict[str, Any]]:
    samples = monthly_result.get(
        "samples",
        [],
    )

    if isinstance(samples, list) and samples:
        return [
            sample
            for sample in samples
            if isinstance(sample, dict)
        ]

    representative_date = (
        monthly_result.get(
            "representative_date_local"
        )
    )

    if not representative_date:
        return []

    return [
        {
            "sample_date_local": (
                representative_date
            ),
            "weight_days": (
                monthly_result.get(
                    "weight_days",
                    1,
                )
            ),
            "mean_air_temperature_c": None,
            "maximum_air_temperature_c": None,
            "mean_solar_radiation_w_m2": None,
            "maximum_solar_radiation_w_m2": None,
            "exposure_eligible": True,
            "beneficial": (
                monthly_result.get(
                    "beneficial"
                )
            ),
            "average_skin_improvement_c": (
                monthly_result.get(
                    (
                        "average_skin_"
                        "improvement_c"
                    )
                )
            ),
            "final_skin_improvement_c": (
                monthly_result.get(
                    (
                        "final_skin_"
                        "improvement_c"
                    )
                )
            ),
            "average_core_improvement_c": (
                monthly_result.get(
                    (
                        "average_core_"
                        "improvement_c"
                    )
                )
            ),
            "maximum_skin_improvement_c": (
                monthly_result.get(
                    (
                        "maximum_skin_"
                        "improvement_c"
                    )
                )
            ),
            "weather_from_cache": None,
        }
    ]


def build_sample_results_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_id",
            "city_name",
            "country",
            "month",
            "sample_date_local",
            "weight_days",
            "mean_air_temperature_c",
            "maximum_air_temperature_c",
            "mean_solar_radiation_w_m2",
            "maximum_solar_radiation_w_m2",
            "exposure_eligible",
            "beneficial",
            "average_skin_improvement_c",
            "final_skin_improvement_c",
            "average_core_improvement_c",
            "maximum_skin_improvement_c",
            "weather_from_cache",
        ]
    )

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        monthly_results = (
            result.monthly_json or []
        )

        for monthly_result in monthly_results:
            if not isinstance(
                monthly_result,
                dict,
            ):
                continue

            month = monthly_result.get(
                "month"
            )

            samples = normalize_month_samples(
                monthly_result
            )

            for sample in samples:
                writer.writerow(
                    [
                        batch.id,
                        result.city_id,
                        result.city_name,
                        result.country,
                        month,
                        sample.get(
                            "sample_date_local"
                        ),
                        sample.get(
                            "weight_days"
                        ),
                        sample.get(
                            "mean_air_temperature_c"
                        ),
                        sample.get(
                            (
                                "maximum_air_"
                                "temperature_c"
                            )
                        ),
                        sample.get(
                            (
                                "mean_solar_"
                                "radiation_w_m2"
                            )
                        ),
                        sample.get(
                            (
                                "maximum_solar_"
                                "radiation_w_m2"
                            )
                        ),
                        sample.get(
                            "exposure_eligible"
                        ),
                        sample.get(
                            "beneficial"
                        ),
                        sample.get(
                            (
                                "average_skin_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            (
                                "final_skin_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            (
                                "average_core_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            (
                                "maximum_skin_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            "weather_from_cache"
                        ),
                    ]
                )

    return output.getvalue()


def build_heatwave_events_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_id",
            "city_name",
            "country",
            "event_number",
            "start_date_local",
            "end_date_local",
            "duration_days",
            "mean_maximum_air_temperature_c",
            "peak_air_temperature_c",
            "mean_skin_improvement_c",
            "p90_skin_improvement_c",
            "beneficial_day_count",
        ]
    )

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        events = get_heatwave_events(
            result
        )

        for event_number, event in enumerate(
            events,
            start=1,
        ):
            writer.writerow(
                [
                    batch.id,
                    result.city_id,
                    result.city_name,
                    result.country,
                    event_number,
                    event.get(
                        "start_date_local"
                    ),
                    event.get(
                        "end_date_local"
                    ),
                    event.get(
                        "duration_days"
                    ),
                    event.get(
                        (
                            "mean_maximum_air_"
                            "temperature_c"
                        )
                    ),
                    event.get(
                        "peak_air_temperature_c"
                    ),
                    event.get(
                        (
                            "mean_skin_"
                            "improvement_c"
                        )
                    ),
                    event.get(
                        (
                            "p90_skin_"
                            "improvement_c"
                        )
                    ),
                    event.get(
                        "beneficial_day_count"
                    ),
                ]
            )

    return output.getvalue()

def build_city_result_json(
    result: GlobalCityResult,
) -> dict[str, Any]:
    analytics = get_attribute(
        result,
        "analytics_json",
        {},
    ) or {}

    if not isinstance(analytics, dict):
        analytics = {}

    status = get_attribute(
        result,
        "status",
    )

    return {
        "id": get_attribute(
            result,
            "id",
        ),
        "batch_id": get_attribute(
            result,
            "batch_id",
        ),
        "celery_task_id": get_attribute(
            result,
            "celery_task_id",
        ),
        "city_id": get_attribute(
            result,
            "city_id",
        ),
        "city_name": get_attribute(
            result,
            "city_name",
        ),
        "country": get_attribute(
            result,
            "country",
        ),
        "latitude": get_attribute(
            result,
            "latitude",
        ),
        "longitude": get_attribute(
            result,
            "longitude",
        ),
        "status": status,
        "stage": get_attribute(
            result,
            "stage",
            status,
        ),
        "progress": get_attribute(
            result,
            "progress",
            100 if status == "completed" else 0,
        ),
        "climate_adaptation_rate_percent": (
            get_attribute(
                result,
                "climate_adaptation_rate_percent",
            )
        ),
        "exposure_coverage_percent": (
            get_attribute(
                result,
                "exposure_coverage_percent",
            )
        ),
        "annual_average_skin_improvement_c": (
            get_attribute(
                result,
                "annual_average_skin_improvement_c",
            )
        ),
        "annual_average_core_improvement_c": (
            get_attribute(
                result,
                "annual_average_core_improvement_c",
            )
        ),
        "maximum_skin_improvement_c": (
            get_attribute(
                result,
                "maximum_skin_improvement_c",
            )
        ),
        "effective_cooling_hours": get_attribute(
            result,
            "effective_cooling_hours",
            0,
        ),
        "sampled_day_count": get_attribute(
            result,
            "sampled_day_count",
            0,
        ),
        "eligible_sample_count": get_attribute(
            result,
            "eligible_sample_count",
            0,
        ),
        "evaluated_weighted_days": get_attribute(
            result,
            "evaluated_weighted_days",
            0,
        ),
        "beneficial_weighted_days": get_attribute(
            result,
            "beneficial_weighted_days",
            0,
        ),
        "completed_month_count": get_attribute(
            result,
            "completed_month_count",
            0,
        ),
        "last_checkpoint_month": get_attribute(
            result,
            "last_checkpoint_month",
        ),
        "resumed_from_checkpoint": get_attribute(
            result,
            "resumed_from_checkpoint",
            False,
        ),
        "last_heartbeat_at": get_attribute(
            result,
            "last_heartbeat_at",
        ),
        "skin_improvement_percentiles_c": {
            "p50": get_attribute(
                result,
                "skin_improvement_p50_c",
            ),
            "p90": get_attribute(
                result,
                "skin_improvement_p90_c",
            ),
            "p95": get_attribute(
                result,
                "skin_improvement_p95_c",
            ),
        },
        "core_improvement_percentiles_c": {
            "p50": get_attribute(
                result,
                "core_improvement_p50_c",
            ),
            "p90": get_attribute(
                result,
                "core_improvement_p90_c",
            ),
            "p95": get_attribute(
                result,
                "core_improvement_p95_c",
            ),
        },
        "heatwave_event_count": get_attribute(
            result,
            "heatwave_event_count",
            0,
        ),
        "longest_heatwave_days": get_attribute(
            result,
            "longest_heatwave_days",
            0,
        ),
        "heatwave_analysis_available": (
            analytics.get(
                "heatwave_analysis_available",
                False,
            )
        ),
        "heatwave_events": get_heatwave_events(
            result
        ),
        "retry_count": get_attribute(
            result,
            "retry_count",
            0,
        ),
        "monthly_results": get_attribute(
            result,
            "monthly_json",
            [],
        ) or [],
        "error_message": get_attribute(
            result,
            "error_message",
        ),
        "started_at": get_attribute(
            result,
            "started_at",
        ),
        "completed_at": get_attribute(
            result,
            "completed_at",
        ),
    }

def build_batch_json(
    batch: GlobalBatchJob,
) -> dict[str, Any]:
    city_results = get_attribute(
        batch,
        "city_results",
        [],
    ) or []

    status = get_attribute(
        batch,
        "status",
    )

    return {
        "id": getattr(
            batch,
            "id",
            None,
        ),
        "celery_group_id": getattr(
            batch,
            "celery_group_id",
            None,
        ),
        "status": status,
        "stage": getattr(
            batch,
            "stage",
            status,
        ),
        "progress": getattr(
            batch,
            "progress",
            100 if status == "completed" else 0,
        ),
        "total_city_count": getattr(
            batch,
            "total_city_count",
            len(city_results),
        ),
        "completed_city_count": getattr(
            batch,
            "completed_city_count",
            sum(
                1
                for result in city_results
                if getattr(
                    result,
                    "status",
                    None,
                ) == "completed"
            ),
        ),
        "failed_city_count": getattr(
            batch,
            "failed_city_count",
            sum(
                1
                for result in city_results
                if getattr(
                    result,
                    "status",
                    None,
                ) == "failed"
            ),
        ),
        "cancelled_city_count": getattr(
            batch,
            "cancelled_city_count",
            sum(
                1
                for result in city_results
                if getattr(
                    result,
                    "status",
                    None,
                ) == "cancelled"
            ),
        ),
        "request": get_attribute(
            batch,
            "request_json",
            {},
        ) or {},
        "summary": get_attribute(
            batch,
            "summary_json",
            {},
        ) or {},
        "error_message": getattr(
            batch,
            "error_message",
            None,
        ),
        "created_at": getattr(
            batch,
            "created_at",
            None,
        ),
        "updated_at": getattr(
            batch,
            "updated_at",
            None,
        ),
        "started_at": getattr(
            batch,
            "started_at",
            None,
        ),
        "completed_at": getattr(
            batch,
            "completed_at",
            None,
        ),
        "city_results": [
            build_city_result_json(result)
            for result in city_results
        ],
    }


def build_readme_text(
    batch: GlobalBatchJob,
) -> str:
    request = batch.request_json or {}

    return "\n".join(
        [
            "Global Climate Adaptation Analysis Export",
            "=========================================",
            "",
            f"Batch ID: {batch.id}",
            f"Status: {batch.status}",
            (
                "Analysis resolution: "
                f"{request.get('analysis_resolution', 'representative')}"
            ),
            (
                "Execution profile: "
                f"{request.get('execution_profile', 'auto')}"
            ),
            "",
            "Files",
            "-----",
            "",
            "city-summary.csv",
            (
                "One row per city containing annual, "
                "checkpoint, percentile, and heatwave "
                "summary metrics."
            ),
            "",
            "monthly-results.csv",
            (
                "One row per city and month containing "
                "weighted monthly adaptation metrics."
            ),
            "",
            "sample-results.csv",
            (
                "One row per sampled day containing "
                "weather exposure and thermal "
                "improvement metrics."
            ),
            "",
            "heatwave-events.csv",
            (
                "One row per detected heatwave event. "
                "This file may contain only its header "
                "when heatwave analysis is unavailable "
                "or no event was detected."
            ),
            "",
            "results.geojson",
            (
                "Completed city results represented as "
                "GeoJSON point features."
            ),
            "",
            "results.json",
            (
                "Complete batch request, summary, city "
                "analytics, monthly results, and "
                "heatwave events."
            ),
            "",
        ]
    )


def build_batch_export_zip(
    batch: GlobalBatchJob,
) -> bytes:
    memory_file = io.BytesIO()

    batch_json = build_batch_json(
        batch
    )

    with zipfile.ZipFile(
        memory_file,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        archive.writestr(
            "README.txt",
            build_readme_text(batch),
        )

        archive.writestr(
            "city-summary.csv",
            build_city_summary_csv(batch),
        )

        archive.writestr(
            "monthly-results.csv",
            build_monthly_results_csv(batch),
        )

        archive.writestr(
            "sample-results.csv",
            build_sample_results_csv(batch),
        )

        archive.writestr(
            "heatwave-events.csv",
            build_heatwave_events_csv(batch),
        )

        archive.writestr(
            "results.geojson",
            json.dumps(
                build_batch_geojson(batch),
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
        )

        archive.writestr(
            "results.json",
            json.dumps(
                batch_json,
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
        )

    return memory_file.getvalue()