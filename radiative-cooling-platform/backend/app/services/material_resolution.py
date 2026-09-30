"""Resolve ``MaterialInput.material_version_id`` against the material library
(Stage 4, PR-4).

Contract
--------
* No ``material_version_id``      -> the input is returned untouched.
* Unknown id                       -> MaterialVersionNotFoundError (422).
* Physical field supplied and != stored value
                                   -> MaterialParameterConflictError (422).
* Physical field omitted           -> filled from the stored version.
* Provenance fields omitted        -> filled from the stored version.
* Stored version not a valid input -> MaterialVersionInvalidError (422).

Resolution happens once, at the API boundary, and the *resolved* request is
what gets persisted in ``request_json``. Workers never resolve again.
"""

from __future__ import annotations

import math
from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.material import MaterialVersion
from app.schemas.provenance import MATERIAL_PHYSICAL_FIELD_ORDER
from app.schemas.simulation import MaterialInput


MATERIAL_NAME_MAX_LENGTH = 100
FLOAT_TOLERANCE = 1e-9
PROVENANCE_FIELDS: tuple[str, ...] = (
    "source_type",
    "source_reference",
    "parameter_sources",
)

RequestT = TypeVar("RequestT", bound=BaseModel)


class MaterialResolutionError(ValueError):
    """Base class; mapped to HTTP 422 by ``app.api.errors``."""

    code: str = "MATERIAL_RESOLUTION_ERROR"

    def __init__(
        self,
        message: str,
        *,
        context: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.context: dict[str, Any] = dict(context or {})

    def to_detail(self) -> dict[str, Any]:
        return {"code": self.code, "message": str(self), **self.context}


class MaterialVersionNotFoundError(MaterialResolutionError):
    code = "MATERIAL_VERSION_NOT_FOUND"


class MaterialVersionInvalidError(MaterialResolutionError):
    code = "MATERIAL_VERSION_INVALID"


class MaterialParameterConflictError(MaterialResolutionError):
    code = "MATERIAL_PARAMETER_CONFLICT"


def version_display_name(version: MaterialVersion) -> str:
    name = f"{version.material.name} v{version.version_number}"
    return name[:MATERIAL_NAME_MAX_LENGTH]


def material_input_from_version(version: MaterialVersion) -> MaterialInput:
    """The single mapping from a stored version to a simulation input."""
    try:
        return MaterialInput(
            name=version_display_name(version),
            clothing_insulation_clo=version.clothing_insulation_clo,
            evaporative_resistance_m2pa_w=version.evaporative_resistance_m2pa_w,
            clothing_area_factor=version.clothing_area_factor,
            solar_reflectance=version.solar_reflectance,
            solar_transmittance=version.solar_transmittance,
            infrared_emissivity=version.infrared_emissivity,
            infrared_transmittance=version.infrared_transmittance,
            projected_solar_area_factor=version.projected_solar_area_factor,
            absorbed_solar_to_body_fraction=(
                version.absorbed_solar_to_body_fraction
            ),
            material_version_id=version.id,
            source_type=version.source_type,
            source_reference=version.source_reference,
            parameter_sources=version.parameter_sources_json,
        )
    except ValidationError as error:
        first = error.errors()[0]
        raise MaterialVersionInvalidError(
            f"Material version {version.id} cannot be used as a simulation "
            f"input: {first['msg']}",
            context={
                "material_version_id": version.id,
                "field": ".".join(str(part) for part in first["loc"]),
            },
        ) from error


def load_material_version(session: Session, version_id: str) -> MaterialVersion:
    version = session.scalar(
        select(MaterialVersion)
        .options(selectinload(MaterialVersion.material))
        .where(MaterialVersion.id == version_id)
    )

    if version is None:
        raise MaterialVersionNotFoundError(
            f"Material version {version_id} does not exist",
            context={"material_version_id": version_id},
        )

    return version


def _values_differ(requested: float | None, stored: float | None) -> bool:
    if requested is None or stored is None:
        return (requested is None) != (stored is None)

    return not math.isclose(
        float(requested), float(stored),
        rel_tol=FLOAT_TOLERANCE, abs_tol=FLOAT_TOLERANCE,
    )


def resolve_material_input(
    session: Session,
    material: MaterialInput,
) -> MaterialInput:
    if material.material_version_id is None:
        return material

    version = load_material_version(session, material.material_version_id)
    stored = material_input_from_version(version)

    explicit = material.model_fields_set
    conflicts: list[dict[str, Any]] = []
    updates: dict[str, Any] = {}

    for field in MATERIAL_PHYSICAL_FIELD_ORDER:
        requested_value = getattr(material, field)
        stored_value = getattr(stored, field)

        if field in explicit:
            if _values_differ(requested_value, stored_value):
                conflicts.append(
                    {
                        "field": field,
                        "requested": requested_value,
                        "stored": stored_value,
                    }
                )
        else:
            updates[field] = stored_value

    if conflicts:
        names = ", ".join(item["field"] for item in conflicts)
        raise MaterialParameterConflictError(
            f"Request values differ from material version "
            f"{version.id} ({version_display_name(version)}) for: {names}. "
            "Remove material_version_id to simulate a modified garment.",
            context={
                "material_version_id": version.id,
                "conflicts": conflicts,
            },
        )

    for field in PROVENANCE_FIELDS:
        if field not in explicit or getattr(material, field) is None:
            updates[field] = getattr(stored, field)

    try:
        return MaterialInput.model_validate(
            {**material.model_dump(), **updates}
        )
    except ValidationError as error:
        raise MaterialVersionInvalidError(
            f"Resolved material input for version {version.id} is invalid: "
            f"{error.errors()[0]['msg']}",
            context={"material_version_id": version.id},
        ) from error


def resolve_request_materials(
    session: Session,
    request: RequestT,
    *,
    fields: tuple[str, ...] = ("control_material", "rc_material"),
) -> RequestT:
    """Resolve every MaterialInput attribute named in ``fields``.

    Returns the same object when nothing needed resolving, so callers can
    detect "no library involvement" with an identity check.
    """
    updates: dict[str, MaterialInput] = {}

    for field in fields:
        material = getattr(request, field, None)

        if material is None:
            continue

        resolved = resolve_material_input(session, material)

        if resolved is not material:
            updates[field] = resolved

    return request.model_copy(update=updates) if updates else request


def linked_material_version_ids(
    request: BaseModel,
) -> tuple[str | None, str | None]:
    """(control, rc) version ids recorded on the job row."""
    control = getattr(request, "control_material", None)
    rc = getattr(request, "rc_material", None)

    return (
        getattr(control, "material_version_id", None),
        getattr(rc, "material_version_id", None),
    )