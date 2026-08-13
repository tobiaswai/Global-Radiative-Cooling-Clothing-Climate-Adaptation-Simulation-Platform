"use client";

import {
  FormEvent,
  useState,
} from "react";
import { useRouter } from "next/navigation";

import { createMaterial } from "@/lib/api-client";
import type {
  MaterialCreate,
} from "@/types/material";


const initialMaterial: MaterialCreate = {
  name: "",
  slug: "",
  description: "",
  institution: "",
  initial_version: {
    mode: "opaque_emitter",
    clothing_insulation_clo: 0.4,
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
          : "建立材料失敗",
      );
    } finally {
      setLoading(false);
    }
  }

  function updateVersion(
    field: string,
    value: string | number,
  ) {
    setMaterial({
      ...material,
      initial_version: {
        ...material.initial_version,
        [field]: value,
      },
    });
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-4xl px-6 py-10">
        <h1 className="text-3xl font-bold">
          新建材料
        </h1>

        <form
          onSubmit={handleSubmit}
          className="mt-8 space-y-8"
        >
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              基本資料
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <TextInput
                label="材料名稱"
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
                label="研究機構"
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
                label="資料來源"
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
              初始物理參數
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <NumberInput
                label="服裝熱阻（clo）"
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

              <NumberInput
                label="太陽反射率"
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
                label="太陽透射率"
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
                label="中紅外發射率"
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
                label="中紅外透射率"
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
                label="面密度（g/m²）"
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
              ? "正在建立……"
              : "建立材料"}
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