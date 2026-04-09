# JPX Comparison Project — 출처 문서

## 폴더 구조와 출처 매핑

### 핵심 규칙
`data/pdfs/` 하위 폴더명은 JPX 영문 Market Alerts URL 경로와 **1:1 대응**합니다:
```
data/pdfs/{folder-name}/  →  https://www.jpx.co.jp/english/listing/.../{folder-name}/
```
> 자동 수집 스크립트: `scrape_jpx_market_alerts.py` (PDF/xlsx 다운로드 + CSV/JSON 생성)

---

## 1차 출처 (JPX 웹사이트에서 직접 수집)

### PDF/xlsx 자료 — `data/pdfs/`

| 폴더 | JPX 페이지 | 수집 스크립트 |
|---|---|---|
| `data/pdfs/supervision_delisting/` | [Market Alerts > Supervision/Delisting](https://www.jpx.co.jp/english/listing/market-alerts/supervision/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/improvement_period/` | [Market Alerts > Improvement Period](https://www.jpx.co.jp/english/listing/market-alerts/improvement-period/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/grace_period/` | [Market Alerts > Grace Period](https://www.jpx.co.jp/english/listing/market-alerts/grace-period/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/public_announcement/` | [Measures > Public Announcement](https://www.jpx.co.jp/english/listing/measures/public-announce/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/violation_penalties/` | [Measures > Violation Penalties](https://www.jpx.co.jp/english/listing/measures/listing-agreement-violation/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/improvement_reports/` | [Measures > Improvement Reports](https://www.jpx.co.jp/english/listing/measures/improvement-reports/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/special_alert/` | [Measures > Special Alert](https://www.jpx.co.jp/english/listing/measures/alert/index.html) | `scrape_jpx_market_alerts.py` |
| `data/pdfs/jpx_official/` | 개별 출처 (아래 참조) | 수동 수집 |

### JPX 공식 보고서 — `data/pdfs/jpx_official/`

| 파일 | 출처 | 설명 |
|---|---|---|
| `E_20250130_1.pdf` | JPX 독립이사 조사위원회 (2025.01.30 공표) | 내부자거래 사건 조사보고서 |
| `E_20250130_2.pdf` | JPX 독립이사 조사위원회 (2025.01.30 공표) | 조사보고서 별첨 자료 |
| `JPX-R_Annual_Report_2025_E.pdf` | [JPX-R 소개 페이지](https://www.jpx.co.jp/english/regulation/outline/about/index.html) | JPX-R 연차보고서 2025 (FY2024) |

### JPX 규정 — `JPX_rules/`

| 폴더 | JPX 페이지 | 수집 스크립트 |
|---|---|---|
| `JPX_rules/TSE_Listing_Regulations/` | [TSE > Securities Listing Regulations](https://www.jpx.co.jp/english/rules-participants/rules/regulations/index.html) | `download_jpx_regulations.py` |
| `JPX_rules/JPX-R/` | [JPX-R Regulations](https://www.jpx.co.jp/english/rules-participants/rules/regulations/02.html) | `download_jpx_regulations.py` |

### 구조화 데이터 — `data/`

**자동 수집 (`scrape_jpx_market_alerts.py`로 생성, history는 전체 연도 archive 포함)**

각 JSON 항목에는 PDF가 있는 경우 다음 필드가 포함됩니다:
- `Details`: PDF에서 추출한 Reason 사유 텍스트
- `Simplified_Details`: Details를 간결한 라벨로 변환 (`simplify_details.py`)
- `Refined_Details`: PDF 테이블에서 추출한 구체적 위반 기준 (`enrich_supervision_details.py`, pdfplumber)
- `File_Path`: 로컬 PDF 상대경로 (GitHub 링크 연결용)
- `File_URL`: JPX 원본 PDF URL
- `fetched_date`: 데이터 수집일자 (JSON 최상위)

| 폴더 | 출처 | 파일 |
|---|---|---|
| `data/supervision_delisting/` | [Supervision/Delisting](https://www.jpx.co.jp/english/listing/market-alerts/supervision/index.html) | `current_stocks`, `current_others`, `history_stocks`, `history_others` (.json) |
| `data/improvement_period/` | [Improvement Period](https://www.jpx.co.jp/english/listing/market-alerts/improvement-period/index.html) | `companies_improvement_period`, `companies_transitional_measures` (.json) |
| `data/grace_period/` | [Grace Period](https://www.jpx.co.jp/english/listing/market-alerts/grace-period/index.html) | `current_stocks`, `history_stocks`, `current_others`, `history_others` (.json) |
| `data/public_announcement/` | [Public Announcement](https://www.jpx.co.jp/english/listing/measures/public-announce/index.html) | `public_announcement` (.json) |
| `data/violation_penalties/` | [Violation Penalties](https://www.jpx.co.jp/english/listing/measures/listing-agreement-violation/index.html) | `violation_penalties` (.json) |
| `data/improvement_reports/` | [Improvement Reports](https://www.jpx.co.jp/english/listing/measures/improvement-reports/index.html) | `improvement_reports` (.json) |
| `data/special_alert/` | [Special Alert](https://www.jpx.co.jp/english/listing/measures/alert/index.html) | `current`, `history` (.json) |

**가공 데이터**

| 파일 | 원본 소스 | 설명 |
|---|---|---|
| `data/pdf_reasons.json` | `data/pdfs/` 내 PDF에서 추출 (`extract_pdf_reasons.py`) | 각 조치 PDF의 사유(Reason) 텍스트 |
| `data/JPX_Consolidated_Report_v3.csv` | 위 JSON 전체 + pdf_reasons.json 통합 | 전체 통합 데이터 + 분류 컬럼 (LLM 분류) |

**후처리 스크립트 (supervision_delisting 데이터 보강)**

| 스크립트 | 입력 | 출력 | 설명 |
|---|---|---|---|
| `enrich_supervision_details.py` | `current_stocks.json` + PDF | `current_stocks.json`에 `Refined_Details` 추가 | pdfplumber로 PDF 테이블의 ● 마크 위치에서 위반 기준 추출 |
| `simplify_details.py` | `current_stocks.json` | `current_stocks.json`에 `Simplified_Details` 추가 | 장문의 Details를 간결한 한글/영문 라벨로 분류 |

**2차 가공** — 위 "가공 데이터" 항목 참조

---

## 2차 자료 (분석 보고서)

| 파일 | 원본 소스 | 설명 |
|---|---|---|
| `JPX_Market_Measures_Report.html` | data/ + data/pdfs/ + E_20250130_1.pdf | 시장조치 종합 분석 보고서 |
| `JPX_JPX-R_TSE_조직및역할분석.html` | data/pdfs/jpx_official/ + Securities Listing Regulations | 조직/역할 분담 분석 보고서 |

### 참고 규정

| 규정 | URL |
|---|---|
| Securities Listing Regulations (2025.12.8) | [JPX Rules & Regulations](https://www.jpx.co.jp/english/rules-participants/rules/regulations/index.html) |

### 참고 웹사이트 (분석 보고서 작성 시 참조)

- JPX-R 개요: https://www.jpx.co.jp/english/regulation/outline/about/index.html
- 상장회사 컴플라이언스: https://www.jpx.co.jp/english/regulation/listing/compliance/index.html
- 상장심사: https://www.jpx.co.jp/english/regulation/listing/eligibility/index.html
- 거래참가자 검사: https://www.jpx.co.jp/english/regulation/maintaining/outline/index.html
