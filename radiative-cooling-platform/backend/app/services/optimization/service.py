"""End-to-end optimization: baseline, DE search, passive limit, requirement map."""

from __future__ import annotations

import calendar
from collections.abc import Callable
from time import perf_counter

from app.schemas.optimization import (
    CandidateEvaluation,
    OptimizationCreate,
    OptimizationEstimate,
    OptimizationResult,
    SkippedOptimizationSample,
)
from app.services.optimization.evaluator import MaterialEvaluator, PreparationReport
from app.services.optimization.objective import constraint_violation, is_feasible, metric_value
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.runner import run_differential_evolution
from app.services.optimization.search_space import build_search_space
from app.services.reproducibility import parameter_fingerprint
from app.services.two_node import MODEL_VERSION


Reporter = Callable[..., None]  # (progress=, stage=, history_record=, force=)


def estimate_optimization(request: OptimizationCreate) -> OptimizationEstimate:
    n = len(request.variables)
    population = request.population_multiplier * n
    optimizer = population * (request.max_generations + 1)
    grid = request.requirement_map.resolution ** 2 if request.requirement_map else 0
    samples = sum(
        min(request.sample_days_per_month, calendar.monthrange(request.year, m)[1])
        for m in request.months
    )
    # +2: baseline and optical upper bound. +1: control garment once per sample.
    return OptimizationEstimate(
        variable_count=n,
        population_size=population,
        optimizer_evaluation_budget=optimizer,
        requirement_map_evaluations=grid,
        sample_count=samples,
        thermal_simulation_budget=(optimizer + grid + 2 + 1) * samples,
        weather_requests=len(request.months),
    )


def evaluate_candidate(
    evaluator: MaterialEvaluator, request: OptimizationCreate, parameters: dict[str, float]
) -> CandidateEvaluation:
    metrics = evaluator.evaluate(evaluator.vector(parameters))
    return CandidateEvaluation(
        parameters={k: round(v, 6) for k, v in parameters.items()},
        metrics=metrics,
        objective_value=None if metrics is None else metric_value(metrics, request.objective.metric),
        constraint_violation=None if metrics is None else constraint_violation(metrics, request.constraints),
        feasible=is_feasible(metrics, request),
    )


def _verdict(request, best, upper) -> tuple[str, str]:
    metric = request.objective.metric
    if not request.constraints:
        return "unconstrained", (
            f"No constraints were given; best {metric} = {best.objective_value:.4f}."
        )
    if best.feasible:
        return "feasible", (
            f"All constraints satisfied. Best {metric} = {best.objective_value:.4f}."
        )
    text = (
        "No candidate inside the bounds satisfies the constraints "
        f"(smallest total violation {best.constraint_violation:.4f})."
    )
    if upper is not None and not upper.feasible:
        text += (
            " Even with reflectance/emissivity at their upper bounds the violation "
            f"is {upper.constraint_violation:.4f}: the target is beyond the passive "
            "radiative-cooling limit of this model for this climate and activity."
        )
    return "infeasible", text


def execute_optimization(
    request: OptimizationCreate,
    evaluator: MaterialEvaluator,
    preparation: PreparationReport,
    *,
    report: Reporter | None = None,
) -> OptimizationResult:
    started = perf_counter()

    def progress(value: int, stage: str, **extra) -> None:
        if report is not None:
            report(progress=value, stage=stage, **extra)

    space = build_search_space(request)
    base = request.base_material

    progress(20, "evaluating_baseline", force=True)
    baseline = evaluate_candidate(
        evaluator, request, {n: float(getattr(base, n)) for n in space.names}
    )

    generations = request.max_generations
    outcome = run_differential_evolution(
        evaluator, request, space=space,
        on_generation=lambda record: progress(
            20 + round(65 * min(record.generation, generations) / generations),
            f"generation_{record.generation}",
            history_record=record,
            force=True,
        ),
    )
    best = evaluate_candidate(evaluator, request, evaluator.parameters(outcome.x))

    optical_upper = None
    optical = [n for n in ("solar_reflectance", "infrared_emissivity") if n in space.names]
    if optical:
        parameters = dict(best.parameters)
        for name in optical:
            parameters[name] = float(space.upper[space.index(name)])
        optical_upper = evaluate_candidate(evaluator, request, parameters)

    requirement_map = None
    if request.requirement_map is not None:
        progress(86, "building_requirement_map", force=True)
        requirement_map = build_requirement_map(
            evaluator, request, best.parameters, space=space,
            on_cell=lambda done, total: progress(86 + round(12 * done / total), "building_requirement_map"),
        )

    verdict, message = _verdict(request, best, optical_upper)

    return OptimizationResult(
        verdict=verdict,
        message=message,
        objective=request.objective,
        constraints=request.constraints,
        best=best,
        baseline=baseline,
        optical_upper_bound=optical_upper,
        requirement_map=requirement_map,
        sample_count=len(preparation.samples),
        skipped_samples=[SkippedOptimizationSample.model_validate(s) for s in preparation.skipped],
        weather_payload_sha256=preparation.weather_payload_sha256,
        evaluation_count=evaluator.evaluation_count,
        simulation_count=evaluator.simulation_count + len(preparation.samples),
        generations=outcome.generations,
        algorithm=request.algorithm,
        algorithm_message=outcome.message,
        elapsed_seconds=round(perf_counter() - started, 3),
        model_version=MODEL_VERSION,
        parameter_fingerprint=parameter_fingerprint(request.environment_assumptions),
    )