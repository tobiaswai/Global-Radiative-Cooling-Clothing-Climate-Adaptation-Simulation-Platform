import numpy as np
import pytest

from app.schemas.activity import ACTIVITY_PRESETS
from app.schemas.simulation import PersonInput
from app.services.two_node import calculate_fluxes, relative_air_speed_m_s, simulate_material


@pytest.mark.unit
@pytest.mark.parametrize("wind", [0.0, 0.37, 1.5, 6.17])
def test_zero_walking_returns_wind_exactly(wind):
    assert relative_air_speed_m_s(wind, 0.0) == wind


@pytest.mark.unit
def test_relative_speed_is_rms_over_walking_direction():
    wind, walk = 2.0, 1.2
    angle = np.linspace(0.0, 2.0 * np.pi, 200_000, endpoint=False)
    rms = np.sqrt(np.mean((wind - walk * np.cos(angle)) ** 2 + (walk * np.sin(angle)) ** 2))
    assert relative_air_speed_m_s(wind, walk) == pytest.approx(rms, rel=1e-6)


@pytest.mark.unit
def test_walking_in_still_air_raises_evaporative_capacity(environment, person, control_material):
    still = environment.model_copy(update={"wind_speed_m_s": 0.0})
    standing = calculate_fluxes(36.8, 33.7, still, person, control_material)
    walking = calculate_fluxes(36.8, 33.7, still, person.model_copy(update={"walking_speed_m_s": 1.11}), control_material)
    assert walking.maximum_evaporation > standing.maximum_evaporation


@pytest.mark.unit
def test_walking_is_recorded(environment, person, control_material):
    result = simulate_material(30, 5, environment, person.model_copy(update={"walking_speed_m_s": 1.0}), control_material)
    assert result.body.walking_speed_m_s == 1.0
    assert any("walking" in note for note in result.assumptions_applied)


@pytest.mark.unit
def test_presets_are_valid_person_inputs():
    for preset in ACTIVITY_PRESETS.values():
        PersonInput(met=preset.met, walking_speed_m_s=preset.walking_speed_m_s)