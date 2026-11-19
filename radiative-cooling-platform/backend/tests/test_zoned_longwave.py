import pytest

from app.schemas.simulation import EnvironmentInput, MaterialInput, PersonInput
from app.services.longwave import zone_sky_views
from app.services.two_node import simulate_material
from app.services.environment_model import derive_environment
from tests.helpers.environment import legacy

HOT_GROUND = EnvironmentInput(
    air_temperature_c=40.0, mean_radiant_temperature_c=60.0, sky_temperature_c=20.0,
    relative_humidity_percent=25.0, wind_speed_m_s=1.5, solar_radiation_w_m2=800.0,
    sky_view_factor=0.5, zone_view_separation=0.5,
)
PERSON = PersonInput()


def garment(**overrides) -> MaterialInput:
    values = dict(name="t", clothing_insulation_clo=0.4, solar_reflectance=0.9,
                  infrared_emissivity=0.95)
    values.update(overrides)
    return MaterialInput(**values)


def run(material: MaterialInput, environment: EnvironmentInput = HOT_GROUND):
    return simulate_material(60, 5, environment, PERSON, material)


def skins(result):
    return [p.skin_temperature_c for p in result.time_series]


@pytest.mark.unit
@pytest.mark.parametrize("f", [0.0, 0.3, 0.5, 1.0])
@pytest.mark.parametrize("s", [0.0, 0.5, 1.0])
def test_zone_views_are_area_consistent(f, s):
    up, down = zone_sky_views(f, s)
    assert f * up + (1 - f) * down == pytest.approx(f)
    assert 0.0 <= down <= up <= 1.0


@pytest.mark.unit
def test_equal_gray_zones_reproduce_uniform_garment():
    uniform = run(garment())
    zoned = run(garment(infrared_emissivity_ground_facing=0.95))
    assert skins(zoned) == pytest.approx(skins(uniform), abs=1e-3)


@pytest.mark.unit
def test_zero_separation_reduces_to_area_weighted_emissivity():
    env = HOT_GROUND.model_copy(update={"zone_view_separation": 0.0})
    zoned = run(garment(infrared_emissivity_ground_facing=0.35), env)
    uniform = run(garment(infrared_emissivity=0.5 * 0.95 + 0.5 * 0.35), env)
    assert skins(zoned) == pytest.approx(skins(uniform), abs=1e-3)


@pytest.mark.unit
def test_low_ground_facing_emissivity_rejects_hot_ground():
    uniform = run(garment())
    zoned = run(garment(infrared_emissivity_ground_facing=0.1))
    assert zoned.final_skin_temperature_c < uniform.final_skin_temperature_c
    assert zoned.clothing.infrared_emissivity_ground_facing == 0.1
    assert any("two-zone garment" in note for note in zoned.assumptions_applied)


@pytest.mark.unit
def test_selective_sky_zone_with_gray_ground_zone_runs():
    result = run(garment(infrared_emissivity=0.9, infrared_emissivity_window=0.95,
                         infrared_emissivity_ground_facing=0.2))
    assert result.time_series[0].longwave_window_w_m2 is not None
    assert result.diagnostics.normalized_residual_percent < 0.5


@pytest.mark.unit
def test_ground_facing_energy_sum_is_validated():
    with pytest.raises(ValueError):
        garment(infrared_emissivity=0.7, infrared_transmittance=0.2,
                infrared_emissivity_ground_facing=0.9)
        
@pytest.mark.unit
def test_zone_view_separation_reaches_environment_input():
    env = derive_environment(air_temperature_c=35.0, relative_humidity_percent=40.0,
                             wind_speed_m_s=2.0, ghi_w_m2=800.0,
                             assumptions=legacy(zone_view_separation=0.8))
    assert env.zone_view_separation == 0.8