"""Load request_json persisted by earlier stages (ADR 0009).

Requests stored before Stage 2 have no ``environment_assumptions`` key. Since
Stage 12 the schema default is the physical environment, so validating those
payloads directly would silently re-interpret them. Every load from the
database goes through ``load_stored_request``.
"""

from __future__ import annotations

from typing import Any, TypeVar

from pydantic import BaseModel

from app.schemas.environment import LEGACY_PRESET, preset_assumptions

ModelT = TypeVar("ModelT", bound=BaseModel)


def with_stored_environment(payload: dict[str, Any] | None) -> dict[str, Any]:
    data = dict(payload or {})
    if data.get("environment_assumptions") is None:
        data["environment_assumptions"] = preset_assumptions(LEGACY_PRESET).model_dump(mode="json")
    return data


def load_stored_request(model: type[ModelT], payload: dict[str, Any] | None) -> ModelT:
    return model.model_validate(with_stored_environment(payload))