import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import derive_environment, required_weather_variables
from app.services.ground_surface import (
    brutsaert_cloud_sky_emissivity,
    brutsaert_cloud_sky_temperature_c,
    ground_energy_residual,
    solve_ground_surface_temperature_c,
)
from app.services.weather_quality import WeatherMissingVariableError


PHYSICAL = EnvironmentAssumptions(
    mean_radiant_temperature_method="ground_energy_balance",
    sky_temperature_method="brutsaert_cloud",
)

GROUND = dict(air_c=40.0, sky_c=25.0, ghi_w_m2=900.0, albedo=0.2,
              wind_speed_m_s=2.0, soil_c=38.0, emissivity=0.95, conductance_w_m2k=15.0)


@pytest.mark.unit
def test_defaults_need_no_extra_weather_variables():
    assert required_weather_variables(EnvironmentAssumptions()) == ()
    assert required_weather_variables(PHYSICAL) == ("cloud_cover", "soil_temperature_0_to_7cm")


@pytest.mark.unit
def test_legacy_path_is_unchanged():
    env = derive_environment(air_temperature_c=35.0, relative_humidity_percent=40.0,
                             wind_speed_m_s=2.0, ghi_w_m2=800.0, assumptions=EnvironmentAssumptions())
    assert env.mean_radiant_temperature_c == pytest.approx(35.0 + 9.6)
    assert env.sky_temperature_c == pytest.approx(35.0 - (5.0 + 10.0 * 0.6))


@pytest.mark.unit
def test_brutsaert_clear_sky_value():
    # e_a = 15.8 hPa at 25 C / 50 % RH -> 1.24 (15.8 / 298.15)^(1/7) = 0.815
    assert brutsaert_cloud_sky_emissivity(25.0, 50.0, 0.0) == pytest.approx(0.815, abs=0.005)


@pytest.mark.unit
def test_overcast_sky_radiates_at_air_temperature():
    assert brutsaert_cloud_sky_temperature_c(30.0, 60.0, 100.0) == pytest.approx(30.0, abs=1e-9)


@pytest.mark.unit
def test_clouds_warm_the_sky():
    clear = brutsaert_cloud_sky_temperature_c(30.0, 40.0, 0.0)
    half = brutsaert_cloud_sky_temperature_c(30.0, 40.0, 50.0)
    assert clear < half < 30.0


@pytest.mark.unit
def test_ground_balance_closes():
    t = solve_ground_surface_temperature_c(**GROUND)
    assert ground_energy_residual(t, **GROUND) == pytest.approx(0.0, abs=1e-6)
    assert 45.0 < t < 75.0


@pytest.mark.unit
def test_ground_warms_with_sun_and_follows_soil_for_large_conductance():
    noon = solve_ground_surface_temperature_c(**GROUND)
    night = solve_ground_surface_temperature_c(**{**GROUND, "ghi_w_m2": 0.0})
    assert night < noon
    stiff = solve_ground_surface_temperature_c(**{**GROUND, "conductance_w_m2k": 200.0})
    assert abs(stiff - GROUND["soil_c"]) < abs(noon - GROUND["soil_c"])


@pytest.mark.unit
def test_physical_methods_require_their_variables():
    with pytest.raises(WeatherMissingVariableError):
        derive_environment(air_temperature_c=30.0, relative_humidity_percent=50.0,
                           wind_speed_m_s=1.0, ghi_w_m2=500.0, assumptions=PHYSICAL)


@pytest.mark.unit
def test_physical_environment_is_valid_input():
    env = derive_environment(air_temperature_c=40.0, relative_humidity_percent=20.0,
                             wind_speed_m_s=2.0, ghi_w_m2=900.0, assumptions=PHYSICAL,
                             cloud_cover_percent=0.0, soil_temperature_c=38.0)
    assert env.sky_temperature_c < 40.0 < env.mean_radiant_temperature_c