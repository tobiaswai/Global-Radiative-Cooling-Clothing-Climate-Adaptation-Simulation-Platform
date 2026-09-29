"""Stage 2 definition of done: every input participates in the computation.

Each case perturbs exactly one input and requires the final skin temperature
to change. A parameter that is stored but never used fails here.
"""

import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.two_node import (
    simulate_material,
    simulate_material_with_weather,
)


THRESHOLD_C = 1e-4


def final_skin(result) -> float:
    return result.final_skin_temperature_c


MATERIAL_PERTURBATIONS = {
    "clothing_insulation_clo": 0.9,
    "evaporative_resistance_m2pa_w": 40.0,
    "clothing_area_factor": 1.4,           # Stage 3
    "solar_reflectance": 0.7,
    "solar_transmittance": 0.2,
    "infrared_emissivity": 0.5,
    "infrared_transmittance": 0.15,
    "projected_solar_area_factor": 0.4,
    "absorbed_solar_to_body_fraction": 0.6,
}


@pytest.mark.unit
@pytest.mark.parametrize(("field", "value"), sorted(MATERIAL_PERTURBATIONS.items()))
def test_every_material_field_participates(
    environment, person, control_material, field, value
):
    baseline = simulate_material(60, 1, environment, person, control_material)
    perturbed = simulate_material(
        60, 1, environment, person, control_material.model_copy(update={field: value})
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, (
        f"MaterialInput.{field} does not influence the result"
    )


PERSON_PERTURBATIONS = {
    "met": 1.2,
    "body_surface_area_m2": 2.4,           # Stage 3: was xfail (ADR 0001)
    "body_mass_kg": 95.0,                  # Stage 3
    "initial_core_temperature_c": 37.4,
    "initial_skin_temperature_c": 31.0,
}


@pytest.mark.unit
@pytest.mark.parametrize(("field", "value"), sorted(PERSON_PERTURBATIONS.items()))
def test_every_person_field_participates(
    environment, person, control_material, field, value
):
    baseline = simulate_material(60, 1, environment, person, control_material)
    perturbed = simulate_material(
        60, 1, environment, person.model_copy(update={field: value}), control_material
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C

# (baseline update, perturbed update). Method-dependent parameters are tested
# with the method that uses them switched on in both runs.
ASSUMPTION_PERTURBATIONS = [
    ({}, {"mean_radiant_temperature_method": "equal_to_air"}),
    ({}, {"solar_mrt_gain_k_per_w_m2": 0.02}),
    ({}, {"solar_mrt_gain_cap_k": 5.0}),
    ({}, {"sky_temperature_method": "swinbank"}),
    ({}, {"sky_temperature_method": "fixed_offset"}),
    ({}, {"sky_offset_base_k": 8.0}),
    ({}, {"sky_offset_humidity_range_k": 2.0}),
    (
        {"sky_temperature_method": "fixed_offset"},
        {"sky_temperature_method": "fixed_offset", "fixed_sky_offset_k": 25.0},
    ),
    ({}, {"sky_view_factor": 0.2}),
    ({}, {"wind_speed_scaling_factor": 0.67}),
]


@pytest.mark.unit
@pytest.mark.parametrize(("baseline_update", "perturbed_update"), ASSUMPTION_PERTURBATIONS)
def test_every_environment_assumption_participates(
    hourly_weather, person, rc_material, baseline_update, perturbed_update
):
    baseline = simulate_material_with_weather(
        120, 10, hourly_weather, person, rc_material,
        assumptions=EnvironmentAssumptions(**baseline_update),
    )
    perturbed = simulate_material_with_weather(
        120, 10, hourly_weather, person, rc_material,
        assumptions=EnvironmentAssumptions(**perturbed_update),
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, (
        f"EnvironmentAssumptions {perturbed_update} does not influence the result"
    )