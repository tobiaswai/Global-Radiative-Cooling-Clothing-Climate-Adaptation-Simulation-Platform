"""Surrogate models trained on physics simulations (Stage 13, ADR 0011)."""

from __future__ import annotations

import calendar
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.optimization import EMISSIVITY_BAND_VARIABLES, DecisionVariable, MetricName
from app.schemas.simulation import MaterialInput, PersonInput

DatasetStatus = Literal["running", "finalizing", "completed", "partial_completed", "failed", "cancelled"]
ChunkStatus = Literal["queued", "running", "completed", "failed", "cancelled"]
SurrogateModelStatus = Literal["queued", "training", "completed", "failed"]
ValidationSplit = Literal["grouped_kfold", "leave_one_city", "leave_one_season"]
PredictionMode = Literal["surrogate", "physics", "both"]
PredictionSource = Literal["surrogate", "physics", "none"]

DEFAULT_TARGETS: list[MetricName] = [
    "mean_skin_cooling_c",
    "mean_core_cooling_c",
    "skin_excess_degree_hours",
    "peak_core_temperature_c",
]

# Out-of-fold MAE thresholds in native units (ADR 0011).
DEFAULT_MAE_THRESHOLDS: dict[str, float] = {
    "mean_skin_temperature_c": 0.05,
    "peak_skin_temperature_c": 0.08,
    "peak_core_temperature_c": 0.05,
    "skin_exceedance_fraction": 0.05,
    "core_exceedance_fraction": 0.05,
    "skin_excess_degree_hours": 0.10,
    "core_excess_degree_hours": 0.05,
    "mean_skin_cooling_c": 0.05,
    "mean_core_cooling_c": 0.03,
}

ACCEPTANCE_SPLITS: tuple[str, ...] = ("leave_one_city", "leave_one_season")
MIN_MATERIAL_COUNT = 16
MAX_MATERIAL_COUNT = 4096
MAX_PREDICTION_MATERIALS = 500


class SurrogateDatasetCreate(BaseModel):
    name: str = Field(default="Surrogate training set", min_length=1, max_length=200)
    city_ids: list[str] = Field(min_length=1, max_length=100)
    year: int = Field(default=2023, ge=1940, le=2100)
    months: list[int] = Field(default_factory=lambda: list(range(1, 13)), min_length=1, max_length=12)
    sample_days_per_month: int = Field(default=3, ge=1, le=10)
    local_start_hour: int = Field(default=12, ge=0, le=23)
    duration_minutes: int = Field(default=120, ge=30, le=480)
    output_interval_minutes: int = Field(default=5, ge=1, le=30)
    skin_threshold_c: float = Field(default=35.0, ge=30.0, le=42.0)
    core_threshold_c: float = Field(default=38.0, ge=36.5, le=41.0)
    person: PersonInput
    control_material: MaterialInput
    base_material: MaterialInput
    environment_assumptions: EnvironmentAssumptions = Field(default_factory=EnvironmentAssumptions)
    variables: list[DecisionVariable] = Field(min_length=1, max_length=8)
    material_count: int = 512
    seed: int = Field(default=0, ge=0)

    @model_validator(mode="after")
    def validate_spec(self) -> "SurrogateDatasetCreate":
        ids = [city.strip().lower() for city in self.city_ids]
        if any(not city for city in ids) or len(set(ids)) != len(ids):
            raise ValueError("city_ids must be unique and non-empty")
        self.city_ids = ids

        if any(m < 1 or m > 12 for m in self.months) or len(set(self.months)) != len(self.months):
            raise ValueError("months must be unique values between 1 and 12")
        self.months = sorted(self.months)

        names = [v.name for v in self.variables]
        if len(set(names)) != len(names):
            raise ValueError("variables cannot contain duplicate names")
        if "infrared_emissivity" in names and EMISSIVITY_BAND_VARIABLES & set(names):
            raise ValueError("infrared_emissivity cannot be combined with band emissivities")
        if "infrared_emissivity" in names and self.base_material.infrared_emissivity_window is not None:
            raise ValueError("base_material is selective; use band emissivity variables")

        n = self.material_count
        if n < MIN_MATERIAL_COUNT or n > MAX_MATERIAL_COUNT or n & (n - 1):
            raise ValueError(
                f"material_count must be a power of two between {MIN_MATERIAL_COUNT} and "
                f"{MAX_MATERIAL_COUNT} (balanced Sobol sequence)"
            )
        return self

    @property
    def variable_names(self) -> tuple[str, ...]:
        return tuple(v.name for v in self.variables)

    def chunk_keys(self) -> list[tuple[str, int]]:
        return [(city, month) for city in self.city_ids for month in self.months]

    def weather_sample_count(self) -> int:
        per_city = sum(
            min(self.sample_days_per_month, calendar.monthrange(self.year, m)[1]) for m in self.months
        )
        return per_city * len(self.city_ids)


class SurrogateDatasetEstimate(BaseModel):
    chunk_count: int
    weather_sample_count: int
    material_count: int
    valid_material_count: int
    rejected_material_count: int
    thermal_simulation_count: int


class SurrogateDatasetChunkResponse(BaseModel):
    id: str
    city_id: str
    month: int
    status: ChunkStatus
    attempt: int
    row_count: int
    skipped_sample_count: int
    elapsed_seconds: float | None
    error_message: str | None


class SurrogateDatasetResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    id: str
    name: str
    status: DatasetStatus
    total_chunks: int
    completed_chunks: int
    failed_chunks: int
    row_count: int
    valid_material_count: int
    model_version: str
    parameter_fingerprint: str
    context_sha256: str
    error_message: str | None
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None


class SurrogateDatasetDetail(SurrogateDatasetResponse):
    spec: SurrogateDatasetCreate
    chunks: list[SurrogateDatasetChunkResponse]


class SurrogateDatasetListResponse(BaseModel):
    items: list[SurrogateDatasetResponse]
    total: int
    limit: int
    offset: int


class SurrogateTrainingCreate(BaseModel):
    name: str = Field(default="Surrogate model", min_length=1, max_length=200)
    dataset_id: str
    targets: list[MetricName] = Field(default_factory=lambda: list(DEFAULT_TARGETS), min_length=1, max_length=9)
    lower_quantile: float = Field(default=0.1, gt=0.0, lt=0.5)
    upper_quantile: float = Field(default=0.9, gt=0.5, lt=1.0)
    max_iter: int = Field(default=300, ge=10, le=2000)
    learning_rate: float = Field(default=0.08, gt=0.0, le=1.0)
    max_leaf_nodes: int = Field(default=31, ge=4, le=255)
    min_samples_leaf: int = Field(default=40, ge=1, le=10000)
    l2_regularization: float = Field(default=0.0, ge=0.0)
    validation_splits: list[ValidationSplit] = Field(
        default_factory=lambda: ["grouped_kfold", "leave_one_city", "leave_one_season"]
    )
    mae_thresholds: dict[str, float] = Field(default_factory=lambda: dict(DEFAULT_MAE_THRESHOLDS))
    minimum_interval_coverage: float = Field(default=0.75, gt=0.0, le=1.0)
    max_rows: int | None = Field(default=None, ge=1000)
    random_seed: int = 0

    @model_validator(mode="after")
    def validate_training(self) -> "SurrogateTrainingCreate":
        if len(set(self.targets)) != len(self.targets):
            raise ValueError("targets must be unique")
        if any(value <= 0 for value in self.mae_thresholds.values()):
            raise ValueError("mae_thresholds must be positive")
        return self

    @property
    def nominal_coverage(self) -> float:
        return self.upper_quantile - self.lower_quantile


class TargetMetrics(BaseModel):
    target: str
    count: int
    mae: float
    rmse: float
    r2: float | None
    interval_coverage: float
    mean_interval_width: float


class SplitReport(BaseModel):
    split: str
    fold_count: int
    metrics: list[TargetMetrics]
    group_mae: dict[str, dict[str, float]]


class AcceptanceCheck(BaseModel):
    split: str
    target: str
    mae: float
    mae_threshold: float
    interval_coverage: float
    minimum_coverage: float
    passed: bool


class ValidationReport(BaseModel):
    row_count: int
    feature_columns: list[str]
    targets: list[str]
    training_cities: list[str]
    splits: list[SplitReport]
    acceptance: list[AcceptanceCheck]
    passed: bool
    nominal_interval_coverage: float
    training_seconds: float
    prediction_microseconds_per_row: float
    physics_seconds_per_simulation: float | None = None
    sklearn_version: str


class SurrogateModelResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    id: str
    name: str
    dataset_id: str | None
    status: SurrogateModelStatus
    accepted: bool
    targets: list[str]
    model_version: str
    parameter_fingerprint: str
    stale: bool
    headline_mae: dict[str, float]
    error_message: str | None
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None


class SurrogateModelDetail(SurrogateModelResponse):
    training: SurrogateTrainingCreate
    report: ValidationReport | None
    variables: list[DecisionVariable]
    base_parameters: dict[str, float]
    training_cities: list[str]
    year: int
    months: list[int]
    local_start_hour: int
    duration_minutes: int


class SurrogateModelListResponse(BaseModel):
    items: list[SurrogateModelResponse]
    total: int
    limit: int
    offset: int


class SurrogatePredictRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    model_id: str | None = None
    city_id: str = Field(min_length=1)
    sample_date: date
    materials: list[dict[str, float]] = Field(min_length=1, max_length=MAX_PREDICTION_MATERIALS)
    mode: PredictionMode = "surrogate"
    physics_fallback: bool = True


class TargetPrediction(BaseModel):
    value: float
    lower: float
    upper: float


class MaterialPrediction(BaseModel):
    parameters: dict[str, float]
    valid: bool
    within_domain: bool
    out_of_domain_features: list[str] = Field(default_factory=list)
    source: PredictionSource
    surrogate: dict[str, TargetPrediction] | None = None
    physics: dict[str, float] | None = None
    message: str | None = None


class SurrogatePredictResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    model_id: str
    model_name: str
    accepted: bool
    stale: bool
    city_id: str
    sample_date: date
    city_in_training: bool
    start_time_local: datetime
    duration_minutes: int
    weather_features: dict[str, float | None]
    weather_payload_sha256: str | None
    predictions: list[MaterialPrediction]
    physics_evaluations: int
    physics_limit: int
    elapsed_ms: float
    warnings: list[str]