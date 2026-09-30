"use client";

import {
  NumberField,
  OptionalNumberField,
} from "@/components/forms/number-field";
import { MaterialVersionPicker } from "@/components/simulation/material-version-picker";
import type { MaterialInput, ParameterSource } from "@/types/simulation";

/** Every MaterialInput key that enters the physics (i.e. not provenance/name). */
type PhysicalKey = Exclude<
  keyof MaterialInput,
  | "name"
  | "material_version_id"
  | "parameter_sources"
  | "source_type"
  | "source_reference"
>;

type MaterialInputFieldsProps = {
  material: MaterialInput;
  showName?: boolean;
  /** Show the material library picker (Stage 4). */
  enableLibrary?: boolean;
  disabled?: boolean;
  onChange: (material: MaterialInput) => void;
};

export function MaterialInputFields({
  material,
  showName = false,
  enableLibrary = false,
  disabled = false,
  onChange,
}: MaterialInputFieldsProps) {
  const linked = Boolean(material.material_version_id);

  function updatePhysical<K extends PhysicalKey>(key: K, value: MaterialInput[K]) {
    const next: MaterialInput = { ...material, [key]: value };

    if (linked) {
      // The backend rejects a version id whose values were edited; drop the
      // link (and the provenance that came with it) instead.
      next.material_version_id = null;
      next.parameter_sources = null;
      next.source_type = null;
      next.source_reference = null;
    }

    onChange(next);
  }

  return (
    <div className="space-y-5">
      {enableLibrary && (
        <MaterialVersionPicker
          material={material}
          disabled={disabled}
          onChange={onChange}
        />
      )}

      {linked && (
        <p className="text-xs text-slate-500">
          Values come from the linked library version. Editing any physical
          value removes the link so the result is not attributed to that version.
        </p>
      )}

      <div className="grid gap-5 sm:grid-cols-2">
        {showName && (
          <label className="block sm:col-span-2">
            <span className="mb-2 block text-sm text-slate-300">Material Name</span>
            <input
              type="text"
              value={material.name}
              maxLength={100}
              disabled={disabled}
              onChange={(event) => onChange({ ...material, name: event.target.value })}
              className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
            />
          </label>
        )}

        <NumberField
          label="Clothing Insulation"
          suffix="clo"
          value={material.clothing_insulation_clo}
          min={0} max={5} step={0.05}
          disabled={disabled}
          onChange={(value) => updatePhysical("clothing_insulation_clo", value)}
        />

        <OptionalNumberField
          label="Evaporative Resistance (Re,cl)"
          suffix="m²·Pa/W"
          value={material.evaporative_resistance_m2pa_w ?? null}
          placeholder="Derived from clo"
          min={0} max={1000} step={0.5}
          disabled={disabled}
          hint="Leave empty to derive R_cl / (LR · i_cl) (Stage 2)."
          onChange={(value) => updatePhysical("evaporative_resistance_m2pa_w", value)}
        />

        <OptionalNumberField
          label="Clothing Area Factor (f_cl)"
          value={material.clothing_area_factor}
          placeholder="Derived from clo"
          min={1} max={2} step={0.01}
          disabled={disabled}
          hint="Leave empty to derive 1 + 0.15 · clo (Stage 3)."
          onChange={(value) => updatePhysical("clothing_area_factor", value)}
        />

        <NumberField
          label="Solar Reflectance"
          value={material.solar_reflectance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("solar_reflectance", value)}
        />

        <NumberField
          label="Solar Transmittance"
          value={material.solar_transmittance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("solar_transmittance", value)}
        />

        <NumberField
          label="Infrared Emissivity"
          value={material.infrared_emissivity}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("infrared_emissivity", value)}
        />

        <NumberField
          label="Infrared Transmittance"
          value={material.infrared_transmittance ?? 0}
          min={0} max={1} step={0.01}
          disabled={disabled}
          hint="Emissivity + transmittance must not exceed 1."
          onChange={(value) => updatePhysical("infrared_transmittance", value)}
        />

        <NumberField
          label="Projected Solar Area Factor"
          value={material.projected_solar_area_factor}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("projected_solar_area_factor", value)}
        />

        <NumberField
          label="Absorbed Solar to Body Fraction"
          value={material.absorbed_solar_to_body_fraction}
          min={0} max={1} step={0.01}
          disabled={disabled}
          hint="Share of textile-absorbed solar heat reaching the skin (ADR 0003)."
          onChange={(value) => updatePhysical("absorbed_solar_to_body_fraction", value)}
        />
      </div>

      <ProvenanceBadges sources={material.parameter_sources} />
    </div>
  );
}

function ProvenanceBadges({
  sources,
}: {
  sources: Record<string, ParameterSource> | null | undefined;
}) {
  const entries = Object.entries(sources ?? {});

  if (entries.length === 0) {
    return null;
  }

  return (
    <div>
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
        Parameter provenance
      </p>

      <ul className="mt-2 flex flex-wrap gap-2">
        {entries.map(([field, source]) => (
          <li
            key={field}
            title={source.reference ?? undefined}
            className="rounded-full border border-slate-700 bg-slate-950 px-2.5 py-1 text-xs text-slate-300"
          >
            <span className="font-mono">{field}</span>
            <span className="ml-1 text-cyan-300">{source.source_type}</span>
            {source.reference && (
              <span className="ml-1 text-slate-500">— {source.reference}</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}