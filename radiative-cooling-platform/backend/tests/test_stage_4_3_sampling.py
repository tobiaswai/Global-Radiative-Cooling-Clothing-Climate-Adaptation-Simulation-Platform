import calendar

import pytest

from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)
from app.services.annual_sampling import (
    build_daily_stride_sample_days,
    build_month_sampling_plan,
    estimate_sample_count,
)


def make_request(
    *,
    resolution: str,
    stride: int = 1,
) -> GlobalBatchCreate:
    person = PersonInput(
        met=2.0,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )

    control = MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.3,
        solar_transmittance=0,
        infrared_emissivity=0.9,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    radiative = MaterialInput(
        name="Radiative cooling",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    return GlobalBatchCreate(
        city_ids=["dubai"],
        year=2024,
        start_month=1,
        end_month=12,
        analysis_resolution=resolution,
        daily_stride_days=stride,
        person=person,
        control_material=control,
        rc_material=radiative,
    )


@pytest.mark.unit
def test_daily_stride_one_has_one_sample_per_day():
    samples = build_daily_stride_sample_days(
        days_in_month=31,
        stride_days=1,
    )

    assert len(samples) == 31

    assert all(
        weight == 1
        for _, weight in samples
    )

    assert sum(
        weight
        for _, weight in samples
    ) == 31


@pytest.mark.unit
def test_daily_stride_seven_covers_month():
    samples = build_daily_stride_sample_days(
        days_in_month=31,
        stride_days=7,
    )

    assert len(samples) == 5

    assert sum(
        weight
        for _, weight in samples
    ) == 31


@pytest.mark.unit
def test_leap_year_daily_plan_has_366_samples():
    request = make_request(
        resolution="daily",
        stride=1,
    )

    assert calendar.isleap(
        request.year
    )

    assert estimate_sample_count(
        request
    ) == 366


@pytest.mark.unit
def test_month_plan_returns_actual_dates():
    request = make_request(
        resolution="daily",
        stride=1,
    )

    plan = build_month_sampling_plan(
        request=request,
        month=2,
    )

    assert len(plan) == 29
    assert plan[0].date_local.day == 1
    assert plan[-1].date_local.day == 29