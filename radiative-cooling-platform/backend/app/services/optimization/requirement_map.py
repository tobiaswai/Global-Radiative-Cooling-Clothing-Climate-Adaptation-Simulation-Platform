"""Grid over two decision variables with the others fixed at the optimum."""

from __future__ import annotations

from collections.abc import Callable

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

    xi, yi = space.index(spec.x_variable), space.index(spec.y_variable)
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
                    metric_value=metric_value(metrics, request.objective.metric),
                    constraint_violation=constraint_violation(metrics, request.constraints),
                    feasible=is_feasible(metrics, request),
                ))
            done += 1
            if on_cell is not None:
                on_cell(done, total)
        cells.append(row)

    frontier = [
        FrontierPoint(
            y=round(float(y), 6),
            minimum_x=next((c.x for c in row if c is not None and c.feasible), None),
        )
        for y, row in zip(ys, cells)
    ]
    last_column = [row[-1] for row in cells]

    return RequirementMapResult(
        x_variable=spec.x_variable,
        y_variable=spec.y_variable,
        x_values=[round(float(v), 6) for v in xs],
        y_values=[round(float(v), 6) for v in ys],
        cells=cells,
        frontier=frontier,
        minimum_x_at_max_y=frontier[-1].minimum_x,
        minimum_y_at_max_x=next((c.y for c in last_column if c is not None and c.feasible), None),
        fixed_parameters={k: v for k, v in fixed_parameters.items()
                          if k not in (spec.x_variable, spec.y_variable)},
    )