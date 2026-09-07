from datetime import (
    datetime,
    timedelta,
    timezone,
)

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.weather import (
    slice_weather_time_series,
)


def make_weather() -> WeatherTimeSeries:
    start = datetime(
        2023,
        7,
        1,
        0,
        tzinfo=timezone.utc,
    )

    points = [
        WeatherPoint(
            timestamp=start
            + timedelta(hours=index),
            air_temperature_c=30,
            relative_humidity_percent=60,
            wind_speed_m_s=2,
            ghi_w_m2=500,
            direct_radiation_w_m2=300,
            diffuse_radiation_w_m2=200,
            dni_w_m2=600,
        )
        for index in range(72)
    ]

    city = CityResponse(
        id="test",
        name="Test City",
        country="Test",
        latitude=0,
        longitude=0,
        elevation_m=0,
        timezone="UTC",
        climate_type="test",
    )

    return WeatherTimeSeries(
        city=city,
        requested_start_time=start,
        requested_end_time=(
            start + timedelta(hours=71)
        ),
        points=points,
        source=WeatherSourceMetadata(
            provider="test",
            dataset="test",
            model="test",
            latitude=0,
            longitude=0,
            elevation_m=0,
            timezone="UTC",
            downloaded_at=start,
            from_cache=True,
            attribution="test",
        ),
    )


@pytest.mark.unit
def test_slice_weather_includes_padding():
    weather = make_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(
            2023,
            7,
            2,
            12,
        ),
        duration_minutes=120,
        padding_hours=1,
    )

    timestamps = [
        point.timestamp
        for point in sliced.points
    ]

    assert datetime(
        2023,
        7,
        2,
        11,
        tzinfo=timezone.utc,
    ) in timestamps

    assert datetime(
        2023,
        7,
        2,
        15,
        tzinfo=timezone.utc,
    ) in timestamps


@pytest.mark.unit
def test_slice_fails_when_range_not_covered():
    weather = make_weather()

    with pytest.raises(
        RuntimeError,
        match="does not cover",
    ):
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(
                2023,
                8,
                1,
                12,
            ),
            duration_minutes=120,
        )