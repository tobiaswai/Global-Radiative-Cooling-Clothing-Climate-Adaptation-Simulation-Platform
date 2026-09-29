"""Helpers for regression ("golden") cases.

Two layers of protection
------------------------
1. Numeric comparison (``compare_regression_payloads``, unchanged): skin/core
   temperatures against the stored fixture, with ``temperature_atol``.
2. Parameter fingerprint (new): a SHA-256 over *every constant that can
   change a result*. Compared exactly, before any number is looked at.

Why the second layer
    A 1 % tweak to one constant can move the 2-hour Dubai case by less than
    ``temperature_atol`` and slip through layer 1. Layer 2 has no tolerance,
    and on mismatch names the key that changed and its old/new value.

What is NOT in the fingerprint
    Library versions. Upgrading numpy in CI must not fail the golden test;
    if the upgrade really changes results, layer 1 still catches it.

Hard limit
    Only constants registered in ``model_parameters.MODEL_PARAMETERS``,
    or ``EnvironmentAssumptions`` are
    visible here. A literal left inside ``two_node.py`` is invisible.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from typing import Any

import numpy as np

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import WeatherSimulationResponse

# Import the module, not the names, so tests can monkeypatch
# ``mp.MODEL_PARAMETERS`` and prove the fingerprint reacts.
from app.services import model_parameters as mp

# Bump only when the *shape* of the snapshot changes (new section, renamed
# key). A changed constant value must bump ``mp.MODEL_VERSION`` instead.
SNAPSHOT_SCHEMA_VERSION = 1


# --------------------------------------------------------------------------
# Canonical serialisation
# --------------------------------------------------------------------------


def _to_builtin(value: Any) -> Any:
    """Recursively convert numpy / tuple values to JSON builtins.

    Must be idempotent and must agree with a JSON round-trip, because the
    fixture stores the snapshot as JSON and we re-hash it on load.
    """
    if isinstance(value, Mapping):
        return {str(k): _to_builtin(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_builtin(v) for v in value]
    if isinstance(value, np.ndarray):
        return [_to_builtin(v) for v in value.tolist()]
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, float) and (value != value or value in (float("inf"), float("-inf"))):
        raise ValueError("Non-finite float in parameter snapshot")
    return value


def canonical_json(obj: Any) -> str:
    """Stable JSON: sorted keys, no whitespace, ASCII only, NaN forbidden."""
    return json.dumps(
        _to_builtin(obj),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


# --------------------------------------------------------------------------
# Snapshot and fingerprint
# --------------------------------------------------------------------------


def parameter_snapshot(
    environment_assumptions: EnvironmentAssumptions | None,
) -> dict[str, Any]:
    """Every constant that can change a simulation result, as one dict.

    ``environment_assumptions`` is recorded exactly as given. ``None`` is a
    legitimate value for the constant-environment endpoint; do not
    substitute defaults here.
    """
    return {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "model_parameter_set_version": mp.MODEL_PARAMETER_SET_VERSION,
        "model_parameter_set_sha256": mp.model_parameter_set_sha256(),
        "model_parameters": {
            p.name: p.value for p in mp.list_model_parameters()
        },
        "environment_assumptions": (
            None
            if environment_assumptions is None
            else environment_assumptions.model_dump(mode="json")
        ),
    }


def fingerprint_of_snapshot(snapshot: Mapping[str, Any]) -> str:
    """SHA-256 hex digest of a snapshot (fresh or loaded from a fixture)."""
    return hashlib.sha256(canonical_json(snapshot).encode("utf-8")).hexdigest()


def parameter_fingerprint(
    environment_assumptions: EnvironmentAssumptions | None,
) -> str:
    """Convenience: fingerprint of the *current* constants."""
    return fingerprint_of_snapshot(parameter_snapshot(environment_assumptions))


# --------------------------------------------------------------------------
# Diagnostics
# --------------------------------------------------------------------------


def flatten_snapshot(
    snapshot: Mapping[str, Any],
    prefix: str = "",
) -> dict[str, Any]:
    """``{"a": {"b": 1}}`` -> ``{"a.b": 1}``. Lists stay as leaf values."""
    flat: dict[str, Any] = {}
    for key, value in snapshot.items():
        path = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, Mapping):
            flat.update(flatten_snapshot(value, path))
        else:
            flat[path] = value
    return flat


def diff_snapshots(
    expected: Mapping[str, Any],
    actual: Mapping[str, Any],
) -> list[str]:
    """One line per differing key: ``section.key: old -> new``."""
    flat_expected = flatten_snapshot(_to_builtin(expected))
    flat_actual = flatten_snapshot(_to_builtin(actual))

    lines: list[str] = []
    for key in sorted(set(flat_expected) | set(flat_actual)):
        if key not in flat_actual:
            lines.append(f"parameter_snapshot.{key}: REMOVED (was {flat_expected[key]!r})")
        elif key not in flat_expected:
            lines.append(f"parameter_snapshot.{key}: ADDED ({flat_actual[key]!r})")
        elif flat_expected[key] != flat_actual[key]:
            lines.append(
                f"parameter_snapshot.{key}: {flat_expected[key]!r} -> {flat_actual[key]!r}"
            )
    return lines


_REGEN_HINT = (
    "If intentional: bump MODEL_PARAMETER_SET_VERSION in "
    "app/services/model_parameters.py, record the change in "
    "docs/acceptance/<stage>/golden-refresh.md, then regenerate the fixture "
    "(UPDATE_GOLDEN=1 pytest tests/test_golden_dubai_2h.py). "
    "Otherwise revert the constant."
)

def _compare_parameter_fingerprint(
    expected: Mapping[str, Any],
    actual: Mapping[str, Any],
) -> list[str]:
    """Exact fingerprint check, plus a key-level explanation on mismatch."""
    expected_fp = expected.get("parameter_fingerprint")
    expected_snapshot = expected.get("parameter_snapshot")
    actual_fp = actual["parameter_fingerprint"]
    actual_snapshot = actual["parameter_snapshot"]

    # Old fixture predating this check: fail loudly rather than skip.
    if expected_fp is None or expected_snapshot is None:
        return [
            "parameter_fingerprint: fixture has no fingerprint/snapshot; "
            "regenerate it (python -m scripts.regenerate_golden)"
        ]

    # Fixture integrity: catches hand-edited snapshots with a stale hash.
    recomputed = fingerprint_of_snapshot(expected_snapshot)
    if recomputed != expected_fp:
        return [
            "parameter_fingerprint: fixture is internally inconsistent "
            f"(stored {expected_fp}, snapshot hashes to {recomputed}); regenerate it"
        ]

    if expected_fp == actual_fp:
        return []

    lines = [
        f"parameter_fingerprint: {expected_fp} != {actual_fp} "
        "(model constants changed since the fixture was recorded)"
    ]
    changes = diff_snapshots(expected_snapshot, actual_snapshot)
    lines.extend(changes or ["parameter_snapshot: no key-level difference found; check canonical_json"])
    lines.append(_REGEN_HINT)
    return lines


# --------------------------------------------------------------------------
# Golden payload
# --------------------------------------------------------------------------


def summarize_result_for_regression(
    result: WeatherSimulationResponse,
    *,
    environment_assumptions: EnvironmentAssumptions | None = None,  # <-- PR-2: if the
) -> dict[str, Any]:
    """Reduce a result to the numeric fields we want to keep stable,
    plus a snapshot/fingerprint of the constants that produced them."""
    assumptions = (
        environment_assumptions
        if environment_assumptions is not None
        else getattr(result, "environment_assumptions", None)
    )
    if assumptions is None:
        # Stage 1 results stored before PR-2 carry no assumptions block.
        assumptions = EnvironmentAssumptions()
        
    snapshot = parameter_snapshot(assumptions)
    return {
        "model_version": result.model_version,
        "parameter_fingerprint": fingerprint_of_snapshot(snapshot),
        "parameter_snapshot": snapshot,
        "city": result.city,
        "duration_minutes": result.duration_minutes,
        "summary": result.summary.model_dump(),
        "weather": {
            "point_count": len(result.weather.points),
            "payload_sha256": result.weather.source.payload_sha256,
            "quality": (
                result.weather.source.quality.model_dump(mode="json")
                if result.weather.source.quality
                else None
            ),
        },
        "control": [
            {
                "minute": p.minute,
                "core_temperature_c": p.core_temperature_c,
                "skin_temperature_c": p.skin_temperature_c,
            }
            for p in result.control.time_series
        ],
        "radiative_cooling": [
            {
                "minute": p.minute,
                "core_temperature_c": p.core_temperature_c,
                "skin_temperature_c": p.skin_temperature_c,
            }
            for p in result.radiative_cooling.time_series
        ],
    }


def compare_regression_payloads(
    expected: dict[str, Any],
    actual: dict[str, Any],
    *,
    temperature_atol: float = 1e-6,
) -> list[str]:
    """Return a list of human-readable differences (empty means identical).

    The fingerprint is checked first and exactly. Numeric checks still run
    afterwards so the report shows whether the constant change actually
    moved any temperature.
    """
    differences: list[str] = []

    # --- new: exact constants check -------------------------------------
    differences.extend(_compare_parameter_fingerprint(expected, actual))

    # --- unchanged from here ---------------------------------------------
    for key in ("model_version", "city", "duration_minutes"):
        if expected.get(key) != actual.get(key):
            differences.append(f"{key}: {expected.get(key)!r} != {actual.get(key)!r}")

    for key, value in expected["summary"].items():
        if abs(value - actual["summary"][key]) > temperature_atol:
            differences.append(f"summary.{key}: {value} != {actual['summary'][key]}")

    for scenario in ("control", "radiative_cooling"):
        expected_points = expected[scenario]
        actual_points = actual[scenario]

        if len(expected_points) != len(actual_points):
            differences.append(
                f"{scenario}: {len(expected_points)} vs {len(actual_points)} points"
            )
            continue

        for index, (e, a) in enumerate(zip(expected_points, actual_points)):
            for field in ("minute", "core_temperature_c", "skin_temperature_c"):
                if abs(e[field] - a[field]) > temperature_atol:
                    differences.append(
                        f"{scenario}[{index}].{field}: {e[field]} != {a[field]}"
                    )

    if expected["weather"]["payload_sha256"] != actual["weather"]["payload_sha256"]:
        differences.append("weather payload sha256 differs")

    return differences