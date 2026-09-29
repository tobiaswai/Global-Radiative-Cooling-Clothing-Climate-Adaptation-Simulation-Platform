import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import derive_environment


@pytest.mark.unit
def test_defaults_reproduce_stage_1_formulas():
    env = derive_environment(
        air_temperature_c=40.0, relative_humidity_percent=30.0,
        wind_speed_m_s=3.0, ghi_w_m2=800.0, assumptions=EnvironmentAssumptions(),
    )

    assert env.mean_radiant_temperature_c == pytest.approx(40.0 + 0.012 * 800.0)
    assert env.sky_temperature_c == pytest.approx(40.0 - (5.0 + 10.0 * 0.7))
    assert env.sky_view_factor == 0.5
    assert env.wind_speed_m_s == pytest.approx(3.0)


@pytest.mark.unit
def test_swinbank_clear_sky():
    env = derive_environment(
        air_temperature_c=30.0, relative_humidity_percent=50.0, wind_speed_m_s=1.0,
        ghi_w_m2=0.0, assumptions=EnvironmentAssumptions(sky_temperature_method="swinbank"),
    )
    # 0.0552 * 303.15^1.5 - 273.15
    assert env.sky_temperature_c == pytest.approx(18.2, abs=0.1)


@pytest.mark.unit
def test_wind_scaling_and_negative_inputs_are_clamped():
    env = derive_environment(
        air_temperature_c=30.0, relative_humidity_percent=120.0, wind_speed_m_s=-1.0,
        ghi_w_m2=-50.0,
        assumptions=EnvironmentAssumptions(wind_speed_scaling_factor=0.67),
    )
    assert env.wind_speed_m_s == 0.0
    assert env.solar_radiation_w_m2 == 0.0
    assert env.relative_humidity_percent == 100.0


@pytest.mark.unit
def test_describe_mentions_every_active_rule():
    lines = EnvironmentAssumptions(sky_temperature_method="fixed_offset").describe()
    text = " ".join(lines)
    assert "T_sky = T_air - 15.0 K" in text
    assert "Sky view factor = 0.5" in text