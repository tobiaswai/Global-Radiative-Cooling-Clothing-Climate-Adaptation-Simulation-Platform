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
        "Simulation request failed",
      ),
    );
  }

  return response.json() as Promise<SimulationResponse>;
}


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
        "Failed to fetch city list",
      ),
    );
  }

  return response.json() as Promise<City[]>;
}


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
        "Failed to fetch weather history",
      ),
    );
  }

  return response.json() as Promise<WeatherTimeSeries>;
}

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
        "Weather simulation failed",
      ),
    );
  }

  return response.json() as Promise<WeatherSimulationResponse>;
}


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
        "Failed to create simulation job",
      ),
    );
  }

  return response.json() as Promise<SimulationJob>;
}

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
        "Failed to fetch simulation job",
      ),
    );
  }

  return response.json() as Promise<SimulationJobDetail>;
}



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
        "Failed to fetch simulation job list",
      ),
    );
  }

  return response.json() as Promise<SimulationJobList>;
}


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
        "Failed to fetch simulation result",
      ),
    );
  }

  return response.json() as Promise<WeatherSimulationResponse>;
}


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
        "Failed to cancel simulation job",
      ),
    );
  }

  return response.json() as Promise<SimulationJob>;
}


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
    throw new Error("Failed to fetch material list");
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
    throw new Error("Failed to fetch material");
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
      body?.detail ?? "Failed to create material",
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
      body?.detail ?? "Failed to upload spectrum",
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
      "Failed to fetch material simulation input",
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

import type {
  GeoJsonFeatureCollection,
  GlobalBatch,
  GlobalBatchCreate,
  GlobalBatchDetail,
  GlobalCity,
} from "@/types/global-batch";

export async function getGlobalCities(): Promise<
  GlobalCity[]
> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/cities`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      "Unable to load supported cities",
    );
  }

  const body = await response.json();

  return body.items;
}


export async function createGlobalBatch(
  request: GlobalBatchCreate,
): Promise<GlobalBatch> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches`,
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
      body?.detail
      ?? "Unable to create global batch",
    );
  }

  return response.json();
}


export async function getGlobalBatch(
  batchId: string,
): Promise<GlobalBatchDetail> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      "Unable to load global batch",
    );
  }

  return response.json();
}


export async function getGlobalBatchGeoJson(
  batchId: string,
): Promise<GeoJsonFeatureCollection> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}/geojson`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      "Unable to load global map data",
    );
  }

  return response.json();
}


export async function cancelGlobalBatch(
  batchId: string,
): Promise<GlobalBatch> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}/cancel`,
    {
      method: "POST",
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail
      ?? "Unable to cancel global batch",
    );
  }

  return response.json();
}