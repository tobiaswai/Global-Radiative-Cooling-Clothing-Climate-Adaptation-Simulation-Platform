import math

import pytest

from app.services.two_node import simulate_material, calculate_fluxes


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
    
@pytest.mark.unit
def test_absorbed_solar_raises_clothing_surface_temperature(
    environment, person, control_material
):
    sunlit = calculate_fluxes(36.8, 33.7, environment, person, control_material)
    shaded = calculate_fluxes(
        36.8, 33.7,
        environment.model_copy(update={"solar_radiation_w_m2": 0.0}),
        person, control_material,
    )

    assert sunlit.clothing_surface_temperature_c > shaded.clothing_surface_temperature_c


@pytest.mark.unit
def test_surface_re_emits_part_of_the_absorbed_solar(
    environment, person, control_material
):
    """ADR 0005: the extra surface losses caused by S_abs lie strictly between
    0 and S_abs, so only a fraction of the absorbed solar reaches the skin."""
    sunlit = calculate_fluxes(36.8, 33.7, environment, person, control_material)
    shaded = calculate_fluxes(
        36.8, 33.7,
        environment.model_copy(update={"solar_radiation_w_m2": 0.0}),
        person, control_material,
    )

    extra_surface_losses = (
        sunlit.convection + sunlit.longwave_radiation
    ) - (shaded.convection + shaded.longwave_radiation)

    assert 0.0 < extra_surface_losses < sunlit.solar_absorbed_by_textile
    assert sunlit.evaporation == pytest.approx(shaded.evaporation)


@pytest.mark.unit
def test_deprecated_absorbed_fraction_is_ignored(environment, person, control_material):
    baseline = simulate_material(30, 1, environment, person, control_material)
    altered = simulate_material(
        30, 1, environment, person,
        control_material.model_copy(update={"absorbed_solar_to_body_fraction": 0.9}),
    )

    assert altered.final_skin_temperature_c == pytest.approx(
        baseline.final_skin_temperature_c, abs=1e-9
    )
    
@pytest.mark.unit
def test_energy_diagnostics_do_not_depend_on_output_interval(environment, person, control_material):
    fine = simulate_material(120, 1, environment, person, control_material)
    coarse = simulate_material(120, 30, environment, person, control_material)

    assert coarse.diagnostics.integrated_net_heat_j_m2 == pytest.approx(
        fine.diagnostics.integrated_net_heat_j_m2, abs=1e-3
    )
    assert coarse.diagnostics.normalized_residual_percent == pytest.approx(
        fine.diagnostics.normalized_residual_percent, abs=1e-6
    )
    assert coarse.peak_skin_temperature_c == pytest.approx(fine.peak_skin_temperature_c, abs=1e-4)
    assert coarse.diagnostics.diagnostic_interval_seconds == 60.0


@pytest.mark.unit
def test_output_interval_does_not_change_trajectory(environment, person, control_material):
    fine = simulate_material(120, 1, environment, person, control_material)
    coarse = simulate_material(120, 10, environment, person, control_material)
    by_minute = {p.minute: p for p in fine.time_series}
    for p in coarse.time_series:
        assert p.skin_temperature_c == pytest.approx(by_minute[p.minute].skin_temperature_c, abs=1e-6)