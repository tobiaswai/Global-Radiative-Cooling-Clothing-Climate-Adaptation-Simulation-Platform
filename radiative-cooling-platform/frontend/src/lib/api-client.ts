import type {
  City,
  SimulationJob,
  SimulationJobDetail,
  SimulationJobList,
  SimulationRequest,
  SimulationResponse,
  WeatherSimulationRequest,
  WeatherSimulationResponse,
  WeatherTimeSeries,
} from "@/types/simulation";


const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ??
  "http://localhost:8000";


/**
 * 嘗試從後端回應中取得可讀的錯誤訊息。
 *
 * FastAPI 的 detail 可能是：
 * 1. 字串
 * 2. Pydantic 驗證錯誤陣列
 * 3. 其他 JSON 物件
 */
async function getErrorMessage(
  response: Response,
  fallbackMessage: string,
): Promise<string> {
  const errorBody: unknown = await response
    .json()
    .catch(() => null);

  if (
    typeof errorBody === "object" &&
    errorBody !== null &&
    "detail" in errorBody
  ) {
    const detail = (
      errorBody as {
        detail?: unknown;
      }
    ).detail;

    if (typeof detail === "string") {
      return detail;
    }

    if (detail !== undefined) {
      return JSON.stringify(detail);
    }
  }

  return `${fallbackMessage}：HTTP ${response.status}`;
}


/**
 * 手動環境參數模擬。
 *
 * 對應後端：
 * POST /api/v1/simulations/run
 */
export async function runSimulation(
  request: SimulationRequest,
): Promise<SimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/run`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "模擬請求失敗",
      ),
    );
  }

  return response.json() as Promise<SimulationResponse>;
}


/**
 * 取得系統目前支援的城市。
 *
 * 對應後端：
 * GET /api/v1/weather/cities
 */
export async function getCities(): Promise<City[]> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/weather/cities`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "無法取得城市列表",
      ),
    );
  }

  return response.json() as Promise<City[]>;
}


/**
 * 取得指定城市的歷史氣象資料。
 *
 * 對應後端：
 * GET /api/v1/weather/history
 */
export async function getWeatherHistory(
  cityId: string,
  startTimeLocal: string,
  durationMinutes: number,
): Promise<WeatherTimeSeries> {
  const parameters = new URLSearchParams({
    city_id: cityId,
    start_time_local: startTimeLocal,
    duration_minutes: String(durationMinutes),
  });

  const response = await fetch(
    `${API_BASE_URL}/api/v1/weather/history?${parameters.toString()}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "無法取得歷史氣象資料",
      ),
    );
  }

  return response.json() as Promise<WeatherTimeSeries>;
}


/**
 * 同步執行氣象驅動模擬。
 *
 * 主要保留給開發、測試和除錯使用。
 * 正式前端應優先使用 createSimulationJob()。
 *
 * 對應後端：
 * POST /api/v1/simulations/run-weather
 */
export async function runWeatherSimulation(
  request: WeatherSimulationRequest,
): Promise<WeatherSimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/run-weather`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "氣象模擬失敗",
      ),
    );
  }

  return response.json() as Promise<WeatherSimulationResponse>;
}


/**
 * 建立異步模擬任務。
 *
 * 對應後端：
 * POST /api/v1/simulations/jobs
 */
export async function createSimulationJob(
  request: WeatherSimulationRequest,
): Promise<SimulationJob> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "建立模擬任務失敗",
      ),
    );
  }

  return response.json() as Promise<SimulationJob>;
}


/**
 * 查詢單一模擬任務。
 *
 * 對應後端：
 * GET /api/v1/simulations/jobs/{jobId}
 */
export async function getSimulationJob(
  jobId: string,
): Promise<SimulationJobDetail> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs/${encodeURIComponent(jobId)}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "無法取得模擬任務",
      ),
    );
  }

  return response.json() as Promise<SimulationJobDetail>;
}


/**
 * 取得模擬任務列表。
 *
 * 對應後端：
 * GET /api/v1/simulations/jobs
 */
export async function getSimulationJobs(
  limit = 20,
  offset = 0,
): Promise<SimulationJobList> {
  const parameters = new URLSearchParams({
    limit: String(limit),
    offset: String(offset),
  });

  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs?${parameters.toString()}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "無法取得模擬任務列表",
      ),
    );
  }

  return response.json() as Promise<SimulationJobList>;
}


/**
 * 讀取已完成任務的完整模擬結果。
 *
 * 對應後端：
 * GET /api/v1/simulations/jobs/{jobId}/result
 */
export async function getSimulationResult(
  jobId: string,
): Promise<WeatherSimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs/${encodeURIComponent(jobId)}/result`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "無法取得模擬結果",
      ),
    );
  }

  return response.json() as Promise<WeatherSimulationResponse>;
}


/**
 * 取消排隊中或執行中的模擬任務。
 *
 * 對應後端：
 * POST /api/v1/simulations/jobs/{jobId}/cancel
 */
export async function cancelSimulationJob(
  jobId: string,
): Promise<SimulationJob> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs/${encodeURIComponent(jobId)}/cancel`,
    {
      method: "POST",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "取消模擬任務失敗",
      ),
    );
  }

  return response.json() as Promise<SimulationJob>;
}


/**
 * 產生 SSE 任務進度地址。
 *
 * 使用方式：
 *
 * const eventSource = new EventSource(
 *   getSimulationEventsUrl(jobId),
 * );
 */
export function getSimulationEventsUrl(
  jobId: string,
): string {
  return (
    `${API_BASE_URL}/api/v1/simulations/jobs/` +
    `${encodeURIComponent(jobId)}/events`
  );
}

import type {
  Material,
  MaterialCreate,
  MaterialListResponse,
} from "@/types/material";
import type {
  MaterialInput,
} from "@/types/simulation";


export async function getMaterials(
  search = "",
): Promise<MaterialListResponse> {
  const parameters = new URLSearchParams();

  if (search) {
    parameters.set("search", search);
  }

  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials?${parameters}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error("無法取得材料列表");
  }

  return response.json();
}


export async function getMaterial(
  materialId: string,
): Promise<Material> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/${materialId}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error("無法取得材料");
  }

  return response.json();
}


export async function createMaterial(
  request: MaterialCreate,
): Promise<Material> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail ?? "建立材料失敗",
    );
  }

  return response.json();
}


export async function uploadMaterialSpectrum(
  versionId: string,
  spectrumType: string,
  file: File,
) {
  const formData = new FormData();

  formData.append(
    "spectrum_type",
    spectrumType,
  );

  formData.append(
    "file",
    file,
  );

  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/versions/${versionId}/spectra`,
    {
      method: "POST",
      body: formData,
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail ?? "上傳光譜失敗",
    );
  }

  return response.json();
}


export async function getMaterialSimulationInput(
  versionId: string,
): Promise<MaterialInput> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/versions/${versionId}/simulation-input`,
  );

  if (!response.ok) {
    throw new Error(
      "無法轉換材料模擬參數",
    );
  }

  return response.json();
}


export function getSimulationExportUrl(
  jobId: string,
  format: "csv" | "json",
): string {
  return (
    `${API_BASE_URL}/api/v1/simulations/jobs/` +
    `${jobId}/export?format=${format}`
  );
}