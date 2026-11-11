"""Read-only endpoints exposing model constants, defaults and input metadata."""

from fastapi import APIRouter, HTTPException

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.provenance import (
    MaterialFieldManifest,
    ModelMetadata,
    ModelParameter,
    ModelParameterManifest,
)
from app.services.material_fields import build_material_field_manifest
from app.services.model_parameters import (
    MODEL_PARAMETERS,
    build_model_metadata,
    build_model_parameter_manifest,
)


router = APIRouter(prefix="/api/v1/model", tags=["model"])


@router.get("/metadata", response_model=ModelMetadata)
def get_model_metadata() -> ModelMetadata:
    """Version and fingerprint of the active parameter set."""
    return build_model_metadata()


@router.get("/parameters", response_model=ModelParameterManifest)
def get_model_parameters() -> ModelParameterManifest:
    return build_model_parameter_manifest()


@router.get("/parameters/{name}", response_model=ModelParameter)
def get_model_parameter(name: str) -> ModelParameter:
    parameter = MODEL_PARAMETERS.get(name)

    if parameter is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown model parameter: {name}",
        )

    return parameter


@router.get("/material-fields", response_model=MaterialFieldManifest)
def get_material_fields() -> MaterialFieldManifest:
    """Bounds, units, defaults and derivation rules of MaterialInput."""
    return build_material_field_manifest()


@router.get(
    "/environment-assumptions/defaults",
    response_model=EnvironmentAssumptions,
)
def get_default_environment_assumptions() -> EnvironmentAssumptions:
    return EnvironmentAssumptions()