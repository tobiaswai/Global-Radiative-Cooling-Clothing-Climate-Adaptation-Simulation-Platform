# Optimization summary

22 completed runs; 0 skipped.

## Runs

| name | city | months | seed | mult | objective | bounds | constraints | verdict | evals | s |
|---|---|---|---|---|---|---|---|---|---|---|
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | dubai | [7] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 621 | 89 |
| H Dubai peak_core min, ε [0.05,0.99] | dubai | [7] | 42 | 10 | ? peak_core_temperature_c minimize | ε[0.05,0.99] | — | unconstrained | 23 | 3.08 |
| Exp-A Guangzhou peak_skin ≤ 33 | guangzhou | [8] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | mean_skin_temperature_c <= 33.0 | infeasible | 500 | 68.2 |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | guangzhou | [8] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 519 | 72.2 |
| Exp-D Guangzhou seed=1 | guangzhou | [8] | 1 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 462 | 64.5 |
| Exp-D Guangzhou seed=2 | guangzhou | [8] | 2 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 522 | 70.1 |
| Exp-D Guangzhou seed=3 | guangzhou | [8] | 3 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 520 | 73.4 |
| Exp-D Guangzhou seed=4 | guangzhou | [8] | 4 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 519 | 72.2 |
| Exp-D Guangzhou seed=5 | guangzhou | [8] | 5 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 501 | 71.1 |
| Exp-E Guangzhou mult=10 | guangzhou | [8] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 519 | 72.7 |
| Exp-E Guangzhou mult=20 | guangzhou | [8] | 42 | 20 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 1042 | 142 |
| Exp-E Guangzhou mult=5 | guangzhou | [8] | 42 | 5 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 340 | 45.3 |
| Guangzhou August requirement search | guangzhou | [9] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 481 | 65 |
| Guangzhou August requirement search | guangzhou | [8] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | infeasible | 519 | 67 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | lhasa | [7] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 200 | 27.7 |
| L 拉薩：最低需求（parameter_demand，權重 1:1） | lhasa | [7] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.1,0.98] ε[0.05,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 242 | 31.3 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | lhasa | [7] | 1 | 10 | ? skin_exceedance_fraction minimize | ρ[0.1,0.98] ε[0.55,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 281 | 36.7 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | lhasa | [7] | 2 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 222 | 28.7 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | lhasa | [7] | 3 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 222 | 29.2 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | lhasa | [7] | 4 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 222 | 29.8 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | lhasa | [7] | 5 | 10 | ? skin_exceedance_fraction minimize | ρ[0.3,0.98] ε[0.5,0.99] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 202 | 27.1 |
| L-W 拉薩權重 2:1 / 1:2 | lhasa | [7] | 42 | 10 | ? skin_exceedance_fraction minimize | ρ[0.05,0.99] ε[0.1,0.98] | skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0 | feasible | 242 | 31.7 |

## Metrics (baseline / best / upper bound)

| name | best | objective | violation | upper viol. | exceedance | peak skin °C | peak core °C | cooling °C |
|---|---|---|---|---|---|---|---|---|
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | ρ=0.9800, ε=0.5004 | 0.969569 | 2.15007 | 2.21873 | 0.972095 / 0.969569 / 0.970232 | 38.5221 / 38.188 / 38.2597 | 39.591 / 39.2805 / 39.3485 | 1.70892 |
| H Dubai peak_core min, ε [0.05,0.99] | ε=0.0500 | 39.4968 | 0 | 0 | 0.972095 / 0.971222 / 0.972127 | 38.5221 / 38.4243 / 38.5257 | 39.591 / 39.4968 / 39.5945 | 1.55468 |
| Exp-A Guangzhou peak_skin ≤ 33 | ρ=0.9798, ε=0.9886 | 0.931456 | 3.02209 | 3.02163 | 0.939176 / 0.931456 / 0.931436 | 37.0283 / 36.7789 / 36.7782 | 38.2249 / 37.9975 / 37.9969 | 1.53397 |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | ρ=0.9799, ε=0.9876 | 0.931447 | 0.831447 | 0.831436 | 0.939176 / 0.931447 / 0.931436 | 37.0283 / 36.7787 / 36.7782 | 38.2249 / 37.9972 / 37.9969 | 1.53411 |
| Exp-D Guangzhou seed=1 | ρ=0.9799, ε=0.9842 | 0.93145 | 0.83145 | 0.831436 | 0.939176 / 0.93145 / 0.931436 | 37.0283 / 36.779 / 36.7782 | 38.2249 / 37.9975 / 37.9969 | 1.53389 |
| Exp-D Guangzhou seed=2 | ρ=0.9800, ε=0.9853 | 0.931443 | 0.831443 | 0.831436 | 0.939176 / 0.931443 / 0.931436 | 37.0283 / 36.7787 / 36.7782 | 38.2249 / 37.9973 / 37.9969 | 1.53408 |
| Exp-D Guangzhou seed=3 | ρ=0.9799, ε=0.9899 | 0.931444 | 0.831444 | 0.831436 | 0.939176 / 0.931444 / 0.931436 | 37.0283 / 36.7784 / 36.7782 | 38.2249 / 37.997 / 37.9969 | 1.53428 |
| Exp-D Guangzhou seed=4 | ρ=0.9800, ε=0.9873 | 0.931442 | 0.831442 | 0.831436 | 0.939176 / 0.931442 / 0.931436 | 37.0283 / 36.7785 / 36.7782 | 38.2249 / 37.9971 / 37.9969 | 1.53421 |
| Exp-D Guangzhou seed=5 | ρ=0.9800, ε=0.9894 | 0.93144 | 0.83144 | 0.831436 | 0.939176 / 0.93144 / 0.931436 | 37.0283 / 36.7784 / 36.7782 | 38.2249 / 37.997 / 37.9969 | 1.53431 |
| Exp-E Guangzhou mult=10 | ρ=0.9799, ε=0.9876 | 0.931447 | 0.831447 | 0.831436 | 0.939176 / 0.931447 / 0.931436 | 37.0283 / 36.7787 / 36.7782 | 38.2249 / 37.9972 / 37.9969 | 1.53411 |
| Exp-E Guangzhou mult=20 | ρ=0.9800, ε=0.9885 | 0.93144 | 0.83144 | 0.831436 | 0.939176 / 0.93144 / 0.931436 | 37.0283 / 36.7784 / 36.7782 | 38.2249 / 37.997 / 37.9969 | 1.5343 |
| Exp-E Guangzhou mult=5 | ρ=0.9800, ε=0.9524 | 0.931483 | 0.831483 | 0.831436 | 0.939176 / 0.931483 / 0.931436 | 37.0283 / 36.7819 / 36.7782 | 38.2249 / 37.9998 / 37.9969 | 1.53179 |
| Guangzhou August requirement search | ρ=0.9800, ε=0.9866 | 0.803111 | 0.703111 | 0.702697 | 0.860251 / 0.803111 / 0.802697 | 36.9582 / 36.6638 / 36.6635 | 38.1699 / 37.9028 / 37.9025 | 1.54986 |
| Guangzhou August requirement search | ρ=0.9799, ε=0.9876 | 0.931447 | 0.831447 | 0.831436 | 0.939176 / 0.931447 / 0.931436 | 37.0283 / 36.7787 / 36.7782 | 38.2249 / 37.9972 / 37.9969 | 1.53411 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | ρ=0.8270, ε=0.7751 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.5537 / 33.7608 | 37.0433 / 37.0906 / 37.0361 | 1.49506 |
| L 拉薩：最低需求（parameter_demand，權重 1:1） | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7608 | 37.0433 / 37.0433 / 37.0361 | 1.96577 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7608 | 37.0433 / 37.0433 / 37.0361 | 1.96577 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7608 | 37.0433 / 37.0433 / 37.0361 | 1.96577 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7608 | 37.0433 / 37.0433 / 37.0361 | 1.96577 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7608 | 37.0433 / 37.0433 / 37.0361 | 1.96577 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7608 | 37.0433 / 37.0433 / 37.0361 | 1.96577 |
| L-W 拉薩權重 2:1 / 1:2 | ρ=0.9000, ε=0.9500 | 0 | 0 | 0 | 0 / 0 / 0 | 34.1375 / 34.1375 / 33.7243 | 37.0433 / 37.0433 / 37.0362 | 1.96577 |

## Constraint excess at best (native units, > 0 = violated)

| name | excess |
|---|---|
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | skin_exceedance_fraction <= 0.1: 0.969569 (+0.8696); peak_core_temperature_c <= 38.0: 39.2805 (+1.281) |
| Exp-A Guangzhou peak_skin ≤ 33 | mean_skin_temperature_c <= 33.0: 36.0221 (+3.022) |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | skin_exceedance_fraction <= 0.1: 0.931447 (+0.8314); peak_core_temperature_c <= 38.0: 37.9972 (-0.0028) |
| Exp-D Guangzhou seed=1 | skin_exceedance_fraction <= 0.1: 0.93145 (+0.8315); peak_core_temperature_c <= 38.0: 37.9975 (-0.0025) |
| Exp-D Guangzhou seed=2 | skin_exceedance_fraction <= 0.1: 0.931443 (+0.8314); peak_core_temperature_c <= 38.0: 37.9973 (-0.0027) |
| Exp-D Guangzhou seed=3 | skin_exceedance_fraction <= 0.1: 0.931444 (+0.8314); peak_core_temperature_c <= 38.0: 37.997 (-0.003) |
| Exp-D Guangzhou seed=4 | skin_exceedance_fraction <= 0.1: 0.931442 (+0.8314); peak_core_temperature_c <= 38.0: 37.9971 (-0.0029) |
| Exp-D Guangzhou seed=5 | skin_exceedance_fraction <= 0.1: 0.93144 (+0.8314); peak_core_temperature_c <= 38.0: 37.997 (-0.003) |
| Exp-E Guangzhou mult=10 | skin_exceedance_fraction <= 0.1: 0.931447 (+0.8314); peak_core_temperature_c <= 38.0: 37.9972 (-0.0028) |
| Exp-E Guangzhou mult=20 | skin_exceedance_fraction <= 0.1: 0.93144 (+0.8314); peak_core_temperature_c <= 38.0: 37.997 (-0.003) |
| Exp-E Guangzhou mult=5 | skin_exceedance_fraction <= 0.1: 0.931483 (+0.8315); peak_core_temperature_c <= 38.0: 37.9998 (-0.0002) |
| Guangzhou August requirement search | skin_exceedance_fraction <= 0.1: 0.803111 (+0.7031); peak_core_temperature_c <= 38.0: 37.9028 (-0.0972) |
| Guangzhou August requirement search | skin_exceedance_fraction <= 0.1: 0.931447 (+0.8314); peak_core_temperature_c <= 38.0: 37.9972 (-0.0028) |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0906 (-0.9094) |
| L 拉薩：最低需求（parameter_demand，權重 1:1） | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |
| L-W 拉薩權重 2:1 / 1:2 | skin_exceedance_fraction <= 0.1: 0 (-0.1); peak_core_temperature_c <= 38.0: 37.0433 (-0.9567) |

## Requirement map

| name | map | metric range | plateau | feasible cells | min x @ max y | min y @ max x | grid step | monotone x / y |
|---|---|---|---|---|---|---|---|---|
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | ρ × ε | 0.969568–0.980992 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / mixed |
| Exp-A Guangzhou peak_skin ≤ 33 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-D Guangzhou seed=1 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-D Guangzhou seed=2 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-D Guangzhou seed=3 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-D Guangzhou seed=4 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-D Guangzhou seed=5 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-E Guangzhou mult=10 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-E Guangzhou mult=20 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-E Guangzhou mult=5 | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Guangzhou August requirement search | ρ × ε | 0.802697–0.94765 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Guangzhou August requirement search | ρ × ε | 0.931436–0.971299 | 0.00826 | 0 | — | — | 0.068 / 0.049 | ↓ / ↓ |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | ρ × ε | 0–0.791461 | 0.413 | 0.521 | 0.572 | 0.5 (LB) | 0.068 / 0.049 | ↓ / ↓ |
| L 拉薩：最低需求（parameter_demand，權重 1:1） | ρ × ε | 0–0.910188 | 0.281 | 0.355 | 0.628 | 0.05 (LB) | 0.088 / 0.094 | ↓ / ↓ |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | ρ × ε | 0–0.858187 | 0.331 | 0.413 | 0.628 | 0.55 (LB) | 0.088 / 0.044 | ↓ / ↓ |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | ρ × ε | 0–0.791461 | 0.413 | 0.521 | 0.572 | 0.5 (LB) | 0.068 / 0.049 | ↓ / ↓ |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | ρ × ε | 0–0.791461 | 0.413 | 0.521 | 0.572 | 0.5 (LB) | 0.068 / 0.049 | ↓ / ↓ |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | ρ × ε | 0–0.791461 | 0.413 | 0.521 | 0.572 | 0.5 (LB) | 0.068 / 0.049 | ↓ / ↓ |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | ρ × ε | 0–0.791461 | 0.413 | 0.521 | 0.572 | 0.5 (LB) | 0.068 / 0.049 | ↓ / ↓ |
| L-W 拉薩權重 2:1 / 1:2 | ρ × ε | 0–0.913965 | 0.273 | 0.355 | 0.614 | 0.1 (LB) | 0.094 / 0.088 | ↓ / ↓ |

Grid readings are accurate to ± one grid step.
(LB) = reading equals the searched lower bound.

## Seed groups (same request apart from name and seed)

| runs | seeds | n | distinct results | params | objective | evals |
|---|---|---|---|---|---|---|
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38; Exp-D Guangzhou seed=1; Exp-D Guangzhou seed=2; Exp-D Guangzhou seed=3; Exp-D Guangzhou seed=4; Exp-D Guangzhou seed=5; Exp-E Guangzhou mult=10; Guangzhou August requirement search | [42, 1, 2, 3, 4, 5, 42, 42] | 8 | 6 | ε 0.9874 ± 0.0019; ρ 0.9799 ± 0.0000 | 0.9314 ± 0.0000 | 510.1250 ± 20.5387 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38; L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2; L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3; L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4; L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | [42, 2, 3, 4, 5] | 5 | 2 | ε 0.9150 ± 0.0782; ρ 0.8854 ± 0.0327 | 0.0000 ± 0.0000 | 213.6000 ± 11.5239 |

Check that every group contains only the runs you intended; a differently named run here means its configuration was identical.

## Identical requests (same seed too)

- Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 = Exp-E Guangzhou mult=10 = Guangzhou August requirement search

## Warnings

**Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its lower bound (0.5); the optimum may lie outside the searched range
- ⚠ best beats the optical upper-bound corner: performance is non-monotone in at least one parameter
- ⚠ violation is an unweighted sum across constraints with different units: skin_exceedance_fraction <= 0.1 (+0.8696); peak_core_temperature_c <= 38.0 (+1.281)
- ⚠ map metric is non-monotone along ε; 'minimum requirement' readings assume monotonicity

**H Dubai peak_core min, ε [0.05,0.99]**
- ⚠ best ε sits at its lower bound (0.05); the optimum may lie outside the searched range
- ⚠ best beats the optical upper-bound corner: performance is non-monotone in at least one parameter
- ⚠ best corner is ε=0.0500, not the upper bound

**Exp-A Guangzhou peak_skin ≤ 33**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-D Guangzhou seed=1**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range

**Exp-D Guangzhou seed=2**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-D Guangzhou seed=3**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-D Guangzhou seed=4**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-D Guangzhou seed=5**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-E Guangzhou mult=10**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-E Guangzhou mult=20**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-E Guangzhou mult=5**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range

**Guangzhou August requirement search**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Guangzhou August requirement search**
- ⚠ best ρ sits at its upper bound (0.98); the optimum may lie outside the searched range
- ⚠ best ε sits at its upper bound (0.99); the optimum may lie outside the searched range

**Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38**
- ⚠ ε requirement reads at its lower bound 0.5: the true requirement lies below the searched range
- ⚠ 41% of map cells share the minimum; the reported optimum is arbitrary

**L 拉薩：最低需求（parameter_demand，權重 1:1）**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.05: the true requirement lies below the searched range
- ⚠ 28% of map cells share the minimum; the reported optimum is arbitrary

**L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.55: the true requirement lies below the searched range
- ⚠ 33% of map cells share the minimum; the reported optimum is arbitrary

**L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.5: the true requirement lies below the searched range
- ⚠ 41% of map cells share the minimum; the reported optimum is arbitrary

**L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.5: the true requirement lies below the searched range
- ⚠ 41% of map cells share the minimum; the reported optimum is arbitrary

**L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.5: the true requirement lies below the searched range
- ⚠ 41% of map cells share the minimum; the reported optimum is arbitrary

**L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.5: the true requirement lies below the searched range
- ⚠ 41% of map cells share the minimum; the reported optimum is arbitrary

**L-W 拉薩權重 2:1 / 1:2**
- ⚠ best equals the baseline fabric; on a tie the first evaluated point wins (check tie-breaking in best_evaluated)
- ⚠ ε requirement reads at its lower bound 0.1: the true requirement lies below the searched range
- ⚠ 27% of map cells share the minimum; the reported optimum is arbitrary

