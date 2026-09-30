import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.clothing import (
    derive_evaporative_resistance_m2pa_w,
    maximum_evaporation_w_m2,
    resolve_clothing,
)
from app.services.two_node import calculate_fluxes, simulate_material


@pytest.mark.unit
def test_derived_evaporative_resistance_matches_formula():
    # 0.155 * 0.5 / (16.5 * 0.45) * 1000
    assert derive_evaporative_resistance_m2pa_w(0.5) == pytest.approx(10.4377, abs=1e-3)


@pytest.mark.unit
def test_none_resistance_is_derived_and_flagged(control_material):
    clothing = resolve_clothing(control_material)

    assert clothing.evaporative_resistance_source == "derived_from_clo"
    assert clothing.evaporative_resistance_m2pa_w == pytest.approx(
        derive_evaporative_resistance_m2pa_w(control_material.clothing_insulation_clo)
    )


@pytest.mark.unit
def test_explicit_resistance_overrides_derivation(control_material):
    material = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 30.0})
    clothing = resolve_clothing(material)

    assert clothing.evaporative_resistance_source == "material_input"
    assert clothing.evaporative_resistance_m2pa_w == pytest.approx(30.0)


@pytest.mark.unit
def test_higher_resistance_lowers_maximum_evaporation(control_material):
    low = resolve_clothing(control_material.model_copy(update={"evaporative_resistance_m2pa_w": 5.0}))
    high = resolve_clothing(control_material.model_copy(update={"evaporative_resistance_m2pa_w": 50.0}))

    e_low = maximum_evaporation_w_m2(low, 10.0, 5.6, 2.0)
    e_high = maximum_evaporation_w_m2(high, 10.0, 5.6, 2.0)

    assert e_high < e_low
    assert e_high > 0.0


@pytest.mark.unit
def test_explicit_derived_value_reproduces_none_result(environment, person, control_material):
    derived = derive_evaporative_resistance_m2pa_w(control_material.clothing_insulation_clo)
    explicit = control_material.model_copy(update={"evaporative_resistance_m2pa_w": derived})

    a = simulate_material(60, 1, environment, person, control_material)
    b = simulate_material(60, 1, environment, person, explicit)

    assert a.final_skin_temperature_c == pytest.approx(b.final_skin_temperature_c, abs=1e-8)
    assert a.clothing.evaporative_resistance_source == "derived_from_clo"
    assert b.clothing.evaporative_resistance_source == "material_input"

    # Stage 3: f_cl and the ADR 0003 solar note are always reported; only the
    # Re,cl derivation note must disappear when the value is supplied.
    assert any("evaporative_resistance" in note for note in a.assumptions_applied)
    assert not any("evaporative_resistance" in note for note in b.assumptions_applied)




@pytest.mark.unit
def test_impermeable_garment_ends_warmer(environment, person, control_material):
    permeable = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 5.0})
    impermeable = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 200.0})

    warm = simulate_material(120, 1, environment, person, impermeable)
    cool = simulate_material(120, 1, environment, person, permeable)

    assert warm.final_skin_temperature_c > cool.final_skin_temperature_c
    assert warm.time_series[-1].skin_wettedness >= cool.time_series[-1].skin_wettedness


@pytest.mark.unit
def test_infrared_transmittance_amplifies_longwave_exchange(
    environment, person, control_material
):
    opaque = control_material.model_copy(update={"infrared_emissivity": 0.5})
    transparent = opaque.model_copy(update={"infrared_transmittance": 0.4})

    # Cold radiant surroundings: the body loses heat; transmittance increases
    # the loss (more positive under the "positive = loss" convention).
    cold = environment.model_copy(
        update={"mean_radiant_temperature_c": 15.0, "sky_temperature_c": 0.0}
    )
    opaque_cold = calculate_fluxes(36.8, 33.7, cold, person, opaque)
    transparent_cold = calculate_fluxes(36.8, 33.7, cold, person, transparent)
    assert opaque_cold.longwave_radiation > 0
    assert transparent_cold.longwave_radiation > opaque_cold.longwave_radiation

    # Hot radiant surroundings well above any clothing surface temperature:
    # the body gains heat; transmittance increases the gain (more negative).
    hot = environment.model_copy(
        update={"mean_radiant_temperature_c": 60.0, "sky_temperature_c": 60.0}
    )
    opaque_hot = calculate_fluxes(36.8, 33.7, hot, person, opaque)
    transparent_hot = calculate_fluxes(36.8, 33.7, hot, person, transparent)
    assert opaque_hot.longwave_radiation < 0
    assert transparent_hot.longwave_radiation < opaque_hot.longwave_radiation

@pytest.mark.unit
def test_area_factor_is_derived_and_flagged(control_material):
    clothing = resolve_clothing(control_material)

    assert clothing.area_factor_source == "derived_from_clo"
    assert clothing.area_factor == pytest.approx(1.0 + 0.15 * 0.5)

@pytest.mark.unit
def test_explicit_area_factor_overrides_derivation(control_material):
    material = control_material.model_copy(update={"clothing_area_factor": 1.4})
    clothing = resolve_clothing(material)

    assert clothing.area_factor_source == "material_input"
    assert clothing.area_factor == pytest.approx(1.4)

@pytest.mark.unit
def test_clothing_surface_balance_is_consistent(environment, person, control_material):
    """Conduction through the textile plus absorbed solar equals what leaves
    the outer surface (ADR 0003 + ADR 0005)."""
    clothing = resolve_clothing(control_material)
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, control_material, clothing)

    conduction = (33.7 - fluxes.clothing_surface_temperature_c) / clothing.dry_resistance_m2k_w
    surface_losses = fluxes.convection + fluxes.longwave_radiation - fluxes.longwave_transmitted

    assert conduction + fluxes.solar_absorbed_by_textile == pytest.approx(
        surface_losses, abs=1e-3
    )

@pytest.mark.unit
def test_nude_surface_temperature_equals_skin(environment, person, control_material):
    nude = control_material.model_copy(update={"clothing_insulation_clo": 0.0})
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, nude)

    assert fluxes.clothing_surface_temperature_c == pytest.approx(33.7)
    
    
@pytest.mark.unit
def test_emissivity_plus_transmittance_above_one_is_rejected():
    with pytest.raises(ValidationError, match="infrared_emissivity"):
        MaterialInput(name="bad", infrared_emissivity=0.8, infrared_transmittance=0.3)


@pytest.mark.unit
def test_unknown_parameter_source_key_is_rejected():
    with pytest.raises(ValidationError, match="unknown material fields"):
        MaterialInput(name="bad", parameter_sources={"not_a_field": {"source_type": "measured"}})