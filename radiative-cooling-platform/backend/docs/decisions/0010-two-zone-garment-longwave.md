# ADR 0010: sky-facing and ground-facing garment zones

## Context
Under the physical environment the ground can be 10-20 K warmer than the air
(K1), and optimisers choose low emissivity (K2-K4) even though high emissivity
is what radiates to the sky. A uniform garment must compromise (K3: eps_W 0.5).

## Decision
- Optional MaterialInput.infrared_emissivity_ground_facing (gray). None -> the
  Stage 11 code path, bit-identical.
- Zone areas F and 1 - F (F = sky view factor); sky views F + s(1 - F) and
  F(1 - s), s = zone_view_separation in [0, 1], default 0.5 (assumed).
  The area-weighted sky view equals F for every s.
- Sky-facing zone: existing gray or selective optics. Ground-facing zone: gray.
- One clothing surface temperature shared by both zones; skin emission
  transmitted through the textile sees the body-average field.
- Optimisation variable infrared_emissivity_ground_facing (demand: decreasing).

## Consequences
- MODEL_VERSION 0.10.0; parameter registry unchanged (6.0.0).
- s = 0 makes the two zones indistinguishable (area-weighted emissivity only).

## Limitations
- Shared surface temperature: in reality the ground-facing zone can be warmer
  than the sky-facing one; the benefit of a low eps_g is therefore uncertain
  in both directions and should be read as a first-order estimate.
- Zone areas tied to F is an idealisation of an open site and a standing person.
- s is not measured; results are reported as a sweep (experiment L2).
- The ground-facing zone has the same solar optics as the rest of the garment.