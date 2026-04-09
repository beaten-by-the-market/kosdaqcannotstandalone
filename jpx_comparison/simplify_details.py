#!/usr/bin/env python3
"""
모든 시장조치 JSON의 Details 필드를 간결한 라벨(Simplified_Details)로 변환.

대상:
  - data/supervision_delisting/current_stocks.json
  - data/public_announcement/public_announcement.json
  - data/violation_penalties/violation_penalties.json
  - data/improvement_reports/improvement_reports.json
  - data/special_alert/current.json
  - data/grace_period/current_stocks.json
"""

import json
from pathlib import Path

DATA_DIR = Path("data")

TARGET_FILES = [
    DATA_DIR / "supervision_delisting" / "current_stocks.json",
    DATA_DIR / "public_announcement" / "public_announcement.json",
    DATA_DIR / "violation_penalties" / "violation_penalties.json",
    DATA_DIR / "improvement_reports" / "improvement_reports.json",
    DATA_DIR / "special_alert" / "current.json",
    DATA_DIR / "grace_period" / "current_stocks.json",
]


def simplify(details: str) -> str:
    """Classify verbose Details into a short label."""
    d = details.lower().strip()
    if not d:
        return ""

    # === Supervision / Delisting ===

    # Reverse Stock Split
    if "reverse stock split" in d:
        if "general shareholders meeting" in d:
            return "Reverse Stock Split (주식병합, 주총결의)"
        if "company implements" in d:
            return "Reverse Stock Split (주식병합)"
        return "Reverse Stock Split (주식병합)"

    # TOB / Special Controlling Shareholder
    if "special controlling shareholder" in d:
        return "TOB/공개매수 (특별지배주주)"

    # TOB via board resolution
    if "board of directors has made a resolution" in d:
        if "share consolidation" in d:
            return "Share Consolidation (주식병합)"
        return "TOB/공개매수 (이사회 결의)"

    # Improvement Period expiry
    if "not likely to meet the continued listing criteria within the improvement period" in d:
        return "상장유지기준 미달 (개선기간 미충족)"
    if "do not meet the continued listing criteria" in d:
        return "상장유지기준 미달 (개선기간 미충족)"
    if "did not meet the continued listing criteria" in d:
        return "상장유지기준 미달 (개선기간 미충족)"

    # Annual securities report
    if "annual securities report" in d or "securities report" in d:
        return "유가증권보고서 미제출"

    # General shareholders meeting
    if "general shareholders meeting" in d:
        if "cash-out" in d or "demand for" in d:
            return "Share Cash-Out (캐시아웃, 주총결의)"
        return "주총결의에 의한 상장폐지"

    # Cash-out
    if "cash-out" in d or "demand for a cash-out" in d:
        return "Share Cash-Out (캐시아웃)"

    # Delisting application / decision
    if "delisting application" in d:
        return "상장폐지 신청"
    if "decision on delisting" in d:
        return "상장폐지 결정"

    # === Public Announcement / Violation Penalty / Improvement Reports ===

    # False Statements (허위공시)
    if "false statements" in d or "false statement" in d:
        return "허위공시 (False Statements)"

    # Timely Disclosure Violation (적시공시 위반)
    if "violated the provisions of timely disclosure" in d:
        return "적시공시 위반 (Timely Disclosure)"

    # Audit Opinion (감사의견)
    if "disclaimer of opinion" in d or "disclaimer of conclusion" in d:
        return "감사의견 미표명/부적정"
    if "opinions are not expressed" in d:
        return "감사의견 미표명/부적정"

    # Written Oath Violation (서약서 위반)
    if "written oath" in d:
        if "application for transfer" in d or "segment transfer" in d:
            return "서약서 위반 (Market Segment Transfer)"
        if "initial listing" in d or "application for listing" in d:
            return "서약서 위반 (신규상장)"
        return "서약서 위반 (신규상장/Market Segment Transfer)"

    # Code of Corporate Conduct (기업행동규범)
    if "code of corporate conduct" in d or "matters to be observed" in d:
        if "independent outside director" in d:
            return "기업행동규범 위반 (사외이사)"
        if "mscb" in d or "moving strike" in d:
            return "MSCB 발행규정 위반"
        return "기업행동규범 위반 (Corporate Conduct)"

    # Internal management improvement
    if "internal management" in d and "improvement" in d:
        return "내부관리체계 개선 필요"

    # Improvement status report request (follow-up of false statements)
    if "improvement status report" in d:
        return "허위공시 (False Statements)"

    # Public announcement deemed necessary
    if "publicly announced" in d or "public announcement" in d:
        return "적시공시 위반 (Timely Disclosure)"

    # === Grace Period ===

    # Not substantial surviving company
    if "substantial surviving company" in d or "not a substantial surviving" in d:
        return "비존속회사 (합병 등)"

    # Grace Period history entries (Reason field)
    if "grace period" in d or "entry into" in d:
        if "liabilities in excess of assets" in d:
            return "채무초과 (Grace Period)"
        if "market capitalization" in d:
            return "시가총액 미달 (Grace Period)"
        if "number of shareholders" in d:
            return "주주수 미달 (Grace Period)"
        if "business performance" in d:
            return "사업실적 미달 (Grace Period)"
        if "recorded profit" in d:
            return "이익미계상 (Grace Period)"
        return "Grace Period 진입"

    # Examination after reconstruction plan
    if "examination of market capitalization" in d or "reconstruction plan" in d:
        return "재건계획 후 시가총액 심사"

    # Fallback
    return details[:80] + ("..." if len(details) > 80 else "")


def process_file(filepath: Path) -> dict:
    """Process a single JSON file, adding Simplified_Details."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw = json.load(f)

    data = raw.get("data", raw)
    if not isinstance(data, list):
        return {}

    label_counts = {}
    for item in data:
        # Use Details or Reason field
        original = item.get("Details") or item.get("Reason") or ""
        simplified = simplify(original)
        if simplified:
            item["Simplified_Details"] = simplified
        label_counts[simplified or "(empty)"] = label_counts.get(simplified or "(empty)", 0) + 1

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)

    return label_counts


def main():
    print("=" * 60)
    print("Simplifying Details across all market measure JSONs")
    print("=" * 60)

    for filepath in TARGET_FILES:
        if not filepath.exists():
            print(f"\n  SKIP: {filepath} not found")
            continue

        print(f"\n--- {filepath} ---")
        counts = process_file(filepath)
        for label, count in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {count:3d}  {label}")

    print("\n" + "=" * 60)
    print("Done.")
    print("=" * 60)


if __name__ == "__main__":
    main()
