from datetime import datetime

from fastapi import APIRouter, HTTPException, Query

from app.core.cities import CITIES, get_city
from app.schemas.weather import (
    CityResponse,
    WeatherTimeSeries,
)
from app.services.weather import (
    city_to_response,
    get_historical_weather,
)


router = APIRouter(
    prefix="/api/v1/weather",
    tags=["weather"],
)


@router.get(
    "/cities",
    response_model=list[CityResponse],
)
def list_cities() -> list[CityResponse]:
    return [
        city_to_response(city)
        for city in CITIES.values()
    ]


@router.get(
    "/history",
    response_model=WeatherTimeSeries,
)
async def weather_history(
    city_id: str = Query(...),
    start_time_local: datetime = Query(...),
    duration_minutes: int = Query(
        default=120,
        ge=1,
        le=1440,
    ),
) -> WeatherTimeSeries:
    try:
        city = get_city(city_id)

        return await get_historical_weather(
            city=city,
            start_time_local=start_time_local,
            duration_minutes=duration_minutes,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error
    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error),
        ) from error