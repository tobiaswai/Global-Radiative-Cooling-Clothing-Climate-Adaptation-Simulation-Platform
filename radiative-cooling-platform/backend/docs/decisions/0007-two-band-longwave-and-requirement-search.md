# ADR 0007: two-band longwave exchange; feasibility-first requirement search

## Context
Stage 9 acceptance runs (docs/acceptance/stage-optimization):
1. Dubai July: the optimum sat at eps = 0.5 (lower bound); with eps in
   [0.05, 0.99], eps = 0.05 lowered peak core by ~0.1 K. A single broadband
   eps cannot represent a selective emitter, and the default
   T_mrt = T_air + min(15, 0.012 GHI) makes the non-sky hemisphere hotter
   than the clothing surface.
2. Guangzhou August: skin_exceedance_fraction stayed 0.93-0.97 over the
   whole design space; the time-fraction metric has no gradient there.
3. Lhasa: 41 % of map cells tied at 0; the reported "best" was the baseline.
4. A 39.5 C objective with tol = 1e-3 converged after one generation.

## Decision
Physics
- MaterialInput.infrared_emissivity is the broadband value Planck-weighted at
  emissivity_reference_temperature (305 K). Optional infrared_emissivity_window
  is eps_W in 8-13 um; eps_N follows from
  F_W eps_W + (1 - F_W) eps_N = eps.
- Selective path: emission and absorption are split into window and
  out-of-window bands. Outside the window the sky is opaque at T_air; inside
  it eps_sky,W is chosen so the broadband sky radiance equals sigma T_sky^4 of
  the configured sky method. Surroundings (1 - F_sky) are blackbodies at T_mrt.
- Gray materials keep the Stage 6 code path: trajectories unchanged.
- Skin emission through tau_IR stays gray (first order).
Search
- New metrics skin/core_excess_degree_hours (exact integral of
  max(0, T - threshold)).
- Constraints normalised by per-metric scales; feasible points always rank
  above infeasible ones; objective normalised against the baseline; DE uses
  tol = 0, atol = convergence_tolerance.
- material_demand objective and tie-breaker; per-variable demand_direction.
- Requirement readings are least-demanding feasible values (no monotonicity
  assumption); backend emits warnings and a sensitivity table.

## Consequences
- MODEL_PARAMETER_SET_VERSION 4.0.0 -> 5.0.0 (four constants);
  MODEL_VERSION 0.7.0 -> 0.8.0. Fingerprint changes; gray trajectories do not.
- Stage 9 checkpoints become non-resumable (model_version differs).
- Results that favour low eps or low eps_N under air_plus_solar_linear must be
  repeated with equal_to_air before being reported (experiment G).

## Not done
Solar spectral weighting (needs ASTM G173), angle-dependent f_p,
sky emissivity from cloud cover, multi-objective search.