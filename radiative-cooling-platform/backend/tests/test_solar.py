import pytest
from pydantic import ValidationError

from app.schemas.simulation import EnvironmentInput, MaterialInput
from app.services.solar import solar_load
from app.services.two_node import effective_radiation_area_ratio


@pytest.mark.unit
def test_without_split_ghi_is_beam_on_projected_area(control_material):
    load = solar_load(
        EnvironmentInput(solar_radiation_w_m2=800.0),
        control_material,
        effective_radiation_area_ratio("standing"),
    )

    assert load.split_available is False
    assert load.incident_w_m2 == pytest.approx(0.25 * 800.0)
    assert load.sky_diffuse_w_m2 == 0.0
    assert load.ground_reflected_w_m2 == 0.0
    # rho = 0.4, tau = 0 -> alpha = 0.6
    assert load.absorbed_by_textile_w_m2 == pytest.approx(0.6 * 200.0)
    assert load.transmitted_to_skin_w_m2 == 0.0


@pytest.mark.unit
def test_split_components_follow_ashrae_55_geometry(control_material):
    environment = EnvironmentInput(
        solar_radiation_w_m2=900.0,
        direct_normal_irradiance_w_m2=700.0,
        diffuse_horizontal_irradiance_w_m2=200.0,
        sky_view_factor=0.5,
        ground_albedo=0.2,
    )

    load = solar_load(environment, control_material, 0.73)

    assert load.split_available is True
    assert load.direct_w_m2 == pytest.approx(0.25 * 700.0)
    assert load.sky_diffuse_w_m2 == pytest.approx(0.5 * 0.73 * 0.5 * 200.0)
    assert load.ground_reflected_w_m2 == pytest.approx(0.5 * 0.73 * 0.2 * 900.0)
    assert load.incident_w_m2 == pytest.approx(
        load.direct_w_m2 + load.sky_diffuse_w_m2 + load.ground_reflected_w_m2
    )


@pytest.mark.unit
def test_partial_split_is_rejected():
    with pytest.raises(ValidationError, match="supplied together"):
        EnvironmentInput(direct_normal_irradiance_w_m2=500.0)


@pytest.mark.unit
def test_transmittance_routes_solar_to_skin():
    material = MaterialInput(name="sheer", solar_reflectance=0.5, solar_transmittance=0.3)

    load = solar_load(EnvironmentInput(solar_radiation_w_m2=800.0), material, 0.73)

    assert load.transmitted_to_skin_w_m2 == pytest.approx(0.3 * 200.0)
    assert load.absorbed_by_textile_w_m2 == pytest.approx(0.2 * 200.0)
    assert load.entering_system_w_m2 == pytest.approx(0.5 * 200.0)


@pytest.mark.unit
def test_posture_selects_radiation_area_ratio():
    assert effective_radiation_area_ratio("standing") == pytest.approx(0.73)
    assert effective_radiation_area_ratio("sitting") == pytest.approx(0.70)