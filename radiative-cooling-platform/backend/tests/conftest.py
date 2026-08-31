import os
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
from app.main import app
from app.schemas.simulation import (
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    SimulationRequest,
)




@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


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