import pytest

from app.schemas.optimization import (
    DecisionVariable,
    EvaluationMetrics,
    MetricConstraint,
    RequirementMapSpec,
)
from app.services.longwave import resolve_longwave_optics
from app.services.optimization.metrics import excess_integral
from app.services.optimization.objective import (
    INFEASIBLE_OFFSET,
    ObjectiveFunction,
    constraint_violation,
)
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.search_space import build_search_space
from app.services.optimization.service import rank_points
from app.services.optimization.variables import candidate_material, variable_value
from tests.test_optimization import RHO_EPS, AnalyticEvaluator, make_request


def metrics(**overrides) -> EvaluationMetrics:
    values = dict(
        sample_count=1, mean_skin_temperature_c=35.0, peak_skin_temperature_c=36.0,
        peak_core_temperature_c=37.5, skin_exceedance_fraction=0.5, core_exceedance_fraction=0.0,
        skin_excess_degree_hours=0.0, core_excess_degree_hours=0.0,
        mean_skin_cooling_c=1.0, mean_core_cooling_c=0.5,
    )
    values.update(overrides)
    return EvaluationMetrics(**values)


@pytest.mark.unit
def test_excess_integral_is_exact():
    assert excess_integral([0, 10], [34, 36], 35) == pytest.approx(2.5)
    assert excess_integral([0, 10], [36, 36], 35) == pytest.approx(10.0)
    assert excess_integral([0, 10], [30, 34], 35) == 0.0


@pytest.mark.unit
def test_violation_is_normalised_and_infeasible_ranks_last(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        constraints=[MetricConstraint(metric="skin_excess_degree_hours", operator="<=", threshold=0.5)],
    )
    bad = metrics(skin_excess_degree_hours=1.0)
    good = metrics(skin_excess_degree_hours=0.2)
    assert constraint_violation(bad, request.constraints) == pytest.approx(1.0)  # 0.5 / 0.5

    objective = ObjectiveFunction(request, reference=0.2)
    params = {"solar_reflectance": 0.9, "infrared_emissivity": 0.9}
    assert objective(good, params) < INFEASIBLE_OFFSET <= objective(bad, params)


@pytest.mark.unit
def test_plateau_ties_resolve_to_least_demanding(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        constraints=[MetricConstraint(metric="skin_excess_degree_hours", operator="<=", threshold=0.1)],
    )
    points = [
        ({"solar_reflectance": 0.98, "infrared_emissivity": 0.99}, metrics()),
        ({"solar_reflectance": 0.6, "infrared_emissivity": 0.7}, metrics()),
        ({"solar_reflectance": 0.3, "infrared_emissivity": 0.5}, metrics(skin_excess_degree_hours=0.4)),
    ]
    best = rank_points(points, request)
    assert best.parameters == {"solar_reflectance": 0.6, "infrared_emissivity": 0.7}
    assert best.feasible


@pytest.mark.unit
def test_band_variables_use_band_pairs(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material, requirement_map=None,
        variables=[
            DecisionVariable(name="infrared_emissivity_window", lower=0.5, upper=1.0),
            DecisionVariable(name="infrared_transmittance", lower=0.0, upper=0.3),
        ],
    )
    space = build_search_space(request)
    assert space.linear_pairs == ((0, 1),)          # eps_W + tau_IR <= 1
    assert space.upper[1] == pytest.approx(0.05)    # eps_N fixed at 0.95


@pytest.mark.unit
def test_gray_and_band_variables_cannot_be_combined(person, control_material, rc_material):
    with pytest.raises(ValueError, match="cannot be combined"):
        make_request(
            person, control_material, rc_material, requirement_map=None,
            variables=[
                DecisionVariable(name="infrared_emissivity", lower=0.5, upper=0.99),
                DecisionVariable(name="infrared_emissivity_window", lower=0.5, upper=0.99),
            ],
        )


@pytest.mark.unit
def test_outside_window_variable_round_trips(rc_material):
    candidate = candidate_material(
        rc_material,
        {"infrared_emissivity_window": 0.95, "infrared_emissivity_outside_window": 0.2},
    )
    optics = resolve_longwave_optics(candidate)
    assert optics.window == pytest.approx(0.95)
    assert optics.outside == pytest.approx(0.2, abs=1e-9)
    assert candidate.material_version_id is None


@pytest.mark.unit
def test_variable_value_derives_missing_evaporative_resistance(rc_material):
    assert rc_material.evaporative_resistance_m2pa_w is None
    assert variable_value(rc_material, "evaporative_resistance_m2pa_w") > 0


@pytest.mark.unit
def test_decreasing_direction_reads_largest_feasible_x(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.5, upper=1.0, demand_direction="decreasing"),
            DecisionVariable(name="infrared_emissivity", lower=0.5, upper=1.0),
        ],
        constraints=[MetricConstraint(metric="mean_skin_cooling_c", operator=">=", threshold=1.6)],
        requirement_map=RequirementMapSpec(resolution=6),
    )
    space = build_search_space(request)
    result = build_requirement_map(
        AnalyticEvaluator(), request, {"solar_reflectance": 0.8, "infrared_emissivity": 0.9}, space=space
    )
    frontier = {round(p.y, 2): p.required_x for p in result.frontier}
    assert result.x_demand_direction == "decreasing"
    assert frontier[1.0] == pytest.approx(1.0)
    assert result.required_x_at_best_y == pytest.approx(1.0)