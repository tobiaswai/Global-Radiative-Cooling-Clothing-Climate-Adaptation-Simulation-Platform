"""File layout and atomic writes for surrogate datasets and artifacts."""

from __future__ import annotations

import hashlib
import json
import os
from collections.abc import Iterable
from pathlib import Path
from typing import Any
from uuid import uuid4

import pandas as pd

from app.core.config import settings


def surrogate_root() -> Path:
    return Path(settings.surrogate_directory)


def dataset_directory(dataset_id: str) -> Path:
    return surrogate_root() / "datasets" / dataset_id


def chunk_path(dataset_id: str, city_id: str, month: int) -> Path:
    return dataset_directory(dataset_id) / f"part-{city_id}-{month:02d}.parquet"


def model_artifact_path(model_id: str) -> Path:
    return surrogate_root() / "models" / f"{model_id}.joblib"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _temporary(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.with_name(f"{path.name}.{uuid4().hex}.tmp")


def write_frame(frame: pd.DataFrame, path: Path) -> str:
    temporary = _temporary(path)
    frame.to_parquet(temporary, index=False)
    os.replace(temporary, path)
    return file_sha256(path)


def write_json(path: Path, payload: Any) -> None:
    temporary = _temporary(path)
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8")
    os.replace(temporary, path)


def load_frame(paths: Iterable[str]) -> pd.DataFrame:
    frames = [pd.read_parquet(p) for p in paths]
    if not frames:
        raise ValueError("dataset has no completed chunk files")
    return pd.concat(frames, ignore_index=True)