"""Context hash: every field a surrogate model assumes fixed (ADR 0011)."""

from __future__ import annotations

import hashlib

from app.schemas.surrogate import SurrogateDatasetCreate
from app.services.reproducibility import canonical_json, parameter_fingerprint

CONTEXT_FIELDS = frozenset({
    "local_start_hour", "duration_minutes", "output_interval_minutes",
    "skin_threshold_c", "core_threshold_c", "person", "control_material",
    "base_material", "environment_assumptions", "variables",
})


def context_sha256(spec: SurrogateDatasetCreate) -> str:
    payload = spec.model_dump(mode="json", include=set(CONTEXT_FIELDS))
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def current_fingerprint(spec: SurrogateDatasetCreate) -> str:
    return parameter_fingerprint(spec.environment_assumptions)