from contextlib import nullcontext
from datetime import timedelta
from importlib.util import find_spec
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.core.time import utc_now
from app.models.global_batch import GlobalBatchJob, GlobalCityResult
from app.schemas.environment import EnvironmentAssumptions
from app.schemas.global_batch import GlobalBatchCreate
from app.services import model_parameters as mp
from app.services.global_batch_export import build_readme_text
from app.worker import tasks


@pytest.mark.integration
def test_reaper_requeues_city_on_its_batch_queue(db_session, monkeypatch, person, control_material, rc_material):
    request = GlobalBatchCreate(city_ids=["dubai"], execution_profile="large", person=person,
                                control_material=control_material, rc_material=rc_material)
    batch = GlobalBatchJob(id=str(uuid4()), status="running", stage="analyzing_cities", progress=0,
                           total_city_count=1, request_json=request.model_dump(mode="json"))
    db_session.add(batch)
    db_session.flush()
    city = GlobalCityResult(id=str(uuid4()), batch_id=batch.id, city_id="dubai", city_name="Dubai",
                            country="UAE", latitude=25.2, longitude=55.3, status="running", stage="x",
                            progress=10, retry_count=0, lease_owner="dead",
                            lease_expires_at=utc_now() - timedelta(minutes=10))
    db_session.add(city)
    db_session.commit()

    calls: list[dict] = []
    monkeypatch.setattr(tasks, "SessionLocal", lambda: nullcontext(db_session))
    monkeypatch.setattr(tasks.run_global_city_analysis_task, "apply_async", lambda **kw: calls.append(kw))

    tasks.reap_expired_leases()

    assert calls == [{"args": [city.id], "queue": "global_large"}]


@pytest.mark.unit
def test_readme_reports_stored_environment():
    physical = SimpleNamespace(id="b", status="completed",
                               request_json={"environment_assumptions": EnvironmentAssumptions().model_dump(mode="json")})
    legacy = SimpleNamespace(id="b", status="completed", request_json={})
    assert "ground_energy_balance / brutsaert_cloud" in build_readme_text(physical)
    assert "air_plus_solar_linear / humidity_offset" in build_readme_text(legacy)


@pytest.mark.unit
def test_parameter_set_version_matches_adr_0008():
    assert mp.MODEL_PARAMETER_SET_VERSION == "6.0.0"
    assert "brutsaert_coefficient" in mp.MODEL_PARAMETERS


@pytest.mark.unit
def test_stale_environment_module_is_removed():
    assert find_spec("app.services.environment") is None