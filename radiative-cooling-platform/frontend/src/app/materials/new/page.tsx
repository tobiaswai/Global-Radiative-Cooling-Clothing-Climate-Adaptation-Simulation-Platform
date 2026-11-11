"use client";

import { type FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import {ProvenanceEditor} from "@/components/materials/provenance-editor";
import { createMaterial } from "@/lib/api-client";
import type { MaterialCreate, MaterialVersionInput } from "@/types/material";
import { MaterialVersionFields } from "@/components/materials/material-version-fields";


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
            <div className="mt-5">
              <MaterialVersionFields
                value={material.initial_version}
                disabled={loading}
                onChange={updateVersion}
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
