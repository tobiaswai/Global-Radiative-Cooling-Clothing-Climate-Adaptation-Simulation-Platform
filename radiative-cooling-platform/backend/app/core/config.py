"""Application settings."""

from functools import lru_cache
from pathlib import Path
from pydantic import Field


from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BACKEND_DIRECTORY = Path(__file__).resolve().parents[2]


def split_csv_setting(value: str) -> list[str]:
    """Split a comma-separated application setting."""
    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ]


class Settings(BaseSettings):
    app_name: str = "Radiative Cooling Simulation API"
    app_env: str = "development"

    database_url: str = (
        "postgresql+psycopg://"
        "rc_user:rc_password@localhost:5432/"
        "radiative_cooling"
    )

    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/1"

    frontend_origin: str = "http://localhost:3000"

    result_directory: Path = (
        BACKEND_DIRECTORY / "data" / "results"
    )

    # Leave this empty to use the operating system temporary directory.
    numba_cache_dir: str | None = Field(
        default=None,
        validation_alias="NUMBA_CACHE_DIR",
    )

    cors_origins: str = "http://localhost:3000"
    cors_methods: str = (
        "GET,POST,PUT,PATCH,DELETE,OPTIONS"
    )
    cors_headers: str = (
        "Accept,Authorization,Content-Type,Origin,"
        "X-Requested-With,Last-Event-ID"
    )
    cors_expose_headers: str = "Content-Disposition"
    cors_allow_credentials: bool = True

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIRECTORY / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        return split_csv_setting(self.cors_origins)

    @property
    def cors_method_list(self) -> list[str]:
        return [
            method.upper()
            for method in split_csv_setting(
                self.cors_methods
            )
        ]

    @property
    def cors_header_list(self) -> list[str]:
        return split_csv_setting(self.cors_headers)

    @property
    def cors_exposed_header_list(self) -> list[str]:
        return split_csv_setting(
            self.cors_expose_headers
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings."""
    application_settings = Settings()

    application_settings.result_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return application_settings


# Keep this alias for modules that still import `settings` directly.
settings = get_settings()