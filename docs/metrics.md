# Metric definitions

Each metric lists: formula, inputs, the time window it is computed over,
and what it does **not** mean.

## effective_cooling_hours
- **Display name**: Estimated beneficial exposure hours under the configured daily exposure scenario
- **Formula**: `beneficial_weighted_days × duration_minutes / 60`
- **beneficial** := `exposure_eligible AND average_skin_improvement_c ≥ minimum_skin_improvement_c`
- **exposure_eligible** := thresholds on the exposure-window mean air temperature / GHI (`exposure_match_mode`: all | any)
- **Window**: `[local_start_hour, local_start_hour + duration_minutes]`. Padding hours are never included.
- **Weights**: each sampled day carries `weight_days` (calendar days it represents; see `annual_sampling`).
- **Not**: hours during which cooling physically occurred; not a physiological exposure limit.

## mean_air_temperature_c / mean_solar_radiation_w_m2 (per sample)
- Trapezoidal time-weighted mean of the piecewise-linear hourly ERA5 series over the exposure window only.
- Maximum values are the maxima over window knots (endpoints + hourly points inside).

## average_skin_improvement_c / average_core_improvement_c (per sample)
- Trapezoidal time-weighted mean of `control − rc` over the simulation output grid.

## data_quality.skipped_*
- Sample days rejected by weather validation (`WEATHER_INSUFFICIENT_COVERAGE`, `WEATHER_GAP_IN_WINDOW`, …).
- Skipped days are **excluded** from `total_weighted_days`; they neither count as evaluated nor as beneficial.