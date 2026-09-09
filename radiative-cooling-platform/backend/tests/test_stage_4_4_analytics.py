from datetime import (
    datetime,
    timedelta,
)

import pytest

from app.schemas.global_batch import (
    DailyAdaptationResult,
)
from app.services.climate_analytics import (
    detect_heatwave_events,
    weighted_percentile,
)


def make_sample(
    *,
    day: int,
    maximum_temperature_c: float,
    skin_improvement_c: float = 0.5,
) -> DailyAdaptationResult:
    return DailyAdaptationResult(
        sample_date_local=datetime(
            2025,
            7,
            day,
            12,
        ),
        weight_days=1,
        mean_air_temperature_c=(
            maximum_temperature_c - 3
        ),
        maximum_air_temperature_c=(
            maximum_temperature_c
        ),
        mean_solar_radiation_w_m2=500,
        maximum_solar_radiation_w_m2=800,
        exposure_eligible=True,
        beneficial=True,
        average_skin_improvement_c=(
            skin_improvement_c
        ),
        final_skin_improvement_c=(
            skin_improvement_c
        ),
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=(
            skin_improvement_c + 0.1
        ),
        weather_from_cache=True,
    )


@pytest.mark.unit
def test_weighted_percentile():
    values = [
        (0.1, 1),
        (0.2, 1),
        (0.3, 1),
        (0.4, 1),
        (0.5, 1),
    ]

    assert weighted_percentile(
        values,
        50,
    ) == 0.3

    assert weighted_percentile(
        values,
        90,
    ) == 0.5


@pytest.mark.unit
def test_weighted_percentile_uses_weights():
    values = [
        (0.1, 10),
        (1.0, 1),
    ]

    assert weighted_percentile(
        values,
        50,
    ) == 0.1


@pytest.mark.unit
def test_detects_consecutive_heatwave():
    samples = [
        make_sample(
            day=1,
            maximum_temperature_c=34,
        ),
        make_sample(
            day=2,
            maximum_temperature_c=36,
        ),
        make_sample(
            day=3,
            maximum_temperature_c=37,
        ),
        make_sample(
            day=4,
            maximum_temperature_c=38,
        ),
        make_sample(
            day=5,
            maximum_temperature_c=33,
        ),
    ]

    events = detect_heatwave_events(
        samples=samples,
        temperature_threshold_c=35,
        minimum_consecutive_days=3,
    )

    assert len(events) == 1
    assert events[0].duration_days == 3
    assert (
        events[0].peak_air_temperature_c
        == 38
    )


@pytest.mark.unit
def test_non_consecutive_hot_days_are_not_heatwave():
    samples = [
        make_sample(
            day=1,
            maximum_temperature_c=36,
        ),
        make_sample(
            day=3,
            maximum_temperature_c=37,
        ),
        make_sample(
            day=4,
            maximum_temperature_c=38,
        ),
    ]

    events = detect_heatwave_events(
        samples=samples,
        temperature_threshold_c=35,
        minimum_consecutive_days=3,
    )

    assert events == []