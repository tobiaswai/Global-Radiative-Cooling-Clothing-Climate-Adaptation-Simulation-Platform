"use client";

import { useEffect, useState } from "react";

import { getMaterialFieldManifest } from "@/lib/api-client";
import type {
  MaterialFieldManifest,
  ParameterSource,
  ParameterSourceType,
} from "@/types/simulation";

type ProvenanceEditorProps = {
  sources: Record<string, ParameterSource> | null;
  /** The version being edited; only physical fields are read. */
  values: Record<string, unknown>;
  disabled?: boolean;
  onChange: (sources: Record<string, ParameterSource> | null) => void;
};

export function ProvenanceEditor({
  sources,
  values,
  disabled = false,
  onChange,
}: ProvenanceEditorProps) {
  const [manifest, setManifest] = useState<MaterialFieldManifest | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    getMaterialFieldManifest()
      .then((response) => {
        if (!ignore) setManifest(response);
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load field manifest",
          );
        }
      });

    return () => {
      ignore = true;
    };
  }, []);

  function update(field: string, patch: Partial<ParameterSource>) {
    const current = sources?.[field] ?? { source_type: "assumed" as ParameterSourceType };
    onChange({ ...(sources ?? {}), [field]: { ...current, ...patch } });
  }

  function clear(field: string) {
    const next = { ...(sources ?? {}) };
    delete next[field];
    onChange(Object.keys(next).length > 0 ? next : null);
  }

  if (error) {
    return <p className="text-sm text-red-300">{error}</p>;
  }

  if (!manifest) {
    return <p className="text-sm text-slate-500">Loading field manifest…</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-160 text-left text-sm">
        <thead className="border-b border-slate-700 text-slate-400">
          <tr>
            <th className="px-3 py-3">Parameter</th>
            <th className="px-3 py-3">Value</th>
            <th className="px-3 py-3">Source type</th>
            <th className="px-3 py-3">Reference</th>
            <th className="px-3 py-3" />
          </tr>
        </thead>

        <tbody>
          {manifest.fields.map((field) => {
            const source = sources?.[field.name];
            const value = values[field.name];

            return (
              <tr key={field.name} className="border-b border-slate-800 align-top">
                <td className="px-3 py-3">
                  <p className="font-mono text-slate-200">{field.name}</p>
                  <p className="mt-1 text-xs text-slate-500">
                    {field.description}
                    {field.unit !== "-" ? ` (${field.unit})` : ""}
                  </p>
                </td>

                <td className="px-3 py-3 text-slate-300">
                  {typeof value === "number"
                    ? value
                    : field.derived_when_null
                      ? <span className="text-slate-500">derived: {field.derived_when_null}</span>
                      : "—"}
                </td>

                <td className="px-3 py-3">
                  <select
                    value={source?.source_type ?? ""}
                    disabled={disabled}
                    onChange={(event) =>
                      event.target.value
                        ? update(field.name, {
                            source_type: event.target.value as ParameterSourceType,
                          })
                        : clear(field.name)
                    }
                    className="rounded-lg border border-slate-700 bg-slate-950 px-2 py-1.5 text-white disabled:opacity-50"
                  >
                    <option value="">— not recorded —</option>
                    {manifest.source_types.map((type) => (
                      <option key={type} value={type}>
                        {type}
                      </option>
                    ))}
                  </select>
                </td>

                <td className="px-3 py-3">
                  <input
                    type="text"
                    value={source?.reference ?? ""}
                    disabled={disabled || !source}
                    maxLength={500}
                    placeholder={source ? "Report, DOI, datasheet…" : ""}
                    onChange={(event) =>
                      update(field.name, { reference: event.target.value || null })
                    }
                    className="w-full rounded-lg border border-slate-700 bg-slate-950 px-2 py-1.5 text-white disabled:opacity-50"
                  />
                </td>

                <td className="px-3 py-3">
                  {source && (
                    <button
                      type="button"
                      disabled={disabled}
                      onClick={() => clear(field.name)}
                      className="text-xs text-slate-400 hover:text-white"
                    >
                      Clear
                    </button>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}