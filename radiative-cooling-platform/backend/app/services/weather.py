from __future__ import annotations

import hashlib
import json
from datetime import (
    date,
    datetime,
    timedelta,
    timezone,
)
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx

from app.core.cities import CityConfig
from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)

import asyncio
import os
from uuid import uuid4

from redis.asyncio import Redis

from app.core.config import settings

OPEN_METEO_ARCHIVE_URL = (
    "https://archive-api.open-meteo.com/v1/archive"
)

HOURLY_VARIABLES = [
    "temperature_2m",
    "relative_humidity_2m",
    "wind_speed_10m",
    "shortwave_radiation",
    "direct_radiation",
    "diffuse_radiation",
    "direct_normal_irradiance",
]

CACHE_DIRECTORY = Path("data/cache/weather")


def city_to_response(
    city: CityConfig,
) -> CityResponse:
    return CityResponse(
        id=city.id,
        name=city.name,
        country=city.country,
        latitude=city.latitude,
        longitude=city.longitude,
        elevation_m=city.elevation_m,
        timezone=city.timezone,
        climate_type=city.climate_type,
    )


def normalize_local_datetime(
    value: datetime,
    timezone_name: str,
) -> datetime:
    city_timezone = ZoneInfo(timezone_name)

    if value.tzinfo is None:
        return value.replace(
            tzinfo=city_timezone
        )

    return value.astimezone(city_timezone)


def validate_archive_date(
    end_time: datetime,
) -> None:
    # ERA5 通常約有五天延遲。
    latest_safe_date = (
        datetime.now(timezone.utc).date()
        - timedelta(days=5)
    )

    if end_time.date() > latest_safe_date:
        raise ValueError(
            "ERA5 historical data are typically delayed by approximately "
            "five days. Please select a date no later than "
            f"{latest_safe_date.isoformat()}."
        )


def build_request_params(
    city: CityConfig,
    start_date: date,
    end_date: date,
) -> dict[str, str | float]:
    return {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "elevation": city.elevation_m,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "hourly": ",".join(HOURLY_VARIABLES),
        "timezone": city.timezone,
        "wind_speed_unit": "ms",
        "temperature_unit": "celsius",
        "models": "era5",
        "cell_selection": "land",
    }


def build_cache_path(
    params: dict[str, str | float],
) -> Path:
    serialized = json.dumps(
        params,
        sort_keys=True,
        ensure_ascii=True,
    )

    digest = hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()[:20]

    return CACHE_DIRECTORY / f"{digest}.json"

def read_cached_payload(
    cache_path: Path,
) -> dict | None:
    if not cache_path.exists():
        return None

    try:
        return json.loads(
            cache_path.read_text(
                encoding="utf-8"
            )
        )
    except (
        OSError,
        json.JSONDecodeError,
    ):
        return None


def write_cached_payload_atomic(
    cache_path: Path,
    payload: dict,
) -> None:
    temporary_path = cache_path.with_name(
        f"{cache_path.name}."
        f"{uuid4().hex}.tmp"
    )

    temporary_path.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    os.replace(
        temporary_path,
        cache_path,
    )


def build_weather_lock_name(
    cache_path: Path,
) -> str:
    return (
        "weather-download-lock:"
        f"{cache_path.stem}"
    )

