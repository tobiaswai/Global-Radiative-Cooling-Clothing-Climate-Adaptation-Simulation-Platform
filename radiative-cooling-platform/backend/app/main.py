import os
from datetime import datetime, timezone
from pathlib import Path
from app.api import materials, simulations

# 必須在匯入可能使用 Numba 的模組之前設定。
NUMBA_CACHE_DIR = Path("C:/nc")
NUMBA_CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

os.environ.setdefault(
    "NUMBA_CACHE_DIR",
    str(NUMBA_CACHE_DIR),
)


from fastapi import FastAPI  # noqa: E402

from app.core.config import get_settings  # noqa: E402
from app.core.cors import add_cors_middleware  # noqa: E402
from app.core.runtime import configure_runtime
from app.api.router import api_router  

from app.api.benchmarks import (  # noqa: E402
    router as benchmarks_router,
)
from app.api.materials import (  # noqa: E402
    router as materials_router,
)
from app.api.simulations import (  # noqa: E402
    router as simulations_router,
)
from app.api.weather import (  # noqa: E402
    router as weather_router,
)


settings = get_settings()
configure_runtime(
    numba_cache_dir=settings.numba_cache_dir,
)


app = FastAPI(
    title=(
        "Global Radiative Cooling Clothing "
        "Climate Adaptation API"
    ),
    description=(
        "Backend API for simulating and evaluating radiative cooling "
        "clothing under global climate conditions."
    ),
    version="0.2.0",
)


# 只加入一次 CORS middleware。
add_cors_middleware(
    app,
    origins=settings.cors_origin_list,
    methods=settings.cors_method_list,
    headers=settings.cors_header_list,
    expose_headers=settings.cors_exposed_header_list,
    allow_credentials=settings.cors_allow_credentials,
)


app.include_router(simulations_router)
app.include_router(benchmarks_router)
app.include_router(weather_router)
app.include_router(materials_router)
app.include_router(api_router)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "radiative-cooling-api",
        "version": app.version,
        "time": datetime.now(
            timezone.utc
        ).isoformat(),
    }