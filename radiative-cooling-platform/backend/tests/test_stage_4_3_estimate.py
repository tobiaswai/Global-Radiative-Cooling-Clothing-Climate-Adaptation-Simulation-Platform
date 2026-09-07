import pytest


@pytest.mark.api
def test_daily_batch_estimate(
    client,
    person,
    control_material,
    rc_material,
):
    response = client.post(
        "/api/v1/global-batches/estimate",
        json={
            "name": "Daily estimate",
            "city_ids": [
                "dubai",
                "singapore",
            ],
            "year": 2024,
            "start_month": 1,
            "end_month": 12,
            "analysis_resolution": "daily",
            "daily_stride_days": 1,
            "sample_days_per_month": 3,
            "local_start_hour": 12,
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "minimum_skin_improvement_c": 0.2,
            "minimum_air_temperature_c": 30,
            "minimum_solar_radiation_w_m2": 300,
            "exposure_match_mode": "all",
            "person": person.model_dump(mode="json"),
            "control_material": control_material.model_dump(mode="json"),
            "rc_material": rc_material.model_dump(mode="json"),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["samples_per_city"] == 366
    assert data["total_samples"] == 732
    assert (
        data["thermal_simulation_count"]
        == 1464
    )
    assert (
        data["estimated_weather_requests"]
        == 24
    )