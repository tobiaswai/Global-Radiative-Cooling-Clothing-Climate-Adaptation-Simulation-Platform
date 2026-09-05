from dataclasses import asdict, dataclass


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
    "singapore": CityConfig(
        id="singapore",
        name="Singapore",
        country="Singapore",
        latitude=1.3521,
        longitude=103.8198,
        elevation_m=15.0,
        timezone="Asia/Singapore",
        climate_type="equatorial_humid",
    ),
    "delhi": CityConfig(
        id="delhi",
        name="Delhi",
        country="India",
        latitude=28.6139,
        longitude=77.2090,
        elevation_m=216.0,
        timezone="Asia/Kolkata",
        climate_type="hot_semi_arid",
    ),
    "riyadh": CityConfig(
        id="riyadh",
        name="Riyadh",
        country="Saudi Arabia",
        latitude=24.7136,
        longitude=46.6753,
        elevation_m=612.0,
        timezone="Asia/Riyadh",
        climate_type="hot_desert",
    ),
    "cairo": CityConfig(
        id="cairo",
        name="Cairo",
        country="Egypt",
        latitude=30.0444,
        longitude=31.2357,
        elevation_m=23.0,
        timezone="Africa/Cairo",
        climate_type="hot_desert",
    ),
    "lagos": CityConfig(
        id="lagos",
        name="Lagos",
        country="Nigeria",
        latitude=6.5244,
        longitude=3.3792,
        elevation_m=41.0,
        timezone="Africa/Lagos",
        climate_type="tropical_humid",
    ),
    "nairobi": CityConfig(
        id="nairobi",
        name="Nairobi",
        country="Kenya",
        latitude=-1.2921,
        longitude=36.8219,
        elevation_m=1795.0,
        timezone="Africa/Nairobi",
        climate_type="tropical_highland",
    ),
    "phoenix": CityConfig(
        id="phoenix",
        name="Phoenix",
        country="United States",
        latitude=33.4484,
        longitude=-112.0740,
        elevation_m=331.0,
        timezone="America/Phoenix",
        climate_type="hot_desert",
    ),
    "houston": CityConfig(
        id="houston",
        name="Houston",
        country="United States",
        latitude=29.7604,
        longitude=-95.3698,
        elevation_m=13.0,
        timezone="America/Chicago",
        climate_type="humid_subtropical",
    ),
    "mexico-city": CityConfig(
        id="mexico-city",
        name="Mexico City",
        country="Mexico",
        latitude=19.4326,
        longitude=-99.1332,
        elevation_m=2240.0,
        timezone="America/Mexico_City",
        climate_type="subtropical_highland",
    ),
    "manaus": CityConfig(
        id="manaus",
        name="Manaus",
        country="Brazil",
        latitude=-3.1190,
        longitude=-60.0217,
        elevation_m=92.0,
        timezone="America/Manaus",
        climate_type="equatorial_humid",
    ),
    "sao-paulo": CityConfig(
        id="sao-paulo",
        name="São Paulo",
        country="Brazil",
        latitude=-23.5505,
        longitude=-46.6333,
        elevation_m=760.0,
        timezone="America/Sao_Paulo",
        climate_type="humid_subtropical",
    ),
    "darwin": CityConfig(
        id="darwin",
        name="Darwin",
        country="Australia",
        latitude=-12.4634,
        longitude=130.8456,
        elevation_m=31.0,
        timezone="Australia/Darwin",
        climate_type="tropical_savanna",
    ),
    "sydney": CityConfig(
        id="sydney",
        name="Sydney",
        country="Australia",
        latitude=-33.8688,
        longitude=151.2093,
        elevation_m=58.0,
        timezone="Australia/Sydney",
        climate_type="humid_subtropical",
    ),
}


def get_city(city_id: str) -> CityConfig:
    normalized_id = city_id.strip().lower()

    if normalized_id not in CITIES:
        supported = ", ".join(sorted(CITIES))

        raise ValueError(
            f"City not supported '{city_id}'. "
            f"Currently supported: {supported}"
        )

    return CITIES[normalized_id]


def list_cities() -> list[CityConfig]:
    return sorted(
        CITIES.values(),
        key=lambda city: (
            city.country,
            city.name,
        ),
    )


def city_to_dict(
    city: CityConfig,
) -> dict[str, str | float]:
    return asdict(city)