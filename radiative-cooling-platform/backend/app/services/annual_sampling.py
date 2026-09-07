import calendar
import math
from dataclasses import dataclass
from datetime import date

from app.schemas.global_batch import (
    GlobalBatchCreate,
)


@dataclass(frozen=True)
class SamplingDay:
    date_local: date
    weight_days: int


def assign_nearest_day_weights(
    *,
    days_in_month: int,
    sample_days: list[int],
) -> list[tuple[int, int]]:
    if days_in_month < 1:
        raise ValueError(
            "days_in_month must be at least 1"
        )

    normalized_days = sorted(
        {
            max(
                1,
                min(days_in_month, day),
            )
            for day in sample_days
        }
    )

    if not normalized_days:
        raise ValueError(
            "sample_days cannot be empty"
        )

    weights = {
        day: 0
        for day in normalized_days
    }

    for calendar_day in range(
        1,
        days_in_month + 1,
    ):
        nearest_sample = min(
            normalized_days,
            key=lambda sample_day: (
                abs(sample_day - calendar_day),
                sample_day,
            ),
        )

        weights[nearest_sample] += 1

    return [
        (
            sample_day,
            weights[sample_day],
        )
        for sample_day in normalized_days
    ]


def build_weighted_sample_days(
    *,
    days_in_month: int,
    sample_count: int,
    legacy_representative_day: int | None = None,
) -> list[tuple[int, int]]:
    sample_count = max(
        1,
        min(sample_count, days_in_month),
    )

    if (
        sample_count == 1
        and legacy_representative_day is not None
    ):
        sample_days = [
            min(
                legacy_representative_day,
                days_in_month,
            )
        ]
    else:
        sample_days: list[int] = []

        for index in range(sample_count):
            sample_day = round(
                (index + 0.5)
                * days_in_month
                / sample_count
            )

            sample_day = max(
                1,
                min(days_in_month, sample_day),
            )

            if sample_day not in sample_days:
                sample_days.append(sample_day)

        candidate = 1

        while len(sample_days) < sample_count:
            if candidate not in sample_days:
                sample_days.append(candidate)

            candidate += 1

        sample_days.sort()

    return assign_nearest_day_weights(
        days_in_month=days_in_month,
        sample_days=sample_days,
    )


def build_daily_stride_sample_days(
    *,
    days_in_month: int,
    stride_days: int,
) -> list[tuple[int, int]]:
    stride_days = max(
        1,
        min(stride_days, 7),
    )

    sample_days = list(
        range(
            1,
            days_in_month + 1,
            stride_days,
        )
    )

    return assign_nearest_day_weights(
        days_in_month=days_in_month,
        sample_days=sample_days,
    )


def build_month_sampling_plan(
    *,
    request: GlobalBatchCreate,
    month: int,
) -> list[SamplingDay]:
    days_in_month = calendar.monthrange(
        request.year,
        month,
    )[1]

    if request.analysis_resolution == "daily":
        weighted_days = (
            build_daily_stride_sample_days(
                days_in_month=days_in_month,
                stride_days=request.daily_stride_days,
            )
        )
    else:
        weighted_days = build_weighted_sample_days(
            days_in_month=days_in_month,
            sample_count=(
                request.sample_days_per_month
            ),
            legacy_representative_day=(
                request.representative_day
            ),
        )

    return [
        SamplingDay(
            date_local=date(
                request.year,
                month,
                day,
            ),
            weight_days=weight,
        )
        for day, weight in weighted_days
    ]


def build_annual_sampling_plan(
    request: GlobalBatchCreate,
) -> list[SamplingDay]:
    plan: list[SamplingDay] = []

    for month in range(
        request.start_month,
        request.end_month + 1,
    ):
        plan.extend(
            build_month_sampling_plan(
                request=request,
                month=month,
            )
        )

    return plan


def estimate_sample_count(
    request: GlobalBatchCreate,
) -> int:
    if request.analysis_resolution == "daily":
        return sum(
            math.ceil(
                calendar.monthrange(
                    request.year,
                    month,
                )[1]
                / request.daily_stride_days
            )
            for month in range(
                request.start_month,
                request.end_month + 1,
            )
        )

    return (
        request.end_month
        - request.start_month
        + 1
    ) * request.sample_days_per_month