"""Model artifact storage. Artifacts are joblib pickles: load only server-made files."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from uuid import uuid4

import joblib

from app.services.surrogate.dataset_io import file_sha256


class SurrogateArtifactError(RuntimeError):
    pass


def save_bundle(bundle: dict, path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.{uuid4().hex}.tmp")
    joblib.dump(bundle, temporary, compress=3)
    os.replace(temporary, path)
    return file_sha256(path)


@lru_cache(maxsize=4)
def load_bundle(path: str, sha256: str) -> dict:
    artifact = Path(path)
    if not artifact.exists():
        raise SurrogateArtifactError(f"artifact not found: {path}")
    if file_sha256(artifact) != sha256:
        raise SurrogateArtifactError(f"artifact checksum mismatch: {path}")
    bundle = joblib.load(artifact)
    if bundle.get("format") != 1:
        raise SurrogateArtifactError("unsupported artifact format")
    return bundle