from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class CityResponse(BaseModel):
    id: str
    name: str
    country: str
    latitude: float
    longitude: float
    elevation_m: float
    timezone: str
    climate_type: str


class WeatherPoint(BaseModel):
    timestamp: datetime

    air_temperature_c: float
    relative_humidity_percent: float
    wind_speed_m_s: float

    ghi_w_m2: float
    direct_radiation_w_m2: float
    diffuse_radiation_w_m2: float
    dni_w_m2: float


class WeatherGap(BaseModel):
    """A break in the hourly timeline between two consecutive points."""

    start: datetime
    end: datetime
    missing_steps: int = Field(ge=1)


class WeatherQualityReport(BaseModel):
    """Result of normalising a raw weather timeline (Stage 1, PR-1)."""

    expected_step_seconds: int = Field(gt=0)
    point_count: int = Field(ge=0)
    first_timestamp: datetime | None = None
    last_timestamp: datetime | None = None
    was_sorted: bool = True
    duplicates_removed: int = 0
    gaps: list[WeatherGap] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


class WeatherSourceMetadata(BaseModel):
    provider: str
    dataset: str
    model: str
    latitude: float
    longitude: float
    elevation_m: float
    timezone: str
    downloaded_at: datetime
    from_cache: bool
    attribution: str

    # Stage 1 additions. Optional so previously stored results still load.
    payload_sha256: str | None = None
    quality: WeatherQualityReport | None = None


class WeatherTimeSeries(BaseModel):
    city: CityResponse
    requested_start_time: datetime
    requested_end_time: datetime
    points: list[WeatherPoint]
    source: WeatherSourceMetadata

    @model_validator(mode="after")
    def validate_points(self):
        if len(self.points) < 2:
            raise ValueError(
                "Dynamic simulation requires at least two weather data points"
            )

        timestamps = [point.timestamp for point in self.points]

        for previous, current in zip(timestamps, timestamps[1:]):
            if current <= previous:
                raise ValueError(
                    "Weather time series must be strictly increasing in time "
                    "(sorted, no duplicate timestamps)"
                )

        return self


class WeatherHistoryQuery(BaseModel):
    city_id: str
    start_time_local: datetime
    duration_minutes: int = Field(
        default=120,
        ge=1,
        le=1440,
    )