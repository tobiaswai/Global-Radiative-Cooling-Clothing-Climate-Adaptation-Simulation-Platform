"use client";

import {
  useEffect,
  useState,
} from "react";
import { useParams } from "next/navigation";

import {
  getMaterial,
  uploadMaterialSpectrum,
} from "@/lib/api-client";
import type {
  Material,
} from "@/types/material";

type SpectrumType =
  | "solar_reflectance"
  | "solar_transmittance"
  | "mir_emissivity"
  | "mir_transmittance";

export default function MaterialDetailPage() {
  const parameters =
    useParams<{ materialId: string }>();

  const materialId = parameters.materialId;

  return (
    <MaterialDetailContent
      key={materialId}
      materialId={materialId}
    />
  );
}

function MaterialDetailContent({
  materialId,
}: {
  materialId: string;
}) {
  const [material, setMaterial] =
    useState<Material | null>(null);

  const [file, setFile] =
    useState<File | null>(null);

  const [spectrumType, setSpectrumType] =
    useState<SpectrumType>(
      "mir_emissivity",
    );

  const [message, setMessage] =
    useState("");

  const [error, setError] =
    useState("");

  const [loading, setLoading] =
    useState(true);

  const [uploading, setUploading] =
    useState(false);

  useEffect(() => {
    let ignore = false;

    getMaterial(materialId)
      .then((response) => {
        if (!ignore) {
          setMaterial(response);
        }
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Loading material failed",
          );
        }
      })
      .finally(() => {
        if (!ignore) {
          setLoading(false);
        }
      });

    return () => {

      ignore = true;
    };
  }, [materialId]);

  async function handleUpload() {
    const latestVersion =
      material?.versions.at(-1);

    if (!file || !latestVersion) {
      return;
    }

    setUploading(true);
    setMessage("");
    setError("");

    try {
      await uploadMaterialSpectrum(
        latestVersion.id,
        spectrumType,
        file,
      );

      const refreshedMaterial =
        await getMaterial(materialId);

      setMaterial(refreshedMaterial);
      setFile(null);
      setMessage("Spectrum uploaded successfully");
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Upload failed",
      );
    } finally {
      setUploading(false);
    }
  }

  if (loading) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        Loading material…
      </main>
    );
  }

  if (error && !material) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
          {error}
        </div>
      </main>
    );
  }

  if (!material) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        Material not found
      </main>
    );
  }

  const latestVersion =
    material.versions.at(-1);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-6xl px-6 py-10">
        <header>
          <p className="text-sm text-cyan-400">
            Material Detail
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            {material.name}
          </h1>

          <p className="mt-2 text-slate-400">
            {material.description ||
              "Material description not available"}
          </p>

          <div className="mt-4 flex flex-wrap gap-4 text-sm text-slate-500">
            <span>
              Slug：{material.slug}
            </span>

            <span>
              Institution:
              {material.institution ?? "—"}
            </span>
          </div>
        </header>

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        {message && (
          <div className="mt-6 rounded-lg border border-emerald-900 bg-emerald-950 p-4 text-emerald-300">
            {message}
          </div>
        )}

        <section className="mt-8 space-y-5">
          {material.versions.map(
            (version) => (
              <article
                key={version.id}
                className="rounded-2xl border border-slate-800 bg-slate-900 p-6"
              >
                <div className="flex flex-wrap items-center justify-between gap-4">
                  <h2 className="text-xl font-semibold">
                    Version{" "}
                    {version.version_number}
                  </h2>

                  <span className="rounded-full bg-slate-800 px-3 py-1 text-xs text-slate-300">
                    {version.mode}
                  </span>
                </div>

                <div className="mt-4 grid gap-4 sm:grid-cols-2 md:grid-cols-4">
                  <Metric
                    label="solar reflectance"
                    value={
                      version.solar_reflectance
                    }
                  />

                  <Metric
                    label="infrared emissivity"
                    value={
                      version.infrared_emissivity
                    }
                  />

                  <Metric
                    label="infrared transmittance"
                    value={
                      version.infrared_transmittance
                    }
                  />

                  <Metric
                    label="clothing insulation"
                    value={
                      version.clothing_insulation_clo
                    }
                    unit="clo"
                  />
                </div>

                <div className="mt-5">
                  <p className="text-sm text-slate-400">
                    Spectra uploaded:
                    {version.spectra.length}
                  </p>

                  {version.spectra.length >
                    0 && (
                    <ul className="mt-3 space-y-2">
                      {version.spectra.map(
                        (spectrum) => (
                          <li
                            key={spectrum.id}
                            className="rounded-lg bg-slate-950 px-4 py-3 text-sm text-slate-300"
                          >
                            <span className="font-medium text-cyan-300">
                              {
                                spectrum.spectrum_type
                              }
                            </span>

                            <span className="ml-3 text-slate-500">
                              {
                                spectrum.point_count
                              }{" "}
                              data points
                            </span>

                            <span className="ml-3 text-slate-500">
                              {
                                spectrum.minimum_wavelength_um
                              }
                              –
                              {
                                spectrum.maximum_wavelength_um
                              }{" "}
                              μm
                            </span>
                          </li>
                        ),
                      )}
                    </ul>
                  )}
                </div>
              </article>
            ),
          )}
        </section>

        {latestVersion && (
          <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Upload Version{" "}
              {latestVersion.version_number}{" "}
              Spectra
            </h2>

            <p className="mt-2 text-sm text-slate-400">
              CSV must contain
              wavelength_um and value
              two columns.
            </p>

            <div className="mt-5 flex flex-wrap gap-4">
              <select
                value={spectrumType}
                disabled={uploading}
                onChange={(event) =>
                  setSpectrumType(
                    event.target
                      .value as SpectrumType,
                  )
                }
                className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 disabled:opacity-50"
              >
                <option value="solar_reflectance">
                  Solar Reflectance Spectra
                </option>

                <option value="solar_transmittance">
                  Solar Transmittance Spectra
                </option>

                <option value="mir_emissivity">
                  Infrared Emissivity Spectra
                </option>

                <option value="mir_transmittance">
                  Infrared Transmittance Spectra
                </option>
              </select>

              <input
                key={
                  file?.name ??
                  "empty-file-input"
                }
                type="file"
                accept=".csv,text/csv"
                disabled={uploading}
                onChange={(event) => {
                  setFile(
                    event.target.files?.[0] ??
                      null,
                  );
                  setMessage("");
                  setError("");
                }}
                className="rounded-lg border border-slate-700 p-2 disabled:opacity-50"
              />

              <button
                type="button"
                onClick={handleUpload}
                disabled={!file || uploading}
                className="rounded-lg bg-cyan-400 px-5 py-2 font-semibold text-slate-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {uploading
                  ? "Uploading…"
                  : "Upload"}
              </button>
            </div>

            {file && (
              <p className="mt-4 text-sm text-slate-400">
                File selected: {file.name}
              </p>
            )}
          </section>
        )}
      </div>
    </main>
  );
}

function Metric({
  label,
  value,
  unit,
}: {
  label: string;
  value: number;
  unit?: string;
}) {
  return (
    <div className="rounded-lg bg-slate-950 p-4">
      <p className="text-sm text-slate-400">
        {label}
      </p>

      <p className="mt-1 text-xl font-semibold text-cyan-300">
        {value.toFixed(3)}

        {unit && (
          <span className="ml-1 text-sm font-normal text-slate-400">
            {unit}
          </span>
        )}
      </p>
    </div>
  );
}