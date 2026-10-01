# Stage 6 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional):
1. Summary average is now the time-weighted trapezoidal mean shared by all
   three pipelines (PR-1a). Trajectories are unchanged.
2. `EnvironmentAssumptions.radiation_time_convention` added (default keeps the
   legacy linear behaviour) -> parameter fingerprint changes although no
   constant changed. MODEL_PARAMETER_SET_VERSION stays 4.0.0.
3. MODEL_VERSION 0.6.0 -> 0.7.0.

| metric | before (0.6.0) | after (0.7.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 2.1232 | 2.1232 | 0 |
| final_core_temperature_improvement_c | 1.9117 | 1.9117 | 0 |
| average_skin_temperature_improvement_c | 1.2703 | 1.2876 | +0.0173 (definition) |

Every control/radiative_cooling point: unchanged to 1e-6 (audit grid does not
alter solve_ivp stepping). parameter_fingerprint: 19ebfc73... -> <fill from run>