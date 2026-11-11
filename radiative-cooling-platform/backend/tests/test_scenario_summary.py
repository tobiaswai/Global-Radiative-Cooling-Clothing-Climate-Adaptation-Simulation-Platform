import pytest

from app.schemas.simulation import WeatherSimulationRequest
from app.services.scenario_summary import (
    ScenarioPairingError,
    build_simulation_summary,
    pair_scenarios,
)
from app.services.two_node import simulate_material
from app.services.weather_simulation import execute_weather_simulation_with_weather


@pytest.mark.unit
def test_average_is_time_weighted_not_arithmetic(environment, person, control_material, rc_material):
    control = simulate_material(120, 10, environment, person, control_material)
    rc = simulate_material(120, 10, environment, person, rc_material)

    summary = build_simulation_summary(control, rc)
    paired = pair_scenarios(control, rc)

    arithmetic = sum(paired.skin_c) / len(paired.skin_c)
    trapezoid = (sum(paired.skin_c) - 0.5 * (paired.skin_c[0] + paired.skin_c[-1])) / (
        len(paired.skin_c) - 1
    )

    assert summary.average_skin_temperature_improvement_c == pytest.approx(trapezoid, abs=1e-4)
    assert summary.average_skin_temperature_improvement_c != pytest.approx(arithmetic, abs=1e-4)
    assert summary.averaging_method == "time_weighted_trapezoid"


@pytest.mark.unit
def test_single_run_and_annual_sample_agree(hourly_weather, person, control_material, rc_material):
    """The same weather window must give the same average in both pipelines."""
    from app.services.scenario_summary import pair_scenarios

    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=hourly_weather.requested_start_time,
        duration_minutes=120,
        output_interval_minutes=10,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )
    single = execute_weather_simulation_with_weather(request=request, weather=hourly_weather, city_name="Dubai")
    paired = pair_scenarios(single.control, single.radiative_cooling)  # what climate_adaptation uses

    assert single.summary.average_skin_temperature_improvement_c == pytest.approx(
        round(paired.average_skin_c, 4)
    )


@pytest.mark.unit
def test_mismatched_time_axis_is_rejected(environment, person, control_material):
    a = simulate_material(60, 1, environment, person, control_material)
    b = simulate_material(60, 2, environment, person, control_material)
    with pytest.raises(ScenarioPairingError):
        pair_scenarios(a, b)