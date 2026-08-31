from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.weather_interpolation import (
    WeatherInterpolator,
)


@pytest.fixture
def weather_series():
    timezone = ZoneInfo("Asia/Dubai")

    start = datetime(
        2025,
        7,
        15,
        10,
        0,
        tzinfo=timezone,
    )

    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai",
            name="Dubai",
            country="United Arab Emirates",
            latitude=25.2048,
            longitude=55.2708,
            elevation_m=16,
            timezone="Asia/Dubai",
            climate_type="hot_dry",
        ),
        requested_start_time=start,
        requested_end_time=start.replace(
            hour=12
        ),
        points=[
            WeatherPoint(
                timestamp=start.replace(hour=9),
                air_temperature_c=36,
                relative_humidity_percent=45,
                wind_speed_m_s=1,
                ghi_w_m2=500,
                direct_radiation_w_m2=400,
                diffuse_radiation_w_m2=100,
                dni_w_m2=700,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=10),
                air_temperature_c=38,
                relative_humidity_percent=40,
                wind_speed_m_s=2,
                ghi_w_m2=700,
                direct_radiation_w_m2=550,
                diffuse_radiation_w_m2=150,
                dni_w_m2=800,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=11),
                air_temperature_c=40,
                relative_humidity_percent=35,
                wind_speed_m_s=3,
                ghi_w_m2=900,
                direct_radiation_w_m2=700,
                diffuse_radiation_w_m2=200,
                dni_w_m2=900,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=12),
                air_temperature_c=42,
                relative_humidity_percent=30,
                wind_speed_m_s=4,
                ghi_w_m2=1000,
                direct_radiation_w_m2=800,
                diffuse_radiation_w_m2=200,
                dni_w_m2=950,
            ),
        ],
        source=WeatherSourceMetadata(
            provider="test",
            dataset="test",
            model="test",
            latitude=25.2,
            longitude=55.2,
            elevation_m=16,
            timezone="Asia/Dubai",
            downloaded_at=start,
            from_cache=False,
            attribution="test",
        ),
    )


@pytest.mark.unit
def test_weather_interpolation_at_start(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series
        )
    )

    environment = interpolator.environment_at(
        0
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(38)
    )

    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(700)
    )


@pytest.mark.unit
def test_weather_interpolation_at_half_hour(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series
        )
    )

    environment = interpolator.environment_at(
        1800
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(39)
    )

    assert (
        environment.wind_speed_m_s
        == pytest.approx(2.5)
    )

    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(800)
    )

import numpy as np


@pytest.mark.unit
def test_environment_clamps_negative_wind_and_solar():
    interpolator = WeatherInterpolator(
        relative_seconds=np.array(
            [0.0, 3600.0]
        ),
        temperatures=np.array(
            [30.0, 30.0]
        ),
        humidities=np.array(
            [50.0, 50.0]
        ),
        wind_speeds=np.array(
            [-2.0, -1.0]
        ),
        ghi_values=np.array(
            [-100.0, -50.0]
        ),
    )

    environment = interpolator.environment_at(
        1800
    )

    assert environment.wind_speed_m_s == 0
    assert (
        environment.solar_radiation_w_m2
        == 0
    )
    assert (
        environment.mean_radiant_temperature_c
        == pytest.approx(30.0)
    )


@pytest.mark.unit
def test_mean_radiant_temperature_increase_is_capped():
    interpolator = WeatherInterpolator(
        relative_seconds=np.array(
            [0.0, 3600.0]
        ),
        temperatures=np.array(
            [30.0, 30.0]
        ),
        humidities=np.array(
            [50.0, 50.0]
        ),
        wind_speeds=np.array(
            [1.0, 1.0]
        ),
        ghi_values=np.array(
            [1500.0, 1500.0]
        ),
    )

    environment = interpolator.environment_at(
        0
    )
    
    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(1500.0)
    )
    
    assert (
        environment.mean_radiant_temperature_c
        == pytest.approx(45.0)
    )


@pytest.mark.unit
def test_interpolation_after_last_point_uses_last_value(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series
        )
    )

    environment = interpolator.environment_at(
        24 * 60 * 60
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(42.0)
    )
    assert (
        environment.wind_speed_m_s
        == pytest.approx(4.0)
    )