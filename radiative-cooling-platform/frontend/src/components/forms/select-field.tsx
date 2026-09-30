"use client";

type Option<T extends string> = { value: T; label: string };

type SelectFieldProps<T extends string> = {
  label: string;
  value: T;
  options: Option<T>[];
  hint?: string;
  disabled?: boolean;
  onChange: (value: T) => void;
};

export function SelectField<T extends string>({
  label,
  value,
  options,
  hint,
  disabled = false,
  onChange,
}: SelectFieldProps<T>) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm text-slate-300">{label}</span>

      <select
        value={value}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value as T)}
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>

      {hint && <span className="mt-1 block text-xs text-slate-500">{hint}</span>}
    </label>
  );
}