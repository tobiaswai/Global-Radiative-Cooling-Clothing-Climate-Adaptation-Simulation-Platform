"use client";

import { NumberField, OptionalNumberField } from "@/components/forms/number-field";
import { SelectField } from "@/components/forms/select-field";
import type { MaterialMode, MaterialVersionInput } from "@/types/material";

const MODE_OPTIONS: { value: MaterialMode; label: string }[] = [
  { value: "ordinary", label: "Ordinary textile" },
  { value: "opaque_emitter", label: "Opaque emitter" },
  { value: "infrared_transparent", label: "Infrared transparent" },
  { value: "hybrid", label: "Hybrid" },
];

type Props = {
  value: MaterialVersionInput;
  disabled?: boolean;
  onChange: <K extends keyof MaterialVersionInput>(
    field: K,
    value: MaterialVersionInput[K],
  ) => void;
};

/** Physical fields of a material version; bounds mirror MaterialVersionCreate. */
export function MaterialVersionFields({ value, disabled = false, onChange }: Props) {
  const solarSumTooHigh = value.solar_reflectance + value.solar_transmittance > 1 + 1e-6;
  const infraredSumTooHigh =
    value.infrared_emissivity + value.infrared_transmittance > 1 + 1e-6;

  return (
    <div className="space-y-4">
      <div className="grid gap-5 md:grid-cols-2">
        <SelectField
          label="Mode"
          value={value.mode}
          options={MODE_OPTIONS}
          disabled={disabled}
          onChange={(mode) => onChange("mode", mode)}
        />
        <NumberField
          label="Clothing Insulation"
          suffix="clo"
          value={value.clothing_insulation_clo}
          min={0} max={5} step={0.05}
          disabled={disabled}
          onChange={(v) => onChange("clothing_insulation_clo", v)}
        />
        <OptionalNumberField
          label="Clothing Area Factor (f_cl)"
          value={value.clothing_area_factor}
          placeholder="Derived from clo"
          min={1} max={2} step={0.01}
          disabled={disabled}
          hint="Leave empty to let the backend derive f_cl from clo."
          onChange={(v) => onChange("clothing_area_factor", v)}
        />
        <OptionalNumberField
          label="Evaporative Resistance (Re,cl)"
          suffix="m²·Pa/W"
          value={value.evaporative_resistance_m2pa_w}
          placeholder="Derived from clo"
          min={0} max={1000} step={0.5}
          disabled={disabled}
          onChange={(v) => onChange("evaporative_resistance_m2pa_w", v)}
        />
        <NumberField
          label="Projected Solar Area Factor"
          value={value.projected_solar_area_factor}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(v) => onChange("projected_solar_area_factor", v)}
        />
        <NumberField
          label="Solar Reflectance"
          value={value.solar_reflectance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(v) => onChange("solar_reflectance", v)}
        />
        <NumberField
          label="Solar Transmittance"
          value={value.solar_transmittance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(v) => onChange("solar_transmittance", v)}
        />
        <NumberField
          label="Infrared Emissivity"
          value={value.infrared_emissivity}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(v) => onChange("infrared_emissivity", v)}
        />
        <NumberField
          label="Infrared Transmittance"
          value={value.infrared_transmittance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(v) => onChange("infrared_transmittance", v)}
        />
        <OptionalNumberField
          label="Areal Density"
          suffix="g/m²"
          value={value.areal_density_g_m2}
          placeholder="Not recorded"
          min={0} step={1}
          disabled={disabled}
          onChange={(v) => onChange("areal_density_g_m2", v)}
        />
        <OptionalNumberField
          label="Specific Heat"
          suffix="J/(kg·K)"
          value={value.specific_heat_j_kgk}
          placeholder="Not recorded"
          min={0} step={10}
          disabled={disabled}
          onChange={(v) => onChange("specific_heat_j_kgk", v)}
        />
      </div>

      {(solarSumTooHigh || infraredSumTooHigh) && (
        <p role="alert" className="text-sm text-amber-300">
          {solarSumTooHigh && "Solar reflectance + transmittance must not exceed 1. "}
          {infraredSumTooHigh && "Infrared emissivity + transmittance must not exceed 1."}
        </p>
      )}
    </div>
  );
}