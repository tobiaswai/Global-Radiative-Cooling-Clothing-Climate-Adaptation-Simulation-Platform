# ADR 0011: physics-trained surrogate models

## Context
Brief section 4.5: global multi-city x multi-material evaluation is too slow for
interactive sweeps (~0.05-0.1 s per 2 h simulation). The physics engine stays the
source of truth; a surrogate only accelerates exploration.

## Decision
Dataset
- Unit: (city, sample day, exposure window, material). Weather days come from the
  same weighted sampling as optimization (3 days/month default); materials are a
  scrambled Sobol sample (power of two) over declared decision-variable ranges,
  shared across all weather samples (crossed design). Impossible garments are dropped.
- Fixed per dataset ("context", hashed as context_sha256): start hour, duration,
  output interval, thresholds, person, control garment, fixed fields of the base
  garment, environment assumptions, variable ranges. A model is only valid in its context.
- Features: exposure-window means/maxima of the *derived* environment (air T, RH,
  vapour pressure, body-height wind, GHI, DNI, DHI, modelled T_sky and T_surround)
  plus the material variables. No city id or latitude: the model must generalise
  through weather, which leave-one-city validation tests.
- Labels: the nine EvaluationMetrics of the candidate vs the control (compute_metrics).
- Generation is chunked by (city, month), written as Parquet with SHA-256, and
  stamped with MODEL_VERSION and parameter_fingerprint.

Model
- scikit-learn HistGradientBoostingRegressor per target: squared-error point model
  plus quantile models (default 0.1 / 0.9), widened by split-conformal calibration
  (CQR) on ~25 % held-out training cities; lower <= point <= upper enforced.
- Validation: grouped k-fold by (city, day), leave-one-city, leave-one-season
  (hemisphere-adjusted). Acceptance requires, for leave-one-city and leave-one-season,
  MAE <= per-target threshold and interval coverage >= 0.75 (nominal 0.80).
- Artifacts: joblib bundle with checksum, feature ranges, context and provenance.

Inference
- Surrogate output is used ("source = surrogate") only if the model is accepted,
  not stale (same MODEL_VERSION and parameter_fingerprint) and every feature lies
  inside the training range. Otherwise the request falls back to physics
  (bounded per request) or reports "none".

## Consequences
- Any physics change invalidates datasets and models automatically (stale flag).
- Reported conclusions and final material recommendations use physics results.

## Limitations
- Domain check is a per-feature box, not a density estimate; joint extrapolation
  inside the box is possible and is quantified only by the validation splits.
- Conformal calibration assumes held-out cities are exchangeable with new cities;
  coverage for cities far outside the training climate is not guaranteed.
- Chunk tasks rely on Celery redelivery (acks_late), not leases; a chunk running longer
  than the broker visibility timeout can be computed twice (results are identical).
- joblib artifacts are pickles: only load artifacts produced by this server.