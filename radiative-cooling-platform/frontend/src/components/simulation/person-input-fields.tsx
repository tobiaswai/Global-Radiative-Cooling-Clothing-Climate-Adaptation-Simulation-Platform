"use client";

import { NumberField } from "@/components/forms/number-field";
import { SelectField } from "@/components/forms/select-field";
import type { PersonInput } from "@/types/simulation";

type PersonInputFieldsProps = {
  person: PersonInput;
  disabled?: boolean;
  onChange: (person: PersonInput) => void;
};

export function PersonInputFields({
  person,
  disabled = false,
  onChange,
}: PersonInputFieldsProps) {
  function update<K extends keyof PersonInput>(key: K, value: PersonInput[K]) {
    onChange({ ...person, [key]: value });
  }

  return (
    <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-6">
      <NumberField
        label="Activity Level"
        suffix="MET"
        value={person.met}
        min={0.7}
        max={10}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("met", value)}
      />

      <NumberField
        label="Body Mass"
        suffix="kg"
        value={person.body_mass_kg}
        min={30}
        max={200}
        step={0.5}
        disabled={disabled}
        hint="Sets the core and skin heat capacities (Stage 3)."
        onChange={(value) => update("body_mass_kg", value)}
      />

      <NumberField
        label="Body Surface Area"
        suffix="m²"
        value={person.body_surface_area_m2}
        min={1}
        max={3}
        step={0.01}
        disabled={disabled}
        onChange={(value) => update("body_surface_area_m2", value)}
      />

      <NumberField
        label="Initial Core Temperature"
        suffix="°C"
        value={person.initial_core_temperature_c}
        min={34}
        max={40}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("initial_core_temperature_c", value)}
      />

      <NumberField
        label="Initial Skin Temperature"
        suffix="°C"
        value={person.initial_skin_temperature_c}
        min={20}
        max={40}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("initial_skin_temperature_c", value)}
      />

      <SelectField
        label="Posture"
        value={person.position}
        disabled={disabled}
        options={[
          { value: "standing", label: "Standing (A_r/A_D = 0.73)" },
          { value: "sitting", label: "Sitting (A_r/A_D = 0.70)" },
        ]}
        hint="Effective radiation area for longwave and diffuse solar (Stage 5)."
        onChange={(value) => update("position", value)}
      />
    </div>
  );
}