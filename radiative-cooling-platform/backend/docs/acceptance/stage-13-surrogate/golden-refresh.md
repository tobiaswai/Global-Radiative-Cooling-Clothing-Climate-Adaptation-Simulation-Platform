# Stage 13 golden refresh (Dubai 2023-07-15 12:00, 2 h, legacy_stage1)

Causes: MODEL_PARAMETER_SET_VERSION 5.0.0 -> 6.0.0 (label fix, no constant changed in
Stage 13); MODEL_VERSION 0.10.0 -> 0.11.0 (ADR 0012). The fixture person does not walk.

| metric | before | after | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 2.1232 | <fill> | must be 0 |
| final_core_temperature_improvement_c | 1.9117 | <fill> | must be 0 |
| average_skin_temperature_improvement_c | 1.2876 | <fill> | must be 0 |

parameter_fingerprint: 80d30c26... -> <fill>