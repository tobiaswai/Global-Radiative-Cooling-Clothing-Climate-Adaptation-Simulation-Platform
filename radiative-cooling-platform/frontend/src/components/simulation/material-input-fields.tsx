"use client";

import {
  NumberField,
  OptionalNumberField,
} from "@/components/forms/number-field";
import type { MaterialInput } from "@/types/simulation";

type MaterialInputFieldsProps = {
  material: MaterialInput;
  showName?: boolean;
  disabled?: boolean;
  onChange: (material: MaterialInput) => void;
};

export function MaterialInputFields({
  material,
  showName = false,
  disabled = false,
  onChange,
}: MaterialInputFieldsProps) {
  function update<K extends keyof MaterialInput>(
    key: K,
    value: MaterialInput[K],
  ) {
    onChange({ ...material, [key]: value });
  }

  return (
    <div className="grid gap-5 sm:grid-cols-2">
      {showName && (
        <label className="block sm:col-span-2">
          <span className="mb-2 block text-sm text-slate-300">
            Material Name
          </span>

          <input
            type="text"
            value={material.name}
            maxLength={100}
            disabled={disabled}
            onChange={(event) => update("name", event.target.value)}
            className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
          />
        </label>
      )}

      <NumberField
        label="Clothing Insulation"
        suffix="clo"
        value={material.clothing_insulation_clo}
        min={0}
        max={5}
        step={0.05}
        disabled={disabled}
        onChange={(value) => update("clothing_insulation_clo", value)}
      />

      <OptionalNumberField
        label="Clothing Area Factor (f_cl)"
        value={material.clothing_area_factor}
        placeholder="Derived from clo"
        min={1}
        max={2}
        step={0.01}
        disabled={disabled}
        hint="Leave empty to let the backend derive f_cl from clo (Stage 3)."
        onChange={(value) => update("clothing_area_factor", value)}
      />

      <NumberField
        label="Solar Reflectance"
        value={material.solar_reflectance}
        min={0}
        max={1}
        step={0.01}
        disabled={disabled}
        onChange={(value) => update("solar_reflectance", value)}
      />

      <NumberField
        label="Solar Transmittance"
        value={material.solar_transmittance}
        min={0}
        max={1}
        step={0.01}
        disabled={disabled}
        onChange={(value) => update("solar_transmittance", value)}
      />

      <NumberField
        label="Infrared Emissivity"
        value={material.infrared_emissivity}
        min={0}
        max={1}
        step={0.01}
        disabled={disabled}
        onChange={(value) => update("infrared_emissivity", value)}
      />
    </div>
  );
}