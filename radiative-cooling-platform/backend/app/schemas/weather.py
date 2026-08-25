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

        timestamps = [
            point.timestamp
            for point in self.points
        ]

        if timestamps != sorted(timestamps):
            raise ValueError(
                "Weather time series must be sorted in ascending order"
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