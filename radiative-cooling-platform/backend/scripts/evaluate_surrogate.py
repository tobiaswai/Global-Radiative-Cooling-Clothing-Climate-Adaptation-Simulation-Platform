"""Evaluate a trained surrogate on an independent dataset (temporal hold-out, N4).

Usage (from backend/): python scripts/evaluate_surrogate.py <model_id> <dataset_id>
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import select  # noqa: E402

from app.db.session import SessionLocal  # noqa: E402
from app.models.surrogate import SurrogateDataset, SurrogateDatasetChunk, SurrogateModel  # noqa: E402
from app.services.surrogate.dataset_io import load_frame  # noqa: E402
from app.services.surrogate.registry import load_bundle  # noqa: E402
from app.services.surrogate.training import evaluate_estimators  # noqa: E402

OUT = Path("docs/acceptance/stage-13-surrogate/temporal-holdout.md")


def main(model_id: str, dataset_id: str) -> None:
    with SessionLocal() as session:
        model = session.get(SurrogateModel, model_id)
        dataset = session.get(SurrogateDataset, dataset_id)
        if model is None or dataset is None:
            raise SystemExit("model or dataset not found")
        if model.context_sha256 != dataset.context_sha256:
            raise SystemExit("context differs: the hold-out set must use the model's context")
        files = session.scalars(select(SurrogateDatasetChunk.file_path).where(
            SurrogateDatasetChunk.dataset_id == dataset_id,
            SurrogateDatasetChunk.status == "completed",
            SurrogateDatasetChunk.file_path.is_not(None))).all()
        bundle = load_bundle(model.artifact_path, model.artifact_sha256)
        name, year = model.name, dataset.spec_json["year"]

    frame = load_frame(files)
    metrics = evaluate_estimators(bundle["estimators"], bundle["feature_columns"], frame)
    thresholds = bundle["training"]["mae_thresholds"]

    lines = [f"# Temporal hold-out – {name} on {year}", "",
             f"Model `{model_id}`, dataset `{dataset_id}`, {len(frame)} rows.", "",
             "| target | n | MAE | threshold | RMSE | R² | coverage |", "|---|---|---|---|---|---|---|"]
    for m in metrics:
        r2 = "—" if m.r2 is None else f"{m.r2:.4f}"
        lines.append(f"| {m.target} | {m.count} | {m.mae:.4f} | {thresholds.get(m.target, '—')} | "
                     f"{m.rmse:.4f} | {r2} | {m.interval_coverage:.3f} |")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])