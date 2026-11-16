"""Grid over two decision variables with the others fixed at the reported optimum."""

from __future__ import annotations

from collections.abc import Callable, Iterable

import numpy as np

from app.schemas.optimization import (
    FrontierPoint,
    OptimizationCreate,
    RequirementCell,
    RequirementMapResult,
)
from app.services.optimization.objective import constraint_violation, is_feasible, metric_value
from app.services.optimization.runner import Evaluator
from app.services.optimization.search_space import SearchSpace


TREND_RELATIVE_TOLERANCE = 1e-3   # of the map metric range; ignores solver noise
PLATEAU_TOLERANCE = 1e-6


def map_metric(request: OptimizationCreate) -> tuple[str, str]:
    """(metric, sense) drawn on the map. material_demand is not a physical metric."""
    if request.objective.metric != "material_demand":
        return request.objective.metric, request.objective.sense
    if request.constraints:
        first = request.constraints[0]
        return first.metric, ("minimize" if first.operator == "<=" else "maximize")
    return "skin_excess_degree_hours", "minimize"


def _least_demanding_feasible(
    values: np.ndarray, line: list[RequirementCell | None], direction: str
) -> float | None:
    order = range(len(values)) if direction == "increasing" else reversed(range(len(values)))
    for i in order:
        cell = line[i]
        if cell is not None and cell.feasible:
            return round(float(values[i]), 6)
    return None


def _most_lenient(values: Iterable[float | None], direction: str) -> float | None:
    present = [v for v in values if v is not None]
    if not present:
        return None
    return min(present) if direction == "increasing" else max(present)


def _trend(
    lines: list[list[RequirementCell | None]], direction: str, sense: str, tolerance: float
) -> str:
    seen: set[str] = set()
    for line in lines:
        ordered = line if direction == "increasing" else list(reversed(line))
        values = [c.metric_value for c in ordered if c is not None]
        for a, b in zip(values, values[1:]):
            gain = (a - b) if sense == "minimize" else (b - a)
            if gain > tolerance:
                seen.add("improves")
            elif gain < -tolerance:
                seen.add("worsens")
    if not seen:
        return "flat"
    return seen.pop() if len(seen) == 1 else "mixed"


def build_requirement_map(
    evaluator: Evaluator,
    request: OptimizationCreate,
    fixed_parameters: dict[str, float],
    *,
    space: SearchSpace,
    on_cell: Callable[[int, int], None] | None = None,
) -> RequirementMapResult:
    spec = request.requirement_map
    if spec is None:
        raise ValueError("request has no requirement_map")

    metric_name, sense = map_metric(request)
    xi, yi = space.index(spec.x_variable), space.index(spec.y_variable)
    x_dir, y_dir = space.directions[xi], space.directions[yi]
    xs = np.linspace(space.lower[xi], space.upper[xi], spec.resolution)
    ys = np.linspace(space.lower[yi], space.upper[yi], spec.resolution)
    total = len(xs) * len(ys)

    cells: list[list[RequirementCell | None]] = []
    done = 0
    for y in ys:
        row: list[RequirementCell | None] = []
        for x in xs:
            parameters = {**fixed_parameters, spec.x_variable: float(x), spec.y_variable: float(y)}
            metrics = evaluator.evaluate([parameters[n] for n in space.names])
            if metrics is None:
                row.append(None)
            else:
                row.append(RequirementCell(
                    x=round(float(x), 6),
                    y=round(float(y), 6),
                    metric_value=metric_value(metrics, metric_name),
                    constraint_violation=constraint_violation(metrics, request.constraints),
                    feasible=is_feasible(metrics, request),
                ))
            done += 1
            if on_cell is not None:
                on_cell(done, total)
        cells.append(row)

    columns = [[cells[j][i] for j in range(len(ys))] for i in range(len(xs))]

    frontier: list[FrontierPoint] = []
    for y, row in zip(ys, cells):
        required = _least_demanding_feasible(xs, row, x_dir)
        frontier.append(FrontierPoint(y=round(float(y), 6), minimum_x=required, required_x=required))

    required_y_per_column = [_least_demanding_feasible(ys, column, y_dir) for column in columns]

    values = [c.metric_value for row in cells for c in row if c is not None]
    metric_min = min(values) if values else None
    metric_max = max(values) if values else None
    spread = (metric_max - metric_min) if values else 0.0
    tolerance = TREND_RELATIVE_TOLERANCE * spread + 1e-12
    plateau = (
        sum(abs(v - metric_min) <= PLATEAU_TOLERANCE * (1.0 + abs(metric_min)) for v in values) / len(values)
        if values else None
    )

    return RequirementMapResult(
        x_variable=spec.x_variable,
        y_variable=spec.y_variable,
        x_values=[round(float(v), 6) for v in xs],
        y_values=[round(float(v), 6) for v in ys],
        cells=cells,
        frontier=frontier,
        # Legacy readings (y at its upper bound / x at its upper bound).
        minimum_x_at_max_y=frontier[-1].required_x,
        minimum_y_at_max_x=required_y_per_column[-1],
        fixed_parameters={k: v for k, v in fixed_parameters.items()
                          if k not in (spec.x_variable, spec.y_variable)},
        x_demand_direction=x_dir,
        y_demand_direction=y_dir,
        required_x_at_best_y=_most_lenient((p.required_x for p in frontier), x_dir),
        required_y_at_best_x=_most_lenient(required_y_per_column, y_dir),
        objective_trend_x=_trend(cells, x_dir, sense, tolerance) if values else None,
        objective_trend_y=_trend(columns, y_dir, sense, tolerance) if values else None,
        plateau_fraction=plateau,
        metric_min=metric_min,
        metric_max=metric_max,
    )