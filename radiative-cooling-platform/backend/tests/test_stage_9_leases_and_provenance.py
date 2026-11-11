"""Stage 9: single-job leases, owner-guarded checkpoint writes, provenance."""

from datetime import datetime, timedelta
from uuid import uuid4

import pytest
from sqlalchemy import select

from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult
from app.models.simulation_job import SimulationJob
from app.schemas.global_batch import GlobalBatchCreate
from app.services.checkpoints import CheckpointProvenance, load_resume_state, upsert_month_checkpoint
from app.services.job_state import IllegalTransition, assert_city_transition, assert_job_transition
from app.services.leases import (
    acquire_city_lease,
    acquire_job_lease,
    heartbeat_city_lease,
    heartbeat_job_lease,
)
from tests.test_stage_8_observability import make_request_json


# --- unit ---------------------------------------------------------------

@pytest.mark.unit
def test_job_transitions():
    assert_job_transition("queued", "running")
    assert_job_transition("running", "queued")      # reaper
    assert_job_transition("cancelling", "completed")
    for current in ("completed", "failed", "cancelled"):
        with pytest.raises(IllegalTransition):
            assert_job_transition(current, "running")


@pytest.mark.unit
def test_failed_city_may_be_retried():
    assert_city_transition("failed", "queued")
    with pytest.raises(IllegalTransition):
        assert_city_transition("completed", "queued")


@pytest.mark.unit
def test_request_hash_ignores_non_physics_fields():
    base = GlobalBatchCreate.model_validate(make_request_json("dubai"))
    renamed = base.model_copy(update={"name": "other", "resume_from_checkpoint": False, "execution_profile": "large"})
    changed = base.model_copy(update={"duration_minutes": 60})

    assert CheckpointProvenance.for_request(base) == CheckpointProvenance.for_request(renamed)
    assert CheckpointProvenance.for_request(base) != CheckpointProvenance.for_request(changed)


# --- integration ----------------------------------------------------------

def seed_job(session, **overrides) -> SimulationJob:
    values = {
        "id": str(uuid4()), "city_id": "dubai", "status": "queued",
        "stage": "queued", "progress": 0, "request_json": {},
    }
    values.update(overrides)
    job = SimulationJob(**values)
    session.add(job)
    session.commit()
    return job


@pytest.mark.integration
def test_job_lease_is_exclusive_and_terminal_rows_cannot_be_acquired(db_session):
    job = seed_job(db_session)

    assert acquire_job_lease(db_session, job.id, "worker-a") is True
    assert acquire_job_lease(db_session, job.id, "worker-b") is False   # live lease
    assert acquire_job_lease(db_session, job.id, "worker-a") is True    # re-entrant

    db_session.refresh(job)
    assert job.status == "running"

    done = seed_job(db_session, status="completed")
    assert acquire_job_lease(db_session, done.id, "worker-a") is False  # never resurrect


@pytest.mark.integration
def test_job_heartbeat_by_non_owner_is_rejected_and_rolled_back(db_session):
    job = seed_job(db_session)
    acquire_job_lease(db_session, job.id, "worker-a")

    assert heartbeat_job_lease(db_session, job.id, "worker-b", progress=50) is False
    db_session.refresh(job)
    assert job.progress == 0
    assert job.lease_owner == "worker-a"


def seed_city(session, *, start_month=7, end_month=12):
    batch = GlobalBatchJob(
        id=str(uuid4()), status="running", stage="analyzing_cities", progress=0,
        total_city_count=1, request_json=make_request_json("dubai", start_month=start_month, end_month=end_month),
    )
    session.add(batch)
    session.flush()
    city = GlobalCityResult(
        id=str(uuid4()), batch_id=batch.id, city_id="dubai", city_name="Dubai",
        country="United Arab Emirates", latitude=25.2, longitude=55.27,
        status="queued", stage="queued", progress=0,
    )
    session.add(city)
    session.commit()
    return batch, city


