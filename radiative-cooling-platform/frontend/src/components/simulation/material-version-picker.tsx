"use client";

import { useEffect, useState } from "react";

import {
  getMaterialSimulationInput,
  getMaterialVersions,
} from "@/lib/api-client";
import type { MaterialVersionListItem } from "@/types/material";
import type { MaterialInput } from "@/types/simulation";

type MaterialVersionPickerProps = {
  material: MaterialInput;
  disabled?: boolean;
  onChange: (material: MaterialInput) => void;
};

/**
 * Links a MaterialInput to an immutable material library version. Selecting a
 * version loads the backend's `simulation-input` projection, so the values
 * shown are exactly what the backend will verify against on submit.
 */
export function MaterialVersionPicker({
  material,
  disabled = false,
  onChange,
}: MaterialVersionPickerProps) {
  const [versions, setVersions] = useState<MaterialVersionListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [applying, setApplying] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    getMaterialVersions()
      .then((response) => {
        if (!ignore) setVersions(response.items);
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load material library",
          );
        }
      })
      .finally(() => {
        if (!ignore) setLoading(false);
      });

    return () => {
      ignore = true;
    };
  }, []);

  const linked = material.material_version_id
    ? versions.find((v) => v.id === material.material_version_id) ?? null
    : null;

  async function applyVersion(versionId: string) {
    if (!versionId) {
      unlink();
      return;
    }

    setApplying(true);
    setError("");

    try {
      const input = await getMaterialSimulationInput(versionId);
      onChange(input);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to apply material version",
      );
    } finally {
      setApplying(false);
    }
  }

  function unlink() {
    onChange({
      ...material,
      material_version_id: null,
      parameter_sources: null,
      source_type: null,
      source_reference: null,
    });
  }

  const grouped = new Map<string, MaterialVersionListItem[]>();
  for (const version of versions) {
    const list = grouped.get(version.material_name) ?? [];
    list.push(version);
    grouped.set(version.material_name, list);
  }

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950/60 p-4">
      <label className="block">
        <span className="mb-2 block text-sm text-slate-300">
          Material library
        </span>

        <select
          value={material.material_version_id ?? ""}
          disabled={disabled || loading || applying}
          onChange={(event) => void applyVersion(event.target.value)}
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
        >
          <option value="">
            {loading ? "Loading library…" : "— Manual values (not linked) —"}
          </option>

          {Array.from(grouped.entries()).map(([name, items]) => (
            <optgroup key={name} label={name}>
              {items.map((version) => (
                <option key={version.id} value={version.id}>
                  v{version.version_number} · {version.clothing_insulation_clo} clo · ρ
                  {version.solar_reflectance.toFixed(2)} · ε
                  {version.infrared_emissivity.toFixed(2)}
                  {version.infrared_transmittance > 0
                    ? ` · τ_IR ${version.infrared_transmittance.toFixed(2)}`
                    : ""}
                </option>
              ))}
            </optgroup>
          ))}
        </select>
      </label>

      {material.material_version_id && (
        <div className="mt-3 flex flex-wrap items-center justify-between gap-3 text-xs">
          <span className="rounded-full border border-emerald-800 bg-emerald-950 px-2.5 py-1 text-emerald-300">
            Linked to{" "}
            {linked
              ? `${linked.material_name} v${linked.version_number}`
              : material.material_version_id}
            {material.source_type ? ` · ${material.source_type}` : ""}
          </span>

          <button
            type="button"
            onClick={unlink}
            disabled={disabled}
            className="text-slate-400 underline-offset-2 hover:text-white hover:underline"
          >
            Unlink
          </button>
        </div>
      )}

      {applying && (
        <p className="mt-2 text-xs text-slate-500">Loading version parameters…</p>
      )}

      {error && (
        <p role="alert" className="mt-2 text-xs text-red-300">
          {error}
        </p>
      )}
    </div>
  );
}