"""Material field manifest for ``GET /model/material-fields`` (Stage 4).

Everything is introspected from ``MaterialInput`` so bounds, defaults and
units cannot drift from the validation actually applied to requests.
"""

from __future__ import annotations

import types
from typing import Any, Union, get_args, get_origin

from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

from app.schemas.provenance import (
    MATERIAL_PHYSICAL_FIELD_ORDER,
    MaterialFieldDescriptor,
    MaterialFieldManifest,
    SourceType,
)
from app.schemas.simulation import MaterialInput
from app.services.model_parameters import build_model_metadata


def _bound(field: FieldInfo, attribute: str) -> float | None:
    for item in field.metadata:
        value = getattr(item, attribute, None)
        if value is not None:
            return float(value)
    return None


def _is_nullable(annotation: Any) -> bool:
    origin = get_origin(annotation)
    if origin is Union or origin is types.UnionType:
        return type(None) in get_args(annotation)
    return False


def _default(field: FieldInfo) -> float | None:
    value = field.default
    if value is PydanticUndefined or value is None:
        return None
    return float(value)


def _extra(field: FieldInfo, key: str) -> str | None:
    extra = field.json_schema_extra
    if isinstance(extra, dict):
        value = extra.get(key)
        return str(value) if value is not None else None
    return None


def describe_material_field(name: str) -> MaterialFieldDescriptor:
    field = MaterialInput.model_fields[name]

    return MaterialFieldDescriptor(
        name=name,
        unit=_extra(field, "unit") or "-",
        description=field.description or "",
        minimum=_bound(field, "ge"),
        maximum=_bound(field, "le"),
        default=_default(field),
        nullable=_is_nullable(field.annotation),
        derived_when_null=_extra(field, "derived_when_null"),
    )


def list_material_fields() -> list[MaterialFieldDescriptor]:
    return [describe_material_field(name) for name in MATERIAL_PHYSICAL_FIELD_ORDER]


def build_material_field_manifest() -> MaterialFieldManifest:
    return MaterialFieldManifest(
        **build_model_metadata().model_dump(),
        source_types=list(get_args(SourceType)),
        fields=list_material_fields(),
    )