import numpy as np
import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.weather_interpolation import WeatherInterpolator


def make_interpolator(convention):
    return WeatherInterpolator(
        relative_seconds=np.array([-3600.0, 0.0, 3600.0, 7200.0]),
        temperatures=np.array([30.0, 32.0, 34.0, 36.0]),
        humidities=np.array([40.0] * 4),
        wind_speeds=np.array([1.0] * 4),
        ghi_values=np.array([200.0, 600.0, 800.0, 700.0]),
        assumptions=EnvironmentAssumptions(radiation_time_convention=convention),
    )


@pytest.mark.unit
def test_step_convention_conserves_hourly_irradiation():
    interp = make_interpolator("preceding_hour_mean_step")
    # Hour ending at t=3600 s has mean 800 W/m^2 -> 800 * 3600 J/m^2.
    ts = np.linspace(1.0, 3600.0, 3600)
    energy = np.trapezoid([interp.environment_at(t).solar_radiation_w_m2 for t in ts], ts)
    assert energy == pytest.approx(800.0 * 3599.0, rel=1e-6)


@pytest.mark.unit
def test_step_convention_leaves_instantaneous_variables_linear():
    interp = make_interpolator("preceding_hour_mean_step")
    env = interp.environment_at(1800.0)
    assert env.air_temperature_c == pytest.approx(33.0)   # still linear
    assert env.solar_radiation_w_m2 == pytest.approx(800.0)  # step


@pytest.mark.unit
def test_default_convention_is_unchanged_legacy_behaviour():
    interp = make_interpolator("instantaneous_linear")
    assert interp.environment_at(1800.0).solar_radiation_w_m2 == pytest.approx(700.0)
    assert "approximation" in " ".join(EnvironmentAssumptions().describe())