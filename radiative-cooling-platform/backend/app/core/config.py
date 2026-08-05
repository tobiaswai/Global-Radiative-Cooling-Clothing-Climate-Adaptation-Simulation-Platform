from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BACKEND_DIRECTORY = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    app_name: str = (
        "Radiative Cooling Simulation API"
    )
    app_env: str = "development"

    database_url: str = (
        "postgresql+psycopg://"
        "rc_user:rc_password@localhost:5432/"
        "radiative_cooling"
    )

    celery_broker_url: str = (
        "redis://localhost:6379/0"
    )
    celery_result_backend: str = (
        "redis://localhost:6379/1"
    )

    frontend_origin: str = (
        "http://localhost:3000"
    )

    result_directory: Path = (
        BACKEND_DIRECTORY / "data" / "results"
    )

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIRECTORY / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
settings.result_directory.mkdir(
    parents=True,
    exist_ok=True,
)