async def request_open_meteo(
    params: dict[str, str | float],
) -> tuple[dict, bool]:
    cache_path = build_cache_path(
        params
    )

    CACHE_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    cached_payload = read_cached_payload(
        cache_path
    )

    if cached_payload is not None:
        return cached_payload, True

    redis_client = Redis.from_url(
        settings.weather_lock_redis_url,
        decode_responses=True,
    )

    lock = redis_client.lock(
        build_weather_lock_name(
            cache_path
        ),
        timeout=(
            settings
            .weather_lock_timeout_seconds
        ),
        blocking_timeout=(
            settings
            .weather_lock_blocking_timeout_seconds
        ),
    )

    acquired = False

    try:
        acquired = await lock.acquire()

        if not acquired:
            raise RuntimeError(
                "Timed out while waiting for "
                "the weather download lock"
            )

        cached_payload = read_cached_payload(
            cache_path
        )

        if cached_payload is not None:
            return cached_payload, True

        payload = await download_open_meteo_payload(
            params
        )

        write_cached_payload_atomic(
            cache_path,
            payload,
        )

        return payload, False

    except (
        ConnectionError,
        TimeoutError,
    ):
        # Redis failure must not make weather
        # simulation completely unavailable.
        cached_payload = read_cached_payload(
            cache_path
        )

        if cached_payload is not None:
            return cached_payload, True

        payload = await download_open_meteo_payload(
            params
        )

        write_cached_payload_atomic(
            cache_path,
            payload,
        )

        return payload, False

    finally:
        if acquired:
            try:
                await lock.release()
            except Exception:
                pass

        await redis_client.aclose()

def require_hourly_array(
    hourly: dict,
    name: str,
    expected_length: int,
) -> list:
    values = hourly.get(name)

    if values is None:
        raise RuntimeError(
            f"Open-Meteo response is missing variable: {name}"
        )

    if len(values) != expected_length:
        raise RuntimeError(
            f"Open-Meteo variable {name} has inconsistent length"
        )

    return values


def safe_float(
    value: object,
    variable_name: str,
    index: int,
) -> float:
    if value is None:
        raise RuntimeError(
            f"{variable_name} is missing at index {index}"
        )

    return float(value)


def parse_weather_points(
    payload: dict,
    city: CityConfig,
) -> list[WeatherPoint]:
    hourly = payload.get("hourly")

    if not hourly:
        raise RuntimeError(
            "Open-Meteo response is missing hourly data"
        )

    times = hourly.get("time", [])
    expected_length = len(times)

    if expected_length == 0:
        raise RuntimeError(
            "Open-Meteo response is missing weather time points"
        )

    temperature = require_hourly_array(
        hourly,
        "temperature_2m",
        expected_length,
    )
    humidity = require_hourly_array(
        hourly,
        "relative_humidity_2m",
        expected_length,
    )
    wind_speed = require_hourly_array(
        hourly,
        "wind_speed_10m",
        expected_length,
    )
    ghi = require_hourly_array(
        hourly,
        "shortwave_radiation",
        expected_length,
    )
    direct = require_hourly_array(
        hourly,
        "direct_radiation",
        expected_length,
    )
    diffuse = require_hourly_array(
        hourly,
        "diffuse_radiation",
        expected_length,
    )
    dni = require_hourly_array(
        hourly,
        "direct_normal_irradiance",
        expected_length,
    )

    city_timezone = ZoneInfo(city.timezone)
    points: list[WeatherPoint] = []

    for index, timestamp_text in enumerate(times):
        # Open-Meteo 在指定 timezone 時返回當地時間，
        # 字符串本身通常不附帶 UTC offset。
        timestamp = datetime.fromisoformat(
            timestamp_text
        ).replace(tzinfo=city_timezone)

        points.append(
            WeatherPoint(
                timestamp=timestamp,
                air_temperature_c=safe_float(
                    temperature[index],
                    "temperature_2m",
                    index,
                ),
                relative_humidity_percent=safe_float(
                    humidity[index],
                    "relative_humidity_2m",
                    index,
                ),
                wind_speed_m_s=safe_float(
                    wind_speed[index],
                    "wind_speed_10m",
                    index,
                ),
                ghi_w_m2=max(
                    0.0,
                    safe_float(
                        ghi[index],
                        "shortwave_radiation",
                        index,
                    ),
                ),
                direct_radiation_w_m2=max(
                    0.0,
                    safe_float(
                        direct[index],
                        "direct_radiation",
                        index,
                    ),
                ),
                diffuse_radiation_w_m2=max(
                    0.0,
                    safe_float(
                        diffuse[index],
                        "diffuse_radiation",
                        index,
                    ),
                ),
                dni_w_m2=max(
                    0.0,
                    safe_float(
                        dni[index],
                        "direct_normal_irradiance",
                        index,
                    ),
                ),
            )
        )

    return points


