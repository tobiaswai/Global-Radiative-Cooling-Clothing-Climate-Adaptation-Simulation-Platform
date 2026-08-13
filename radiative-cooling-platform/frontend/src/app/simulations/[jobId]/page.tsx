"use client";

import {
  useEffect,
  useState,
} from "react";
import { useParams } from "next/navigation";

import { HeatFluxChart } from "@/components/charts/heat-flux-chart";
import { TemperatureChart } from "@/components/charts/temperature-chart";
import { WeatherChart } from "@/components/charts/weather-chart";
import {
  cancelSimulationJob,
  getSimulationEventsUrl,
  getSimulationJob,
  getSimulationResult,
} from "@/lib/api-client";
import type {
  SimulationJob,
  WeatherSimulationResponse,
} from "@/types/simulation";
import {
  getSimulationExportUrl,
} from "@/lib/api-client";


const terminalStatuses =
  new Set<SimulationJob["status"]>([
    "completed",
    "failed",
    "cancelled",
  ]);


const stageLabels: Record<string, string> = {
  queued: "等待計算資源",
  initializing: "正在初始化模型",
  downloading_weather:
    "正在取得歷史氣象資料",
  running_control_simulation:
    "正在模擬普通對照服裝",
  running_radiative_cooling_simulation:
    "正在模擬輻射製冷服裝",
  generating_summary:
    "正在生成結果摘要",
  saving_result:
    "正在保存結果",
  completed: "模擬完成",
  failed: "模擬失敗",
  cancelling: "正在取消",
  waiting_for_cooperative_cancel:
    "正在等待安全取消",
  cancelled: "已取消",
};


