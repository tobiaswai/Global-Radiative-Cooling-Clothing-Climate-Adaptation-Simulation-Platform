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

  /*
   * materialId 改變時，React 會把它視為另一個材料詳情元件，
   * 自動重設 material、file、message 等內部狀態。
   */
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

    /*
     * Effect 負責讓頁面和外部 API 同步。
     * 不要在 Effect 中呼叫一個會同步 setState 的函式。
     */
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
              : "載入材料失敗",
          );
        }
      })
      .finally(() => {
        if (!ignore) {
          setLoading(false);
        }
      });

    return () => {
      /*
       * 如果元件卸載或 materialId 改變，
       * 忽略舊請求的結果，防止競態條件。
       */
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

      /*
       * 上傳是由使用者點擊按鈕觸發，
       * 所以重新取得材料資料應放在事件處理函式中。
       */
      const refreshedMaterial =
        await getMaterial(materialId);

      setMaterial(refreshedMaterial);
      setFile(null);
      setMessage("光譜上傳成功");
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "上傳失敗",
      );
    } finally {
      setUploading(false);
    }
  }

  if (loading) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        正在載入材料……
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
        找不到材料
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
              "尚未提供材料說明"}
          </p>

          <div className="mt-4 flex flex-wrap gap-4 text-sm text-slate-500">
            <span>
              Slug：{material.slug}
            </span>

            <span>
              機構：
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
                    label="太陽反射率"
                    value={
                      version.solar_reflectance
                    }
                  />

                  <Metric
                    label="中紅外發射率"
                    value={
                      version.infrared_emissivity
                    }
                  />

                  <Metric
                    label="中紅外透射率"
                    value={
                      version.infrared_transmittance
                    }
                  />

                  <Metric
                    label="服裝熱阻"
                    value={
                      version.clothing_insulation_clo
                    }
                    unit="clo"
                  />
                </div>

                <div className="mt-5">
                  <p className="text-sm text-slate-400">
                    已上傳光譜：
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
                              個數據點
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
              上傳 Version{" "}
              {latestVersion.version_number}{" "}
              光譜
            </h2>

            <p className="mt-2 text-sm text-slate-400">
              CSV 必須包含
              wavelength_um 和 value
              兩個欄位。
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
                  太陽反射光譜
                </option>

                <option value="solar_transmittance">
                  太陽透射光譜
                </option>

                <option value="mir_emissivity">
                  中紅外發射光譜
                </option>

                <option value="mir_transmittance">
                  中紅外透射光譜
                </option>
              </select>

              <input
                key={
                  /*
                   * 上傳成功後 file 被設為 null。
                   * key 改變可重建原生文件輸入。
                   */
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
                  ? "正在上傳……"
                  : "上傳"}
              </button>
            </div>

            {file && (
              <p className="mt-4 text-sm text-slate-400">
                已選擇文件：{file.name}
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