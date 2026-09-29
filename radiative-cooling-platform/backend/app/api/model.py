"""Read-only endpoints exposing model constants and default assumptions."""

from fastapi import APIRouter

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.provenance import ModelParameterManifest
from app.services.model_parameters import build_model_parameter_manifest


router = APIRouter(prefix="/api/v1/model", tags=["model"])


@router.get("/parameters", response_model=ModelParameterManifest)
def get_model_parameters() -> ModelParameterManifest:
    return build_model_parameter_manifest()


@router.get(
    "/environment-assumptions/defaults",
    response_model=EnvironmentAssumptions,
)
def get_default_environment_assumptions() -> EnvironmentAssumptions:
    return EnvironmentAssumptions()