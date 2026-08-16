#!/usr/bin/env node
/**
 * Avatar Generator Script
 * 
 * Generates SVG avatars for all attorneys based on their names.
 * Each avatar displays the attorney's initials on a colored background.
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ATTORNEYS_JSON = join(__dirname, '../src/data/attorneys.json');
const AVATARS_DIR = join(__dirname, '../public/avatars');

// Ensure avatars directory exists
if (!existsSync(AVATARS_DIR)) {
  mkdirSync(AVATARS_DIR, { recursive: true });
}

// Read attorneys data
const data = JSON.parse(readFileSync(ATTORNEYS_JSON, 'utf-8'));
const attorneys = data.attorneys;

/**
 * Generate a deterministic color from a string
 */
function stringToColor(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }
  
  // Generate HSL color with good contrast
  const hue = hash % 360;
  const saturation = 65 + (hash % 20); // 65-85%
  const lightness = 40 + (hash % 15); // 40-55% (darker for better contrast with white text)
  
  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}

/**
 * Get initials from full name
 */
function getInitials(name) {
  const parts = name.trim().split(/\s+/);
  if (parts.length === 1) {
    return parts[0].substring(0, 2).toUpperCase();
  }
  // Take first letter of first name and first letter of last name
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
}

/**
 * Generate SVG avatar
 */
function generateAvatar(name, slug) {
  const initials = getInitials(name);
  const bgColor = stringToColor(name);
  
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <rect width="200" height="200" fill="${bgColor}"/>
  <text x="50%" y="50%" text-anchor="middle" dy=".35em" fill="white" font-family="Arial, sans-serif" font-size="80" font-weight="600">${initials}</text>
</svg>`;
  
  return svg;
}

// Generate avatars for all attorneys
let count = 0;
for (const attorney of attorneys) {
  const svg = generateAvatar(attorney.name, attorney.slug);
  const filename = `${attorney.slug}.svg`;
  const filepath = join(AVATARS_DIR, filename);
  writeFileSync(filepath, svg, 'utf-8');
  count++;
}

console.log(`✓ Generated ${count} SVG avatars in ${AVATARS_DIR}`);
