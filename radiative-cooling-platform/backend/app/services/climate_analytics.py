from __future__ import annotations

import math
from datetime import timedelta
from typing import Iterable

from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    HeatwaveEvent,
)


def weighted_percentile(
    values: Iterable[tuple[float, int]],
    percentile: float,
) -> float | None:
    normalized = sorted(
        (
            float(value),
            int(weight),
        )
        for value, weight in values
        if weight > 0 and math.isfinite(value)
    )

    if not normalized:
        return None

    if percentile < 0.0 or percentile > 100.0:
        raise ValueError(
            "percentile must be between 0 and 100"
        )

    total_weight = sum(
        weight
        for _, weight in normalized
    )

    target_weight = (
        percentile
        / 100.0
        * total_weight
    )

    cumulative_weight = 0

    for value, weight in normalized:
        cumulative_weight += weight

        if cumulative_weight >= target_weight:
            return value

    return normalized[-1][0]


def round_optional(
    value: float | None,
    digits: int = 4,
) -> float | None:
    if value is None:
        return None

    return round(value, digits)


def build_heatwave_event(
    samples: list[DailyAdaptationResult],
) -> HeatwaveEvent:
    temperatures = [
        sample.maximum_air_temperature_c
        for sample in samples
    ]

    skin_improvements = [
        sample.average_skin_improvement_c
        for sample in samples
    ]

    p90 = weighted_percentile(
        (
            (
                improvement,
                1,
            )
            for improvement in skin_improvements
        ),
        percentile=90,
    )

    return HeatwaveEvent(
        start_date_local=samples[0].sample_date_local,
        end_date_local=samples[-1].sample_date_local,
        duration_days=len(samples),
        mean_maximum_air_temperature_c=round(
            sum(temperatures) / len(temperatures),
            4,
        ),
        peak_air_temperature_c=round(
            max(temperatures),
            4,
        ),
        mean_skin_improvement_c=round(
            sum(skin_improvements)
            / len(skin_improvements),
            4,
        ),
        p90_skin_improvement_c=round(
            p90 or 0.0,
            4,
        ),
        beneficial_day_count=sum(
            1
            for sample in samples
            if sample.beneficial
        ),
    )


def detect_heatwave_events(
    *,
    samples: list[DailyAdaptationResult],
    temperature_threshold_c: float,
    minimum_consecutive_days: int,
) -> list[HeatwaveEvent]:
    ordered_samples = sorted(
        samples,
        key=lambda sample: sample.sample_date_local,
    )

    events: list[HeatwaveEvent] = []
    current_event: list[DailyAdaptationResult] = []

    def flush_event() -> None:
        nonlocal current_event

        if (
            len(current_event)
            >= minimum_consecutive_days
        ):
            events.append(
                build_heatwave_event(
                    current_event
                )
            )

        current_event = []

    for sample in ordered_samples:
        qualifies = (
            sample.maximum_air_temperature_c
            >= temperature_threshold_c
        )

        if not qualifies:
            flush_event()
            continue

        if current_event:
            expected_date = (
                current_event[-1].sample_date_local
                + timedelta(days=1)
            ).date()

            if (
                sample.sample_date_local.date()
                != expected_date
            ):
                flush_event()

        current_event.append(sample)

    flush_event()

    return events


def build_city_analytics(
    *,
    samples: list[DailyAdaptationResult],
    request: GlobalBatchCreate,
) -> dict:
    eligible_samples = [
        sample
        for sample in samples
        if sample.exposure_eligible
    ]

    skin_values = [
        (
            sample.average_skin_improvement_c,
            sample.weight_days,
        )
        for sample in eligible_samples
    ]

    core_values = [
        (
            sample.average_core_improvement_c,
            sample.weight_days,
        )
        for sample in eligible_samples
    ]

    heatwave_available = (
        request.enable_heatwave_analysis
        and request.analysis_resolution == "daily"
        and request.daily_stride_days == 1
    )

    heatwave_events: list[HeatwaveEvent] = []

    if heatwave_available:
        heatwave_events = detect_heatwave_events(
            samples=samples,
            temperature_threshold_c=(
                request
                .heatwave_temperature_threshold_c
            ),
            minimum_consecutive_days=(
                request
                .heatwave_minimum_consecutive_days
            ),
        )

    longest_heatwave_days = (
        max(
            event.duration_days
            for event in heatwave_events
        )
        if heatwave_events
        else 0
    )

    return {
        "skin_improvement_p50_c": round_optional(
            weighted_percentile(
                skin_values,
                50,
            )
        ),
        "skin_improvement_p90_c": round_optional(
            weighted_percentile(
                skin_values,
                90,
            )
        ),
        "skin_improvement_p95_c": round_optional(
            weighted_percentile(
                skin_values,
                95,
            )
        ),
        "core_improvement_p50_c": round_optional(
            weighted_percentile(
                core_values,
                50,
            )
        ),
        "core_improvement_p90_c": round_optional(
            weighted_percentile(
                core_values,
                90,
            )
        ),
        "core_improvement_p95_c": round_optional(
            weighted_percentile(
                core_values,
                95,
            )
        ),
        "heatwave_analysis_available": (
            heatwave_available
        ),
        "heatwave_event_count": (
            len(heatwave_events)
            if heatwave_available
            else None
        ),
        "longest_heatwave_days": (
            longest_heatwave_days
            if heatwave_available
            else None
        ),
        "heatwave_events": [
            event.model_dump(
                mode="json"
            )
            for event in heatwave_events
        ],
    }