export default function SimulationJobPage() {
  const parameters =
    useParams<{ jobId: string }>();

  const jobId = parameters.jobId;

  const [job, setJob] =
    useState<SimulationJob | null>(null);

  const [result, setResult] =
    useState<WeatherSimulationResponse | null>(
      null,
    );

  const [error, setError] =
    useState("");

  const [cancelling, setCancelling] =
    useState(false);


  useEffect(() => {
    let ignore = false;

    function handleJobUpdate(
      nextJob: SimulationJob,
    ) {
      if (ignore) {
        return;
      }

      setJob((currentJob) => {
        if (!currentJob) {
          return nextJob;
        }

        return {
          ...currentJob,
          ...nextJob,
        };
      });
    }

    function handleRequestError(
      caughtError: unknown,
    ) {
      if (ignore) {
        return;
      }

      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "載入模擬任務失敗",
      );
    }

    getSimulationJob(jobId)
      .then(handleJobUpdate)
      .catch(handleRequestError);

    const eventSource = new EventSource(
      getSimulationEventsUrl(jobId),
    );

    eventSource.addEventListener(
      "progress",
      (event) => {
        try {
          const nextJob = JSON.parse(
            (event as MessageEvent<string>).data,
          ) as SimulationJob;

          handleJobUpdate(nextJob);
        } catch {
          if (!ignore) {
            setError("無法解析任務進度資料");
          }
        }
      },
    );

    eventSource.addEventListener(
      "terminal",
      (event) => {
        try {
          const nextJob = JSON.parse(
            (event as MessageEvent<string>).data,
          ) as SimulationJob;

          handleJobUpdate(nextJob);
        } catch {
          if (!ignore) {
            setError("無法解析任務終止狀態");
          }
        } finally {
          eventSource.close();
        }
      },
    );

    eventSource.onerror = () => {
      eventSource.close();
    };

    const pollingTimer = window.setInterval(
      () => {
        getSimulationJob(jobId)
          .then(handleJobUpdate)
          .catch(handleRequestError);
      },
      5000,
    );

    return () => {
      ignore = true;
      window.clearInterval(pollingTimer);
      eventSource.close();
    };
  }, [jobId]);


  useEffect(() => {
    if (
      job?.status !== "completed"
      || result !== null
    ) {
      return;
    }

    let ignore = false;

    getSimulationResult(jobId)
      .then((nextResult) => {
        if (!ignore) {
          setResult(nextResult);
        }
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "載入模擬結果失敗",
          );
        }
      });

    return () => {
      ignore = true;
    };
  }, [job?.status, jobId, result]);


  async function handleCancel() {
    if (cancelling) {
      return;
    }

    setCancelling(true);
    setError("");

    try {
      const updatedJob =
        await cancelSimulationJob(jobId);

      setJob((currentJob) => {
        if (!currentJob) {
          return updatedJob;
        }

        return {
          ...currentJob,
          ...updatedJob,
        };
      });
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "取消模擬任務失敗",
      );
    } finally {
      setCancelling(false);
    }
  }
  
  if (!job) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="mx-auto max-w-4xl">
          {error ? (
            <div
              role="alert"
              className="rounded-xl border border-red-900 bg-red-950 p-5 text-red-300"
            >
              {error}
            </div>
          ) : (
            <p className="text-slate-400">
              正在載入模擬任務……
            </p>
          )}
        </div>
      </main>
    );
  }

  const isTerminal =
    terminalStatuses.has(job.status);

  const progress = Math.min(
    100,
    Math.max(0, job.progress),
  );


  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Simulation Job
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            模擬任務
          </h1>

          <p className="mt-2 break-all text-sm text-slate-400">
            {job.id}
          </p>
        </header>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p className="text-sm text-slate-400">
                目前階段
              </p>

              <p className="mt-1 text-xl font-semibold">
                {stageLabels[job.stage]
                  ?? job.stage}
              </p>
            </div>

            {!isTerminal && (
              <button
                type="button"
                onClick={handleCancel}
                disabled={cancelling}
                className="rounded-lg border border-red-800 px-4 py-2 text-red-300 transition hover:bg-red-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {cancelling
                  ? "正在取消……"
                  : "取消任務"}
              </button>
            )}
          </div>

          <div className="mt-6 h-3 overflow-hidden rounded-full bg-slate-800">
            <div
              className="h-full bg-cyan-400 transition-all duration-500"
              style={{
                width: `${progress}%`,
              }}
            />
          </div>

          <div className="mt-2 flex justify-between text-sm text-slate-400">
            <span>{job.status}</span>
            <span>{progress}%</span>
          </div>

          <dl className="mt-6 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
            <div>
              <dt className="text-slate-500">
                城市
              </dt>
              <dd className="mt-1">
                {job.city_id}
              </dd>
            </div>

            <div>
              <dt className="text-slate-500">
                建立時間
              </dt>
              <dd className="mt-1">
                {new Date(
                  job.created_at,
                ).toLocaleString()}
              </dd>
            </div>

            <div>
              <dt className="text-slate-500">
                開始時間
              </dt>
              <dd className="mt-1">
                {job.started_at
                  ? new Date(
                      job.started_at,
                    ).toLocaleString()
                  : "尚未開始"}
              </dd>
            </div>

            <div>
              <dt className="text-slate-500">
                完成時間
              </dt>
              <dd className="mt-1">
                {job.completed_at
                  ? new Date(
                      job.completed_at,
                    ).toLocaleString()
                  : "尚未完成"}
              </dd>
            </div>
          </dl>

          {job.error_message && (
            <div className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
              {job.error_message}
            </div>
          )}

          {error && (
            <div
              role="alert"
              className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300"
            >
              {error}
            </div>
          )}
        </section>

        {job.status === "completed"
          && !result && (
            <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6 text-slate-400">
              正在載入完整模擬結果……
            </section>
          )}

        {result && (
          <section className="mt-10 space-y-8">
            <div className="grid gap-4 md:grid-cols-3">
              <SummaryCard
                label="最終皮膚溫度改善"
                value={
                  result.summary
                    .final_skin_temperature_improvement_c
                }
              />

              <SummaryCard
                label="平均皮膚溫度改善"
                value={
                  result.summary
                    .average_skin_temperature_improvement_c
                }
              />

              <SummaryCard
                label="核心溫度改善"
                value={
                  result.summary
                    .final_core_temperature_improvement_c
                }
              />
            </div>

            <div className="rounded-xl border border-amber-800 bg-amber-950/50 p-4 text-amber-200">
              <p>{result.warning}</p>

              <p className="mt-2 text-sm">
                {result.environment_model_note}
              </p>
            </div>

            <WeatherChart
              weather={result.weather}
            />

            <TemperatureChart
              result={result}
            />

            <HeatFluxChart
              result={result}
            />
            <div className="flex flex-wrap gap-3">
              <a
                href={getSimulationExportUrl(
                  jobId,
                  "csv",
                )}
                className="rounded-lg bg-cyan-400 px-5 py-2 font-semibold text-slate-950"
              >
                導出 CSV
              </a>

              <a
                href={getSimulationExportUrl(
                  jobId,
                  "json",
                )}
                className="rounded-lg border border-slate-700 px-5 py-2"
              >
                導出 JSON
              </a>
            </div>
          </section>
        )}
      </div>
    </main>
  );
}


function SummaryCard({
  label,
  value,
}: {
  label: string;
  value: number;
}) {
  return (
    <article className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">
        {label}
      </p>

      <p className="mt-2 text-3xl font-bold text-cyan-300">
        {value.toFixed(3)}

        <span className="ml-1 text-base font-normal">
          °C
        </span>
      </p>
    </article>
  );
}

