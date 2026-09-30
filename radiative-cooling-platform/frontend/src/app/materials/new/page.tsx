"use client";

import { type FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import {ProvenanceEditor} from "@/components/materials/provenance-editor";
import { OptionalNumberField } from "@/components/forms/number-field";
import { createMaterial } from "@/lib/api-client";
import type { MaterialCreate, MaterialVersionInput } from "@/types/material";


const initialMaterial: MaterialCreate = {
  name: "",
  slug: "",
  description: "",
  institution: "",
  initial_version: {
    mode: "opaque_emitter",
    clothing_insulation_clo: 0.4,
    clothing_area_factor: null,
    evaporative_resistance_m2pa_w: 18,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    infrared_transmittance: 0,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
    areal_density_g_m2: 150,
    specific_heat_j_kgk: 1300,
    source_type: "manual",
    source_reference: "",
    notes: "",
  },
};


export default function NewMaterialPage() {
  const router = useRouter();

  const [material, setMaterial] =
    useState(initialMaterial);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  async function handleSubmit(
    event: FormEvent,
  ) {
    event.preventDefault();
    setLoading(true);
    setError("");

    try {
      const created =
        await createMaterial(material);

      router.push(
        `/materials/${created.id}`,
      );
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to load materials.",
      );
    } finally {
      setLoading(false);
    }
  }

  function updateVersion<K extends keyof MaterialVersionInput>(
    field: K,
    value: MaterialVersionInput[K],
  ) {
    setMaterial({
      ...material,
      initial_version: { ...material.initial_version, [field]: value },
    });
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-4xl px-6 py-10">
        <h1 className="text-3xl font-bold">
          New Material
        </h1>

        <form
          onSubmit={handleSubmit}
          className="mt-8 space-y-8"
        >
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Basic Information
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <TextInput
                label="Material Name"
                value={material.name}
                onChange={(value) =>
                  setMaterial({
                    ...material,
                    name: value,
                  })
                }
              />

              <TextInput
                label="Slug"
                value={material.slug}
                onChange={(value) =>
                  setMaterial({
                    ...material,
                    slug: value
                      .toLowerCase()
                      .replace(
                        /[^a-z0-9]+/g,
                        "-",
                      )
                      .replace(/^-|-$/g, ""),
                  })
                }
              />

              <TextInput
                label="Institution"
                value={
                  material.institution ?? ""
                }
                onChange={(value) =>
                  setMaterial({
                    ...material,
                    institution: value,
                  })
                }
              />

              <TextInput
                label="Source Reference"
                value={
                  material.initial_version
                    .source_reference ?? ""
                }
                onChange={(value) =>
                  updateVersion(
                    "source_reference",
                    value,
                  )
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Initial Physical Parameters
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <NumberInput
                label="Clothing Insulation (clo)"
                value={
                  material.initial_version
                    .clothing_insulation_clo
                }
                onChange={(value) =>
                  updateVersion(
                    "clothing_insulation_clo",
                    value,
                  )
                }
              />

              <OptionalNumberField
                label="Clothing Area Factor (f_cl)"
                value={material.initial_version.clothing_area_factor}
                placeholder="Derived from clo"
                min={1}
                max={2}
                step={0.01}
                hint="Leave empty to let the backend derive f_cl from clo."
                onChange={(value) => updateVersion("clothing_area_factor", value)}
              />

              <OptionalNumberField
                label="Evaporative Resistance (Re,cl)"
                suffix="m²·Pa/W"
                value={material.initial_version.evaporative_resistance_m2pa_w}
                placeholder="Derived from clo"
                min={0} max={1000} step={0.5}
                onChange={(value) => updateVersion("evaporative_resistance_m2pa_w", value)}
              />
              <NumberInput
                label="Projected Solar Area Factor"
                value={material.initial_version.projected_solar_area_factor}
                onChange={(value) => updateVersion("projected_solar_area_factor", value)}
              />
              <NumberInput
                label="Absorbed Solar to Body Fraction"
                value={material.initial_version.absorbed_solar_to_body_fraction}
                onChange={(value) => updateVersion("absorbed_solar_to_body_fraction", value)}
              />

              <NumberInput
                label="Solar Reflectance"
                value={
                  material.initial_version
                    .solar_reflectance
                }
                onChange={(value) =>
                  updateVersion(
                    "solar_reflectance",
                    value,
                  )
                }
              />

              <NumberInput
                label="Solar Transmittance"
                value={
                  material.initial_version
                    .solar_transmittance
                }
                onChange={(value) =>
                  updateVersion(
                    "solar_transmittance",
                    value,
                  )
                }
              />

              <NumberInput
                label="Infrared Emissivity"
                value={
                  material.initial_version
                    .infrared_emissivity
                }
                onChange={(value) =>
                  updateVersion(
                    "infrared_emissivity",
                    value,
                  )
                }
              />

              <NumberInput
                label="Infrared Transmittance"
                value={
                  material.initial_version
                    .infrared_transmittance
                }
                onChange={(value) =>
                  updateVersion(
                    "infrared_transmittance",
                    value,
                  )
                }
              />

              <NumberInput
                label="Areal Density (g/m²)"
                value={
                  material.initial_version
                    .areal_density_g_m2 ?? 0
                }
                onChange={(value) =>
                  updateVersion(
                    "areal_density_g_m2",
                    value,
                  )
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Parameter Provenance</h2>
            <p className="mt-2 text-sm text-slate-400">
              Record where each value came from. Provenance travels with the
              version into every simulation that references it.
            </p>
            <div className="mt-5">
              <ProvenanceEditor
                sources={material.initial_version.parameter_sources ?? null}
                values={material.initial_version}
                disabled={loading}
                onChange={(sources) => updateVersion("parameter_sources", sources)}
              />
            </div>
          </section>

          {error && (
            <div className="rounded-lg bg-red-950 p-4 text-red-300">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="rounded-lg bg-cyan-400 px-7 py-3 font-semibold text-slate-950 disabled:opacity-50"
          >
            {loading
              ? "Creating Material…"
              : "Create Material"}
          </button>
        </form>
      </div>
    </main>
  );
}


function TextInput({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        required
        value={value}
        onChange={(event) =>
          onChange(event.target.value)
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
      />
    </label>
  );
}


function NumberInput({
  label,
  value,
  onChange,
}: {
  label: string;
  value: number;
  onChange: (value: number) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        type="number"
        min={0}
        step={0.01}
        value={value}
        onChange={(event) =>
          onChange(
            Number(event.target.value),
          )
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
      />
    </label>
  );
}