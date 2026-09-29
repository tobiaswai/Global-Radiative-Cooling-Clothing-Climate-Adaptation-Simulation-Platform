# ADR 0003: explicit clothing surface temperature; solar stays on the skin node

Decision: solve (T_sk - T_cl)/R_cl = f_cl [h_c (T_cl - T_a) + eps sigma (T_cl^4 - T_env^4)]
each evaluation (Newton, monotone). f_cl = material value or 1 + 0.15 clo, and
also enters Re,a = 1/(LR f_cl h_c). The `assumed` linearised h_r is removed.
T_cl is exported (`clothing_surface_temperature_c`) because it governs the net
sky radiation of a radiative-cooling garment.

Kept simplification: absorbed solar is still deposited on the skin via
`absorbed_solar_to_body_fraction` and does not enter the surface balance.
Moving it to the surface would remove a MaterialInput field and a DB column
and requires spectral data; scheduled for Stage 4. Recorded in
`assumptions_applied` of every result.

Effective radiation area (added after the first Stage 3 benchmark run): the
surface balance and both longwave terms are scaled by A_r/A_D = 0.73
(Fanger 1970, standing). Without it the prototype exchanged ~37 % more
longwave radiation than the reference, which appeared as a +0.30 K core bias
after 60 min in the default benchmark scenario (T_mrt = 45 C > T_cl).