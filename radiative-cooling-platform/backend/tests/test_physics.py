import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.two_node import (
    calculate_fluxes,
    saturation_vapor_pressure_kpa,
)


@pytest.mark.unit
def test_saturation_pressure_increases_with_temperature():
    pressure_20 = saturation_vapor_pressure_kpa(20.0)
    pressure_30 = saturation_vapor_pressure_kpa(30.0)
    pressure_40 = saturation_vapor_pressure_kpa(40.0)

    assert pressure_20 < pressure_30 < pressure_40


@pytest.mark.unit
def test_saturation_pressure_near_reference_value():
    pressure = saturation_vapor_pressure_kpa(30.0)

    assert pressure == pytest.approx(
        4.24,
        abs=0.08,
    )


@pytest.mark.unit
def test_invalid_optical_sum_is_rejected():
    with pytest.raises(ValidationError):
        MaterialInput(
            name="Invalid material",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.8,
            solar_transmittance=0.4,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        )


@pytest.mark.unit
def test_higher_reflectance_reduces_solar_absorption(
    environment,
    person,
    control_material,
    rc_material,
):
    control_fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=environment,
        person=person,
        material=control_material,
    )

    rc_fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert (
        rc_fluxes.absorbed_solar
        < control_fluxes.absorbed_solar
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "wind_speed",
    [0.0, 0.1, 1.0, 3.0, 8.0],
)
def test_flux_calculation_is_finite(
    wind_speed,
    environment,
    person,
    control_material,
):
    modified_environment = environment.model_copy(
        update={
            "wind_speed_m_s": wind_speed,
        }
    )

    fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=modified_environment,
        person=person,
        material=control_material,
    )

    assert fluxes.metabolism > 0
    assert fluxes.evaporation >= 0
    assert fluxes.absorbed_solar >= 0