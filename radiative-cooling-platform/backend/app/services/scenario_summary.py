"""Shared control-vs-RC summary (Stage 6, PR-1a).

Every entry point that compares a control garment with a radiative-cooling
garment -- fixed environment (/simulations/run), single weather run
(/simulations/run-weather, Celery job) and annual sampling
(climate_adaptation) -- must build its summary here. "Average improvement"
therefore has exactly one meaning: the time-weighted (trapezoidal) mean of
the paired temperature difference over the exposure window.

The two series are paired point by point and must share the same time axis;
equal length alone is not sufficient.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import ScenarioResult, SimulationSummary
from app.services.exposure_statistics import time_weighted_mean


AVERAGING_METHOD = "time_weighted_trapezoid"
PAIRING_TOLERANCE_MINUTES = 1e-6


class ScenarioPairingError(ValueError):
    """Control and RC time series do not share the same time axis."""


@dataclass(frozen=True)
class PairedImprovement:
    """control - rc at every shared output time (positive = RC is cooler)."""

    minutes: list[float]
    skin_c: list[float]
    core_c: list[float]

    @property
    def average_skin_c(self) -> float:
        return time_weighted_mean(self.minutes, self.skin_c)

    @property
    def average_core_c(self) -> float:
        return time_weighted_mean(self.minutes, self.core_c)

    @property
    def final_skin_c(self) -> float:
        return self.skin_c[-1]

    @property
    def final_core_c(self) -> float:
        return self.core_c[-1]

    @property
    def maximum_skin_c(self) -> float:
        return max(self.skin_c)


def pair_scenarios(control: ScenarioResult, rc: ScenarioResult) -> PairedImprovement:
    control_points = control.time_series
    rc_points = rc.time_series

    if not control_points or not rc_points:
        raise ScenarioPairingError("Cannot summarise an empty time series")

    if len(control_points) != len(rc_points):
        raise ScenarioPairingError(
            f"Series length mismatch: {len(control_points)} control vs "
            f"{len(rc_points)} radiative-cooling points"
        )

    minutes: list[float] = []
    skin: list[float] = []
    core: list[float] = []

    for index, (c, r) in enumerate(zip(control_points, rc_points, strict=True)):
        if abs(c.minute - r.minute) > PAIRING_TOLERANCE_MINUTES:
            raise ScenarioPairingError(
                f"Time axis mismatch at index {index}: "
                f"control minute {c.minute} vs RC minute {r.minute}"
            )
        minutes.append(c.minute)
        skin.append(c.skin_temperature_c - r.skin_temperature_c)
        core.append(c.core_temperature_c - r.core_temperature_c)

    return PairedImprovement(minutes=minutes, skin_c=skin, core_c=core)


def build_simulation_summary(
    control: ScenarioResult,
    rc: ScenarioResult,
) -> SimulationSummary:
    paired = pair_scenarios(control, rc)

    return SimulationSummary(
        final_skin_temperature_improvement_c=round(paired.final_skin_c, 4),
        final_core_temperature_improvement_c=round(paired.final_core_c, 4),
        average_skin_temperature_improvement_c=round(paired.average_skin_c, 4),
        averaging_method=AVERAGING_METHOD,
    )