"""Inverse design: target performance -> material parameter requirements (Stage 3)."""

from __future__ import annotations

import calendar
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, model_validator

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import MaterialInput, PersonInput


DecisionVariableName = Literal[
    "solar_reflectance",
    "solar_transmittance",
    "infrared_emissivity",
    "infrared_transmittance",
    "clothing_insulation_clo",
    "evaporative_resistance_m2pa_w",
]

# Search limits; tighter than MaterialInput where the full range is not a
# sensible design space (clo <= 2, Re,cl <= 200).
VARIABLE_LIMITS: dict[str, tuple[float, float]] = {
    "solar_reflectance": (0.0, 1.0),
    "solar_transmittance": (0.0, 1.0),
    "infrared_emissivity": (0.0, 1.0),
    "infrared_transmittance": (0.0, 1.0),
    "clothing_insulation_clo": (0.0, 2.0),
    "evaporative_resistance_m2pa_w": (0.0, 200.0),
}

MetricName = Literal[
    "mean_skin_temperature_c",
    "peak_skin_temperature_c",
    "peak_core_temperature_c",
    "skin_exceedance_fraction",
    "core_exceedance_fraction",
    "mean_skin_cooling_c",
    "mean_core_cooling_c",
]

OptimizationStatus = Literal["queued", "running", "cancelling", "cancelled", "completed", "failed"]
LeaseState = Literal["none", "live", "expired"]


class DecisionVariable(BaseModel):
    name: DecisionVariableName
    lower: float
    upper: float

    @model_validator(mode="after")
    def check_bounds(self) -> "DecisionVariable":
        low, high = VARIABLE_LIMITS[self.name]
        if not (low <= self.lower < self.upper <= high):
            raise ValueError(
                f"{self.name}: bounds must satisfy {low} <= lower < upper <= {high}"
            )
        return self


class MetricConstraint(BaseModel):
    metric: MetricName
    operator: Literal["<=", ">="] = "<="
    threshold: float


class OptimizationObjective(BaseModel):
    metric: MetricName = "skin_exceedance_fraction"
    sense: Literal["minimize", "maximize"] = "minimize"


class RequirementMapSpec(BaseModel):
    x_variable: DecisionVariableName = "solar_reflectance"
    y_variable: DecisionVariableName = "infrared_emissivity"
    resolution: int = Field(default=11, ge=3, le=21)


class OptimizationCreate(BaseModel):
    name: str = Field(default="Material requirement search", min_length=1, max_length=200)
    city_id: str = Field(min_length=1)
    year: int = Field(default=2023, ge=1940, le=2100)
    months: list[int] = Field(default_factory=lambda: [8], min_length=1, max_length=12)
    sample_days_per_month: int = Field(default=3, ge=1, le=31)
    local_start_hour: int = Field(default=12, ge=0, le=23)
    duration_minutes: int = Field(default=120, ge=30, le=480)
    output_interval_minutes: int = Field(default=5, ge=1, le=30)

    # Thresholds behind the *_exceedance_fraction metrics.
    skin_threshold_c: float = Field(default=35.0, ge=30.0, le=42.0)
    core_threshold_c: float = Field(default=38.0, ge=36.5, le=41.0)

    person: PersonInput
    control_material: MaterialInput
    # Candidate garment; fields that are not decision variables stay fixed here.
    base_material: MaterialInput
    environment_assumptions: EnvironmentAssumptions = Field(default_factory=EnvironmentAssumptions)

    variables: list[DecisionVariable] = Field(min_length=1, max_length=6)
    objective: OptimizationObjective = Field(default_factory=OptimizationObjective)
    constraints: list[MetricConstraint] = Field(default_factory=list, max_length=6)

    algorithm: Literal["differential_evolution"] = "differential_evolution"
    population_multiplier: int = Field(default=10, ge=4, le=30)
    max_generations: int = Field(default=30, ge=1, le=200)
    seed: int | None = 42

    requirement_map: RequirementMapSpec | None = Field(default_factory=RequirementMapSpec)

    @model_validator(mode="after")
    def validate_request(self) -> "OptimizationCreate":
        self.city_id = self.city_id.strip().lower()

        if any(m < 1 or m > 12 for m in self.months) or len(set(self.months)) != len(self.months):
            raise ValueError("months must be unique values between 1 and 12")
        self.months = sorted(self.months)

        names = [v.name for v in self.variables]
        if len(set(names)) != len(names):
            raise ValueError("variables cannot contain duplicate names")

        spec = self.requirement_map
        if spec is not None:
            if spec.x_variable == spec.y_variable:
                raise ValueError("requirement_map axes must differ")
            missing = {spec.x_variable, spec.y_variable} - set(names)
            if missing:
                raise ValueError(
                    "requirement_map axes must be decision variables: " + ", ".join(sorted(missing))
                )
        return self

    def samples_per_month(self, month: int) -> int:
        return min(self.sample_days_per_month, calendar.monthrange(self.year, month)[1])


