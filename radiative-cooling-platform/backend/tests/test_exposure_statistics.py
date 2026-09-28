from datetime import datetime, timedelta, timezone

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.exposure_statistics import (
    compute_exposure_window_statistics,
    time_weighted_mean,
)
from app.services.weather import slice_weather_time_series


def make_day_weather() -> WeatherTimeSeries:
    """24 hourly points with a non-linear temperature profile so that padded
    and un-padded averages differ."""
    start = datetime(2023, 7, 1, 0, tzinfo=timezone.utc)

    points = [
        WeatherPoint(
            timestamp=start + timedelta(hours=i),
            air_temperature_c=20.0 + 0.1 * i * i,
            relative_humidity_percent=50.0,
            wind_speed_m_s=2.0,
            ghi_w_m2=float(50 * i),
            direct_radiation_w_m2=0.0,
            diffuse_radiation_w_m2=0.0,
            dni_w_m2=0.0,
        )
        for i in range(24)
    ]

    city = CityResponse(
        id="test", name="Test", country="Test",
        latitude=0, longitude=0, elevation_m=0,
        timezone="UTC", climate_type="test",
    )

    return WeatherTimeSeries(
        city=city,
        requested_start_time=start,
        requested_end_time=start + timedelta(hours=23),
        points=points,
        source=WeatherSourceMetadata(
            provider="test", dataset="test", model="test",
            latitude=0, longitude=0, elevation_m=0, timezone="UTC",
            downloaded_at=start, from_cache=True, attribution="test",
        ),
    )


@pytest.mark.unit
def test_time_weighted_mean_matches_trapezoid():
    assert time_weighted_mean([0, 1, 2], [0, 2, 4]) == pytest.approx(2.0)
    assert time_weighted_mean([0, 1, 3], [0, 0, 6]) == pytest.approx(2.0)
    assert time_weighted_mean([5], [7]) == pytest.approx(7.0)


@pytest.mark.unit
def test_statistics_use_exposure_window_not_padded_points():
    weather = make_day_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(2023, 7, 1, 12),
        duration_minutes=120,
        padding_hours=1,
    )

    stats = compute_exposure_window_statistics(sliced)

    # Knots 12:00 (34.4), 13:00 (36.9), 14:00 (39.6) -> trapezoid = 36.95
    assert stats.mean_air_temperature_c == pytest.approx(36.95)
    assert stats.maximum_air_temperature_c == pytest.approx(39.6)

    padded_arithmetic_mean = sum(
        p.air_temperature_c for p in sliced.points
    ) / len(sliced.points)  # 11:00..15:00 -> 37.5 (the old, wrong number)

    assert stats.mean_air_temperature_c != pytest.approx(padded_arithmetic_mean)


@pytest.mark.unit
@pytest.mark.parametrize("padding_hours", [1, 3, 6])
def test_statistics_are_invariant_to_padding(padding_hours):
    weather = make_day_weather()

    reference = compute_exposure_window_statistics(
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 7, 1, 12),
            duration_minutes=120,
            padding_hours=1,
        )
    )

    candidate = compute_exposure_window_statistics(
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 7, 1, 12),
            duration_minutes=120,
            padding_hours=padding_hours,
        )
    )

    assert candidate.mean_air_temperature_c == pytest.approx(
        reference.mean_air_temperature_c, abs=1e-9
    )
    assert candidate.maximum_air_temperature_c == pytest.approx(
        reference.maximum_air_temperature_c, abs=1e-9
    )
    assert candidate.mean_solar_radiation_w_m2 == pytest.approx(
        reference.mean_solar_radiation_w_m2, abs=1e-9
    )


@pytest.mark.unit
def test_half_hour_start_uses_interpolated_boundary():
    weather = make_day_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(2023, 7, 1, 12, 30),
        duration_minutes=60,
        padding_hours=1,
    )

    stats = compute_exposure_window_statistics(sliced)

    # Linear between 12:00 (34.4) and 13:00 (36.9) and 13:00..14:00 (39.6)
    t_1230 = 35.65
    t_1330 = 38.25
    expected = ((t_1230 + 36.9) / 2 * 0.5 + (36.9 + t_1330) / 2 * 0.5) / 1.0

    assert stats.mean_air_temperature_c == pytest.approx(expected)