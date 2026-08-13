from datetime import datetime

import httpx
import pytest

from app.core.cities import get_city
from app.services.weather import (
    get_historical_weather,
)


OPEN_METEO_RESPONSE = {
    "latitude": 25.25,
    "longitude": 55.25,
    "elevation": 12.0,
    "timezone": "Asia/Dubai",
    "hourly": {
        "time": [
            "2025-07-15T09:00",
            "2025-07-15T10:00",
            "2025-07-15T11:00",
            "2025-07-15T12:00",
            "2025-07-15T13:00",
        ],
        "temperature_2m": [
            36.0,
            38.0,
            39.0,
            40.0,
            40.5,
        ],
        "relative_humidity_2m": [
            45.0,
            40.0,
            38.0,
            35.0,
            34.0,
        ],
        "wind_speed_10m": [
            1.0,
            1.5,
            2.0,
            2.5,
            2.0,
        ],
        "shortwave_radiation": [
            500.0,
            700.0,
            800.0,
            900.0,
            850.0,
        ],
        "direct_radiation": [
            350.0,
            520.0,
            620.0,
            700.0,
            650.0,
        ],
        "diffuse_radiation": [
            150.0,
            180.0,
            180.0,
            200.0,
            200.0,
        ],
        "direct_normal_irradiance": [
            600.0,
            750.0,
            820.0,
            880.0,
            830.0,
        ],
    },
}


@pytest.mark.integration
@pytest.mark.asyncio
async def test_historical_weather_with_mock(
    monkeypatch,
    tmp_path,
):
    async def mock_request_open_meteo(
        params,
    ):
        return OPEN_METEO_RESPONSE, False

    monkeypatch.setattr(
        "app.services.weather.request_open_meteo",
        mock_request_open_meteo,
    )

    city = get_city("dubai")

    result = await get_historical_weather(
        city=city,
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=120,
    )

    assert result.city.id == "dubai"
    assert len(result.points) >= 2
    assert result.source.from_cache is False
    assert (
        result.points[1]
        .air_temperature_c
        == pytest.approx(38.0)
    )