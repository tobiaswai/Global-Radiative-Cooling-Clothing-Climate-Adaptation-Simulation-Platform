import type { PersonInput } from "@/types/simulation";

export type ActivityPresetName = "standing" | "slow_walk" | "moderate_walk" | "brisk_walk";

/** Mirrors ACTIVITY_PRESETS in app/schemas/activity.py (ADR 0012). One preset per line. */
export const ACTIVITY_PRESETS: Record<ActivityPresetName, { label: string; met: number; walking_speed_m_s: number }> = {
  standing: { label: "Standing, light activity", met: 1.4, walking_speed_m_s: 0 },
  slow_walk: { label: "Slow walk, 2 km/h", met: 1.9, walking_speed_m_s: 0.56 },
  moderate_walk: { label: "Moderate walk, 4 km/h", met: 2.8, walking_speed_m_s: 1.11 },
  brisk_walk: { label: "Brisk walk, 5 km/h", met: 3.4, walking_speed_m_s: 1.39 },
};

export function matchActivity(person: PersonInput): ActivityPresetName | "custom" {
  for (const name of Object.keys(ACTIVITY_PRESETS) as ActivityPresetName[]) {
    const preset = ACTIVITY_PRESETS[name];
    if (preset.met === person.met && preset.walking_speed_m_s === (person.walking_speed_m_s ?? 0)) return name;
  }
  return "custom";
}