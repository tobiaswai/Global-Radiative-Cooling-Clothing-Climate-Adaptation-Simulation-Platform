"""Training and validation of surrogate models (Stage 13, ADR 0011)."""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GroupKFold, GroupShuffleSplit, LeaveOneGroupOut

from app.schemas.surrogate import (
    ACCEPTANCE_SPLITS,
    DEFAULT_MAE_THRESHOLDS,
    AcceptanceCheck,
    SplitReport,
    SurrogateDatasetCreate,
    SurrogateTrainingCreate,
    TargetMetrics,
    ValidationReport,
)
from app.services.surrogate.context import context_sha256, current_fingerprint
from app.services.surrogate.features import WEATHER_FEATURES
from app.services.two_node import MODEL_VERSION

BUNDLE_FORMAT = 1
GROUPED_FOLDS = 5
TIMING_ROWS = 10_000

SEASON_BY_MONTH = {
    12: "DJF", 1: "DJF", 2: "DJF", 3: "MAM", 4: "MAM", 5: "MAM",
    6: "JJA", 7: "JJA", 8: "JJA", 9: "SON", 10: "SON", 11: "SON",
}

CALIBRATION_FRACTION = 0.25
MIN_CALIBRATION_GROUPS = 3

def season_label(month: int, latitude: float) -> str:
    """Northern-hemisphere-equivalent meteorological season."""
    equivalent = month if latitude >= 0 else (month + 5) % 12 + 1
    return SEASON_BY_MONTH[equivalent]


def feature_columns_for(spec: SurrogateDatasetCreate) -> list[str]:
    return [*WEATHER_FEATURES, *spec.variable_names]


