"""Markdown rendering of a validation report."""

from __future__ import annotations

from app.schemas.surrogate import SurrogateTrainingCreate, TargetMetrics, ValidationReport


def _metrics_table(metrics: list[TargetMetrics]) -> list[str]:
    lines = ["| target | n | MAE | RMSE | R² | coverage | mean width |", "|---|---|---|---|---|---|---|"]
    for m in metrics:
        r2 = "—" if m.r2 is None else f"{m.r2:.4f}"
        lines.append(f"| {m.target} | {m.count} | {m.mae:.4f} | {m.rmse:.4f} | {r2} | "
                     f"{m.interval_coverage:.3f} | {m.mean_interval_width:.4f} |")
    return lines


def render_validation_report(*, name: str, model_id: str, dataset_id: str | None,
                             report: ValidationReport, training: SurrogateTrainingCreate) -> str:
    lines = [
        f"# Surrogate validation report – {name}", "",
        f"- Model: `{model_id}`  Dataset: `{dataset_id}`",
        f"- Rows: {report.row_count}; training cities: {', '.join(report.training_cities)}",
        f"- Interval: quantiles {training.lower_quantile:g}–{training.upper_quantile:g} "
        f"(nominal coverage {report.nominal_interval_coverage:.0%})",
        f"- Verdict: **{'ACCEPTED' if report.passed else 'REJECTED'}**", "",
        "## Acceptance checks", "",
        "| split | target | MAE | threshold | coverage | minimum | passed |",
        "|---|---|---|---|---|---|---|",
    ]
    for c in report.acceptance:
        lines.append(f"| {c.split} | {c.target} | {c.mae:.4f} | {c.mae_threshold:g} | "
                     f"{c.interval_coverage:.3f} | {c.minimum_coverage:g} | {'yes' if c.passed else 'NO'} |")
    if not report.acceptance:
        lines.append("| — | no acceptance split could be evaluated | | | | | NO |")

    for split in report.splits:
        lines += ["", f"## {split.split} ({split.fold_count} folds)", "", *_metrics_table(split.metrics)]
        if split.split in ("leave_one_city", "leave_one_season"):
            targets = [m.target for m in split.metrics]
            lines += ["", "| held-out group | " + " | ".join(targets) + " |",
                      "|---|" + "---|" * len(targets)]
            for group, values in sorted(split.group_mae.items()):
                lines.append(f"| {group} | " + " | ".join(f"{values[t]:.4f}" for t in targets) + " |")

    lines += ["", "## Cost", "",
              f"- Surrogate: {report.prediction_microseconds_per_row:.1f} µs per material (all targets)"]
    if report.physics_seconds_per_simulation:
        speedup = report.physics_seconds_per_simulation * 1e6 / max(report.prediction_microseconds_per_row, 1e-9)
        lines += [f"- Physics: {report.physics_seconds_per_simulation:.4f} s per simulation",
                  f"- Speed-up: ~{speedup:,.0f}x"]
    lines += [f"- Training time: {report.training_seconds:.1f} s; scikit-learn {report.sklearn_version}"]
    return "\n".join(lines) + "\n"