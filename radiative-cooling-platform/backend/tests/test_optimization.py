from types import SimpleNamespace

import numpy as np
import pytest
from pydantic import ValidationError

from app.api import optimizations as optimizations_api
from app.schemas.optimization import (
    DecisionVariable,
    EvaluationMetrics,
    MetricConstraint,
    OptimizationCreate,
    RequirementMapSpec,
)
from app.services.optimization.evaluator import MaterialEvaluator, PreparedSample
from app.services.optimization.metrics import fraction_above
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.runner import OptimizationCancelled, run_differential_evolution
from app.services.optimization.search_space import build_search_space
from app.services.optimization.service import estimate_optimization
from app.services.two_node import simulate_material_with_interpolator
from app.services.weather_interpolation import WeatherInterpolator


RHO_EPS = [
    DecisionVariable(name="solar_reflectance", lower=0.3, upper=0.98),
    DecisionVariable(name="infrared_emissivity", lower=0.5, upper=0.99),
]


def make_request(person, control_material, rc_material, **overrides) -> OptimizationCreate:
    payload = dict(
        city_id="dubai", months=[7], duration_minutes=120, output_interval_minutes=10,
        person=person, control_material=control_material, base_material=rc_material,
        variables=RHO_EPS, requirement_map=RequirementMapSpec(resolution=3),
        population_multiplier=4, max_generations=2,
    )
    payload.update(overrides)
    return OptimizationCreate(**payload)


# --- metrics -----------------------------------------------------------------

@pytest.mark.unit
def test_fraction_above_is_exact_for_linear_segments():
    assert fraction_above([0, 10], [30, 40], 35) == pytest.approx(0.5)
    assert fraction_above([0, 10, 20], [36, 36, 34], 35) == pytest.approx(0.75)
    assert fraction_above([0, 10], [30, 31], 35) == 0.0


# --- schema / search space -------------------------------------------------

@pytest.mark.unit
def test_map_axes_must_be_decision_variables(person, control_material, rc_material):
    with pytest.raises(ValidationError, match="requirement_map axes"):
        make_request(person, control_material, rc_material,
                     variables=[RHO_EPS[0]], requirement_map=RequirementMapSpec())


@pytest.mark.unit
def test_single_optical_variable_is_tightened_by_fixed_partner(person, control_material, rc_material):
    base = rc_material.model_copy(
        update={"solar_reflectance": 0.8, "solar_transmittance": 0.1}
    )
    request = make_request(
        person, control_material, base,
        variables=[DecisionVariable(name="solar_reflectance", lower=0.3, upper=1.0)],
        requirement_map=None,
    )
    space = build_search_space(request)
    assert space.upper[0] == pytest.approx(0.9)
    assert space.linear_pairs == ()


@pytest.mark.unit
def test_paired_optical_variables_become_linear_constraint(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.3, upper=1.0),
            DecisionVariable(name="solar_transmittance", lower=0.0, upper=0.5),
        ],
        requirement_map=None,
    )
    assert build_search_space(request).linear_pairs == ((0, 1),)


@pytest.mark.unit
def test_estimate_counts(person, control_material, rc_material):
    request = make_request(person, control_material, rc_material, sample_days_per_month=3)
    estimate = estimate_optimization(request)
    assert estimate.population_size == 8
    assert estimate.optimizer_evaluation_budget == 8 * 3
    assert estimate.requirement_map_evaluations == 9
    assert estimate.thermal_simulation_budget == (24 + 9 + 3) * 3


# --- evaluator (real physics on the fixture window) ------------------------

@pytest.fixture
def prepared(hourly_weather, person, control_material):
    interpolator = WeatherInterpolator.from_series(hourly_weather)
    control = simulate_material_with_interpolator(120, 10, interpolator, person, control_material)
    return PreparedSample(hourly_weather.requested_start_time, 1, interpolator, control)


@pytest.mark.unit
def test_higher_reflectance_lowers_skin_temperature(prepared, person, control_material, rc_material):
    evaluator = MaterialEvaluator(make_request(person, control_material, rc_material), [prepared])

    low = evaluator.evaluate([0.3, 0.9])
    high = evaluator.evaluate([0.95, 0.9])

    assert high.mean_skin_temperature_c < low.mean_skin_temperature_c
    assert high.mean_skin_cooling_c > low.mean_skin_cooling_c
    assert 0.0 <= high.skin_exceedance_fraction <= 1.0

    count = evaluator.evaluation_count
    evaluator.evaluate([0.95, 0.9])
    assert evaluator.evaluation_count == count  # memoised


