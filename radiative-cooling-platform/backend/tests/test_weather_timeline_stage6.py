from datetime import datetime, timedelta, timezone

import pytest

from app.core.cities import CityConfig
from app.services.weather import parse_weather_points, get_historical_weather
from app.services.weather_quality import WeatherGapInWindowError, normalize_timeline


BERLIN = CityConfig(
    id="berlin", name="Berlin", country="Germany", latitude=52.52, longitude=13.41,
    elevation_m=34.0, timezone="Europe/Berlin", climate_type="test",
)


def hourly_payload(times, offset_seconds, **overrides):
    n = len(times)
    hourly = {
        "time": times,
        "temperature_2m": [20.0 + i for i in range(n)],
        "relative_humidity_2m": [50.0] * n,
        "wind_speed_10m": [2.0] * n,
        "shortwave_radiation": [100.0] * n,
        "direct_radiation": [60.0] * n,
        "diffuse_radiation": [40.0] * n,
        "direct_normal_irradiance": [70.0] * n,
    }
    hourly.update(overrides)
    return {"utc_offset_seconds": offset_seconds, "hourly": hourly}


@pytest.mark.unit
def test_dst_fall_back_day_parses_without_duplicate_conflict():
    # 2023-10-29 Europe/Berlin: 02:00 occurs twice in wall-clock time.
    # Open-Meteo renders the day with one fixed offset (+7200 s here), so the
    # 24 strings are 24 distinct instants when parsed with that offset.
    times = [f"2023-10-29T{h:02d}:00" for h in range(24)]
    points = parse_weather_points(hourly_payload(times, 7200), BERLIN)

    instants = [p.timestamp.timestamp() for p in points]
    assert len(set(instants)) == 24
    assert all(b - a == 3600 for a, b in zip(instants, instants[1:]))

    cleaned, report = normalize_timeline(points, expected_step_seconds=3600)
    assert report.duplicates_removed == 0
    assert report.gaps == []


@pytest.mark.unit
@pytest.mark.asyncio
async def test_two_hourly_data_is_reported_as_gaps_not_as_normal_step(monkeypatch):
    # Every other hour missing: inference would call this a clean 2 h series.
    times = [f"2023-07-15T{h:02d}:00" for h in range(0, 24, 2)]

    async def fake_request(params):
        return hourly_payload(times, 14400), True

    monkeypatch.setattr("app.services.weather.request_open_meteo", fake_request)

    from app.core.cities import get_city
    with pytest.raises(WeatherGapInWindowError):
        await get_historical_weather(
            city=get_city("dubai"),
            start_time_local=datetime(2023, 7, 15, 12),
            duration_minutes=120,
        )


@pytest.mark.unit
def test_requested_window_is_two_elapsed_hours_across_dst(monkeypatch):
    from app.services.weather import normalize_local_datetime, to_utc
    start = normalize_local_datetime(datetime(2023, 10, 29, 1, 30), "Europe/Berlin")
    end = (to_utc(start) + timedelta(minutes=120)).astimezone(start.tzinfo)
    assert end.timestamp() - start.timestamp() == 7200