class OptimizationEstimate(BaseModel):
    variable_count: int
    population_size: int
    optimizer_evaluation_budget: int
    requirement_map_evaluations: int
    sample_count: int
    thermal_simulation_budget: int
    weather_requests: int


class EvaluationMetrics(BaseModel):
    sample_count: int
    mean_skin_temperature_c: float
    peak_skin_temperature_c: float
    peak_core_temperature_c: float
    skin_exceedance_fraction: float
    core_exceedance_fraction: float
    mean_skin_cooling_c: float
    mean_core_cooling_c: float


class CandidateEvaluation(BaseModel):
    parameters: dict[str, float]
    metrics: EvaluationMetrics | None
    objective_value: float | None  # raw metric value (unsigned, no penalty)
    constraint_violation: float | None
    feasible: bool


class GenerationRecord(BaseModel):
    generation: int
    penalised_objective: float
    best_parameters: dict[str, float]
    best_metric_value: float | None
    best_feasible: bool
    evaluation_count: int


class RequirementCell(BaseModel):
    x: float
    y: float
    metric_value: float
    constraint_violation: float
    feasible: bool


class FrontierPoint(BaseModel):
    y: float
    minimum_x: float | None


class RequirementMapResult(BaseModel):
    x_variable: DecisionVariableName
    y_variable: DecisionVariableName
    x_values: list[float]
    y_values: list[float]
    # cells[j][i] -> (x_values[i], y_values[j]); None = optically impossible
    cells: list[list[RequirementCell | None]]
    frontier: list[FrontierPoint]
    minimum_x_at_max_y: float | None
    minimum_y_at_max_x: float | None
    fixed_parameters: dict[str, float]


class SkippedOptimizationSample(BaseModel):
    sample_date_local: datetime
    reason_code: str
    message: str


class OptimizationResult(BaseModel):
    verdict: Literal["feasible", "infeasible", "unconstrained"]
    message: str
    objective: OptimizationObjective
    constraints: list[MetricConstraint]
    best: CandidateEvaluation
    baseline: CandidateEvaluation
    optical_upper_bound: CandidateEvaluation | None
    requirement_map: RequirementMapResult | None
    sample_count: int
    skipped_samples: list[SkippedOptimizationSample]
    weather_payload_sha256: dict[str, str | None]
    evaluation_count: int
    simulation_count: int
    generations: int
    algorithm: str
    algorithm_message: str
    elapsed_seconds: float
    model_version: str
    parameter_fingerprint: str


class OptimizationJobResponse(BaseModel):
    id: str
    celery_task_id: str | None
    name: str
    city_id: str
    status: OptimizationStatus
    stage: str
    progress: int
    evaluation_count: int
    error_message: str | None
    created_at: datetime
    updated_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    attempt: int = 0
    lease_owner: str | None = None
    lease_expires_at: datetime | None = None
    last_heartbeat_at: datetime | None = None
    lease_state: LeaseState = "none"
    cancel_requested_at: datetime | None = None
    control_material_version_id: str | None = None
    base_material_version_id: str | None = None


class OptimizationJobDetail(OptimizationJobResponse):
    request: OptimizationCreate
    history: list[GenerationRecord]
    result: OptimizationResult | None


class OptimizationJobListResponse(BaseModel):
    items: list[OptimizationJobResponse]
    total: int
    limit: int
    offset: int