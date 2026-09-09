from datetime import datetime
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)

@pytest.fixture
def completed_partial_batch(
    db_session,
    person,
    control_material,
    rc_material,
):
    request = GlobalBatchCreate(
        city_ids=["dubai"],
        year=2025,
        sample_days_per_month=1,
        resume_from_checkpoint=True,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )
    
    batch = GlobalBatchJob(
        id=str(uuid4()),
        status="failed",
        request_json=request.model_dump(
            mode="json",
        ),
        summary_json={},
    )

    db_session.add(batch)
    db_session.flush()

    city_result = GlobalCityResult(
        id=str(uuid4()),
        batch_id=batch.id,
        city_id="dubai",
        city_name="Dubai",
        country="United Arab Emirates",
        latitude=25.2048,
        longitude=55.2708,
        status="failed",
        stage="failed",
        progress=25,
        monthly_json=[
            {
                "month": 1,
                "sampled_day_count": 1,
                "eligible_sample_count": 1,
                "total_weighted_days": 31,
                "evaluated_weighted_days": 31,
                "beneficial_weighted_days": 31,
                "exposure_coverage_percent": 100,
                "climate_adaptation_rate_percent": 100,
                "average_skin_improvement_c": 0.5,
                "average_core_improvement_c": 0.1,
                "maximum_skin_improvement_c": 0.8,
                "samples": [],
            }
        ],
        completed_month_count=1,
        last_checkpoint_month=1,
        resumed_from_checkpoint=False,
        retry_count=0,
        error_message="Simulated interruption",
    )

    db_session.add(city_result)
    db_session.commit()

    db_session.refresh(batch)
    db_session.refresh(city_result)

    return SimpleNamespace(
        id=batch.id,
        batch=batch,
        city_result=city_result,
        session=db_session,
    )


@pytest.mark.integration
def test_retry_preserves_checkpoint_when_enabled(
    client,
    completed_partial_batch,
):
    session = completed_partial_batch.session
    batch = completed_partial_batch.batch
    city_result = completed_partial_batch.city_result

    # 驗證 fixture 符合 retry endpoint 的前置條件。
    assert batch.status == "failed"
    assert city_result.status == "failed"
    assert city_result.monthly_json is not None
    assert len(city_result.monthly_json) == 1
    assert city_result.completed_month_count == 1
    assert city_result.last_checkpoint_month == 1

    original_monthly_json = (
        city_result.monthly_json.copy()
    )

    response = client.post(
        (
            "/api/v1/global-batches/"
            f"{batch.id}"
            "/retry-failed"
        )
    )

    assert response.status_code == 202, (
        response.text
    )

    session.expire_all()

    refreshed_result = session.get(
        GlobalCityResult,
        city_result.id,
    )

    assert refreshed_result is not None

    # Checkpoint 不應在 retry 時被刪除。
    assert refreshed_result.monthly_json is not None
    assert (
        refreshed_result.monthly_json
        == original_monthly_json
    )
    assert (
        refreshed_result.completed_month_count
        == 1
    )
    assert (
        refreshed_result.last_checkpoint_month
        == 1
    )
    assert (
        refreshed_result.resumed_from_checkpoint
        is True
    )


@pytest.mark.unit
def test_monthly_checkpoint_round_trip():
    sample = DailyAdaptationResult(
        sample_date_local=datetime(
            2025,
            1,
            15,
            12,
        ),
        weight_days=31,
        mean_air_temperature_c=32,
        maximum_air_temperature_c=36,
        mean_solar_radiation_w_m2=500,
        maximum_solar_radiation_w_m2=800,
        exposure_eligible=True,
        beneficial=True,
        average_skin_improvement_c=0.5,
        final_skin_improvement_c=0.6,
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=0.8,
        weather_from_cache=True,
    )

    result = MonthlyAdaptationResult(
        month=1,
        sampled_day_count=1,
        eligible_sample_count=1,
        total_weighted_days=31,
        evaluated_weighted_days=31,
        beneficial_weighted_days=31,
        exposure_coverage_percent=100,
        climate_adaptation_rate_percent=100,
        average_skin_improvement_c=0.5,
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=0.8,
        samples=[sample],
    )

    payload = result.model_dump(
        mode="json"
    )

    restored = (
        MonthlyAdaptationResult
        .model_validate(payload)
    )

    assert restored.month == 1
    assert restored.sampled_day_count == 1
    assert len(restored.samples) == 1