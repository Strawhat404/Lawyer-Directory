#!/usr/bin/env python3
"""
Personal Injury Attorney Directory - Data Import Script

Reads multiple Excel files (.xlsx) with attorney data and converts them
into a structured JSON file used by the Astro static site generator.

Usage:
    python3 scripts/import.py

Input:  Multiple XLSX files in project root (Miami Area Data.xlsx, etc.)
Output: src/data/attorneys.json
"""

import json
import re
import sys
from datetime import date
from pathlib import Path
from glob import glob

import openpyxl

OUTPUT_FILE = Path("src") / "data" / "attorneys.json"

# XLSX files to process
XLSX_PATTERN = "*.xlsx"

STATE_ABBREV_TO_SLUG = {
    "FL": "florida",
    "NJ": "new-jersey",
    "NY": "new-york",
    "CA": "california",
    "TX": "texas",
    "GA": "georgia",
    "PA": "pennsylvania",
    "IL": "illinois",
    "OH": "ohio",
    "NC": "north-carolina",
}


def slugify(text):
    """Convert any text to a URL-friendly lowercase slug."""
    if not text:
        return ""
    text = text.lower().strip()
    # Remove credentials in parentheses, e.g., "John Smith, Esq." -> "john smith"
    text = re.sub(r'\s*,\s*(esq|jr|sr|ii|iii)\.?\s*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-_\s]+", "-", text)
    return text.strip("-")


def normalize_phone(phone):
    """Clean and standardize phone numbers."""
    if not phone:
        return ""
    phone = str(phone).strip()
    # Remove leading country codes like "1-" or "1 "
    phone = re.sub(r"^1[-.\s]", "", phone)
    # Standardize dash spacing
    phone = re.sub(r"\s*-\s*", "-", phone)
    return phone


# Known city name variants that should be merged into one canonical name.
# Keys are matched case-insensitively after whitespace/punctuation normalization.
CITY_ALIASES = {
    "ft lauderdale": "Fort Lauderdale",
    "ft. lauderdale": "Fort Lauderdale",
    "ft myers": "Fort Myers",
    "ft. myers": "Fort Myers",
    "ft pierce": "Fort Pierce",
    "ft. pierce": "Fort Pierce",
    "ft walton beach": "Fort Walton Beach",
    "ft. walton beach": "Fort Walton Beach",
}


def normalize_city_name(city):
    """
    Normalize a raw city string so that variants like "Ft Lauderdale",
    "Ft. Lauderdale", and "FORT LAUDERDALE" all collapse to a single
    canonical form ("Fort Lauderdale"), preventing duplicate city pages.
    """
    if not city:
        return city

    # Collapse whitespace
    city = re.sub(r"\s+", " ", city.strip())

    # Check alias table first (case-insensitive, normalize trailing periods)
    lookup_key = city.lower().rstrip(".")
    # Also try with a period after "ft" since alias keys include both forms
    for key, canonical in CITY_ALIASES.items():
        if lookup_key == key.rstrip("."):
            return canonical

    # Title-case if the string is fully upper/lower (e.g. "FORT LAUDERDALE")
    if city.isupper() or city.islower():
        city = city.title()

    return city


def parse_address(address):
    """Extract city, state from address string."""
    if not address:
        return "", "FL"
    
    address_clean = re.sub(r'\s+', ' ', address.strip())
    
    # Pattern 1: "..., City, ST ZIPCODE" (comma before city)
    match = re.search(r',\s*([A-Za-z][^,]+?),\s*([A-Z]{2})\s+\d{5}', address_clean)
    if match:
        city = normalize_city_name(match.group(1).strip())
        state = match.group(2).strip()
        return city, state

    # Pattern 2: "... CityName, ST ZIPCODE" or "... CityName, New Jersey ZIPCODE"
    # Handles cases like "48 South Street Morristown, NJ 07960"
    # or "48 South Street Morristown, New Jersey 07960"
    match = re.search(r'\s([A-Z][a-zA-Z\s]+(?:Township|Borough|City)?),\s*(NJ|FL|NY|CA|TX|New\s+Jersey|New\s+York|Florida)\s+\d{5}', address_clean)
    if match:
        city = normalize_city_name(match.group(1).strip())
        raw_state = match.group(2).strip()
        # Normalize full state names to abbreviations
        state_map = {
            "New Jersey": "NJ", "New York": "NY", "Florida": "FL",
            "California": "CA", "Texas": "TX"
        }
        state = state_map.get(raw_state, raw_state)
        return city, state

    # Pattern 3: No comma — "123 Street CityName ST ZIPCODE"
    # e.g. "601 Longwood Ave Cherry Hill NJ 08002"
    match = re.search(r'\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)\s+([A-Z]{2})\s+\d{5}\s*$', address_clean)
    if match:
        city = normalize_city_name(match.group(1).strip())
        state = match.group(2).strip()
        return city, state

    return "", "FL"



def parse_attorney_row(row: dict, index: int, source_file: str) -> dict | None:
    """
    Parse a single row from the xlsx into an attorney dictionary.
    Returns None if the row should be skipped (missing critical data).
    """
    name = (row.get("Full Name") or "").strip()
    nickname = (row.get("Nickname") or "").strip()
    bar_number = str(row.get("Bar Number") or "").strip()
    status = (row.get("Status") or "").strip()
    firm = (row.get("Firm") or "").strip()
    address = (row.get("Address") or "").strip()
    office_phone = normalize_phone(row.get("Office Phone") or "")
    other_phones = (row.get("Other Phones") or "").strip()
    email = (row.get("Email") or "").strip().lower()

    # Validate — skip rows without name
    if not name:
        return None

    # Parse city from address
    city, state_code = parse_address(address)
    
    # If no city parsed, try to infer from source file name
    if not city and source_file:
        filename_match = re.match(r'([^/]+?)\s+Area\s+Data', source_file)
        if filename_match:
            city = filename_match.group(1)
    
    if not city:
        city = "Unknown"

    # Determine state slug
    state_slug = STATE_ABBREV_TO_SLUG.get(state_code, slugify(state_code) if state_code else "unknown")

    # Skip if we couldn't determine state or city
    if state_slug == "unknown" or city == "Unknown":
        return None

    city_slug = slugify(city)

    # Generate description
    state_display = state_code if state_code else "USA"
    description = f"Personal injury attorney at {firm}" if firm else f"Personal injury attorney in {city}, {state_display}"

    # Slug from name — make unique with index if needed
    attorney_slug = slugify(name)
    if not attorney_slug:
        attorney_slug = f"attorney-{index + 1}"

    return {
        "id": index + 1,
        "name": name,
        "nickname": nickname,
        "barNumber": bar_number,
        "status": status,
        "firm": firm,
        "state": state_slug,
        "stateCode": state_code,
        "city": city_slug,
        "cityDisplay": city,
        "address": address,
        "phone": office_phone,
        "otherPhones": other_phones,
        "email": email,
        "description": description,
        "slug": attorney_slug,
    }


def process_xlsx_file(file_path: Path, start_index: int):
    """Process a single XLSX file and return list of attorneys."""
    print(f"\nProcessing {file_path.name}...")
    
    wb = openpyxl.load_workbook(file_path, read_only=True)
    ws = wb.active

    # Find header row (it's in row 2 based on our earlier investigation)
    headers = None
    for i in range(1, 6):  # Check first 5 rows
        row_values = [cell.value for cell in ws[i]]
        if 'Full Name' in row_values:
            headers = row_values
            header_row = i
            break
    
    if not headers:
        print(f"  Warning: No headers found in {file_path.name}, skipping")
        wb.close()
        return [], 0

    # Read all data rows after header
    raw_rows = list(ws.iter_rows(min_row=header_row + 1, values_only=True))
    total_raw = len(raw_rows)

    # Parse each row
    attorneys = []
    skipped = 0
    for i, row_data in enumerate(raw_rows):
        row_dict = dict(zip(headers, row_data))
        parsed = parse_attorney_row(row_dict, start_index + i, file_path.name)
        if parsed:
            attorneys.append(parsed)
        else:
            skipped += 1

    wb.close()
    
    print(f"  Found {len(attorneys)} attorneys (skipped {skipped})")
    return attorneys, total_raw


def main():
    # Find all XLSX files matching pattern
    xlsx_files = glob(XLSX_PATTERN)
    
    if not xlsx_files:
        print(f"Error: No XLSX files found matching pattern '{XLSX_PATTERN}'")
        print("Expected files like: 'Miami Area Data.xlsx', 'Tampa Area Data.xlsx', etc.")
        sys.exit(1)

    print(f"Found {len(xlsx_files)} XLSX files to process")

    all_attorneys = []
    total_raw_count = 0
    
    # Process each file
    for file_path in sorted(xlsx_files):
        attorneys, raw_count = process_xlsx_file(Path(file_path), len(all_attorneys))
        all_attorneys.extend(attorneys)
        total_raw_count += raw_count

    if not all_attorneys:
        print("\nError: No valid attorneys found after filtering.")
        sys.exit(1)

    # Deduplicate slugs
    seen_slugs = {}
    for attorney in all_attorneys:
        slug = attorney["slug"]
        if slug in seen_slugs:
            seen_slugs[slug] += 1
            attorney["slug"] = f"{slug}-{seen_slugs[slug]}"
        else:
            seen_slugs[slug] = 0

    # Gather metadata
    cities = sorted(set(a["city"] for a in all_attorneys if a["city"]))
    states = sorted(set(a["state"] for a in all_attorneys if a["state"]))
    
    data = {
        "attorneys": all_attorneys,
        "metadata": {
            "total": len(all_attorneys),
            "totalRaw": total_raw_count,
            "skipped": total_raw_count - len(all_attorneys),
            "lastUpdated": date.today().isoformat(),
            "cities": cities,
            "states": states,
            "filesProcessed": len(xlsx_files),
        },
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Imported {len(all_attorneys)} attorneys from {len(xlsx_files)} files")
    print(f"   Raw rows: {total_raw_count} | Skipped: {data['metadata']['skipped']} | Kept: {len(all_attorneys)}")
    print(f"   States: {', '.join(states)}")
    print(f"   Cities: {len(cities)}")
    print(f"   Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
