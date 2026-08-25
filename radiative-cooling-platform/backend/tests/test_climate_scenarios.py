import pytest

from app.schemas.simulation import EnvironmentInput
from app.services.two_node import simulate_material


@pytest.mark.unit
@pytest.mark.parametrize(
    (
        "name",
        "air_temperature",
        "humidity",
        "wind_speed",
        "solar_radiation",
    ),
    [
        (
            "hot_dry",
            42.0,
            20.0,
            2.0,
            900.0,
        ),
        (
            "hot_humid",
            34.0,
            85.0,
            1.0,
            700.0,
        ),
        (
            "high_altitude_solar",
            24.0,
            25.0,
            2.5,
            1000.0,
        ),
        (
            "night",
            30.0,
            60.0,
            0.5,
            0.0,
        ),
    ],
)
def test_typical_climate_scenarios_run_successfully(
    name,
    air_temperature,
    humidity,
    wind_speed,
    solar_radiation,
    person,
    rc_material,
):
    environment = EnvironmentInput(
        air_temperature_c=air_temperature,
        mean_radiant_temperature_c=(
            air_temperature + 5.0
        ),
        sky_temperature_c=(
            air_temperature - 12.0
        ),
        relative_humidity_percent=humidity,
        wind_speed_m_s=wind_speed,
        solar_radiation_w_m2=solar_radiation,
        sky_view_factor=0.5,
    )

    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert len(result.time_series) == 121

    assert (
        result.diagnostics
        .normalized_residual_percent
        < 1.0
    ), f"{name} Excessive energy residual"