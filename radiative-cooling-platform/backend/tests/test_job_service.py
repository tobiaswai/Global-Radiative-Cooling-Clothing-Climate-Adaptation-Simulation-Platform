from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.models.simulation_job import (
    SimulationJob,
)
from app.services.job_service import (
    get_job_or_none,
    job_to_detail,
    job_to_response,
)


def make_job(
    *,
    simulation_request,
):
    now = datetime.now(timezone.utc)

    return SimpleNamespace(
        id="job-123",
        celery_task_id="task-456",
        status="completed",
        stage="completed",
        progress=100,
        city_id="dubai",
        summary_json={
            "final_skin_temperature_improvement_c": 1.2,
        },
        error_message=None,
        request_json={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
            "output_interval_minutes": 1,
            "person": (
                simulation_request
                .person.model_dump(
                    mode="json"
                )
            ),
            "control_material": (
                simulation_request
                .control_material.model_dump(
                    mode="json"
                )
            ),
            "rc_material": (
                simulation_request
                .rc_material.model_dump(
                    mode="json"
                )
            ),
        },
        created_at=now,
        updated_at=now,
        started_at=now,
        completed_at=now,
    )


@pytest.mark.unit
def test_job_to_response_maps_job_fields(
    simulation_request,
):
    job = make_job(
        simulation_request=simulation_request,
    )

    response = job_to_response(job)

    assert response.id == "job-123"
    assert response.celery_task_id == "task-456"
    assert response.status == "completed"
    assert response.stage == "completed"
    assert response.progress == 100
    assert response.city_id == "dubai"
    assert response.error_message is None
    assert response.summary == {
        "final_skin_temperature_improvement_c": 1.2,
    }


@pytest.mark.unit
def test_job_to_detail_validates_saved_request(
    simulation_request,
):
    job = make_job(
        simulation_request=simulation_request,
    )

    detail = job_to_detail(job)

    assert detail.id == "job-123"
    assert detail.request.city_id == "dubai"
    assert (
        detail.request.duration_minutes
        == 120
    )
    assert (
        detail.request.person.met
        == simulation_request.person.met
    )
    assert (
        detail.request.control_material.name
        == simulation_request
        .control_material.name
    )


@pytest.mark.unit
def test_get_job_or_none_uses_session_get():
    expected_job = object()
    session = Mock()
    session.get.return_value = expected_job

    result = get_job_or_none(
        session=session,
        job_id="job-123",
    )

    assert result is expected_job
    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )


@pytest.mark.unit
def test_get_job_or_none_returns_none():
    session = Mock()
    session.get.return_value = None

    result = get_job_or_none(
        session=session,
        job_id="missing-job",
    )

    assert result is None