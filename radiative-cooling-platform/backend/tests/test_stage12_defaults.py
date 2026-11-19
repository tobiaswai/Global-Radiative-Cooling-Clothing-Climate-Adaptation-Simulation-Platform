from datetime import datetime

import pytest

from app.schemas.environment import EnvironmentAssumptions, preset_assumptions
from app.schemas.simulation import MaterialInput, PersonInput, WeatherSimulationRequest
from app.services.stored_requests import load_stored_request
from tests.helpers.environment import LEGACY


@pytest.mark.unit
def test_default_is_open_ground_physical():
    assert EnvironmentAssumptions() == preset_assumptions("open_ground_physical")
    assert EnvironmentAssumptions().mean_radiant_temperature_method == "ground_energy_balance"


@pytest.mark.unit
def test_unknown_preset_is_rejected():
    with pytest.raises(ValueError):
        preset_assumptions("tropical_canyon")


@pytest.mark.unit
def test_pre_stage2_request_loads_as_legacy():
    material = MaterialInput(name="m")
    payload = WeatherSimulationRequest(
        start_time_local=datetime(2023, 7, 15, 12), person=PersonInput(),
        control_material=material, rc_material=material,
    ).model_dump(mode="json")
    payload.pop("environment_assumptions")
    assert load_stored_request(WeatherSimulationRequest, payload).environment_assumptions == LEGACY


@pytest.mark.unit
def test_explicit_stored_assumptions_are_kept():
    material = MaterialInput(name="m")
    payload = WeatherSimulationRequest(
        start_time_local=datetime(2023, 7, 15, 12), person=PersonInput(),
        control_material=material, rc_material=material,
        environment_assumptions=EnvironmentAssumptions(),
    ).model_dump(mode="json")
    loaded = load_stored_request(WeatherSimulationRequest, payload)
    assert loaded.environment_assumptions.mean_radiant_temperature_method == "ground_energy_balance"