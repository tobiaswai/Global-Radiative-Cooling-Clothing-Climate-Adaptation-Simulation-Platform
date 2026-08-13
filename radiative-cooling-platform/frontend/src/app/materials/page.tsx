"use client";

import Link from "next/link";
import {
  FormEvent,
  useEffect,
  useState,
} from "react";

import { getMaterials } from "@/lib/api-client";
import type {
  MaterialListItem,
} from "@/types/material";

export default function MaterialsPage() {
  const [materials, setMaterials] =
    useState<MaterialListItem[]>([]);

  const [search, setSearch] =
    useState("");

  // 初始畫面本來就是載入狀態，不需要 Effect 再設為 true
  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    let ignore = false;

    getMaterials()
      .then((response) => {
        if (!ignore) {
          setMaterials(response.items);
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
      // 防止元件卸載後，過期請求繼續更新 state
      ignore = true;
    };
  }, []);

  async function handleSearchSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    // 這些更新由使用者提交表單觸發，
    // 因此應該放在事件處理函式中。
    setLoading(true);
    setError("");

    try {
      const response = await getMaterials(
        search,
      );

      setMaterials(response.items);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "載入材料失敗",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-sm text-cyan-400">
              Material Database
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              輻射製冷材料
            </h1>
          </div>

          <Link
            href="/materials/new"
            className="rounded-lg bg-cyan-400 px-5 py-2.5 font-semibold text-slate-950"
          >
            新建材料
          </Link>
        </header>

        <form
          className="mt-8 flex gap-3"
          onSubmit={handleSearchSubmit}
        >
          <input
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
            placeholder="搜尋材料名稱"
            className="max-w-md flex-1 rounded-lg border border-slate-700 bg-slate-900 px-4 py-2"
          />

          <button
            type="submit"
            disabled={loading}
            className="rounded-lg border border-slate-700 px-5 py-2 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "載入中……" : "搜尋"}
          </button>
        </form>

        {error && (
          <div className="mt-6 rounded-lg bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <table className="w-full text-left">
            <thead className="bg-slate-900 text-sm text-slate-400">
              <tr>
                <th className="px-5 py-4">
                  材料
                </th>
                <th className="px-5 py-4">
                  機構
                </th>
                <th className="px-5 py-4">
                  最新版本
                </th>
                <th className="px-5 py-4">
                  建立時間
                </th>
              </tr>
            </thead>

            <tbody>
              {materials.map((material) => (
                <tr
                  key={material.id}
                  className="border-t border-slate-800 bg-slate-950"
                >
                  <td className="px-5 py-4">
                    <Link
                      href={`/materials/${material.id}`}
                      className="font-medium text-cyan-300 hover:underline"
                    >
                      {material.name}
                    </Link>

                    <p className="mt-1 text-xs text-slate-500">
                      {material.slug}
                    </p>
                  </td>

                  <td className="px-5 py-4 text-slate-300">
                    {material.institution ?? "—"}
                  </td>

                  <td className="px-5 py-4">
                    {material.latest_version_number
                      ? `v${material.latest_version_number}`
                      : "—"}
                  </td>

                  <td className="px-5 py-4 text-sm text-slate-400">
                    {new Date(
                      material.created_at,
                    ).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {loading && (
            <div className="p-10 text-center text-slate-400">
              正在載入……
            </div>
          )}

          {!loading &&
            materials.length === 0 && (
              <div className="p-10 text-center text-slate-400">
                尚未建立材料
              </div>
            )}
        </section>
      </div>
    </main>
  );
}