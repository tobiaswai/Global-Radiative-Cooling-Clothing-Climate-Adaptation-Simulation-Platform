from datetime import datetime, timedelta, timezone

import pytest

from app.schemas.global_batch import DailyAdaptationResult
from app.services.climate_analytics import detect_heatwave_events
from app.services.exposure_statistics import (
    compute_daily_maximum_air_temperature,
    compute_exposure_window_statistics,
)
from app.services.weather import slice_weather_time_series
from tests.test_exposure_statistics import make_day_weather


@pytest.mark.unit
def test_daily_maximum_differs_from_exposure_window_maximum():
    weather = make_day_weather()  # T = 20 + 0.1 i^2 rises all day, exposure 12:00-14:00

    sliced = slice_weather_time_series(
        weather=weather, start_time_local=datetime(2023, 7, 1, 12), duration_minutes=120
    )
    window_max = compute_exposure_window_statistics(sliced).maximum_air_temperature_c
    daily_max = compute_daily_maximum_air_temperature(
        weather, local_date=datetime(2023, 7, 1).date(), timezone_name="UTC"
    )

    assert window_max == pytest.approx(39.6)
    assert daily_max is None  # series ends 23:00, does not bracket 24:00 -> refuse partial day


@pytest.mark.unit
def test_daily_maximum_requires_full_day_coverage():
    weather = make_day_weather()
    extended = weather.model_copy(update={"points": weather.points + [
        weather.points[-1].model_copy(update={
            "timestamp": weather.points[-1].timestamp + timedelta(hours=1),
            "air_temperature_c": 10.0,
        })
    ]})
    daily_max = compute_daily_maximum_air_temperature(
        extended, local_date=datetime(2023, 7, 1).date(), timezone_name="UTC"
    )
    assert daily_max == pytest.approx(20.0 + 0.1 * 23 * 23)


def make_sample(day, exposure_max, daily_max):
    return DailyAdaptationResult(
        sample_date_local=datetime(2025, 7, day, 12), weight_days=1,
        mean_air_temperature_c=exposure_max - 3, maximum_air_temperature_c=exposure_max,
        daily_maximum_air_temperature_c=daily_max,
        mean_solar_radiation_w_m2=500, maximum_solar_radiation_w_m2=800,
        exposure_eligible=True, beneficial=True,
        average_skin_improvement_c=0.5, final_skin_improvement_c=0.5,
        average_core_improvement_c=0.1, maximum_skin_improvement_c=0.6,
        weather_from_cache=True,
    )


@pytest.mark.unit
def test_heatwave_uses_daily_maximum_not_exposure_window():
    # Cool noon window every day, but afternoons above 35 C for three days.
    samples = [make_sample(d, exposure_max=33.0, daily_max=37.0) for d in (1, 2, 3)]
    events = detect_heatwave_events(samples=samples, temperature_threshold_c=35, minimum_consecutive_days=3)
    assert len(events) == 1
    assert events[0].peak_air_temperature_c == 37.0


@pytest.mark.unit
def test_heatwave_refuses_samples_without_daily_maximum():
    samples = [make_sample(d, exposure_max=38.0, daily_max=None) for d in (1, 2, 3)]
    with pytest.raises(ValueError, match="daily_maximum_air_temperature_c"):
        detect_heatwave_events(samples=samples, temperature_threshold_c=35, minimum_consecutive_days=3)