@dataclass
class TargetEstimator:
    point: HistGradientBoostingRegressor
    lower: HistGradientBoostingRegressor
    upper: HistGradientBoostingRegressor
    margin: float = 0.0  # conformal widening (CQR), native units

    def predict(self, features: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        point = self.point.predict(features)
        lower = np.minimum(self.lower.predict(features) - self.margin, point)
        upper = np.maximum(self.upper.predict(features) + self.margin, point)
        return point, lower, upper


def _regressor(training: SurrogateTrainingCreate, quantile: float | None = None) -> HistGradientBoostingRegressor:
    params: dict = dict(
        max_iter=training.max_iter, learning_rate=training.learning_rate,
        max_leaf_nodes=training.max_leaf_nodes, min_samples_leaf=training.min_samples_leaf,
        l2_regularization=training.l2_regularization, early_stopping=False,
        random_state=training.random_seed,
    )
    if quantile is not None:
        params.update(loss="quantile", quantile=quantile)
    return HistGradientBoostingRegressor(**params)


def conformal_margin(y: np.ndarray, lower: np.ndarray, upper: np.ndarray, alpha: float) -> float:
    """Split-conformal quantile regression (Romano et al., 2019)."""
    scores = np.maximum(lower - y, y - upper)
    n = len(scores)
    level = min(1.0, np.ceil((n + 1) * (1.0 - alpha)) / n)
    return float(np.quantile(scores, level, method="higher"))


def calibration_groups(frame: pd.DataFrame) -> np.ndarray:
    """Calibrate against unseen cities when possible, otherwise unseen days."""
    cities = frame["city_id"].astype(str).to_numpy()
    if len(np.unique(cities)) >= MIN_CALIBRATION_GROUPS:
        return cities
    return _groups(frame, "grouped_kfold")


def fit_target(features: np.ndarray, target: np.ndarray, training: SurrogateTrainingCreate,
               groups: np.ndarray | None = None) -> TargetEstimator:
    margin = 0.0
    if groups is not None and len(np.unique(groups)) >= MIN_CALIBRATION_GROUPS:
        splitter = GroupShuffleSplit(n_splits=1, test_size=CALIBRATION_FRACTION,
                                     random_state=training.random_seed)
        fit_index, calibration_index = next(splitter.split(features, groups=groups))
        lower = _regressor(training, training.lower_quantile).fit(features[fit_index], target[fit_index])
        upper = _regressor(training, training.upper_quantile).fit(features[fit_index], target[fit_index])
        margin = conformal_margin(
            target[calibration_index],
            lower.predict(features[calibration_index]),
            upper.predict(features[calibration_index]),
            alpha=1.0 - training.nominal_coverage,
        )
    return TargetEstimator(
        point=_regressor(training).fit(features, target),
        lower=_regressor(training, training.lower_quantile).fit(features, target),
        upper=_regressor(training, training.upper_quantile).fit(features, target),
        margin=margin,
    )


def _groups(frame: pd.DataFrame, split: str) -> np.ndarray:
    if split == "grouped_kfold":
        return (frame["city_id"].astype(str) + "|" + frame["sample_date"].astype(str)).to_numpy()
    if split == "leave_one_city":
        return frame["city_id"].astype(str).to_numpy()
    if split == "leave_one_season":
        return np.asarray([season_label(int(m), float(lat))
                           for m, lat in zip(frame["month"], frame["latitude"])])
    raise ValueError(f"unknown split {split}")


def _folds(groups: np.ndarray, split: str) -> list[tuple[np.ndarray, np.ndarray]]:
    distinct = len(np.unique(groups))
    if distinct < 2:
        return []
    if split == "grouped_kfold":
        splitter = GroupKFold(n_splits=min(GROUPED_FOLDS, distinct))
    else:
        splitter = LeaveOneGroupOut()
    return list(splitter.split(groups, groups=groups))


def target_metrics(target: str, y: np.ndarray, point: np.ndarray,
                   lower: np.ndarray, upper: np.ndarray) -> TargetMetrics:
    return TargetMetrics(
        target=target,
        count=int(len(y)),
        mae=round(float(mean_absolute_error(y, point)), 6),
        rmse=round(float(np.sqrt(mean_squared_error(y, point))), 6),
        r2=round(float(r2_score(y, point)), 6) if np.ptp(y) > 0 else None,
        interval_coverage=round(float(np.mean((y >= lower) & (y <= upper))), 6),
        mean_interval_width=round(float(np.mean(upper - lower)), 6),
    )


def cross_validate(frame: pd.DataFrame, features: np.ndarray, targets: list[str],
                   training: SurrogateTrainingCreate, split: str) -> SplitReport | None:
    groups = _groups(frame, split)
    folds = _folds(groups, split)
    if not folds:
        return None

    observed = {t: frame[t].to_numpy(dtype=float) for t in targets}
    out_of_fold = {t: np.full((3, len(frame)), np.nan) for t in targets}
    for train_index, test_index in folds:
        fold_groups = calibration_groups(frame.iloc[train_index])
        for t in targets:
            estimator = fit_target(features[train_index], observed[t][train_index], training, fold_groups)
            out_of_fold[t][:, test_index] = np.vstack(estimator.predict(features[test_index]))

    group_mae: dict[str, dict[str, float]] = {}
    for group in np.unique(groups):
        mask = groups == group
        group_mae[str(group)] = {
            t: round(float(np.mean(np.abs(observed[t][mask] - out_of_fold[t][0][mask]))), 6)
            for t in targets
        }

    return SplitReport(
        split=split,
        fold_count=len(folds),
        metrics=[target_metrics(t, observed[t], *out_of_fold[t]) for t in targets],
        group_mae=group_mae,
    )


def acceptance_checks(splits: list[SplitReport], training: SurrogateTrainingCreate) -> list[AcceptanceCheck]:
    checks: list[AcceptanceCheck] = []
    for report in splits:
        if report.split not in ACCEPTANCE_SPLITS:
            continue
        for metric in report.metrics:
            threshold = training.mae_thresholds.get(metric.target, DEFAULT_MAE_THRESHOLDS[metric.target])
            checks.append(AcceptanceCheck(
                split=report.split, target=metric.target, mae=metric.mae, mae_threshold=threshold,
                interval_coverage=metric.interval_coverage,
                minimum_coverage=training.minimum_interval_coverage,
                passed=metric.mae <= threshold
                and metric.interval_coverage >= training.minimum_interval_coverage,
            ))
    return checks


def feature_ranges(frame: pd.DataFrame, spec: SurrogateDatasetCreate) -> dict[str, tuple[float, float]]:
    ranges: dict[str, tuple[float, float]] = {}
    for column in WEATHER_FEATURES:
        values = frame[column].dropna()
        if len(values):
            ranges[column] = (float(values.min()), float(values.max()))
    for variable in spec.variables:
        ranges[variable.name] = (float(variable.lower), float(variable.upper))
    return ranges


@dataclass
class TrainingOutcome:
    report: ValidationReport
    estimators: dict[str, TargetEstimator]
    feature_columns: list[str]
    feature_ranges: dict[str, tuple[float, float]]


def prepare_frame(frame: pd.DataFrame, spec: SurrogateDatasetCreate,
                  training: SurrogateTrainingCreate) -> pd.DataFrame:
    missing = set(feature_columns_for(spec) + list(training.targets)) - set(frame.columns)
    if missing:
        raise ValueError(f"dataset is missing columns: {sorted(missing)}")
    frame = frame.dropna(subset=list(training.targets)).reset_index(drop=True)
    if training.max_rows is not None and len(frame) > training.max_rows:
        frame = frame.sample(n=training.max_rows, random_state=training.random_seed).reset_index(drop=True)
    if frame.empty:
        raise ValueError("dataset has no labelled rows")
    return frame


def train_and_validate(frame: pd.DataFrame, spec: SurrogateDatasetCreate,
                       training: SurrogateTrainingCreate, *,
                       physics_seconds_per_simulation: float | None = None) -> TrainingOutcome:
    started = perf_counter()
    frame = prepare_frame(frame, spec, training)
    columns = feature_columns_for(spec)
    features = frame[columns].to_numpy(dtype=float)
    targets = list(training.targets)
    final_groups = calibration_groups(frame)
    estimators = {t: fit_target(features, frame[t].to_numpy(dtype=float), training, final_groups)
                  for t in targets}
    splits = [
        report for split in training.validation_splits
        if (report := cross_validate(frame, features, targets, training, split)) is not None
    ]
    estimators = {t: fit_target(features, frame[t].to_numpy(dtype=float), training) for t in targets}

    timing = features[:TIMING_ROWS]
    timer = perf_counter()
    for estimator in estimators.values():
        estimator.predict(timing)
    per_row = (perf_counter() - timer) / max(1, len(timing)) * 1e6

    checks = acceptance_checks(splits, training)
    report = ValidationReport(
        row_count=len(frame),
        feature_columns=columns,
        targets=targets,
        training_cities=sorted(frame["city_id"].astype(str).unique().tolist()),
        splits=splits,
        acceptance=checks,
        passed=bool(checks) and all(c.passed for c in checks),
        nominal_interval_coverage=round(training.nominal_coverage, 6),
        training_seconds=round(perf_counter() - started, 3),
        prediction_microseconds_per_row=round(per_row, 3),
        physics_seconds_per_simulation=physics_seconds_per_simulation,
        sklearn_version=sklearn.__version__,
    )
    return TrainingOutcome(report, estimators, columns, feature_ranges(frame, spec))


def evaluate_estimators(estimators: dict[str, TargetEstimator], columns: list[str],
                        frame: pd.DataFrame) -> list[TargetMetrics]:
    """Metrics of a trained bundle on an independent dataset (temporal hold-out)."""
    features = frame[columns].to_numpy(dtype=float)
    results = []
    for target, estimator in estimators.items():
        mask = frame[target].notna().to_numpy()
        point, lower, upper = estimator.predict(features[mask])
        results.append(target_metrics(target, frame[target].to_numpy(dtype=float)[mask], point, lower, upper))
    return results


def build_bundle(outcome: TrainingOutcome, *, spec: SurrogateDatasetCreate,
                 training: SurrogateTrainingCreate, model_id: str, dataset_id: str | None) -> dict:
    return {
        "format": BUNDLE_FORMAT,
        "model_id": model_id,
        "dataset_id": dataset_id,
        "spec": spec.model_dump(mode="json"),
        "training": training.model_dump(mode="json"),
        "targets": list(outcome.estimators),
        "estimators": outcome.estimators,
        "feature_columns": outcome.feature_columns,
        "feature_ranges": outcome.feature_ranges,
        "training_cities": outcome.report.training_cities,
        "context_sha256": context_sha256(spec),
        "model_version": MODEL_VERSION,
        "parameter_fingerprint": current_fingerprint(spec),
        "sklearn_version": sklearn.__version__,
    }