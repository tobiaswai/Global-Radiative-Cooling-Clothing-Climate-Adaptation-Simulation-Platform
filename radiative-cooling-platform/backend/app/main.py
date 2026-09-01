import os
from datetime import datetime, timezone
from pathlib import Path

NUMBA_CACHE_DIR = Path("C:/nc")
NUMBA_CACHE_DIR.mkdir(parents=True, exist_ok=True)

os.environ.setdefault(
    "NUMBA_CACHE_DIR",
    str(NUMBA_CACHE_DIR),
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.simulations import router as simulations_router
from app.api.benchmarks import router as benchmarks_router
from app.api.weather import router as weather_router
from app.api.materials import ( router as materials_router,)


app = FastAPI(
    title="Global Radiative Cooling Clothing Climate Adaptation API",
    description=(
        "Backend API for simulating and evaluating radiative cooling "
        "clothing under global climate conditions."
    ),
    version="0.2.0",
)

from app.core.config import settings

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.frontend_origin,
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulations_router)
app.include_router(benchmarks_router)
app.include_router(weather_router)
app.include_router(materials_router)

@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "radiative-cooling-api",
        "version": "0.2.0",
        "time": datetime.now(
            timezone.utc
        ).isoformat(),
    }
