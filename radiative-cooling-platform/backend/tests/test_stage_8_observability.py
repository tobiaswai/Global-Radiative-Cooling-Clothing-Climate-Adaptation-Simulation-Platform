from datetime import timedelta
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.api import ops as ops_api
from app.core.time import utc_now
from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult  
from app.schemas.global_batch import GlobalBatchCreate,MaterialInput,PersonInput
from app.schemas.ops import WorkerStatus
from app.services.checkpoints import load_resume_state
from app.services.global_batch_service import batch_progress_event, derive_lease_state
from app.services.job_state import BatchStatus, derive_batch_status
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)



# --------------------------------------------------------------------------
# unit
# --------------------------------------------------------------------------
def make_request_json(city_id: str, *, start_month: int = 7, end_month: int = 12) -> dict:
    """Complete, schema-valid request so GlobalBatchDetail can re-validate it."""
    request = GlobalBatchCreate(
        city_ids=[city_id],
        year=2023,
        start_month=start_month,
        end_month=end_month,
        duration_minutes=120,
        output_interval_minutes=10,
        minimum_skin_improvement_c=0.2,
        person=PersonInput(
            met=2.0,
            body_surface_area_m2=1.8,
            local_start_hour=12,
            initial_core_temperature_c=36.8,
            initial_skin_temperature_c=33.7,
        ),
        control_material=MaterialInput(
            name="Control",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.3,
            solar_transmittance=0,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
        ),
        rc_material=MaterialInput(
            name="RC",
            clothing_insulation_clo=0.4,
            solar_reflectance=0.92,
            solar_transmittance=0,
            infrared_emissivity=0.95,
            projected_solar_area_factor=0.25,
        ),
    )
    return request.model_dump(mode="json")

@pytest.mark.unit
def test_lease_state_is_derived_server_side():
    now = utc_now()
    assert derive_lease_state(None, None, now) == "none"
    assert derive_lease_state("w", None, now) == "none"
    assert derive_lease_state("w", now + timedelta(seconds=30), now) == "live"
    assert derive_lease_state("w", now - timedelta(seconds=1), now) == "expired"


@pytest.mark.unit
def test_progress_event_is_lightweight_and_carries_checkpoint_months():
    now = utc_now()
    city = SimpleNamespace(
        id="c1", city_id="dubai", status="running", stage="analyzing", progress=40,
        retry_count=1, completed_month_count=4, last_checkpoint_month=4,
        last_heartbeat_at=now, lease_owner="host:1:task", lease_expires_at=now + timedelta(minutes=2),
        error_message=None,
    )
    batch = SimpleNamespace(
        id="b1", celery_group_id=None, status="running", stage="analyzing_cities", progress=40,
        total_city_count=1, completed_city_count=0, failed_city_count=0, cancelled_city_count=0,
        summary_json=None, error_message=None, created_at=now, updated_at=now,
        started_at=now, completed_at=None, attempt=1, lease_owner=None, lease_expires_at=None,
        last_heartbeat_at=None, cancel_requested_at=None, city_results=[city],
    )

    event = batch_progress_event(batch, {"c1": [1, 2, 3, 4]})

    assert event.batch.attempt == 1
    assert event.cities[0].lease_state == "live"
    assert event.cities[0].checkpoint_months == [1, 2, 3, 4]
    assert "monthly_results" not in event.cities[0].model_dump()


@pytest.mark.unit
def test_derive_batch_status_matches_refresh_rules():
    assert derive_batch_status({"completed": 1}, 2, False) is None
    assert derive_batch_status({"completed": 2}, 2, False) == BatchStatus.COMPLETED
    assert derive_batch_status({"completed": 1, "failed": 1}, 2, False) == BatchStatus.PARTIAL_COMPLETED
    assert derive_batch_status({"failed": 2}, 2, False) == BatchStatus.FAILED
    assert derive_batch_status({"cancelled": 2}, 2, True) == BatchStatus.CANCELLED
    assert derive_batch_status({"completed": 1, "cancelled": 1}, 2, True) == BatchStatus.PARTIAL_COMPLETED


