"""End-to-end optimization (Stage 10).

Order: baseline -> differential evolution -> corners + most demanding design
-> requirement map -> best point -> sensitivity -> warnings -> verdict.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Sequence
from itertools import product
from time import perf_counter

from app.schemas.optimization import (
    CandidateEvaluation,
    EvaluationMetrics,
    OptimizationCreate,
    OptimizationEstimate,
    OptimizationResult,
    ParameterSensitivity,
    RequirementMapResult,
    SkippedOptimizationSample,
)
from app.services.optimization.evaluator import MaterialEvaluator, PreparationReport
from app.services.optimization.objective import (
    METRIC_SCALES,
    ObjectiveFunction,
    constraint_excess,
    constraint_label,
    constraint_violation,
    is_feasible,
    material_demand,
    objective_value,
)
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.runner import run_differential_evolution
from app.services.optimization.search_space import SearchSpace, build_search_space
from app.services.reproducibility import parameter_fingerprint
from app.services.two_node import MODEL_VERSION


Reporter = Callable[..., None]  # (progress=, stage=, history_record=, force=)

SENSITIVITY_STEP_FRACTION = 0.05
BOUND_TOLERANCE_FRACTION = 1e-3
PLATEAU_WARNING_FRACTION = 0.2
SATURATION_REACH_FRACTION = 0.25
FLAT_OBJECTIVE_FRACTION = 0.01

EFFECT_METRICS: tuple[str, ...] = (
    "mean_skin_temperature_c",
    "peak_skin_temperature_c",
    "peak_core_temperature_c",
    "skin_exceedance_fraction",
    "core_exceedance_fraction",
    "skin_excess_degree_hours",
    "core_excess_degree_hours",
    "mean_skin_cooling_c",
    "mean_core_cooling_c",
)


# --------------------------------------------------------------------------
# Estimate
# --------------------------------------------------------------------------

def estimate_optimization(request: OptimizationCreate) -> OptimizationEstimate:
    n = len(request.variables)
    population = request.population_multiplier * n
    optimizer = population * (request.max_generations + 1)
    grid = request.requirement_map.resolution ** 2 if request.requirement_map else 0
    corners = 2 ** n
    sensitivity = 2 * n
    samples = sum(request.samples_per_month(m) for m in request.months)
    candidates = optimizer + grid + corners + sensitivity + 2  # + baseline + most demanding
    return OptimizationEstimate(
        variable_count=n,
        population_size=population,
        optimizer_evaluation_budget=optimizer,
        requirement_map_evaluations=grid,
        sample_count=samples,
        thermal_simulation_budget=candidates * samples + samples,  # + control once per sample
        weather_requests=len(request.months),
        corner_evaluations=corners,
        sensitivity_evaluations=sensitivity,
    )


# --------------------------------------------------------------------------
# Candidates and ranking
# --------------------------------------------------------------------------

def candidate_from(
    parameters: dict[str, float],
    metrics: EvaluationMetrics | None,
    request: OptimizationCreate,
) -> CandidateEvaluation:
    rounded = {k: round(float(v), 6) for k, v in parameters.items()}
    demand = round(material_demand(parameters, request), 6)
    if metrics is None:
        return CandidateEvaluation(
            parameters=rounded, metrics=None, objective_value=None,
            constraint_violation=None, feasible=False, material_demand=demand,
        )
    return CandidateEvaluation(
        parameters=rounded,
        metrics=metrics,
        objective_value=objective_value(metrics, parameters, request),
        constraint_violation=round(constraint_violation(metrics, request.constraints), 6),
        feasible=is_feasible(metrics, request),
        constraint_excess=constraint_excess(metrics, request.constraints),
        material_demand=demand,
    )


def evaluate_candidate(
    evaluator: MaterialEvaluator,
    request: OptimizationCreate,
    parameters: dict[str, float],
) -> CandidateEvaluation:
    return candidate_from(parameters, evaluator.evaluate(evaluator.vector(parameters)), request)


def candidate_rank(candidate: CandidateEvaluation, request: OptimizationCreate) -> tuple:
    """Lower is better: feasible first, then violation, objective, demand."""
    if candidate.metrics is None or candidate.objective_value is None:
        return (2, math.inf, math.inf, math.inf)
    sign = -1.0 if request.objective.sense == "maximize" else 1.0
    objective = round(sign * candidate.objective_value, 9)
    demand = candidate.material_demand or 0.0
    if candidate.feasible:
        return (0, 0.0, objective, demand)
    return (1, candidate.constraint_violation or 0.0, objective, demand)


def rank_points(
    points: Sequence[tuple[dict[str, float], EvaluationMetrics]],
    request: OptimizationCreate,
) -> CandidateEvaluation | None:
    candidates = [candidate_from(p, m, request) for p, m in points]
    if not candidates:
        return None
    return min(candidates, key=lambda c: candidate_rank(c, request))


def best_evaluated(evaluator: MaterialEvaluator, request: OptimizationCreate) -> CandidateEvaluation | None:
    return rank_points(evaluator.cached_points(), request)


def corner_parameters(space: SearchSpace) -> list[dict[str, float]]:
    """All 2^n corners of the (tightened) search box."""
    return [
        dict(zip(space.names, map(float, combo)))
        for combo in product(*[(lo, hi) for lo, hi in zip(space.lower, space.upper)])
    ]


def most_demanding_parameters(space: SearchSpace) -> dict[str, float]:
    return {name: space.most_demanding_bound(name) for name in space.names}


# --------------------------------------------------------------------------
# Sensitivity
# --------------------------------------------------------------------------

def sensitivity_analysis(
    evaluator: MaterialEvaluator,
    space: SearchSpace,
    best_parameters: dict[str, float],
) -> list[ParameterSensitivity]:
    """Central difference at the optimum, scaled to each variable's full range.

    A probe that is physically impossible falls back to the centre point, so the
    estimate degrades to a one-sided difference instead of being dropped.
    """
    center = evaluator.evaluate(evaluator.vector(best_parameters))
    if center is None:
        return []

    out: list[ParameterSensitivity] = []
    for i, name in enumerate(space.names):
        lower, upper = float(space.lower[i]), float(space.upper[i])
        span = upper - lower
        x = float(best_parameters[name])
        step = SENSITIVITY_STEP_FRACTION * span

        probes: list[tuple[float, EvaluationMetrics]] = []
        for value in (max(lower, x - step), min(upper, x + step)):
            metrics = evaluator.evaluate(evaluator.vector({**best_parameters, name: value}))
            probes.append((value, metrics) if metrics is not None else (x, center))

        (x_low, m_low), (x_high, m_high) = probes
        if x_high - x_low <= 1e-12:
            continue

        effects: dict[str, float] = {}
        for metric in EFFECT_METRICS:
            a, b = getattr(m_low, metric), getattr(m_high, metric)
            if a is None or b is None:
                continue
            effects[metric] = round((b - a) / (x_high - x_low) * span, 6)

        out.append(ParameterSensitivity(
            name=name, probe_low=round(x_low, 6), probe_high=round(x_high, 6),
            full_range_effects=effects,
        ))
    return out


def total_reach(sensitivities: list[ParameterSensitivity], metric: str) -> float:
    """Linearised upper bound on how far the search box can move ``metric``."""
    return sum(abs(s.full_range_effects.get(metric, 0.0)) for s in sensitivities)


# --------------------------------------------------------------------------
# Warnings and verdict
# --------------------------------------------------------------------------

def build_warnings(
    request: OptimizationCreate,
    space: SearchSpace,
    best: CandidateEvaluation,
    baseline: CandidateEvaluation,
    most_demanding: CandidateEvaluation | None,
    requirement_map: RequirementMapResult | None,
    sensitivities: list[ParameterSensitivity],
) -> list[str]:
    warnings: list[str] = []

    # 1. Optimum on a bound.
    at_lower_bound: set[str] = set()
    for i, name in enumerate(space.names):
        span = float(space.upper[i] - space.lower[i])
        x = best.parameters.get(name)
        if x is None:
            continue
        if abs(x - space.lower[i]) <= BOUND_TOLERANCE_FRACTION * span:
            at_lower_bound.add(name)
            warnings.append(
                f"best {name} sits at its lower search bound ({space.lower[i]:g}); "
                "the optimum may lie outside the searched range"
            )
        elif abs(x - space.upper[i]) <= BOUND_TOLERANCE_FRACTION * span:
            warnings.append(
                f"best {name} sits at its upper search bound ({space.upper[i]:g}); "
                "the optimum may lie outside the searched range"
            )

    # 2. Constraints out of reach / saturated threshold metrics.
    for constraint in request.constraints:
        label = constraint_label(constraint)
        excess = best.constraint_excess.get(label, 0.0)
        if excess <= 0:
            continue
        reach = total_reach(sensitivities, constraint.metric)
        if reach < excess:
            warnings.append(
                f"{label}: violated by {excess:.4g}, but the whole search range moves "
                f"{constraint.metric} by only about {reach:.4g} (linearised at the "
                "optimum); the target is out of reach of the selected variables"
            )
        if constraint.metric.endswith("exceedance_fraction") and reach < SATURATION_REACH_FRACTION * excess:
            replacement = constraint.metric.replace("exceedance_fraction", "excess_degree_hours")
            warnings.append(
                f"{constraint.metric} is saturated: the threshold is crossed in almost "
                f"the whole design space, so the metric has no usable gradient. Use "
                f"{replacement}, which keeps one."
            )

    # 3. Flat objective.
    if request.objective.metric != "material_demand" and sensitivities:
        reach = total_reach(sensitivities, request.objective.metric)
        if reach < FLAT_OBJECTIVE_FRACTION * METRIC_SCALES[request.objective.metric]:
            warnings.append(
                f"objective {request.objective.metric} is flat over the search range "
                f"(total linearised effect {reach:.3g}); the reported optimum is arbitrary"
            )

    # 4. Non-monotone performance.
    if (
        request.objective.metric != "material_demand"
        and most_demanding is not None
        and most_demanding.objective_value is not None
        and best.objective_value is not None
        and best.feasible == most_demanding.feasible
    ):
        sign = -1.0 if request.objective.sense == "maximize" else 1.0
        margin = 1e-6 * METRIC_SCALES[request.objective.metric]
        if sign * best.objective_value < sign * most_demanding.objective_value - margin:
            warnings.append(
                "best beats the most demanding design: performance is non-monotone in "
                "at least one variable (check demand directions and the trends below)"
            )

    # 5. Requirement map readings.
    if requirement_map is not None:
        for axis, variable, trend, required in (
            ("x", requirement_map.x_variable, requirement_map.objective_trend_x,
             requirement_map.required_x_at_best_y),
            ("y", requirement_map.y_variable, requirement_map.objective_trend_y,
             requirement_map.required_y_at_best_x),
        ):
            if trend == "mixed":
                warnings.append(
                    f"map metric is non-monotone along {variable}; requirement readings "
                    "are least-demanding feasible values, not thresholds"
                )
            elif trend == "worsens":
                warnings.append(
                    f"performance worsens as {variable} becomes more demanding; its "
                    "demand_direction is probably inverted for this scenario"
                )
            if required is not None and abs(required - space.least_demanding_bound(variable)) <= 1e-9:
                warnings.append(
                    f"{variable} requirement reads at its least demanding bound "
                    f"({required:g}): the true requirement lies beyond the searched range"
                )
        if (requirement_map.plateau_fraction or 0.0) > PLATEAU_WARNING_FRACTION:
            warnings.append(
                f"{requirement_map.plateau_fraction:.0%} of map cells share the minimum; "
                "ties are resolved towards the least demanding design"
            )

    # 6. Baseline tie.
    if all(abs(best.parameters[k] - baseline.parameters.get(k, math.nan)) < 1e-6 for k in best.parameters):
        warnings.append("best equals the baseline garment")

    # 7. Mean radiant temperature proxy (ADR 0007, ADR 0008).
    method = request.environment_assumptions.mean_radiant_temperature_method
    ir_names = {"infrared_emissivity", "infrared_emissivity_window", "infrared_emissivity_outside_window", "infrared_emissivity_ground_facing"}
    if method == "air_plus_solar_linear" and ir_names & set(space.names):
        warnings.append(
            "air_plus_solar_linear adds a GHI term to the non-sky longwave temperature although "
            "body shortwave is computed explicitly, so the sun is counted twice and hot "
            "surroundings are over-stated (ADR 0008). Infrared conclusions should be checked "
            "with mean_radiant_temperature_method = ground_energy_balance."
        )
        for name in ("infrared_emissivity", "infrared_emissivity_outside_window"):
            if name in at_lower_bound:
                warnings.append(
                    f"low {name} is favoured under the double-counting proxy; do not report "
                    "this without the ground_energy_balance rerun"
                )

    # 8. Two-zone garments (ADR 0010).
    if "infrared_emissivity_ground_facing" in space.names:
        s = request.environment_assumptions.zone_view_separation
        if s < 0.05:
            warnings.append(
                "zone_view_separation is ~0: both zones see the same radiant field, so only "
                "the area-weighted emissivity is identifiable; ground-facing and sky-facing "
                "values are not separately meaningful"
            )
        warnings.append(
            f"the ground-facing emissivity requirement depends on the assumed "
            f"zone_view_separation = {s:g} (not measured, ADR 0010); report it together "
            "with the separation sweep of experiment L2"
        )
        
    return warnings


def _verdict(
    request: OptimizationCreate,
    best: CandidateEvaluation,
    most_demanding: CandidateEvaluation | None,
) -> tuple[str, str]:
    metric = request.objective.metric
    value = "n/a" if best.objective_value is None else f"{best.objective_value:.4f}"
    if not request.constraints:
        return "unconstrained", f"No constraints were given; best {metric} = {value}."
    if best.feasible:
        return "feasible", (
            f"All constraints satisfied. Best {metric} = {value} "
            f"(material demand {best.material_demand:.3f})."
        )

    excess = "; ".join(f"{k} (+{v:.4g})" for k, v in best.constraint_excess.items() if v > 0)
    text = (
        "No candidate inside the bounds satisfies the constraints. Smallest normalised "
        f"violation {best.constraint_violation:.4f}: {excess}."
    )
    if most_demanding is not None and most_demanding.metrics is not None and not most_demanding.feasible:
        text += (
            " The most demanding design is also infeasible: the target is beyond the "
            "passive limit of this model for this climate, activity and garment."
        )
    return "infeasible", text


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------

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

    # 1. Baseline; it is also the reference of the normalised objective.
    progress(20, "evaluating_baseline", force=True)
    baseline = evaluate_candidate(evaluator, request, evaluator.base_parameters())
    reference = (
        baseline.objective_value
        if baseline.objective_value is not None and request.objective.metric != "material_demand"
        else 0.0
    )
    objective = ObjectiveFunction(request, reference=reference)

    # 2. Differential evolution.
    generations = request.max_generations
    outcome = run_differential_evolution(
        evaluator,
        request,
        space=space,
        objective=objective,
        on_generation=lambda record: progress(
            20 + round(64 * min(record.generation, generations) / generations),
            f"generation_{record.generation}",
            history_record=record,
            force=True,
        ),
    )

    # 3. Corners and the most demanding design (populate the cache).
    progress(84, "evaluating_corners", force=True)
    corners = [evaluate_candidate(evaluator, request, p) for p in corner_parameters(space)]
    corner_best = min(corners, key=lambda c: candidate_rank(c, request))
    most_demanding = evaluate_candidate(evaluator, request, most_demanding_parameters(space))

    anchor = best_evaluated(evaluator, request) or evaluate_candidate(
        evaluator, request, evaluator.parameters(outcome.x)
    )

    # 4. Requirement map with the other variables at the current optimum.
    requirement_map = None
    if request.requirement_map is not None:
        progress(86, "building_requirement_map", force=True)
        requirement_map = build_requirement_map(
            evaluator,
            request,
            anchor.parameters,
            space=space,
            on_cell=lambda done, total: progress(
                86 + round(10 * done / total), "building_requirement_map"
            ),
        )

    # 5. Final reported point over everything evaluated so far.
    best = best_evaluated(evaluator, request) or anchor

    # 6. Sensitivity at that point (probes do not change ``best``).
    progress(97, "sensitivity_analysis", force=True)
    sensitivities = sensitivity_analysis(evaluator, space, best.parameters)

    warnings = build_warnings(
        request, space, best, baseline, most_demanding, requirement_map, sensitivities
    )
    verdict, message = _verdict(request, best, most_demanding)

    return OptimizationResult(
        verdict=verdict,
        message=message,
        objective=request.objective,
        constraints=request.constraints,
        best=best,
        baseline=baseline,
        optical_upper_bound=most_demanding,
        best_corner=corner_best,
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
        warnings=warnings,
        sensitivities=sensitivities,
        objective_reference=reference,
        objective_scale=objective.scale,
    )