"""Differential evolution over the decision vector (scipy)."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Protocol, Sequence

import numpy as np
from scipy.optimize import LinearConstraint, differential_evolution

from app.schemas.optimization import EvaluationMetrics, GenerationRecord, OptimizationCreate
from app.services.optimization.objective import ObjectiveFunction, is_feasible, objective_value
from app.services.optimization.search_space import SearchSpace, build_search_space


class OptimizationCancelled(Exception):
    pass


class Evaluator(Protocol):
    evaluation_count: int

    def evaluate(self, x: Sequence[float]) -> EvaluationMetrics | None: ...
    def parameters(self, x: Sequence[float]) -> dict[str, float]: ...


@dataclass
class DifferentialEvolutionOutcome:
    x: np.ndarray
    fun: float
    message: str
    generations: int
    history: list[GenerationRecord] = field(default_factory=list)


def run_differential_evolution(
    evaluator: Evaluator,
    request: OptimizationCreate,
    *,
    space: SearchSpace | None = None,
    objective: ObjectiveFunction | None = None,
    on_generation: Callable[[GenerationRecord], None] | None = None,
) -> DifferentialEvolutionOutcome:
    space = space or build_search_space(request)
    objective = objective or ObjectiveFunction(request)
    history: list[GenerationRecord] = []

    def fun(x: np.ndarray) -> float:
        return objective(evaluator.evaluate(x), evaluator.parameters(x))

    def callback(intermediate_result) -> None:
        x = np.asarray(intermediate_result.x, dtype=float)
        metrics = evaluator.evaluate(x)  # memoised; no extra physics
        parameters = evaluator.parameters(x)
        record = GenerationRecord(
            generation=len(history) + 1,
            penalised_objective=float(intermediate_result.fun),
            best_parameters=parameters,
            best_metric_value=(
                None if metrics is None else objective_value(metrics, parameters, request)
            ),
            best_feasible=is_feasible(metrics, request),
            evaluation_count=evaluator.evaluation_count,
        )
        history.append(record)
        if on_generation is not None:
            on_generation(record)  # may raise OptimizationCancelled

    constraints = ()
    if space.linear_pairs:
        matrix = np.zeros((len(space.linear_pairs), len(space.names)))
        for row, (i, j) in enumerate(space.linear_pairs):
            matrix[row, i] = matrix[row, j] = 1.0
        constraints = (LinearConstraint(matrix, -np.inf, 1.0),)

    # Stage 10: the objective is normalised (order one, reference = baseline),
    # so convergence is purely absolute. tol=0 removes the relative term that
    # stopped earlier runs after one generation on a ~39.5 C objective.
    result = differential_evolution(
        fun,
        bounds=list(zip(space.lower, space.upper)),
        constraints=constraints,
        popsize=request.population_multiplier,
        maxiter=request.max_generations,
        rng=np.random.default_rng(request.seed),
        init="latinhypercube",
        updating="immediate",
        polish=False,
        tol=0.0,
        atol=request.convergence_tolerance,
        callback=callback,
    )

    return DifferentialEvolutionOutcome(
        x=np.asarray(result.x, dtype=float),
        fun=float(result.fun),
        message=str(result.message),
        generations=len(history),
        history=history,
    )