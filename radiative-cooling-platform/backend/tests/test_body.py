import pytest

from app.schemas.simulation import PersonInput
from app.services.body import body_heat_capacities


@pytest.mark.unit
def test_default_person_reproduces_gagge_lumped_value():
    capacities = body_heat_capacities(PersonInput())

    # 3490 * 70 / 1.8 = 135 722 J/(m^2 K); alpha = 0.1
    assert capacities.total_j_m2k == pytest.approx(135_722.2, abs=0.5)
    assert capacities.skin_j_m2k == pytest.approx(13_572.2, abs=0.5)
    assert capacities.core_j_m2k == pytest.approx(122_150.0, abs=0.5)


@pytest.mark.unit
def test_heavier_person_has_larger_capacity_per_area():
    light = body_heat_capacities(PersonInput(body_mass_kg=55.0))
    heavy = body_heat_capacities(PersonInput(body_mass_kg=95.0))

    assert heavy.total_j_m2k > light.total_j_m2k


@pytest.mark.unit
def test_larger_surface_area_lowers_capacity_per_area():
    small = body_heat_capacities(PersonInput(body_surface_area_m2=1.6))
    large = body_heat_capacities(PersonInput(body_surface_area_m2=2.2))

    assert large.total_j_m2k < small.total_j_m2k