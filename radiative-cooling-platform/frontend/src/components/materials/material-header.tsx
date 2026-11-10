"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { type FormEvent, useState } from "react";

import { deleteMaterial, updateMaterial } from "@/lib/api-client";
import type { Material, MaterialUpdate } from "@/types/material";

type Busy = "saving" | "archiving" | "deleting" | null;
type Draft = { name: string; description: string; institution: string };

function toDraft(material: Material): Draft {
  return {
    name: material.name,
    description: material.description ?? "",
    institution: material.institution ?? "",
  };
}

/** PATCH semantics: send only what changed. */
function diff(material: Material, draft: Draft): MaterialUpdate {
  const changes: MaterialUpdate = {};
  const name = draft.name.trim();
  const description = draft.description.trim();
  const institution = draft.institution.trim();

  if (name !== material.name) changes.name = name;
  if (description !== (material.description ?? "")) changes.description = description || null;
  if (institution !== (material.institution ?? "")) changes.institution = institution || null;

  return changes;
}

export function MaterialHeader({
  material,
  onUpdated,
}: {
  material: Material;
  onUpdated: (material: Material) => void;
}) {
  const router = useRouter();
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState<Draft>(() => toDraft(material));
  const [busy, setBusy] = useState<Busy>(null);
  const [error, setError] = useState("");
  const disabled = busy !== null;

  async function run(kind: Exclude<Busy, null>, action: () => Promise<void>) {
    setBusy(kind);
    setError("");
    try {
      await action();
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Request failed");
    } finally {
      setBusy(null);
    }
  }

  function startEditing() {
    setDraft(toDraft(material));
    setError("");
    setEditing(true);
  }

  function handleSave(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!draft.name.trim()) {
      setError("Material name is required.");
      return;
    }

    const changes = diff(material, draft);

    if (Object.keys(changes).length === 0) {
      setEditing(false);
      return;
    }

    void run("saving", async () => {
      onUpdated(await updateMaterial(material.id, changes));
      setEditing(false);
    });
  }

  function toggleArchived() {
    void run("archiving", async () => {
      onUpdated(await updateMaterial(material.id, { is_archived: !material.is_archived }));
    });
  }

  function handleDelete() {
    const confirmed = window.confirm(
      `Permanently delete "${material.name}" with its ${material.versions.length} ` +
        "version(s) and uploaded spectra? This cannot be undone.",
    );
    if (!confirmed) return;

    void run("deleting", async () => {
      await deleteMaterial(material.id);
      router.push("/materials");
    });
  }

  return (
    <header>
      <p className="text-sm text-cyan-400">Material Detail</p>

      {editing ? (
        <form
          onSubmit={handleSave}
          className="mt-4 space-y-4 rounded-2xl border border-slate-800 bg-slate-900 p-6"
        >
          <div className="grid gap-4 md:grid-cols-2">
            <TextField
              label="Material Name"
              value={draft.name}
              maxLength={200}
              disabled={disabled}
              onChange={(name) => setDraft({ ...draft, name })}
            />
            <TextField
              label="Institution"
              value={draft.institution}
              maxLength={255}
              disabled={disabled}
              onChange={(institution) => setDraft({ ...draft, institution })}
            />
          </div>

          <label className="block">
            <span className="mb-2 block text-sm text-slate-300">Description</span>
            <textarea
              value={draft.description}
              rows={3}
              disabled={disabled}
              onChange={(event) => setDraft({ ...draft, description: event.target.value })}
              className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:opacity-50"
            />
          </label>

          <p className="text-xs text-slate-500">
            Slug <span className="font-mono">{material.slug}</span> cannot be changed.
            Physical parameters are versioned; create a new version to change them.
          </p>

          <div className="flex gap-3">
            <button
              type="submit"
              disabled={disabled}
              className="rounded-lg bg-cyan-400 px-5 py-2 font-semibold text-slate-950 disabled:opacity-50"
            >
              {busy === "saving" ? "Saving…" : "Save"}
            </button>
            <button
              type="button"
              disabled={disabled}
              onClick={() => setEditing(false)}
              className="rounded-lg border border-slate-700 px-5 py-2 text-slate-300 hover:bg-slate-800 disabled:opacity-50"
            >
              Cancel
            </button>
          </div>
        </form>
      ) : (
        <>
          <div className="mt-2 flex flex-wrap items-center gap-3">
            <h1 className="text-3xl font-bold">{material.name}</h1>
            {material.is_archived && (
              <span className="rounded-full border border-slate-700 bg-slate-800 px-3 py-1 text-xs text-slate-300">
                Archived
              </span>
            )}
          </div>

          <p className="mt-2 text-slate-400">
            {material.description || "Material description not available"}
          </p>

          <div className="mt-4 flex flex-wrap gap-4 text-sm text-slate-500">
            <span>Slug: <span className="font-mono">{material.slug}</span></span>
            <span>Institution: {material.institution ?? "—"}</span>
          </div>

          <div className="mt-5 flex flex-wrap gap-3">
            <button
              type="button"
              disabled={disabled}
              onClick={startEditing}
              className="rounded-lg border border-cyan-700 px-4 py-2 text-sm text-cyan-300 hover:bg-cyan-950 disabled:opacity-50"
            >
              Edit details
            </button>

            <Link
              href={`/materials/${material.id}/versions/new`}
              className="rounded-lg border border-cyan-700 px-4 py-2 text-sm text-cyan-300 hover:bg-cyan-950"
            >
              New version
            </Link>

            <button
              type="button"
              disabled={disabled}
              onClick={toggleArchived}
              className="rounded-lg border border-amber-700 px-4 py-2 text-sm text-amber-300 hover:bg-amber-950 disabled:opacity-50"
            >
              {busy === "archiving"
                ? "Updating…"
                : material.is_archived ? "Unarchive" : "Archive"}
            </button>

            <button
              type="button"
              disabled={disabled}
              onClick={handleDelete}
              className="rounded-lg border border-red-800 px-4 py-2 text-sm text-red-300 hover:bg-red-950 disabled:opacity-50"
            >
              {busy === "deleting" ? "Deleting…" : "Delete"}
            </button>
          </div>
        </>
      )}

      {error && (
        <div role="alert" className="mt-4 rounded-lg border border-red-900 bg-red-950 p-4 text-sm text-red-300">
          {error}
        </div>
      )}
    </header>
  );
}

function TextField({
  label,
  value,
  maxLength,
  disabled,
  onChange,
}: {
  label: string;
  value: string;
  maxLength: number;
  disabled: boolean;
  onChange: (value: string) => void;
}) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm text-slate-300">{label}</span>
      <input
        value={value}
        maxLength={maxLength}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:opacity-50"
      />
    </label>
  );
}