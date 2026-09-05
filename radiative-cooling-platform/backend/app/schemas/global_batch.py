from datetime import datetime
from typing import Literal

from pydantic import (
    BaseModel,
    Field,
    model_validator,
)

from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)


GlobalBatchStatus = Literal[
    "queued",
    "running",
    "cancelling",
    "cancelled",
    "completed",
    "partial_completed",
    "failed",
]

GlobalCityStatus = Literal[
    "queued",
    "running",
    "cancelled",
    "completed",
    "failed",
]

ExposureMatchMode = Literal[
    "all",
    "any",
]


class GlobalBatchCreate(BaseModel):
    name: str = Field(
        default="Global multi-day climate adaptation analysis",
        min_length=1,
        max_length=200,
    )

    city_ids: list[str] = Field(
        min_length=1,
        max_length=100,
    )

    year: int = Field(
        default=2023,
        ge=1940,
        le=2100,
    )

    start_month: int = Field(
        default=1,
        ge=1,
        le=12,
    )

    end_month: int = Field(
        default=12,
        ge=1,
        le=12,
    )

    # 4.2：每月多個代表日。
    sample_days_per_month: int = Field(
        default=3,
        ge=1,
        le=7,
    )

    # 保留供讀取舊有 4.1 request_json。
    representative_day: int | None = Field(
        default=None,
        ge=1,
        le=28,
    )

    local_start_hour: int = Field(
        default=12,
        ge=0,
        le=23,
    )

    duration_minutes: int = Field(
        default=120,
        ge=30,
        le=1440,
    )

    output_interval_minutes: int = Field(
        default=10,
        ge=1,
        le=60,
    )

    minimum_skin_improvement_c: float = Field(
        default=0.2,
        ge=-5,
        le=10,
    )

    minimum_air_temperature_c: float | None = Field(
        default=30.0,
        ge=-50,
        le=70,
    )

    minimum_solar_radiation_w_m2: float | None = Field(
        default=300.0,
        ge=0,
        le=1500,
    )

    exposure_match_mode: ExposureMatchMode = "all"

    person: PersonInput
    control_material: MaterialInput
    rc_material: MaterialInput

    @model_validator(mode="after")
    def validate_request(self):
        normalized_ids = [
            city_id.strip().lower()
            for city_id in self.city_ids
        ]

        if len(normalized_ids) != len(set(normalized_ids)):
            raise ValueError(
                "city_ids cannot contain duplicate cities"
            )

        if self.start_month > self.end_month:
            raise ValueError(
                "start_month cannot be greater than end_month"
            )

        if (
            "representative_day" in self.model_fields_set
            and "sample_days_per_month" not in self.model_fields_set
        ):
            self.sample_days_per_month = 1

        self.city_ids = normalized_ids
        return self


class DailyAdaptationResult(BaseModel):
    sample_date_local: datetime
    weight_days: int

    mean_air_temperature_c: float
    maximum_air_temperature_c: float
    mean_solar_radiation_w_m2: float
    maximum_solar_radiation_w_m2: float

    exposure_eligible: bool
    beneficial: bool

    average_skin_improvement_c: float
    final_skin_improvement_c: float
    average_core_improvement_c: float
    maximum_skin_improvement_c: float

    weather_from_cache: bool


class MonthlyAdaptationResult(BaseModel):
    month: int

    sampled_day_count: int = 1
    eligible_sample_count: int = 0

    total_weighted_days: int = 0
    evaluated_weighted_days: int = 0
    beneficial_weighted_days: int = 0

    exposure_coverage_percent: float = 0.0
    climate_adaptation_rate_percent: float | None = None

    average_skin_improvement_c: float | None = None
    average_core_improvement_c: float | None = None
    maximum_skin_improvement_c: float | None = None

    samples: list[DailyAdaptationResult] = Field(
        default_factory=list
    )

    # 4.1 backward compatibility。
    representative_date_local: datetime | None = None
    weight_days: int | None = None
    final_skin_improvement_c: float | None = None
    beneficial: bool | None = None


class GlobalCityResultResponse(BaseModel):
    id: str
    batch_id: str
    celery_task_id: str | None

    city_id: str
    city_name: str
    country: str
    latitude: float
    longitude: float

    status: GlobalCityStatus
    stage: str
    progress: int

    climate_adaptation_rate_percent: float | None
    exposure_coverage_percent: float | None

    annual_average_skin_improvement_c: float | None
    annual_average_core_improvement_c: float | None
    maximum_skin_improvement_c: float | None
    effective_cooling_hours: float | None

    sampled_day_count: int | None
    eligible_sample_count: int | None

    evaluated_weighted_days: int | None
    beneficial_weighted_days: int | None

    retry_count: int

    monthly_results: list[MonthlyAdaptationResult] | None

    error_message: str | None
    started_at: datetime | None
    completed_at: datetime | None


class GlobalBatchResponse(BaseModel):
    id: str
    celery_group_id: str | None

    status: GlobalBatchStatus
    stage: str
    progress: int

    total_city_count: int
    completed_city_count: int
    failed_city_count: int
    cancelled_city_count: int

    summary: dict | None
    error_message: str | None

    created_at: datetime
    updated_at: datetime
    started_at: datetime | None
    completed_at: datetime | None


class GlobalBatchDetail(GlobalBatchResponse):
    request: GlobalBatchCreate
    city_results: list[GlobalCityResultResponse]


class GlobalBatchListResponse(BaseModel):
    items: list[GlobalBatchResponse]
    total: int
    limit: int
    offset: int