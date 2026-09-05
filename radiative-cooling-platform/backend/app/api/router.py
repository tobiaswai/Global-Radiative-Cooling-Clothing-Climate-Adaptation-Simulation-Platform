"""Top-level API router."""

from fastapi import APIRouter

from app.api import materials, simulations


api_router = APIRouter()

api_router.include_router(materials.router)
api_router.include_router(simulations.router)