@pytest.mark.integration
def test_checkpoint_write_requires_lease_and_rolls_back_with_lost_heartbeat(db_session):
    batch, city = seed_city(db_session)
    city_id = city.id
    request = GlobalBatchCreate.model_validate(batch.request_json)
    provenance = CheckpointProvenance.for_request(request)
    payload = {"month": 7, "sampled_day_count": 1, "skipped_samples": [], "samples": []}

    # No lease at all: nothing staged.
    assert upsert_month_checkpoint(
        db_session, city_result_id=city_id, owner="ghost", month=7, attempt=0,
        payload=payload, provenance=provenance,
    ) is False

    acquire_city_lease(db_session, city_id, "worker-a")

    # Staged by the owner but the heartbeat is attempted by someone else:
    # the rollback must discard the staged row.
    assert upsert_month_checkpoint(
        db_session, city_result_id=city_id, owner="worker-a", month=7, attempt=0,
        payload=payload, provenance=provenance,
    ) is True
    assert heartbeat_city_lease(db_session, city_id, "worker-b", last_checkpoint_month=7) is False
    assert db_session.scalar(select(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == city_id)) is None

    # Owner path: row and heartbeat land together.
    assert upsert_month_checkpoint(
        db_session, city_result_id=city_id, owner="worker-a", month=7, attempt=0,
        payload=payload, provenance=provenance,
    ) is True
    assert heartbeat_city_lease(db_session, city_id, "worker-a", last_checkpoint_month=7) is True
    row = db_session.scalar(select(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == city_id))
    assert row.model_version == provenance.model_version
    assert row.parameter_fingerprint == provenance.parameter_fingerprint


@pytest.mark.integration
def test_resume_discards_rows_with_foreign_provenance(db_session):
    batch, city = seed_city(db_session)
    request = GlobalBatchCreate.model_validate(batch.request_json)
    good = CheckpointProvenance.for_request(request)

    def add(month, **override):
        db_session.add(GlobalCityCheckpoint(
            city_result_id=city.id, month=month, attempt=0,
            payload_json={"month": month, "sampled_day_count": 1, "skipped_samples": [], "samples": []},
            model_version=override.get("model_version", good.model_version),
            parameter_fingerprint=override.get("parameter_fingerprint", good.parameter_fingerprint),
            request_sha256=override.get("request_sha256", good.request_sha256),
        ))

    add(7)
    add(8)
    add(9, model_version="0.0.1")   # written by an older model
    add(10)                          # valid, but behind the mismatch
    add(11, model_version=None, parameter_fingerprint=None, request_sha256=None)  # legacy
    db_session.commit()

    state = load_resume_state(db_session, city.id, start_month=7, provenance=good)

    assert state.next_month == 9
    assert [p["month"] for p in state.payloads] == [7, 8]
    assert [d["month"] for d in state.discarded] == [9, 10, 11]
    assert "model_version" in state.discarded[0]["reason"]
    assert "not contiguous" in state.discarded[1]["reason"]
    assert "legacy" in state.discarded[2]["reason"]


@pytest.mark.integration
def test_retry_without_resume_deletes_checkpoint_rows(client, db_session):
    batch, city = seed_city(db_session)
    request = GlobalBatchCreate.model_validate(batch.request_json)
    provenance = CheckpointProvenance.for_request(request)
    db_session.add(GlobalCityCheckpoint(
        city_result_id=city.id, month=7, attempt=0,
        payload_json={"month": 7, "sampled_day_count": 1, "skipped_samples": [], "samples": []},
        model_version=provenance.model_version,
        parameter_fingerprint=provenance.parameter_fingerprint,
        request_sha256=provenance.request_sha256,
    ))
    batch.status = "failed"
    batch.request_json = {**batch.request_json, "resume_from_checkpoint": False}
    city.status = "failed"
    db_session.commit()

    from app.api import global_batches as api
    from types import SimpleNamespace
    api_submit = lambda *, city_results, queue_name: SimpleNamespace(  # noqa: E731
        id="g", results=[SimpleNamespace(id=f"t-{r.city_id}") for r in city_results]
    )
    original = api.submit_city_tasks
    api.submit_city_tasks = api_submit
    try:
        response = client.post(f"/api/v1/global-batches/{batch.id}/retry-failed")
    finally:
        api.submit_city_tasks = original

    assert response.status_code == 202, response.text
    db_session.expire_all()
    assert db_session.scalar(select(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == city.id)) is None
    assert db_session.get(GlobalCityResult, city.id).status == "queued"