# JPX Comparison Project — 출처 문서

## 폴더 구조와 출처 매핑

### 핵심 규칙
`pdfs/` 하위 폴더명은 JPX 영문 Market Alerts URL 경로와 **1:1 대응**합니다:
```
pdfs/{folder-name}/  →  https://www.jpx.co.jp/english/listing/market-alerts/{folder-name}/
```
> 상세 매핑 및 파일명 규칙은 [pdfs/SOURCES.md](pdfs/SOURCES.md) 참조

---

## 1차 출처 (JPX 웹사이트에서 직접 수집)

### PDF 자료 — `pdfs/`

| 폴더 | JPX 페이지 | 건수 | 수집일 |
|---|---|---|---|
| `pdfs/jpx_official/` | 개별 출처 (아래 참조) | 3 | 2026-03 |
| `pdfs/improvement_period/` | [Market Alerts > Improvement Period](https://www.jpx.co.jp/english/listing/market-alerts/improvement-period/index.html) | 1 (xlsx) | 2026-03-18 |
| `pdfs/improvement_reports/` | [Market Alerts > Improvement Reports](https://www.jpx.co.jp/english/listing/market-alerts/improvement-reports/index.html) | 23 | 2026-03-23 |
| `pdfs/violation_penalties/` | [Market Alerts > Violation Penalties](https://www.jpx.co.jp/english/listing/market-alerts/violation-penalties/index.html) | 18 | 2026-03-23 |
| `pdfs/public_announcement/` | [Market Alerts > Public Announcement](https://www.jpx.co.jp/english/listing/market-alerts/public-announcement/index.html) | 17 | 2026-03-23 |
| `pdfs/supervision_delisting/` | [Market Alerts > Supervision/Delisting](https://www.jpx.co.jp/english/listing/market-alerts/supervision/index.html) | 46 | 2026-03-23 |
| `pdfs/special_alert/` | [Market Alerts > Special Alert](https://www.jpx.co.jp/english/listing/market-alerts/special-alert/index.html) | 9 | 2026-03-23 |
| `pdfs/grace_period/` | [Market Alerts > Grace Period](https://www.jpx.co.jp/english/listing/market-alerts/grace-period/index.html) | 3 | 2026-03-23 |

### JPX 공식 보고서 — `pdfs/jpx_official/`

| 파일 | 출처 | 설명 |
|---|---|---|
| `E_20250130_1.pdf` | JPX 독립이사 조사위원회 (2025.01.30 공표) | 내부자거래 사건 조사보고서 |
| `E_20250130_2.pdf` | JPX 독립이사 조사위원회 (2025.01.30 공표) | 조사보고서 별첨 자료 |
| `JPX-R_Annual_Report_2025_E.pdf` | [JPX-R 소개 페이지](https://www.jpx.co.jp/english/regulation/outline/about/index.html) | JPX-R 연차보고서 2025 (FY2024) |

### 구조화 데이터 — `data/`

**1차 수집 (JPX 웹테이블에서 직접 수집)**

| 파일 | 출처 | 설명 |
|---|---|---|
| `data/current_improvement_period.csv` | [Improvement Period 페이지](https://www.jpx.co.jp/english/listing/market-alerts/improvement-period/index.html) 웹테이블 | 현재 개선기간 중인 종목 |
| `data/current_supervision_delisting.csv` | [Supervision/Delisting 페이지](https://www.jpx.co.jp/english/listing/market-alerts/supervision/index.html) 웹테이블 | 현재 감리종목/상장폐지 |
| `data/current_special_alert.csv` | [Special Alert 페이지](https://www.jpx.co.jp/english/listing/market-alerts/special-alert/index.html) 웹테이블 | 현재 특별경고 종목 |
| `data/current_grace_period.csv` | [Grace Period 페이지](https://www.jpx.co.jp/english/listing/market-alerts/grace-period/index.html) 웹테이블 | 현재 유예기간 종목 |
| `data/history_improvement_reports.csv` | [Improvement Reports 페이지](https://www.jpx.co.jp/english/listing/market-alerts/improvement-reports/index.html) 웹테이블 | 개선보고서 이력 |
| `data/history_violation_penalties.csv` | [Violation Penalties 페이지](https://www.jpx.co.jp/english/listing/market-alerts/violation-penalties/index.html) 웹테이블 | 위약금 부과 이력 |
| `data/history_public_announcement.csv` | [Public Announcement 페이지](https://www.jpx.co.jp/english/listing/market-alerts/public-announcement/index.html) 웹테이블 | 공표조치 이력 |
| `data/tdnet_disclosure_links.json` | [TDnet](https://www.release.tdnet.info/) | 감리종목 관련 적시공시 링크 |

**2차 가공**

| 파일 | 원본 소스 | 설명 |
|---|---|---|
| `data/JPX_Consolidated_Report_v3.csv` | 위 CSV 파일 전체 + xlsx 통합 | 228건 통합 데이터 + 분류 컬럼(Reason Category, Decision Authority 등) 추가 |
| `data/pdf_reasons.json` | 개별 PDF에서 추출 | 각 조치 PDF의 사유(Reason) 텍스트 |

---

## 2차 자료 (분석 보고서)

| 파일 | 원본 소스 | 설명 |
|---|---|---|
| `JPX_Market_Measures_Report.html` | data/ + pdfs/ + E_20250130_1.pdf | 시장조치 종합 분석 보고서 |
| `JPX_Market_Measures_Report.md` | 위 HTML의 마크다운 버전 | |
| `JPX_JPX-R_TSE_조직및역할분석.html` | pdfs/jpx_official/ + Securities Listing Regulations | 조직/역할 분담 분석 보고서 |
| `JPX_JPX-R_TSE_조직및역할분석.md` | 위 HTML의 마크다운 버전 | |
| `JPX_JPX-R_TSE_조직및역할분석.docx` | 위 HTML의 Word 버전 | |
| `JPX_상장관리기준_상세.xlsx` | Securities Listing Regulations 규정 기반 정리 | 상장유지기준 상세 |

### 참고 규정

| 규정 | URL |
|---|---|
| Securities Listing Regulations (2025.12.8) | [JPX Rules & Regulations](https://www.jpx.co.jp/english/rules-participants/rules/regulations/index.html) |

### 참고 웹사이트 (분석 보고서 작성 시 참조)

- JPX-R 개요: https://www.jpx.co.jp/english/regulation/outline/about/index.html
- 상장회사 컴플라이언스: https://www.jpx.co.jp/english/regulation/listing/compliance/index.html
- 상장심사: https://www.jpx.co.jp/english/regulation/listing/eligibility/index.html
- 거래참가자 검사: https://www.jpx.co.jp/english/regulation/maintaining/outline/index.html
