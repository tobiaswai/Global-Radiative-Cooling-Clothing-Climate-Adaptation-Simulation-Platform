from types import SimpleNamespace

import pytest

from app.api import simulations as simulations_api


@pytest.mark.integration
def test_material_library_round_trip(client, monkeypatch, simulation_request):
    created = client.post(
        "/api/v1/materials",
        json={
            "name": "PR-4 Test Fabric",
            "slug": "pr-4-test-fabric",
            "institution": "Test Lab",
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "evaporative_resistance_m2pa_w": 18.0,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
                "source_type": "measured",
                "parameter_sources": {
                    "solar_reflectance": {
                        "source_type": "measured",
                        "reference": "UV-Vis-NIR, 2024-03",
                    }
                },
            },
        },
    )
    assert created.status_code == 201, created.text
    version_id = created.json()["versions"][0]["id"]

    listing = client.get("/api/v1/materials/versions").json()
    assert any(item["id"] == version_id for item in listing["items"])

    simulation_input = client.get(
        f"/api/v1/materials/versions/{version_id}/simulation-input"
    ).json()
    assert simulation_input["name"] == "PR-4 Test Fabric v1"
    assert simulation_input["material_version_id"] == version_id

    # Hydration: only the id is sent.
    body = simulation_request.model_dump(mode="json")
    body["rc_material"] = {"name": "RC from library", "material_version_id": version_id}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 200, response.text
    rc = response.json()["radiative_cooling"]
    assert rc["material_name"] == "RC from library"
    assert rc["clothing"]["evaporative_resistance_source"] == "material_input"
    assert rc["clothing"]["evaporative_resistance_m2pa_w"] == pytest.approx(18.0)

    # Conflict: id plus a different value.
    body["rc_material"] = {"name": "Edited", "material_version_id": version_id, "solar_reflectance": 0.5}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MATERIAL_PARAMETER_CONFLICT"

    # Unknown id.
    body["rc_material"] = {"name": "Ghost", "material_version_id": "does-not-exist"}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MATERIAL_VERSION_NOT_FOUND"

    # Job link is recorded and queryable.
    monkeypatch.setattr(
        simulations_api,
        "run_weather_simulation_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-test-task")),
    )
    job = client.post(
        "/api/v1/simulations/jobs",
        json={
            "city_id": "dubai",
            "start_time_local": "2023-07-15T12:00:00",
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "person": body["person"],
            "control_material": body["control_material"],
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert job.status_code == 202, job.text
    assert job.json()["rc_material_version_id"] == version_id
    assert job.json()["control_material_version_id"] is None

    detail = client.get(f"/api/v1/simulations/jobs/{job.json()['id']}").json()
    assert detail["request"]["rc_material"]["solar_reflectance"] == pytest.approx(0.92)

    listed = client.get("/api/v1/simulations/jobs", params={"material_version_id": version_id}).json()
    assert any(item["id"] == job.json()["id"] for item in listed["items"])


@pytest.mark.integration
def test_version_with_unknown_provenance_key_is_rejected_on_write(client):
    response = client.post(
        "/api/v1/materials",
        json={
            "name": "Bad provenance",
            "slug": "bad-provenance",
            "initial_version": {"parameter_sources": {"not_a_field": {"source_type": "measured"}}},
        },
    )
    assert response.status_code == 422