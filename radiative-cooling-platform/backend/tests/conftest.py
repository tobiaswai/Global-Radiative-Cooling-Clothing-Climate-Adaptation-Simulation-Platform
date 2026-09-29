import os
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings
from app.core.runtime import configure_runtime

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from app.schemas.weather import (
    CityResponse, WeatherPoint, WeatherSourceMetadata, WeatherTimeSeries,
)


_test_settings = get_settings()

configure_runtime(
    numba_cache_dir=_test_settings.numba_cache_dir,
)

NUMBA_CACHE_DIR = Path(
    os.environ.get(
        "NUMBA_CACHE_DIR",
        Path(tempfile.gettempdir())
        / "radiative-cooling-numba-cache",
    )
)

NUMBA_CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

os.environ["NUMBA_CACHE_DIR"] = str(
    NUMBA_CACHE_DIR
)


from app.core.config import settings
from app.db.session import get_db
from app.main import app
from app.schemas.simulation import (
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    SimulationRequest,
)


@pytest.fixture
def db_session():
    engine = create_engine(
        settings.database_url,
        pool_pre_ping=True,
    )

    connection = engine.connect()
    transaction = connection.begin()

    TestingSessionLocal = sessionmaker(
        bind=connection,
        autoflush=False,
        expire_on_commit=False,
    )

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
        engine.dispose()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = (
        override_get_db
    )

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(
            get_db,
            None,
        )


@pytest.fixture
def environment() -> EnvironmentInput:
    return EnvironmentInput(
        air_temperature_c=38.0,
        mean_radiant_temperature_c=45.0,
        sky_temperature_c=23.0,
        relative_humidity_percent=40.0,
        wind_speed_m_s=1.5,
        solar_radiation_w_m2=800.0,
        sky_view_factor=0.5,
    )


@pytest.fixture
def person() -> PersonInput:
    return PersonInput(
        met=2.6,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )


@pytest.fixture
def control_material() -> MaterialInput:
    return MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.4,
        solar_transmittance=0.0,
        infrared_emissivity=0.8,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )


@pytest.fixture
def rc_material() -> MaterialInput:
    return MaterialInput(
        name="Radiative Cooling",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0.0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )


@pytest.fixture
def simulation_request(
    environment: EnvironmentInput,
    person: PersonInput,
    control_material: MaterialInput,
    rc_material: MaterialInput,
) -> SimulationRequest:
    return SimulationRequest(
        city="Dubai",
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

@pytest.fixture
def hourly_weather() -> WeatherTimeSeries:
    """Five hourly points 11:00-15:00 Asia/Dubai; exposure 12:00-14:00."""
    tz = ZoneInfo("Asia/Dubai")
    start = datetime(2023, 7, 15, 12, tzinfo=tz)

    temperatures = [41.8, 43.4, 44.2, 44.9, 44.7]
    humidities = [29.0, 26.0, 25.0, 24.0, 24.0]
    winds = [6.17, 5.11, 4.32, 3.69, 3.62]
    ghis = [807.0, 901.0, 929.0, 892.0, 789.0]

    points = [
        WeatherPoint(
            timestamp=start + timedelta(hours=i - 1),
            air_temperature_c=temperatures[i],
            relative_humidity_percent=humidities[i],
            wind_speed_m_s=winds[i],
            ghi_w_m2=ghis[i],
            direct_radiation_w_m2=ghis[i] * 0.75,
            diffuse_radiation_w_m2=ghis[i] * 0.25,
            dni_w_m2=ghis[i] * 0.8,
        )
        for i in range(5)
    ]

    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai", name="Dubai", country="United Arab Emirates",
            latitude=25.2048, longitude=55.2708, elevation_m=16.0,
            timezone="Asia/Dubai", climate_type="hot_dry",
        ),
        requested_start_time=start,
        requested_end_time=start + timedelta(hours=2),
        points=points,
        source=WeatherSourceMetadata(
            provider="test", dataset="test", model="test",
            latitude=25.2, longitude=55.3, elevation_m=16.0,
            timezone="Asia/Dubai", downloaded_at=start,
            from_cache=True, attribution="test",
        ),
    )