@pytest.mark.unit
def test_optically_impossible_candidate_returns_none(prepared, person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material, requirement_map=None,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.3, upper=1.0),
            DecisionVariable(name="solar_transmittance", lower=0.0, upper=0.5),
        ],
    )
    evaluator = MaterialEvaluator(request, [prepared])
    assert evaluator.evaluate([0.8, 0.5]) is None
    assert evaluator.evaluation_count == 0


# --- runner / map with an analytic evaluator -------------------------------

class AnalyticEvaluator:
    """skin_exceedance_fraction = distance^2 to (0.8, 0.9); feasibility via
    mean_skin_cooling_c = rho + eps."""

    def __init__(self, names=("solar_reflectance", "infrared_emissivity")):
        self.names = names
        self.evaluation_count = 0

    def parameters(self, x):
        return {n: float(v) for n, v in zip(self.names, x)}

    def evaluate(self, x):
        self.evaluation_count += 1
        rho, eps = float(x[0]), float(x[1])
        return EvaluationMetrics(
            sample_count=1, mean_skin_temperature_c=35.0, peak_skin_temperature_c=36.0,
            peak_core_temperature_c=37.5,
            skin_exceedance_fraction=(rho - 0.8) ** 2 + (eps - 0.9) ** 2,
            core_exceedance_fraction=0.0,
            mean_skin_cooling_c=rho + eps, mean_core_cooling_c=0.0,
        )


@pytest.mark.unit
def test_differential_evolution_finds_known_minimum(person, control_material, rc_material):
    request = make_request(person, control_material, rc_material,
                           population_multiplier=10, max_generations=60)
    outcome = run_differential_evolution(AnalyticEvaluator(), request)

    assert outcome.x == pytest.approx([0.8, 0.9], abs=0.02)
    assert outcome.generations == len(outcome.history) >= 1
    assert outcome.history[-1].best_feasible  # no constraints


@pytest.mark.unit
def test_cancel_from_generation_callback_stops_the_search(person, control_material, rc_material):
    request = make_request(person, control_material, rc_material, max_generations=50)

    def cancel(_record):
        raise OptimizationCancelled()

    with pytest.raises(OptimizationCancelled):
        run_differential_evolution(AnalyticEvaluator(), request, on_generation=cancel)


@pytest.mark.unit
def test_requirement_frontier(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.5, upper=1.0),
            DecisionVariable(name="infrared_emissivity", lower=0.5, upper=1.0),
        ],
        constraints=[MetricConstraint(metric="mean_skin_cooling_c", operator=">=", threshold=1.6)],
        requirement_map=RequirementMapSpec(resolution=6),  # steps of 0.1
    )
    space = build_search_space(request)
    result = build_requirement_map(
        AnalyticEvaluator(), request, {"solar_reflectance": 0.8, "infrared_emissivity": 0.9}, space=space
    )

    frontier = {round(p.y, 2): p.minimum_x for p in result.frontier}
    assert frontier[1.0] == pytest.approx(0.6)
    assert frontier[0.6] == pytest.approx(1.0)
    assert frontier[0.5] is None
    assert result.minimum_x_at_max_y == pytest.approx(0.6)
    assert result.minimum_y_at_max_x == pytest.approx(0.6)


# --- API -------------------------------------------------------------------

@pytest.mark.integration
def test_optimization_api_round_trip(client, monkeypatch, person, control_material, rc_material):
    monkeypatch.setattr(
        optimizations_api, "run_optimization_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-opt")),
    )
    monkeypatch.setattr(optimizations_api.celery_app.control, "revoke", lambda *a, **k: None)

    body = make_request(person, control_material, rc_material).model_dump(mode="json")

    estimate = client.post("/api/v1/optimizations/estimate", json=body)
    assert estimate.status_code == 200, estimate.text

    created = client.post("/api/v1/optimizations", json=body)
    assert created.status_code == 202, created.text
    job_id = created.json()["id"]
    assert created.json()["celery_task_id"] == "celery-opt"

    detail = client.get(f"/api/v1/optimizations/{job_id}").json()
    assert detail["status"] == "queued"
    assert detail["history"] == [] and detail["result"] is None

    cancelled = client.post(f"/api/v1/optimizations/{job_id}/cancel").json()
    assert cancelled["status"] == "cancelled"
    assert client.post(f"/api/v1/optimizations/{job_id}/cancel").status_code == 409

    bad = {**body, "city_id": "atlantis"}
    assert client.post("/api/v1/optimizations", json=bad).status_code == 422