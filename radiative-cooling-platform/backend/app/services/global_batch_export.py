import csv
import io
import json
import zipfile

from app.models.global_batch import (
    GlobalBatchJob,
)


def build_batch_geojson(
    batch: GlobalBatchJob,
) -> dict:
    features = []

    for result in batch.city_results:
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
                "properties": {
                    "city_id": result.city_id,
                    "city_name": result.city_name,
                    "country": result.country,
                    "status": result.status,
                    "climate_adaptation_rate_percent": (
                        result
                        .climate_adaptation_rate_percent
                    ),
                    "exposure_coverage_percent": (
                        result
                        .exposure_coverage_percent
                    ),
                    "annual_average_skin_improvement_c": (
                        result
                        .annual_average_skin_improvement_c
                    ),
                    "annual_average_core_improvement_c": (
                        result
                        .annual_average_core_improvement_c
                    ),
                    "maximum_skin_improvement_c": (
                        result
                        .maximum_skin_improvement_c
                    ),
                    "effective_cooling_hours": (
                        result
                        .effective_cooling_hours
                    ),
                    "sampled_day_count": (
                        result.sampled_day_count
                    ),
                    "eligible_sample_count": (
                        result.eligible_sample_count
                    ),
                },
            }
        )

    return {
        "type": "FeatureCollection",
        "metadata": {
            "batch_id": batch.id,
            "status": batch.status,
            "year": batch.request_json.get(
                "year"
            ),
            "method": (
                "multi_day_heat_exposure_weighted"
            ),
            "sample_days_per_month": (
                batch.request_json.get(
                    "sample_days_per_month",
                    1,
                )
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
            "city_id",
            "city_name",
            "country",
            "status",
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
            "retry_count",
            "error_message",
        ]
    )

    for result in batch.city_results:
        writer.writerow(
            [
                batch.id,
                result.city_id,
                result.city_name,
                result.country,
                result.status,
                result.latitude,
                result.longitude,
                result
                .climate_adaptation_rate_percent,
                result.exposure_coverage_percent,
                result
                .annual_average_skin_improvement_c,
                result
                .annual_average_core_improvement_c,
                result.maximum_skin_improvement_c,
                result.effective_cooling_hours,
                result.sampled_day_count,
                result.eligible_sample_count,
                result.evaluated_weighted_days,
                result.beneficial_weighted_days,
                result.retry_count,
                result.error_message,
            ]
        )

    return output.getvalue()


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

    for result in batch.city_results:
        for monthly_result in (
            result.monthly_json or []
        ):
            month = monthly_result.get(
                "month"
            )

            samples = monthly_result.get(
                "samples",
                [],
            )

            # 舊有 4.1 格式。
            if not samples and monthly_result.get(
                "representative_date_local"
            ):
                samples = [
                    {
                        "sample_date_local": (
                            monthly_result.get(
                                "representative_date_local"
                            )
                        ),
                        "weight_days": (
                            monthly_result.get(
                                "weight_days"
                            )
                        ),
                        "exposure_eligible": True,
                        "beneficial": (
                            monthly_result.get(
                                "beneficial"
                            )
                        ),
                        "average_skin_improvement_c": (
                            monthly_result.get(
                                "average_skin_improvement_c"
                            )
                        ),
                        "final_skin_improvement_c": (
                            monthly_result.get(
                                "final_skin_improvement_c"
                            )
                        ),
                        "average_core_improvement_c": (
                            monthly_result.get(
                                "average_core_improvement_c"
                            )
                        ),
                        "maximum_skin_improvement_c": (
                            monthly_result.get(
                                "maximum_skin_improvement_c"
                            )
                        ),
                    }
                ]

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
                            "maximum_air_temperature_c"
                        ),
                        sample.get(
                            "mean_solar_radiation_w_m2"
                        ),
                        sample.get(
                            "maximum_solar_radiation_w_m2"
                        ),
                        sample.get(
                            "exposure_eligible"
                        ),
                        sample.get(
                            "beneficial"
                        ),
                        sample.get(
                            "average_skin_improvement_c"
                        ),
                        sample.get(
                            "final_skin_improvement_c"
                        ),
                        sample.get(
                            "average_core_improvement_c"
                        ),
                        sample.get(
                            "maximum_skin_improvement_c"
                        ),
                        sample.get(
                            "weather_from_cache"
                        ),
                    ]
                )

    return output.getvalue()


def build_batch_export_zip(
    batch: GlobalBatchJob,
) -> bytes:
    memory_file = io.BytesIO()

    batch_json = {
        "id": batch.id,
        "status": batch.status,
        "request": batch.request_json,
        "summary": batch.summary_json,
        "city_results": [
            {
                "city_id": result.city_id,
                "city_name": result.city_name,
                "country": result.country,
                "status": result.status,
                "climate_adaptation_rate_percent": (
                    result
                    .climate_adaptation_rate_percent
                ),
                "exposure_coverage_percent": (
                    result
                    .exposure_coverage_percent
                ),
                "annual_average_skin_improvement_c": (
                    result
                    .annual_average_skin_improvement_c
                ),
                "annual_average_core_improvement_c": (
                    result
                    .annual_average_core_improvement_c
                ),
                "maximum_skin_improvement_c": (
                    result.maximum_skin_improvement_c
                ),
                "effective_cooling_hours": (
                    result.effective_cooling_hours
                ),
                "sampled_day_count": (
                    result.sampled_day_count
                ),
                "eligible_sample_count": (
                    result.eligible_sample_count
                ),
                "retry_count": result.retry_count,
                "monthly_results": (
                    result.monthly_json
                ),
                "error_message": (
                    result.error_message
                ),
            }
            for result in batch.city_results
        ],
    }

    with zipfile.ZipFile(
        memory_file,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        archive.writestr(
            "city-summary.csv",
            build_city_summary_csv(batch),
        )

        archive.writestr(
            "sample-results.csv",
            build_sample_results_csv(batch),
        )

        archive.writestr(
            "results.geojson",
            json.dumps(
                build_batch_geojson(batch),
                ensure_ascii=False,
                indent=2,
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