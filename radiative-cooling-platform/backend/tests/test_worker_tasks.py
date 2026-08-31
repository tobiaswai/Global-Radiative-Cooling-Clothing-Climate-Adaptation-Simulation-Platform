from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.models.simulation_job import (
    SimulationJob,
)
from app.worker import tasks


def make_session_context(session):
    context = MagicMock()
    context.__enter__.return_value = session
    context.__exit__.return_value = False

    return context


@pytest.mark.unit
def test_update_job_updates_fields_and_commits(
    monkeypatch,
):
    job = SimpleNamespace(
        status="queued",
        stage="queued",
        progress=0,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    tasks.update_job(
        "job-123",
        status="running",
        stage="initializing",
        progress=10,
    )

    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )

    assert job.status == "running"
    assert job.stage == "initializing"
    assert job.progress == 10

    session.commit.assert_called_once_with()


@pytest.mark.unit
def test_update_job_rejects_missing_job(
    monkeypatch,
):
    session = MagicMock()
    session.get.return_value = None

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        RuntimeError,
        match="Simulation task not found:job-404",
    ):
        tasks.update_job(
            "job-404",
            status="running",
        )

    session.commit.assert_not_called()


@pytest.mark.unit
@pytest.mark.parametrize(
    "status",
    [
        "queued",
        "running",
        "completed",
        "failed",
    ],
)
def test_ensure_not_cancelled_accepts_active_status(
    monkeypatch,
    status,
):
    job = SimpleNamespace(
        status=status,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    tasks.ensure_not_cancelled("job-123")

    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "status",
    [
        "cancelling",
        "cancelled",
    ],
)
def test_ensure_not_cancelled_raises_for_cancelled_job(
    monkeypatch,
    status,
):
    job = SimpleNamespace(
        status=status,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        tasks.JobCancelledError,
    ):
        tasks.ensure_not_cancelled(
            "job-123"
        )


@pytest.mark.unit
def test_ensure_not_cancelled_rejects_missing_job(
    monkeypatch,
):
    session = MagicMock()
    session.get.return_value = None

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        RuntimeError,
        match="Simulation task not found:job-404",
    ):
        tasks.ensure_not_cancelled(
            "job-404"
        )