# Stage 13 acceptance: P0 fixes, walking, physics-trained surrogate

Record raw commands and observed values; an entry without a value is not accepted.

| # | Experiment | Expected | Observed |
|---|---|---|---|
| N0a | Re-run Stage 9 drill 9 (global_large batch, kill -9 worker) | re-queued task on `global_large` | |
| N0b | Golden refresh (golden-refresh.md) | all temperatures unchanged; version labels changed | |
| N0c | Export ZIP of a default batch | README shows ground_energy_balance / brutsaert_cloud | |
| N1 | D3 smoke: create, generate, finalize, train | dataset completed; model completed; report renders | |
| N2 | D1 generation (16 cities x 12 months x 3 days x 512 materials) | <1 % failed chunks; record rows, simulations, wall time, workers | |
| N3 | Train M1 on D1; save /report.md as validation-report.md | leave-one-city and leave-one-season meet thresholds -> accepted | |
| N4 | evaluate_surrogate.py M1 on D2 (2022) | MAE within 1.5x thresholds; coverage >= 0.70 | |
| N5 | Cost: report µs/material vs physics s/simulation; /predict latency for 42 materials | sweep request < 1 s after weather cache warm | |
| N6 | Fallback drills: (a) material outside bounds -> source physics; (b) model with passed=false -> physics; (c) bump MODEL_VERSION locally -> stale=true, training refuses dataset (409) | as stated | |
| N7 | Sweep UI vs physics: 10 random designs, "Verify with physics" | physics value inside interval for >= 7 of 10 | |

If N3 fails: increase material_count to 1024 or sample_days_per_month to 5, or inspect
per-city MAE in the report (a single extreme city, e.g. Lhasa, may need its own dataset).
Do not lower thresholds without recording the reason in ADR 0011.