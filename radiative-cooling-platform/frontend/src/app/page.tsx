"use client";

import { useState } from "react";

type HealthResponse = {
  status: string;
  service: string;
  time: string;
};

export default function Home() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function checkBackend() {
    setLoading(true);
    setError("");
    setHealth(null);

    const apiBaseUrl =
      process.env.NEXT_PUBLIC_API_BASE_URL ??
      "http://127.0.0.1:8000";

    const requestUrl = `${apiBaseUrl}/api/v1/health`;

    console.log("Requesting backend:", requestUrl);

    try {
      const response = await fetch(requestUrl, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });

      if (!response.ok) {
        throw new Error(
          `後端返回 HTTP ${response.status}: ${response.statusText}`
        );
      }

      const data: HealthResponse = await response.json();
      setHealth(data);
    } catch (err) {
      console.error("Backend connection error:", err);

      setError(
        err instanceof Error
          ? `${err.message}；請求地址：${requestUrl}`
          : `無法連接後端；請求地址：${requestUrl}`
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-5xl px-6 py-16">
        <p className="mb-3 text-sm font-medium text-cyan-400">
          Radiative Cooling Platform
        </p>

        <h1 className="text-4xl font-bold tracking-tight">
          輻射製冷服裝全球氣候適應性模擬平台－自動更新測試
        </h1>

        <p className="mt-4 max-w-2xl text-slate-400">
          基於全球氣象數據、人體熱調節模型與服裝輻射傳熱模型的
          虛擬測試平台。
        </p>

        <section className="mt-10 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            系統連接測試
          </h2>

          <button
            type="button"
            onClick={checkBackend}
            disabled={loading}
            className="mt-5 rounded-lg bg-cyan-500 px-5 py-2.5 font-medium text-slate-950 hover:bg-cyan-400 disabled:opacity-50"
          >
            {loading ? "正在檢查……" : "檢查後端狀態"}
          </button>

          {health && (
            <div className="mt-5 rounded-lg bg-emerald-950 p-4 text-emerald-300">
              <p>狀態：{health.status}</p>
              <p>服務：{health.service}</p>
              <p>時間：{health.time}</p>
            </div>
          )}

          {error && (
            <div className="mt-5 rounded-lg bg-red-950 p-4 text-red-300">
              連接失敗：{error}
            </div>
          )}
        </section>
      </div>
    </main>
  );
}