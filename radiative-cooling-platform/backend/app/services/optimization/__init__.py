"""Exposure-weighted performance metrics of one garment over prepared samples."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from app.schemas.optimization import EvaluationMetrics
from app.schemas.simulation import ScenarioResult
from app.services.exposure_statistics import time_weighted_mean
from app.services.scenario_summary import pair_scenarios


def fraction_above(minutes: Sequence[float], values: Sequence[float], threshold: float) -> float:
    """Exact time fraction a piecewise-linear series spends strictly above
    ``threshold``. Continuous in the data, so the optimizer sees a smooth-ish
    landscape instead of a step count."""
    t = np.asarray(minutes, dtype=float)
    y = np.asarray(values, dtype=float)

    if t.size == 0:
        return 0.0
    if t.size == 1 or t[-1] <= t[0]:
        return float(y[0] > threshold)

    above = 0.0
    for t0, t1, y0, y1 in zip(t[:-1], t[1:], y[:-1], y[1:]):
        dt = t1 - t0
        if y0 > threshold and y1 > threshold:
            above += dt
        elif y0 <= threshold and y1 <= threshold:
            continue
        else:
            crossing = (threshold - y0) / (y1 - y0)  # in [0, 1]
            above += dt * (1.0 - crossing) if y1 > threshold else dt * crossing

    return float(above / (t[-1] - t[0]))


def compute_metrics(
    pairs: Sequence[tuple[int, ScenarioResult, ScenarioResult]],
    *,
    skin_threshold_c: float,
    core_threshold_c: float,
) -> EvaluationMetrics:
    """``pairs`` = (weight_days, control, candidate) per sample day."""
    if not pairs:
        raise ValueError("compute_metrics requires at least one sample")

    weights = np.asarray([w for w, _, _ in pairs], dtype=float)
    mean_skin, skin_exc, core_exc, cooling_skin, cooling_core = [], [], [], [], []
    peak_skin = peak_core = -np.inf

    for _, control, candidate in pairs:
        minutes = [p.minute for p in candidate.time_series]
        skin = [p.skin_temperature_c for p in candidate.time_series]
        core = [p.core_temperature_c for p in candidate.time_series]

        mean_skin.append(time_weighted_mean(minutes, skin))
        skin_exc.append(fraction_above(minutes, skin, skin_threshold_c))
        core_exc.append(fraction_above(minutes, core, core_threshold_c))

        paired = pair_scenarios(control, candidate)
        cooling_skin.append(paired.average_skin_c)
        cooling_core.append(paired.average_core_c)

        peak_skin = max(peak_skin, candidate.peak_skin_temperature_c)
        peak_core = max(peak_core, candidate.peak_core_temperature_c)

    def weighted(values: list[float]) -> float:
        return float(np.average(values, weights=weights))

    return EvaluationMetrics(
        sample_count=len(pairs),
        mean_skin_temperature_c=round(weighted(mean_skin), 5),
        peak_skin_temperature_c=round(float(peak_skin), 5),
        peak_core_temperature_c=round(float(peak_core), 5),
        skin_exceedance_fraction=round(weighted(skin_exc), 6),
        core_exceedance_fraction=round(weighted(core_exc), 6),
        mean_skin_cooling_c=round(weighted(cooling_skin), 5),
        mean_core_cooling_c=round(weighted(cooling_core), 5),
    )