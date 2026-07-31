from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="Radiative Cooling Simulation API",
    description="輻射製冷服裝全球氣候適應性模擬平台後端",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SimulationRequest(BaseModel):
    city: str = Field(min_length=1)
    duration_minutes: int = Field(default=120, ge=1, le=1440)
    air_temperature_c: float
    relative_humidity_percent: float = Field(ge=0, le=100)
    solar_reflectance: float = Field(ge=0, le=1)
    mir_emissivity: float = Field(ge=0, le=1)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "radiative-cooling-api",
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/api/v1/simulations/preview")
def preview_simulation(request: SimulationRequest):
    # 目前只是用於測試前後端通信的臨時公式。
    # 後續需要替換為 Two-Node 或 JOS-3 模型。
    estimated_cooling = (
        request.solar_reflectance * 1.2
        + request.mir_emissivity * 0.8
    )

    estimated_skin_temperature = (
        33.5
        + max(request.air_temperature_c - 30.0, 0) * 0.08
        - estimated_cooling
    )

    return {
        "status": "preview_completed",
        "city": request.city,
        "duration_minutes": request.duration_minutes,
        "estimated_skin_temperature_c": round(
            estimated_skin_temperature, 2
        ),
        "estimated_cooling_effect_c": round(
            estimated_cooling, 2
        ),
        "warning": "此結果僅為接口測試，不是正式物理模型結果。",
    }