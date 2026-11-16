"""Scalarisation (Stage 10): feasibility-first ranking in normalised units.

* Constraint violations are divided by a per-metric scale before summing.
* Feasible:   sign * (value - reference) / scale + w * material_demand
* Infeasible: INFEASIBLE_OFFSET + normalised violation
The reference is the baseline garment, so DE tolerances act on differences of
order one rather than on the absolute magnitude of e.g. 39.5 C.
"""

from __future__ import annotations

from app.schemas.optimization import EvaluationMetrics, MetricConstraint, OptimizationCreate
from app.services.optimization.variables import demand_direction


METRIC_SCALES: dict[str, float] = {
    "mean_skin_temperature_c": 1.0,
    "peak_skin_temperature_c": 1.0,
    "peak_core_temperature_c": 1.0,
    "skin_exceedance_fraction": 0.1,
    "core_exceedance_fraction": 0.1,
    "skin_excess_degree_hours": 0.5,
    "core_excess_degree_hours": 0.5,
    "mean_skin_cooling_c": 1.0,
    "mean_core_cooling_c": 1.0,
    "material_demand": 0.1,
}

INVALID_OBJECTIVE = 1.0e6
INFEASIBLE_OFFSET = 1.0e3
FEASIBILITY_TOLERANCE = 1e-9


def metric_value(metrics: EvaluationMetrics, name: str) -> float:
    value = getattr(metrics, name)
    if value is None:
        raise ValueError(f"metric {name} is not available on this result")
    return float(value)


def constraint_label(constraint: MetricConstraint) -> str:
    return f"{constraint.metric} {constraint.operator} {constraint.threshold:g}"


def constraint_scale(constraint: MetricConstraint) -> float:
    return constraint.scale if constraint.scale is not None else METRIC_SCALES[constraint.metric]


def signed_excess(metrics: EvaluationMetrics, constraint: MetricConstraint) -> float:
    value = metric_value(metrics, constraint.metric)
    return value - constraint.threshold if constraint.operator == "<=" else constraint.threshold - value


def constraint_excess(metrics: EvaluationMetrics, constraints: list[MetricConstraint]) -> dict[str, float]:
    return {constraint_label(c): round(signed_excess(metrics, c), 6) for c in constraints}


def constraint_violation(metrics: EvaluationMetrics, constraints: list[MetricConstraint]) -> float:
    return sum(max(0.0, signed_excess(metrics, c)) / constraint_scale(c) for c in constraints)


def material_demand(parameters: dict[str, float], request: OptimizationCreate) -> float:
    """0 = every variable at its least demanding bound, 1 = all at the most demanding."""
    total = weight = 0.0
    for variable in request.variables:
        span = variable.upper - variable.lower
        x = parameters[variable.name]
        if demand_direction(variable) == "increasing":
            normalised = (x - variable.lower) / span
        else:
            normalised = (variable.upper - x) / span
        total += variable.demand_weight * min(1.0, max(0.0, normalised))
        weight += variable.demand_weight
    return total / weight


def objective_value(
    metrics: EvaluationMetrics, parameters: dict[str, float], request: OptimizationCreate
) -> float:
    if request.objective.metric == "material_demand":
        return material_demand(parameters, request)
    return metric_value(metrics, request.objective.metric)


def is_feasible(metrics: EvaluationMetrics | None, request: OptimizationCreate) -> bool:
    return metrics is not None and (
        constraint_violation(metrics, request.constraints) <= FEASIBILITY_TOLERANCE
    )


class ObjectiveFunction:
    def __init__(self, request: OptimizationCreate, reference: float = 0.0) -> None:
        self.request = request
        self.sign = 1.0 if request.objective.sense == "minimize" else -1.0
        self.scale = METRIC_SCALES[request.objective.metric]
        self.reference = reference
        self.demand_weight = (
            0.0 if request.objective.metric == "material_demand" else request.secondary_demand_weight
        )

    def __call__(self, metrics: EvaluationMetrics | None, parameters: dict[str, float]) -> float:
        if metrics is None:
            return INVALID_OBJECTIVE

        violation = constraint_violation(metrics, self.request.constraints)
        if violation > FEASIBILITY_TOLERANCE:
            return INFEASIBLE_OFFSET + violation

        value = self.sign * (objective_value(metrics, parameters, self.request) - self.reference) / self.scale
        value += self.demand_weight * material_demand(parameters, self.request)
        return min(value, INFEASIBLE_OFFSET - 1.0)