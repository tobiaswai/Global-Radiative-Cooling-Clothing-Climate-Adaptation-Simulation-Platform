"""Activity presets: metabolic rate and walking speed (Stage 13, ADR 0012)."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

ActivityName = Literal["standing", "slow_walk", "moderate_walk", "brisk_walk"]

ISO_8996_WALKING = (
    "ISO 8996:2004, Annex B, walking on level even path (110/165/200 W/m^2 at "
    "2/4/5 km/h); 1 met = 58.15 W/m^2. Verify against the standard before publication."
)


class ActivityPreset(BaseModel):
    name: ActivityName
    label: str
    met: float
    walking_speed_m_s: float
    reference: str


ACTIVITY_PRESETS: dict[str, ActivityPreset] = {
    preset.name: preset
    for preset in (
        ActivityPreset(name="standing", label="Standing, light activity", met=1.4,
                       walking_speed_m_s=0.0, reference="ISO 8996:2004, Annex B (standing, light activity)"),
        ActivityPreset(name="slow_walk", label="Slow walk, 2 km/h", met=1.9,
                       walking_speed_m_s=0.56, reference=ISO_8996_WALKING),
        ActivityPreset(name="moderate_walk", label="Moderate walk, 4 km/h", met=2.8,
                       walking_speed_m_s=1.11, reference=ISO_8996_WALKING),
        ActivityPreset(name="brisk_walk", label="Brisk walk, 5 km/h", met=3.4,
                       walking_speed_m_s=1.39, reference=ISO_8996_WALKING),
    )
}