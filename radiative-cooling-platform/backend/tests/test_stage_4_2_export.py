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