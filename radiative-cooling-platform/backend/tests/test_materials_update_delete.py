"""Material metadata update (PATCH) and delete (DELETE)."""

from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.api import simulations as simulations_api


def create_material(client) -> dict:
    suffix = uuid4().hex[:8]
    response = client.post(
        "/api/v1/materials",
        json={
            "name": f"Edit Fabric {suffix}",
            "slug": f"edit-fabric-{suffix}",
            "description": "original",
            "institution": "Test Lab",
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
            },
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


@pytest.mark.integration
def test_patch_changes_only_given_fields(client):
    material = create_material(client)

    response = client.patch(
        f"/api/v1/materials/{material['id']}", json={"description": "  updated  "}
    )

    assert response.status_code == 200, response.text
    body = response.json()
    assert body["description"] == "updated"
    assert body["name"] == material["name"]
    assert body["institution"] == "Test Lab"
    assert len(body["versions"]) == 1


@pytest.mark.integration
def test_patch_clears_optional_text_with_blank(client):
    material = create_material(client)
    body = client.patch(
        f"/api/v1/materials/{material['id']}", json={"institution": "   "}
    ).json()
    assert body["institution"] is None


@pytest.mark.integration
@pytest.mark.parametrize(
    "payload",
    [{"name": None}, {"name": "   "}, {"is_archived": None}, {"slug": "renamed"}],
)
def test_patch_rejects_invalid_payload(client, payload):
    material = create_material(client)
    response = client.patch(f"/api/v1/materials/{material['id']}", json=payload)
    assert response.status_code == 422


@pytest.mark.integration
def test_patch_and_delete_missing_material_return_404(client):
    assert client.patch("/api/v1/materials/nope", json={"name": "x"}).status_code == 404
    assert client.delete("/api/v1/materials/nope").status_code == 404


@pytest.mark.integration
def test_unreferenced_material_is_deleted_with_its_versions(client):
    material = create_material(client)
    version_id = material["versions"][0]["id"]

    response = client.delete(f"/api/v1/materials/{material['id']}")

    assert response.status_code == 204
    assert client.get(f"/api/v1/materials/{material['id']}").status_code == 404
    assert client.get(
        f"/api/v1/materials/versions/{version_id}/simulation-input"
    ).status_code == 404


@pytest.mark.integration
def test_referenced_material_cannot_be_deleted_but_can_be_archived(
    client, monkeypatch, simulation_request
):
    material = create_material(client)
    version_id = material["versions"][0]["id"]

    monkeypatch.setattr(
        simulations_api,
        "run_weather_simulation_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-test-task")),
    )
    base = simulation_request.model_dump(mode="json")
    job = client.post(
        "/api/v1/simulations/jobs",
        json={
            "city_id": "dubai",
            "start_time_local": "2023-07-15T12:00:00",
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "person": base["person"],
            "control_material": base["control_material"],
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert job.status_code == 202, job.text

    blocked = client.delete(f"/api/v1/materials/{material['id']}")
    assert blocked.status_code == 409
    detail = blocked.json()["detail"]
    assert detail["code"] == "MATERIAL_IN_USE"
    assert detail["simulation_job_count"] == 1
    assert detail["global_batch_count"] == 0
    assert client.get(f"/api/v1/materials/{material['id']}").status_code == 200

    archived = client.patch(
        f"/api/v1/materials/{material['id']}", json={"is_archived": True}
    )
    assert archived.status_code == 200
    assert archived.json()["is_archived"] is True

    hidden = client.get("/api/v1/materials", params={"search": material["name"]}).json()
    assert all(item["id"] != material["id"] for item in hidden["items"])

    shown = client.get(
        "/api/v1/materials",
        params={"search": material["name"], "include_archived": "true"},
    ).json()
    assert any(item["id"] == material["id"] for item in shown["items"])

    picker = client.get(
        "/api/v1/materials/versions", params={"material_id": material["id"]}
    ).json()
    assert picker["items"] == []