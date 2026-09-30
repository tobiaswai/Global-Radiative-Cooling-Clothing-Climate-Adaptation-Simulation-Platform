"""FastAPI application entry point."""

from datetime import datetime, timezone

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.cors import add_cors_middleware
from app.core.runtime import configure_runtime


settings = get_settings()

# Must run before any module that imports Numba (pythermalcomfort).
configure_runtime(numba_cache_dir=settings.numba_cache_dir)

from app.api.errors import register_exception_handlers  # noqa: E402
from app.api.router import api_router  # noqa: E402


app = FastAPI(
    title="Global Radiative Cooling Clothing Climate Adaptation API",
    description=(
        "Backend API for simulating and evaluating radiative cooling "
        "clothing under global climate conditions."
    ),
    version="0.3.0",
)

add_cors_middleware(
    app,
    origins=settings.cors_origin_list,
    methods=settings.cors_method_list,
    headers=settings.cors_header_list,
    expose_headers=settings.cors_exposed_header_list,
    allow_credentials=settings.cors_allow_credentials,
)

register_exception_handlers(app)

app.include_router(api_router)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "radiative-cooling-api",
        "version": app.version,
        "time": datetime.now(timezone.utc).isoformat(),
    }