"""Regression: material library links must be persisted for global batches."""

from types import SimpleNamespace

import pytest

from app.api import global_batches as global_batches_api


def fake_submit_city_tasks(*, city_results, queue_name):
    return SimpleNamespace(
        id="group-test",
        results=[
            SimpleNamespace(id=f"task-{result.city_id}") for result in city_results
        ],
    )


@pytest.mark.integration
def test_global_batch_records_material_version_links(
    client, monkeypatch, person, control_material
):
    monkeypatch.setattr(
        global_batches_api, "submit_city_tasks", fake_submit_city_tasks
    )

    created = client.post(
        "/api/v1/materials",
        json={
            "name": "Batch Link Fabric",
            "slug": "batch-link-fabric",
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
            },
        },
    )
    assert created.status_code == 201, created.text
    version_id = created.json()["versions"][0]["id"]

    response = client.post(
        "/api/v1/global-batches",
        json={
            "city_ids": ["dubai"],
            "year": 2023,
            "start_month": 7,
            "end_month": 7,
            "person": person.model_dump(mode="json"),
            "control_material": control_material.model_dump(mode="json"),
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert response.status_code == 202, response.text

    body = response.json()
    assert body["rc_material_version_id"] == version_id
    assert body["control_material_version_id"] is None
    assert body["celery_group_id"] == "group-test"

    detail = client.get(f"/api/v1/global-batches/{body['id']}").json()
    assert detail["request"]["rc_material"]["solar_reflectance"] == pytest.approx(0.92)
    assert detail["city_results"][0]["celery_task_id"] == "task-dubai"