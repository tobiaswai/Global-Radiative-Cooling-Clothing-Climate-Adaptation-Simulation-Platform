# app/api/router.py
"""Top-level API router. The only place routers are aggregated."""

from fastapi import APIRouter

from app.api import benchmarks, global_batches, materials, model, ops, simulations, weather


api_router = APIRouter()

for router in (
    simulations.router,
    benchmarks.router,
    weather.router,
    materials.router,
    global_batches.router,
    model.router,
    ops.router,
):
    api_router.include_router(router)