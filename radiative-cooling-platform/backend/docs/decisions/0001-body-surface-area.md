# ADR 0001: body_surface_area_m2 is currently informational — RESOLVED (Stage 3)

Finding (Stage 2): heat capacities were fixed per m^2 (245 + 35 kJ/(m^2 K)), so
`PersonInput.body_surface_area_m2` had no effect and the lumped value was
about 2x the Gagge two-node value for 70 kg / 1.8 m^2.

Resolution (Stage 3, PR-1): `PersonInput.body_mass_kg` (default 70) added.
C_core = m c_p (1 - alpha) / A_D, C_skin = m c_p alpha / A_D with
c_p = 3490 J/(kg K) and alpha = 0.1 (Gagge 1986). Default person gives
135.7 kJ/(m^2 K), matching the reference model. alpha is kept constant
(Gagge varies it with skin blood flow) so node capacities are state-independent
and the energy diagnostics stay exact. `test_body_surface_area_participates`
xfail removed; both fields are now covered by test_parameter_participation.