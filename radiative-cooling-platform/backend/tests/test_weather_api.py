from datetime import datetime

import pytest

from app.api import weather as weather_api
from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)

@pytest.fixture
def weather_series() -> WeatherTimeSeries:
    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai",
            name="Dubai",
            country="United Arab Emirates",
            latitude=25.25,
            longitude=55.25,
            elevation_m=12.0,
            timezone="Asia/Dubai",
            climate_type="hot_arid",
        ),
        requested_start_time=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        requested_end_time=datetime(
            2025,
            7,
            15,
            12,
            0,
        ),
        points=[
            WeatherPoint(
                timestamp=datetime(
                    2025,
                    7,
                    15,
                    10,
                    0,
                ),
                air_temperature_c=38.0,
                relative_humidity_percent=40.0,
                wind_speed_m_s=1.5,
                ghi_w_m2=700.0,
                direct_radiation_w_m2=520.0,
                diffuse_radiation_w_m2=180.0,
                dni_w_m2=750.0,
            ),
            WeatherPoint(
                timestamp=datetime(
                    2025,
                    7,
                    15,
                    11,
                    0,
                ),
                air_temperature_c=39.0,
                relative_humidity_percent=38.0,
                wind_speed_m_s=2.0,
                ghi_w_m2=800.0,
                direct_radiation_w_m2=620.0,
                diffuse_radiation_w_m2=180.0,
                dni_w_m2=820.0,
            ),
        ],
        source=WeatherSourceMetadata(
            provider="Open-Meteo",
            dataset="Historical Weather API",
            model="ERA5",
            latitude=25.25,
            longitude=55.25,
            elevation_m=12.0,
            timezone="Asia/Dubai",
            downloaded_at=datetime(
                2025,
                7,
                15,
                13,
                0,
            ),
            from_cache=False,
            attribution="Weather data by Open-Meteo",
        ),
    )

@pytest.mark.unit
def test_weather_cities_endpoint(client):
    response = client.get(
        "/api/v1/weather/cities"
    )

    assert response.status_code == 200

    payload = response.json()

    assert len(payload) >= 3

    city_ids = {
        city["id"]
        for city in payload
    }

    assert {
        "dubai",
        "guangzhou",
        "lhasa",
    }.issubset(city_ids)

@pytest.mark.unit
def test_weather_history_endpoint(
    client,
    monkeypatch,
    weather_series,
):
    async def fake_get_historical_weather(
        **kwargs,
    ):
        return weather_series

    monkeypatch.setattr(
        weather_api,
        "get_historical_weather",
        fake_get_historical_weather,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["city"]["id"] == "dubai"
    assert len(payload["points"]) == 2

    assert (
        payload["points"][0]["air_temperature_c"]
        == pytest.approx(38.0)
    )

    assert payload["source"]["from_cache"] is False

@pytest.mark.unit
def test_weather_history_rejects_unknown_city(
    client,
    monkeypatch,
):
    def fake_get_city(city_id):
        raise ValueError(
            f"City not supported: {city_id}"
        )

    monkeypatch.setattr(
        weather_api,
        "get_city",
        fake_get_city,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "unknown",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 422

    assert (
        "City not supported"
        in response.json()["detail"]
    )


@pytest.mark.unit
def test_weather_history_converts_service_error_to_502(
    client,
    monkeypatch,
):
    async def fake_get_historical_weather(
        **kwargs,
    ):
        raise RuntimeError(
            "Open-Meteo unavailable"
        )

    monkeypatch.setattr(
        weather_api,
        "get_historical_weather",
        fake_get_historical_weather,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 502
    assert response.json()["detail"] == (
        "Open-Meteo unavailable"
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "duration",
    [
        0,
        1441,
    ],
)
def test_weather_history_validates_duration(
    client,
    duration,
):
    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": duration,
        },
    )

    assert response.status_code == 422