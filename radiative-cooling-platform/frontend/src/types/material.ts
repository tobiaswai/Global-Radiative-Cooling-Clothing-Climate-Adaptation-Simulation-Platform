export type MaterialMode =
  | "ordinary"
  | "opaque_emitter"
  | "infrared_transparent"
  | "hybrid";

export type MaterialVersionInput = {
  mode: MaterialMode;
  clothing_insulation_clo: number;
  evaporative_resistance_m2pa_w: number | null;
  solar_reflectance: number;
  solar_transmittance: number;
  infrared_emissivity: number;
  infrared_transmittance: number;
  projected_solar_area_factor: number;
  absorbed_solar_to_body_fraction: number;
  areal_density_g_m2: number | null;
  specific_heat_j_kgk: number | null;
  source_type: string;
  source_reference: string | null;
  notes: string | null;
};

export type MaterialCreate = {
  name: string;
  slug: string;
  description: string | null;
  institution: string | null;
  initial_version: MaterialVersionInput;
};

export type SpectrumSummary = {
  id: string;
  spectrum_type: string;
  wavelength_unit: string;
  point_count: number;
  minimum_wavelength_um: number;
  maximum_wavelength_um: number;
  original_filename: string;
  file_checksum_sha256: string;
  created_at: string;
};

export type MaterialVersion = MaterialVersionInput & {
  id: string;
  material_id: string;
  version_number: number;
  created_at: string;
  spectra: SpectrumSummary[];
};

export type Material = {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  institution: string | null;
  is_archived: boolean;
  created_at: string;
  updated_at: string;
  versions: MaterialVersion[];
};

export type MaterialListItem = {
  id: string;
  name: string;
  slug: string;
  institution: string | null;
  is_archived: boolean;
  latest_version_number: number | null;
  created_at: string;
};

export type MaterialListResponse = {
  items: MaterialListItem[];
  total: number;
  limit: number;
  offset: number;
};