import math

import pytest

from app.services.two_node import simulate_material


@pytest.mark.unit
def test_simulation_returns_expected_number_of_points(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert len(result.time_series) == 121
    assert result.time_series[0].minute == 0
    assert result.time_series[-1].minute == 120


@pytest.mark.unit
def test_initial_temperatures_are_preserved(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    initial = result.time_series[0]

    assert initial.core_temperature_c == pytest.approx(
        person.initial_core_temperature_c,
        abs=1e-4,
    )

    assert initial.skin_temperature_c == pytest.approx(
        person.initial_skin_temperature_c,
        abs=1e-4,
    )


@pytest.mark.unit
def test_all_temperatures_are_finite(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    for point in result.time_series:
        assert math.isfinite(
            point.core_temperature_c
        )
        assert math.isfinite(
            point.skin_temperature_c
        )


@pytest.mark.unit
def test_temperature_stays_in_broad_physiological_range(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    for point in result.time_series:
        assert 30.0 < point.core_temperature_c < 43.0
        assert 15.0 < point.skin_temperature_c < 45.0


@pytest.mark.unit
def test_energy_balance_residual_is_small(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert (
        result.diagnostics
        .normalized_residual_percent
        < 1.0
    )


@pytest.mark.unit
def test_rc_material_reduces_skin_temperature(
    environment,
    person,
    control_material,
    rc_material,
):
    control = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    rc = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert (
        rc.final_skin_temperature_c
        < control.final_skin_temperature_c
    )


@pytest.mark.unit
def test_identical_materials_produce_identical_results(
    environment,
    person,
    control_material,
):
    first = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    second = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert (
        first.final_core_temperature_c
        == pytest.approx(
            second.final_core_temperature_c,
            abs=1e-8,
        )
    )

    assert (
        first.final_skin_temperature_c
        == pytest.approx(
            second.final_skin_temperature_c,
            abs=1e-8,
        )
    )