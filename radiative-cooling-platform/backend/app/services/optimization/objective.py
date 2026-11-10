"""Scalarisation: signed objective + exterior penalty on metric constraints."""

from __future__ import annotations

from app.schemas.optimization import EvaluationMetrics, MetricConstraint, OptimizationCreate


PENALTY_WEIGHT = 1000.0
INVALID_OBJECTIVE = 1.0e6
FEASIBILITY_TOLERANCE = 1e-9


def metric_value(metrics: EvaluationMetrics, name: str) -> float:
    return float(getattr(metrics, name))


def constraint_violation(metrics: EvaluationMetrics, constraints: list[MetricConstraint]) -> float:
    total = 0.0
    for c in constraints:
        value = metric_value(metrics, c.metric)
        total += max(0.0, value - c.threshold) if c.operator == "<=" else max(0.0, c.threshold - value)
    return total


def penalised_objective(metrics: EvaluationMetrics | None, request: OptimizationCreate) -> float:
    if metrics is None:
        return INVALID_OBJECTIVE
    sign = 1.0 if request.objective.sense == "minimize" else -1.0
    value = sign * metric_value(metrics, request.objective.metric)
    return value + PENALTY_WEIGHT * constraint_violation(metrics, request.constraints)


def is_feasible(metrics: EvaluationMetrics | None, request: OptimizationCreate) -> bool:
    return metrics is not None and (
        constraint_violation(metrics, request.constraints) <= FEASIBILITY_TOLERANCE
    )