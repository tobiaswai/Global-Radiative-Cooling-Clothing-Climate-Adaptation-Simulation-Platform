# ADR 0009: physical radiant environment becomes the default

## Context
Stage 11 (ADR 0008) added opt-in physical sky and ground temperatures and gated a
default switch on experiment K. K1 passed in all three cities; K4 showed the
material conclusions do not depend on the unmeasured surface-soil conductance;
K5 showed annual skin improvement changes by ~0.03 C in Dubai and Guangzhou.
The legacy rule counts the sun twice (ADR 0008) and has no remaining advantage.

## Decision
- EnvironmentAssumptions() defaults to ground_energy_balance + brutsaert_cloud.
- Named presets: open_ground_physical (= default) and legacy_stage1.
- Stored request_json without environment_assumptions (pre-Stage 2) is loaded
  with legacy_stage1 through services.stored_requests; payloads with explicit
  assumptions (Stage 2+) keep them.
- Golden fixture pinned to legacy_stage1; its temperatures must not change.

## Consequences
- Default requests fetch cloud_cover and soil_temperature_0_to_7cm: new cache
  entries and payload hashes for default runs; samples with missing values are
  skipped as WEATHER_MISSING_VARIABLE.
- Tests on synthetic weather must pin legacy_stage1 or provide the variables.
- API clients that omit environment_assumptions get different results.