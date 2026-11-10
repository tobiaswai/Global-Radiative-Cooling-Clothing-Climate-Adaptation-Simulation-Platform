import zipfile
from io import BytesIO
from types import SimpleNamespace

import pytest

from app.services.global_batch_export import (
    build_batch_export_zip,
)


@pytest.mark.unit
def test_export_contains_required_files():
    city_result = SimpleNamespace(
        city_id="dubai",
        city_name="Dubai",
        country="United Arab Emirates",
        status="completed",
        latitude=25.2048,
        longitude=55.2708,
        climate_adaptation_rate_percent=80.0,
        exposure_coverage_percent=75.0,
        annual_average_skin_improvement_c=0.5,
        annual_average_core_improvement_c=0.1,
        maximum_skin_improvement_c=1.2,
        effective_cooling_hours=400,
        sampled_day_count=36,
        eligible_sample_count=27,
        evaluated_weighted_days=274,
        beneficial_weighted_days=219,
        retry_count=0,
        error_message=None,
        monthly_json=[],
    )

    batch = SimpleNamespace(
        id="test-batch",
        status="completed",
        request_json={
            "year": 2023,
            "sample_days_per_month": 3,
        },
        summary_json={},
        city_results=[city_result],
    )

    archive_bytes = build_batch_export_zip(
        batch
    )

    with zipfile.ZipFile(
        BytesIO(archive_bytes)
    ) as archive:
        names = set(
            archive.namelist()
        )

    assert "city-summary.csv" in names
    assert "sample-results.csv" in names
    assert "results.geojson" in names
    assert "results.json" in names

@pytest.mark.unit
def test_sample_csv_header_and_rows_have_same_width():
    import csv, io
    from app.services.global_batch_export import build_sample_results_csv

    sample = {
        "sample_date_local": "2023-07-16T12:00:00", "weight_days": 31,
        "mean_air_temperature_c": 40.0, "maximum_air_temperature_c": 42.0,
        "daily_maximum_air_temperature_c": 44.0,
        "mean_solar_radiation_w_m2": 800.0, "maximum_solar_radiation_w_m2": 900.0,
        "exposure_eligible": True, "beneficial": True,
        "average_skin_improvement_c": 1.0, "final_skin_improvement_c": 1.2,
        "average_core_improvement_c": 0.5, "maximum_skin_improvement_c": 1.5,
        "weather_from_cache": True,
    }
    city = SimpleNamespace(city_id="dubai", city_name="Dubai", country="UAE",
                           monthly_json=[{"month": 7, "samples": [sample]}])
    batch = SimpleNamespace(id="b", city_results=[city])

    rows = list(csv.reader(io.StringIO(build_sample_results_csv(batch))))
    assert len(rows[0]) == len(rows[1])
    header = rows[0]
    assert rows[1][header.index("daily_maximum_air_temperature_c")] == "44.0"
    assert rows[1][header.index("mean_solar_radiation_w_m2")] == "800.0"