import math

import pytest
from pythermalcomfort.models import two_nodes_gagge

from app.services.gagge_reference import run_gagge_reference


PARITY_TOLERANCE_C = 0.05

CASES = [
    # tdb, tr, v, rh, met, clo
    (38.0, 45.0, 1.5, 40.0, 2.6, 0.5),
    (30.0, 30.0, 0.3, 60.0, 1.2, 0.6),
    (42.0, 42.0, 2.0, 20.0, 2.0, 0.4),
    (34.0, 36.0, 1.0, 85.0, 1.8, 0.5),
    (25.0, 25.0, 0.1, 50.0, 1.0, 1.0),
]


@pytest.mark.benchmark
@pytest.mark.parametrize(("tdb", "tr", "v", "rh", "met", "clo"), CASES)
def test_port_matches_library_after_sixty_minutes(tdb, tr, v, rh, met, clo):
    library = two_nodes_gagge(
        tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo, wme=0,
        body_surface_area=1.8, p_atm=101325, position="standing",
        max_skin_blood_flow=90, max_sweating=500, round_output=False,
    )

    port = run_gagge_reference(
        tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo,
        body_surface_area=1.8, body_mass_kg=70.0, duration_minutes=60,
    ).final

    assert port.core_temperature_c == pytest.approx(
        float(library.t_core), abs=PARITY_TOLERANCE_C
    )
    assert port.skin_temperature_c == pytest.approx(
        float(library.t_skin), abs=PARITY_TOLERANCE_C
    )
    assert port.skin_wettedness == pytest.approx(float(library.w), abs=0.02)


@pytest.mark.unit
def test_port_returns_one_point_per_minute_plus_initial_state():
    result = run_gagge_reference(
        tdb=38.0, tr=45.0, v=1.5, rh=40.0, met=2.6, clo=0.5, duration_minutes=90
    )

    assert len(result.points) == 91
    assert result.points[0].minute == 0
    assert result.points[0].skin_temperature_c == 33.7
    assert result.points[-1].minute == 90
    assert all(math.isfinite(p.core_temperature_c) for p in result.points)


@pytest.mark.unit
def test_heavier_body_warms_more_slowly():
    light = run_gagge_reference(
        tdb=40.0, tr=40.0, v=0.5, rh=40.0, met=2.0, clo=0.5, body_mass_kg=55.0
    ).final
    heavy = run_gagge_reference(
        tdb=40.0, tr=40.0, v=0.5, rh=40.0, met=2.0, clo=0.5, body_mass_kg=95.0
    ).final

    assert heavy.core_temperature_c < light.core_temperature_c