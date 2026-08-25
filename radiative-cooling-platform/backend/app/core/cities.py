from dataclasses import dataclass


@dataclass(frozen=True)
class CityConfig:
    id: str
    name: str
    country: str
    latitude: float
    longitude: float
    elevation_m: float
    timezone: str
    climate_type: str


CITIES: dict[str, CityConfig] = {
    "dubai": CityConfig(
        id="dubai",
        name="Dubai",
        country="United Arab Emirates",
        latitude=25.2048,
        longitude=55.2708,
        elevation_m=16.0,
        timezone="Asia/Dubai",
        climate_type="hot_dry",
    ),
    "guangzhou": CityConfig(
        id="guangzhou",
        name="Guangzhou",
        country="China",
        latitude=23.1291,
        longitude=113.2644,
        elevation_m=21.0,
        timezone="Asia/Shanghai",
        climate_type="hot_humid",
    ),
    "lhasa": CityConfig(
        id="lhasa",
        name="Lhasa",
        country="China",
        latitude=29.6520,
        longitude=91.1721,
        elevation_m=3650.0,
        timezone="Asia/Shanghai",
        climate_type="high_altitude_solar",
    ),
}


def get_city(city_id: str) -> CityConfig:
    normalized_id = city_id.strip().lower()

    if normalized_id not in CITIES:
        supported = ", ".join(sorted(CITIES))
        raise ValueError(
            f"City not supported '{city_id}'."
            f"Currently supported: {supported}"
        )

    return CITIES[normalized_id]