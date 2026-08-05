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