async def get_historical_weather(
    city: CityConfig,
    start_time_local: datetime,
    duration_minutes: int,
) -> WeatherTimeSeries:
    start_time = normalize_local_datetime(
        start_time_local,
        city.timezone,
    )

    end_time = start_time + timedelta(
        minutes=duration_minutes
    )

    return await get_historical_weather_range(
        city=city,
        start_time_local=start_time,
        end_time_local=end_time,
        padding_hours=1,
    )

async def get_historical_weather_range(
    *,
    city: CityConfig,
    start_time_local: datetime,
    end_time_local: datetime,
    padding_hours: int = 1,
) -> WeatherTimeSeries:
    start_time = normalize_local_datetime(
        start_time_local,
        city.timezone,
    )

    end_time = normalize_local_datetime(
        end_time_local,
        city.timezone,
    )

    if end_time <= start_time:
        raise ValueError(
            "end_time_local must be after "
            "start_time_local"
        )

    validate_archive_date(end_time)

    query_start = start_time - timedelta(
        hours=padding_hours
    )

    query_end = end_time + timedelta(
        hours=padding_hours
    )

    params = build_request_params(
        city=city,
        start_date=query_start.date(),
        end_date=query_end.date(),
    )

    payload, from_cache = await request_open_meteo(
        params
    )

    all_points = parse_weather_points(
        payload,
        city,
    )

    selected_points = [
        point
        for point in all_points
        if query_start
        <= point.timestamp
        <= query_end
    ]

    if len(selected_points) < 2:
        raise RuntimeError(
            "Open-Meteo response is missing "
            "weather time points"
        )

    return WeatherTimeSeries(
        city=city_to_response(city),
        requested_start_time=start_time,
        requested_end_time=end_time,
        points=selected_points,
        source=WeatherSourceMetadata(
            provider="Open-Meteo",
            dataset="Historical Weather API",
            model="ERA5",
            latitude=float(
                payload.get(
                    "latitude",
                    city.latitude,
                )
            ),
            longitude=float(
                payload.get(
                    "longitude",
                    city.longitude,
                )
            ),
            elevation_m=float(
                payload.get(
                    "elevation",
                    city.elevation_m,
                )
            ),
            timezone=payload.get(
                "timezone",
                city.timezone,
            ),
            downloaded_at=datetime.now(
                timezone.utc
            ),
            from_cache=from_cache,
            attribution=(
                "Weather data by Open-Meteo.com; "
                "underlying reanalysis: ERA5."
            ),
        ),
    )


def slice_weather_time_series(
    *,
    weather: WeatherTimeSeries,
    start_time_local: datetime,
    duration_minutes: int,
    padding_hours: int = 1,
) -> WeatherTimeSeries:
    start_time = normalize_local_datetime(
        start_time_local,
        weather.city.timezone,
    )

    end_time = start_time + timedelta(
        minutes=duration_minutes
    )

    query_start = start_time - timedelta(
        hours=padding_hours
    )

    query_end = end_time + timedelta(
        hours=padding_hours
    )

    selected_points = [
        point
        for point in weather.points
        if query_start
        <= point.timestamp
        <= query_end
    ]

    if len(selected_points) < 2:
        raise RuntimeError(
            "Prefetched weather does not cover "
            f"{start_time.isoformat()} to "
            f"{end_time.isoformat()}"
        )

    return WeatherTimeSeries(
        city=weather.city,
        requested_start_time=start_time,
        requested_end_time=end_time,
        points=selected_points,
        source=weather.source,
    )

async def download_open_meteo_payload(
    params: dict[str, str | float],
) -> dict:
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(60.0),
    ) as client:
        response = await client.get(
            OPEN_METEO_ARCHIVE_URL,
            params=params,
        )

    if response.status_code != 200:
        try:
            error_body = response.json()
            reason = error_body.get(
                "reason",
                response.text,
            )
        except ValueError:
            reason = response.text

        raise RuntimeError(
            "Open-Meteo request failed: "
            f"HTTP {response.status_code}: "
            f"{reason}"
        )

    return response.json()