# --------------------------------------------------------------------------
# integration (PostgreSQL via the db_session / client fixtures)
# --------------------------------------------------------------------------

def seed_batch(session, *, start_month=7, end_month=12, checkpoint_months=(7, 8, 10)):
    batch = GlobalBatchJob(
        id=str(uuid4()), status="running", stage="analyzing_cities", progress=10,
        total_city_count=1, attempt=1, request_json=make_request_json("dubai"),
    )
    session.add(batch)
    session.flush()

    city = GlobalCityResult(
        id=str(uuid4()), batch_id=batch.id, city_id="dubai", city_name="Dubai",
        country="United Arab Emirates", latitude=25.2, longitude=55.27,
        status="running", stage="analyzing", progress=30,
        lease_owner="host:1:task", lease_expires_at=utc_now() + timedelta(minutes=2),
        last_heartbeat_at=utc_now(),
    )
    session.add(city)
    session.flush()

    for month in checkpoint_months:
        session.add(GlobalCityCheckpoint(
            city_result_id=city.id, month=month, attempt=0,
            payload_json={"month": month, "sampled_day_count": 3, "skipped_samples": [], "samples": []},
        ))
    session.commit()
    return batch, city


@pytest.mark.integration
def test_resume_prefix_respects_start_month(db_session):
    _, city = seed_batch(db_session, start_month=7, checkpoint_months=(7, 8, 10))

    next_month, payloads = load_resume_state(db_session, city.id, start_month=7)

    assert next_month == 9                       # hole at 9 -> resume there, discard 10
    assert [p["month"] for p in payloads] == [7, 8]


@pytest.mark.integration
def test_detail_and_checkpoint_endpoints_expose_stage_7_state(client, db_session):
    batch, city = seed_batch(db_session)

    detail = client.get(f"/api/v1/global-batches/{batch.id}").json()
    row = detail["city_results"][0]
    assert detail["attempt"] == 1
    assert row["lease_state"] == "live"
    assert row["lease_owner"] == "host:1:task"
    assert row["checkpoint_months"] == [7, 8, 10]

    checkpoints = client.get(
        f"/api/v1/global-batches/{batch.id}/cities/{city.id}/checkpoints"
    ).json()
    assert checkpoints["start_month"] == 7
    assert checkpoints["resume_from_month"] == 9
    assert [item["month"] for item in checkpoints["items"]] == [7, 8, 10]
    assert len(checkpoints["items"][0]["payload_sha256"]) == 64

    assert client.get(
        f"/api/v1/global-batches/{batch.id}/cities/does-not-exist/checkpoints"
    ).status_code == 404


@pytest.mark.integration
def test_ops_status_reports_workers_and_leases(client, db_session, monkeypatch):
    seed_batch(db_session)
    monkeypatch.setattr(
        ops_api, "inspect_workers",
        lambda timeout=1.0: (True, [WorkerStatus(name="w1@host", active_task_count=1, reserved_task_count=0)]),
    )

    body = client.get("/api/v1/ops/status").json()

    assert body["broker_reachable"] is True
    assert body["worker_count"] == 1
    assert body["leases"]["running_cities"] >= 1
    assert body["leases"]["live_leases"] >= 1
    assert body["worst_case_recovery_seconds"] == body["lease_ttl_seconds"] + body["reaper_interval_seconds"]


@pytest.mark.integration
def test_ops_status_survives_broker_outage(client, monkeypatch):
    def broken_inspect(timeout=1.0):
        raise ConnectionError("redis down")

    # inspect_workers wraps exceptions itself; emulate by patching the Celery call.
    monkeypatch.setattr(ops_api.celery_app.control, "inspect", broken_inspect)

    body = client.get("/api/v1/ops/status").json()
    assert body["broker_reachable"] is False
    assert body["workers"] == []