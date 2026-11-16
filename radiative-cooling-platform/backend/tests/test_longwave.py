import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.clothing import resolve_clothing
from app.services.longwave import radiant_field, resolve_longwave_optics
from app.services.two_node import calculate_fluxes, simulate_material


KELVIN = 273.15


@pytest.mark.unit
def test_field_total_equals_gray_environment(environment):
    field = radiant_field(environment)
    f = environment.sky_view_factor
    expected = (
        f * (environment.sky_temperature_c + KELVIN) ** 4
        + (1 - f) * (environment.mean_radiant_temperature_c + KELVIN) ** 4
    )
    assert field.total_k4 == pytest.approx(expected, rel=1e-9)
    assert 0.0 < field.sky_window_emissivity < 1.0


@pytest.mark.unit
def test_equal_band_emissivities_reproduce_the_gray_path(environment, person, control_material):
    selective = control_material.model_copy(
        update={"infrared_emissivity_window": control_material.infrared_emissivity}
    )
    assert resolve_longwave_optics(selective).selective

    gray = calculate_fluxes(36.8, 33.7, environment, person, control_material)
    split = calculate_fluxes(36.8, 33.7, environment, person, selective)

    assert split.longwave_radiation == pytest.approx(gray.longwave_radiation, abs=1e-6)
    assert split.clothing_surface_temperature_c == pytest.approx(
        gray.clothing_surface_temperature_c, abs=1e-6
    )
    assert gray.longwave_window is None and split.longwave_window is not None


@pytest.mark.unit
def test_selective_emitter_loses_more_heat_in_hot_surroundings(environment, person, control_material):
    hot = environment.model_copy(update={"mean_radiant_temperature_c": 55.0, "sky_temperature_c": 18.0})
    gray = control_material.model_copy(update={"infrared_emissivity": 0.5})
    selective = MaterialInput.model_validate(
        {**gray.model_dump(), "infrared_emissivity_window": 0.95}
    )

    gray_flux = calculate_fluxes(36.8, 33.7, hot, person, gray)
    selective_flux = calculate_fluxes(36.8, 33.7, hot, person, selective)

    assert selective_flux.longwave_radiation > gray_flux.longwave_radiation


@pytest.mark.unit
def test_inconsistent_band_split_is_rejected():
    with pytest.raises(ValidationError, match="out-of-window emissivity"):
        MaterialInput(name="bad", infrared_emissivity=0.9, infrared_emissivity_window=0.0)


@pytest.mark.unit
def test_selective_surface_balance_and_energy(environment, person, rc_material):
    selective = MaterialInput.model_validate(
        {**rc_material.model_dump(), "infrared_emissivity": 0.6, "infrared_emissivity_window": 0.95}
    )
    clothing = resolve_clothing(selective)
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, selective, clothing)

    conduction = (33.7 - fluxes.clothing_surface_temperature_c) / clothing.dry_resistance_m2k_w
    losses = fluxes.convection + fluxes.longwave_radiation - fluxes.longwave_transmitted
    assert conduction + fluxes.solar_absorbed_by_textile == pytest.approx(losses, abs=1e-3)

    result = simulate_material(120, 1, environment, person, selective)
    assert result.diagnostics.normalized_residual_percent < 1.0
    assert result.clothing.infrared_emissivity_window == pytest.approx(0.95)
    assert any("selective longwave emitter" in note for note in result.assumptions_applied)