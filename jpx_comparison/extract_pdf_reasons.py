#!/usr/bin/env python3
"""
PDF에서 Reason 텍스트를 추출하여 pdf_reasons.json 생성.

각 PDF의 "Reason" 또는 "Reason (Related Clause)" 필드 바로 뒤에 나오는
사유 텍스트를 추출한다. 괄호 안 조항 참조(Securities Listing Regulations, Rule ...)는 제외.
"""

import json
import os
import re
import sys
from datetime import date

import fitz  # pymupdf

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_BASE = os.path.join(SCRIPT_DIR, "data", "pdfs")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "data", "pdf_reasons.json")

# 추출 대상 섹션
SECTIONS = [
    "supervision_delisting",
    "public_announcement",
    "violation_penalties",
    "improvement_reports",
    "special_alert",
    "grace_period",
]


def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def extract_reason(text: str) -> str:
    """PDF 텍스트에서 첫 번째 Reason 사유 문구를 추출."""

    # 패턴: "Reason" 또는 "Reason\n(Related Clause)" 뒤에 나오는 텍스트 블록
    # PDF 텍스트는 줄바꿈이 불규칙하므로 유연하게 매칭
    patterns = [
        # "Reason\n(Related Clause)\n<text>" 또는 "Reason (Related Clause)\n<text>"
        r"Reason\s*\n?\(Related\s+Clause\)\s*\n(.+?)(?:\n\s*\((?:Securities|Enforcement|Rule))",
        # "Provision\n<text>" (public_announcement, improvement_reports 스타일)
        r"Provision\s*\n\s*Securities Listing Regulations[^\n]*\n\s*\(([^)]+)\)",
        # "Reason\n<text>" (일반)
        r"(?:^|\n)\s*Reason\s*\n(.+?)(?:\n\s*\((?:Securities|Enforcement|Rule))",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            reason = match.group(1).strip()
            # 줄바꿈을 공백으로
            reason = re.sub(r"\s*\n\s*", " ", reason)
            # 연속 공백 정리
            reason = re.sub(r"\s{2,}", " ", reason)
            if len(reason) > 20:  # 너무 짧으면 잘못 매칭된 것
                return reason

    # Fallback: "Reason" 다음 줄부터 "(Securities" 또는 번호(3.) 전까지
    match = re.search(
        r"Reason\s*(?:\n\s*\(Related\s+Clause\))?\s*\n(.+?)(?:\n\s*(?:\(Securities|\(Enforcement|\d+\.\s))",
        text,
        re.DOTALL,
    )
    if match:
        reason = match.group(1).strip()
        reason = re.sub(r"\s*\n\s*", " ", reason)
        reason = re.sub(r"\s{2,}", " ", reason)
        if len(reason) > 20:
            return reason

    # Fallback: "Details of\nReason" 블록에서 추출 (Examination 타입)
    match = re.search(
        r"Details\s+of\s*\n\s*Reason\s*\n(.+?)(?:\n\s*(?:\(Securities|\(Enforcement|\d+\.\s)|$)",
        text,
        re.DOTALL,
    )
    if match:
        reason = match.group(1).strip()
        reason = re.sub(r"\s*\n\s*", " ", reason)
        reason = re.sub(r"\s{2,}", " ", reason)
        if len(reason) > 20:
            return reason

    # Fallback: 일괄지정 문서 - "Reason" 라벨 없이 "Because..." 또는 "Due to..."가 직접 등장
    match = re.search(
        r"((?:Because|Due to)\s.+?)(?:\n\s*\((?:Securities|Enforcement|Rule))",
        text,
        re.DOTALL,
    )
    if match:
        reason = match.group(1).strip()
        reason = re.sub(r"\s*\n\s*", " ", reason)
        reason = re.sub(r"\s{2,}", " ", reason)
        if len(reason) > 20:
            return reason

    return ""


def main():
    print("Extracting reasons from PDFs...")
    print(f"Source: {PDF_BASE}")
    print(f"Output: {OUTPUT_PATH}")
    print()

    result = {}

    for section in SECTIONS:
        section_dir = os.path.join(PDF_BASE, section)
        if not os.path.exists(section_dir):
            print(f"[SKIP] {section}/ not found")
            continue

        pdf_files = sorted(f for f in os.listdir(section_dir) if f.endswith(".pdf"))
        if not pdf_files:
            continue

        section_reasons = {}
        success = 0
        fail = 0

        for filename in pdf_files:
            pdf_path = os.path.join(section_dir, filename)
            text = extract_text(pdf_path)
            reason = extract_reason(text)

            if reason:
                section_reasons[filename] = reason
                success += 1
            else:
                section_reasons[filename] = "(reason not extracted)"
                fail += 1

        result[section] = section_reasons
        print(f"  {section}: {success} extracted, {fail} failed (total {len(pdf_files)})")

    output = {
        "extracted_date": date.today().isoformat(),
        "data": result,
    }
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
