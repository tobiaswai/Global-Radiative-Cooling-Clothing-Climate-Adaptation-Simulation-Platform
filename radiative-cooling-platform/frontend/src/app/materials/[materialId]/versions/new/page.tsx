"use client";

import Link from "next/link";
import { useParams, useRouter } from "next/navigation";
import { type FormEvent, useEffect, useState } from "react";

import { MaterialVersionFields } from "@/components/materials/material-version-fields";
import { ProvenanceEditor } from "@/components/materials/provenance-editor";
import { createMaterialVersion, getMaterial } from "@/lib/api-client";
import type { Material, MaterialVersion, MaterialVersionInput } from "@/types/material";

/** Pre-fill from an existing version. Deprecated fields are not copied. */
function versionToInput(version: MaterialVersion): MaterialVersionInput {
  return {
    mode: version.mode,
    clothing_insulation_clo: version.clothing_insulation_clo,
    clothing_area_factor: version.clothing_area_factor ?? null,
    evaporative_resistance_m2pa_w: version.evaporative_resistance_m2pa_w,
    solar_reflectance: version.solar_reflectance,
    solar_transmittance: version.solar_transmittance,
    infrared_emissivity: version.infrared_emissivity,
    infrared_transmittance: version.infrared_transmittance,
    projected_solar_area_factor: version.projected_solar_area_factor,
    areal_density_g_m2: version.areal_density_g_m2,
    specific_heat_j_kgk: version.specific_heat_j_kgk,
    source_type: version.source_type,
    source_reference: version.source_reference,
    notes: null,
    parameter_sources: version.parameter_sources ?? null,
  };
}

export default function NewMaterialVersionPage() {
  const { materialId } = useParams<{ materialId: string }>();
  return <NewVersionContent key={materialId} materialId={materialId} />;
}

function NewVersionContent({ materialId }: { materialId: string }) {
  const router = useRouter();
  const [material, setMaterial] = useState<Material | null>(null);
  const [draft, setDraft] = useState<MaterialVersionInput | null>(null);
  const [loadError, setLoadError] = useState("");
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    let ignore = false;

    getMaterial(materialId)
      .then((response) => {
        if (ignore) return;
        const latest = response.versions.at(-1);
        setMaterial(response);
        if (latest) {
          setDraft(versionToInput(latest));
        } else {
          setLoadError("This material has no version to start from.");
        }
      })
      .catch((caught: unknown) => {
        if (!ignore) {
          setLoadError(caught instanceof Error ? caught.message : "Failed to load material");
        }
      });

    return () => {
      ignore = true;
    };
  }, [materialId]);

  function update<K extends keyof MaterialVersionInput>(field: K, value: MaterialVersionInput[K]) {
    setDraft((current) => (current ? { ...current, [field]: value } : current));
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!draft || submitting) return;

    setSubmitting(true);
    setError("");

    try {
      await createMaterialVersion(materialId, draft);
      router.push(`/materials/${materialId}`);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Failed to create version");
      setSubmitting(false);
    }
  }

  if (loadError) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{loadError}</div>
      </main>
    );
  }

  if (!material || !draft) {
    return <main className="min-h-screen bg-slate-950 p-10 text-white">Loading material…</main>;
  }

  const base = material.versions.at(-1);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-4xl px-6 py-10">
        <nav className="mb-4 flex items-center gap-2 text-sm text-slate-400">
          <Link href="/materials" className="hover:text-slate-100">Materials</Link>
          <span>/</span>
          <Link href={`/materials/${material.id}`} className="hover:text-slate-100">{material.name}</Link>
          <span>/</span>
          <span className="text-slate-200">New version</span>
        </nav>

        <h1 className="text-3xl font-bold">New Version of {material.name}</h1>
        <p className="mt-3 text-slate-400">
          Pre-filled from v{base?.version_number}. Existing versions are immutable because
          simulations reference them; saving creates v{(base?.version_number ?? 0) + 1}.
          Spectra are not copied.
        </p>

        <form onSubmit={handleSubmit} className="mt-8 space-y-8">
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Physical Parameters</h2>
            <div className="mt-5">
              <MaterialVersionFields value={draft} disabled={submitting} onChange={update} />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Source</h2>
            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <label className="block">
                <span className="mb-2 block text-sm text-slate-300">Source Type</span>
                <input
                  value={draft.source_type}
                  maxLength={50}
                  disabled={submitting}
                  onChange={(event) => update("source_type", event.target.value)}
                  className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 disabled:opacity-50"
                />
              </label>
              <label className="block">
                <span className="mb-2 block text-sm text-slate-300">Source Reference</span>
                <input
                  value={draft.source_reference ?? ""}
                  disabled={submitting}
                  onChange={(event) => update("source_reference", event.target.value || null)}
                  className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 disabled:opacity-50"
                />
              </label>
              <label className="block md:col-span-2">
                <span className="mb-2 block text-sm text-slate-300">Notes (what changed and why)</span>
                <textarea
                  rows={3}
                  value={draft.notes ?? ""}
                  disabled={submitting}
                  onChange={(event) => update("notes", event.target.value || null)}
                  className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 disabled:opacity-50"
                />
              </label>
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Parameter Provenance</h2>
            <p className="mt-2 text-sm text-slate-400">
              Copied from v{base?.version_number}. Update the entries for values you changed.
            </p>
            <div className="mt-5">
              <ProvenanceEditor
                sources={draft.parameter_sources ?? null}
                values={draft}
                disabled={submitting}
                onChange={(sources) => update("parameter_sources", sources)}
              />
            </div>
          </section>

          {error && (
            <div role="alert" className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={submitting}
            className="rounded-lg bg-cyan-400 px-7 py-3 font-semibold text-slate-950 disabled:opacity-50"
          >
            {submitting ? "Creating version…" : "Create Version"}
          </button>
        </form>
      </div>
    </main>
  );
}