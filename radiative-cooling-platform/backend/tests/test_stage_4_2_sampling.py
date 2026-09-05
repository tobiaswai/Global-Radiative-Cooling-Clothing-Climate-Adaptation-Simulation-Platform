import pytest

from app.services.climate_adaptation import (
    build_weighted_sample_days,
)


@pytest.mark.unit
def test_three_samples_cover_entire_month():
    samples = build_weighted_sample_days(
        days_in_month=31,
        sample_count=3,
    )

    assert len(samples) == 3

    assert sum(
        weight
        for _, weight in samples
    ) == 31

    assert samples == sorted(
        samples,
        key=lambda item: item[0],
    )


@pytest.mark.unit
def test_one_legacy_sample_uses_requested_day():
    samples = build_weighted_sample_days(
        days_in_month=30,
        sample_count=1,
        legacy_representative_day=15,
    )

    assert samples == [
        (15, 30),
    ]


@pytest.mark.unit
def test_sample_count_cannot_exceed_month_days():
    samples = build_weighted_sample_days(
        days_in_month=3,
        sample_count=7,
    )

    assert len(samples) == 3

    assert sum(
        weight
        for _, weight in samples
    ) == 3