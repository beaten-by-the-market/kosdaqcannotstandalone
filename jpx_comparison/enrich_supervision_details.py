#!/usr/bin/env python3
"""
supervision_delisting PDF에서 위반 기준 ● 마크를 추출하여
current_stocks.json의 'not likely to meet' 항목에 Refined_Details를 추가.

pdfplumber를 사용하여 테이블을 구조적으로 파싱.
"""

import json
import pdfplumber
from pathlib import Path

DATA_DIR = Path("data")
SD_JSON = DATA_DIR / "supervision_delisting" / "current_stocks.json"
PDF_DIR = DATA_DIR / "pdfs" / "supervision_delisting"

# Expected column headers (normalized)
CRITERIA_HEADERS = [
    "Number of Shareholders",
    "Number of Tradable Shares",
    "Tradable Share Ratio",
    "Tradable Share Market Capitalization",
]


def normalize_header(h):
    """Normalize header text by removing newlines and extra spaces."""
    if not h:
        return ""
    return " ".join(h.replace("\n", " ").split()).strip()


def find_criteria_columns(header_rows):
    """
    From header rows, find which column indices map to which criteria.
    Returns {col_index: criteria_name}
    """
    col_map = {}
    for row in header_rows:
        for i, cell in enumerate(row):
            if not cell:
                continue
            normed = normalize_header(cell)
            if "Shareholders" in normed:
                col_map[i] = "Number of Shareholders"
            elif "Tradable" in normed and "Shares" in normed and "Ratio" not in normed and "Market" not in normed:
                col_map[i] = "Number of Tradable Shares"
            elif "Share Ratio" in normed:
                col_map[i] = "Tradable Share Ratio"
            elif "Capitalization" in normed or "Market" in normed and "Tradable" in normed:
                col_map[i] = "Tradable Share Market Capitalization"
    return col_map


def is_bullet(cell):
    """Check if a cell contains a bullet mark (●)."""
    if not cell:
        return False
    stripped = cell.strip()
    return stripped in ("●", "○", "\ufffd\ufffd", "��", "\uf0b7", "・")


def process_pdf(pdf_path):
    """Process a single PDF and return {code: [violated_criteria]}."""
    results = {}
    try:
        pdf = pdfplumber.open(pdf_path)
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if not table or len(table) < 3:
                    continue

                # Find header rows (first 2 rows typically)
                col_map = find_criteria_columns(table[:2])
                if not col_map:
                    continue

                # Find Code column index
                code_col = None
                for i, cell in enumerate(table[0]):
                    if cell and "Code" in cell:
                        code_col = i
                        break
                if code_col is None:
                    code_col = 1  # default

                # Process data rows
                for row in table[2:]:
                    if not row or len(row) <= code_col:
                        continue

                    code = (row[code_col] or "").strip()
                    if not code or len(code) < 3:
                        continue

                    violated = []
                    for col_idx, criteria_name in col_map.items():
                        if col_idx < len(row) and is_bullet(row[col_idx]):
                            violated.append(criteria_name)

                    if violated:
                        results[code] = violated

        pdf.close()
    except Exception as e:
        print(f"  ERROR: {pdf_path.name}: {e}")

    return results


def extract_criteria_from_text(pdf_path):
    """
    Fallback: extract criteria from PDF body text for single-company PDFs
    that don't have a table structure.
    """
    try:
        pdf = pdfplumber.open(pdf_path)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        pdf.close()

        criteria = []
        text_lower = text.lower()
        # Look for "criteria (xxx)" pattern which is the most reliable
        import re
        # Clean text: remove "Reason" artifacts from PDF layout, normalize whitespace
        clean_text = re.sub(r'\breason\b', '', text_lower)
        clean_text = ' '.join(clean_text.split())
        criteria_match = re.search(r'listing criteria\s*\(([^)]+)\)', clean_text)
        if criteria_match:
            found = criteria_match.group(1).strip()
            if "tradable share market capitalization" in found:
                criteria.append("Tradable Share Market Capitalization")
            elif "market capitalization" in found:
                criteria.append("Market Capitalization")
            if "tradable share ratio" in found:
                criteria.append("Tradable Share Ratio")
            if "number of shareholders" in found or "shareholders" in found:
                criteria.append("Number of Shareholders")
            if "number of tradable shares" in found:
                criteria.append("Number of Tradable Shares")
        if not criteria:
            # Broader fallback
            if "tradable share market capitalization" in text_lower:
                criteria.append("Tradable Share Market Capitalization")
            elif "market capitalization" in text_lower:
                criteria.append("Market Capitalization")
            if "tradable share ratio" in text_lower:
                criteria.append("Tradable Share Ratio")
            if "number of shareholders" in text_lower:
                criteria.append("Number of Shareholders")
            if "number of tradable shares" in text_lower:
                criteria.append("Number of Tradable Shares")

        return criteria
    except Exception as e:
        print(f"  TEXT FALLBACK ERROR: {pdf_path.name}: {e}")
        return []


def main():
    print("=" * 60)
    print("Enriching supervision_delisting with Refined_Details")
    print("(using pdfplumber)")
    print("=" * 60)

    # Load JSON
    with open(SD_JSON, "r", encoding="utf-8") as f:
        sd_json = json.load(f)

    data = sd_json.get("data", sd_json)

    # Find entries that need enrichment
    targets = [
        d for d in data
        if d.get("Details", "").find("not likely to meet") >= 0
    ]
    print(f"\nTargets (Improvement Period expiry): {len(targets)}")

    # Clear existing Refined_Details to re-process
    for d in data:
        if "Refined_Details" in d:
            del d["Refined_Details"]

    # Collect unique PDFs
    pdf_paths = {}
    for d in targets:
        fp = d.get("File_Path", "")
        if fp:
            pdf_paths[fp] = pdf_paths.get(fp, [])
            pdf_paths[fp].append(d["Code"])

    print(f"Unique PDFs to process: {len(pdf_paths)}\n")

    # Process each PDF
    all_results = {}
    for fp in sorted(pdf_paths.keys()):
        full_path = Path(fp)
        if not full_path.exists():
            full_path = PDF_DIR / Path(fp).name
        if not full_path.exists():
            print(f"  SKIP: {fp} not found")
            continue

        print(f"Processing: {full_path.name}")
        results = process_pdf(full_path)

        if not results:
            # Fallback: try text extraction for single-company PDFs
            print(f"  No table found, trying text fallback...")
            for code in pdf_paths[fp]:
                criteria = extract_criteria_from_text(full_path)
                if criteria:
                    results[code] = criteria
                    print(f"  Text fallback: {code} -> {criteria}")

        print(f"  Found {len(results)} companies with criteria")
        all_results.update(results)

    print(f"\nTotal companies matched: {len(all_results)}")

    # Enrich JSON
    enriched = 0
    for d in data:
        code = d.get("Code", "")
        if code in all_results:
            d["Refined_Details"] = all_results[code]
            enriched += 1
            print(f"  {code} {d.get('Issue Name','')}: {all_results[code]}")

    # Check for missed targets
    missed = [d for d in targets if "Refined_Details" not in d]
    if missed:
        print(f"\nMissed {len(missed)} entries:")
        for d in missed:
            print(f"  {d['Code']} {d.get('Issue Name','')}")

    print(f"\nEnriched {enriched}/{len(targets)} entries")

    # Save
    with open(SD_JSON, "w", encoding="utf-8") as f:
        json.dump(sd_json, f, ensure_ascii=False, indent=2)

    print(f"Saved to {SD_JSON}")
    print("=" * 60)


if __name__ == "__main__":
    main()
