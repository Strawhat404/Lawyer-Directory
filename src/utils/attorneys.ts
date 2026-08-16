import type { Attorney } from "../types/attorney";
import data from "../data/attorneys.json";

const attorneys: Attorney[] = data.attorneys;

export function getAllCities(): string[] {
  return [...new Set(attorneys.map((a) => a.city))].sort();
}

export function getAttorneysByCity(city: string): Attorney[] {
  return attorneys.filter((a) => a.city === city).sort((a, b) => a.name.localeCompare(b.name));
}

export function getAttorneyBySlug(slug: string): Attorney | undefined {
  return attorneys.find((a) => a.slug === slug);
}

export function getCityDisplayName(citySlug: string): string {
  const attorney = attorneys.find((a) => a.city === citySlug);
  return attorney?.cityDisplay || citySlug.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

// Alias used by pages
export const getCityName = getCityDisplayName;

export function getAttorneyCountByCity(city: string): number {
  return attorneys.filter((a) => a.city === city).length;
}

export function getAllAttorneys(): Attorney[] {
  return [...attorneys].sort((a, b) => a.name.localeCompare(b.name));
}

export function getTotalAttorneyCount(): number {
  return attorneys.length;
}
