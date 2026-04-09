# 프로젝트 구조 — 데이터/PDF 관계도

```
jpx_comparison/
│
├─ 스크립트 ─────────────────────────────────────────────────
│  ├─ scrape_jpx_market_alerts.py    ← 시장조치 데이터 + PDF 자동 수집
│  ├─ download_jpx_regulations.py    ← JPX 규정 PDF 자동 다운로드
│  ├─ extract_pdf_text.py            ← 규정 PDF → txt 변환
│  ├─ extract_pdf_reasons.py         ← 조치 PDF → Reason 텍스트 추출
│  ├─ enrich_supervision_details.py  ← 감리종목 PDF에서 위반 기준 상세 추출 (pdfplumber)
│  │                                    → current_stocks.json에 Refined_Details 추가
│  └─ simplify_details.py            ← Details 텍스트를 간결한 라벨로 변환
│                                       → current_stocks.json에 Simplified_Details 추가
│
├─ 분석 프롬프트 ────────────────────────────────────────────
│  └─ PROMPT_consolidated_report.md  ← 통합 보고서 생성용 LLM 프롬프트
│
├─ 분석 보고서 (HTML) ──────────────────────────────────────
│  ├─ JPX_Market_Measures_Report.html
│  ├─ JPX_JPX-R_TSE_조직및역할분석.html
│  ├─ JPX_상장공시관련조직.html
│  └─ JPX_통합보고서.html
│
├─ 분석 노트 (MD) ──────────────────────────────────────────
│  ├─ 2026-03-29-jpx-insider-trading.md
│  └─ 2026-04-01-jpx-listing-management-delisting.md
│
├─ SOURCES.md                        ← 출처 문서
│
│
├─ data/ ────────────────────────────────────────────────────
│  │
│  │  ◆ 통합 가공물
│  ├─ JPX_Consolidated_Report_v3.csv ← 전체 통합 + LLM 분류 (PROMPT 기반 생성)
│  ├─ pdf_reasons.json               ← PDF에서 추출한 Reason 텍스트
│  │                                    (extract_pdf_reasons.py → data/pdfs/ 참조)
│  │
│  │  ◆ 섹션별 구조화 데이터 (scrape_jpx_market_alerts.py 생성)
│  │
│  ├─ supervision_delisting/         ← 감리종목/상장폐지
│  │  ├─ current_stocks.json    ──→ data/pdfs/supervision_delisting/*.pdf
│  │  │   ├ fetched_date: 수집일자
│  │  │   ├ Simplified_Details: 간결한 사유 라벨 (simplify_details.py)
│  │  │   └ Refined_Details: PDF 테이블에서 추출한 위반 기준 (enrich_supervision_details.py)
│  │  ├─ current_others.json    ──→ data/pdfs/supervision_delisting/*.pdf
│  │  ├─ history_stocks.json        (File_Path로 로컬 PDF 연결, Details에 Reason 포함)
│  │  └─ history_others.json
│  │
│  ├─ improvement_period/            ← 개선기간
│  │  ├─ companies_improvement_period.json
│  │  │   ├ fetched_date: 수집일자
│  │  │   └ Violated Criteria: 위반 기준 (xlsx에서 추출)
│  │  │                              ──→ data/pdfs/improvement_period/*.xlsx (원본)
│  │  └─ companies_transitional_measures.json
│  │                                 ──→ data/pdfs/improvement_period/*.xlsx (원본)
│  │
│  ├─ grace_period/                  ← 유예기간
│  │  ├─ current_stocks.json    ──→ data/pdfs/grace_period/*.pdf, *.xlsx
│  │  ├─ history_stocks.json    ──→ data/pdfs/grace_period/*.pdf
│  │  └─ history_others.json
│  │
│  ├─ public_announcement/           ← 공표조치
│  │  └─ public_announcement.json ─→ data/pdfs/public_announcement/*.pdf
│  │
│  ├─ violation_penalties/            ← 위약금
│  │  └─ violation_penalties.json ─→ data/pdfs/violation_penalties/*.pdf
│  │
│  ├─ improvement_reports/            ← 개선보고서
│  │  └─ improvement_reports.json ─→ data/pdfs/improvement_reports/*.pdf
│  │
│  ├─ special_alert/                  ← 특별경고
│  │  ├─ current.json           ──→ data/pdfs/special_alert/*.pdf
│  │  └─ history.json
│  │
│  └─ pdfs/ ─────────────────────────────────────────────────
│     │
│     │  ◆ 시장조치 PDF/xlsx (scrape_jpx_market_alerts.py 다운로드)
│     │    파일명: {code}_{name}.pdf 또는 {year}_{code}_{name}.pdf
│     │
│     ├─ supervision_delisting/   (74 files)  ← JPX Supervision/Delisting 페이지
│     ├─ improvement_period/      (2 xlsx)    ← JPX Improvement Period 페이지
│     ├─ grace_period/            (5 files)   ← JPX Grace Period 페이지
│     ├─ public_announcement/     (26 pdfs)   ← JPX Public Announcement 페이지
│     ├─ violation_penalties/     (22 pdfs)   ← JPX Violation Penalties 페이지
│     ├─ improvement_reports/     (23 pdfs)   ← JPX Improvement Reports 페이지
│     ├─ special_alert/           (8 pdfs)    ← JPX Special Alert 페이지
│     │
│     │  ◆ 별도 수집
│     └─ jpx_official/            (3 pdfs)    ← 수동 수집 (조사보고서, 연차보고서)
│
│
└─ JPX_rules/ ───────────────────────────────────────────────
   │
   │  ◆ JPX 규정 원문 (download_jpx_regulations.py 다운로드)
   │    extract_pdf_text.py로 txt 변환
   │
   ├─ TSE_Listing_Regulations/       ← TSE 상장규정
   │  ├─ Securities Listing Regulations (as of ...).pdf/.txt
   │  ├─ Enforcement Rules for Securities Listing Regulations (as of ...).pdf/.txt
   │  ├─ Guidelines Concerning Listing Examination, etc. (as of ...).pdf/.txt
   │  └─ Guidelines Concerning Listed Company Compliance, etc.(as of ...).pdf/.txt
   │
   └─ JPX-R/                         ← JPX-R 규정
      ├─ Articles of Incorporation (as of ...).pdf/.txt
      ├─ Business Regulations (as of ...).pdf/.txt
      └─ Enforcement Rules for the Business Regulations (as of ...).pdf/.txt
```

## 데이터 흐름

```
JPX 웹사이트
    │
    ├─ scrape_jpx_market_alerts.py
    │      │  1. 웹 테이블 크롤링 → JSON 생성
    │      │  2. PDF 다운로드 → data/pdfs/{섹션}/
    │      │  3. PDF에서 Reason 추출 → JSON의 Details 필드에 기입
    │      │  4. File_Path에 로컬 상대경로 설정 (GitHub 클릭 연결용)
    │      │
    │      ├──→ data/{섹션}/*.json             (표 데이터 + Details + File_Path)
    │      └──→ data/pdfs/{섹션}/*.pdf, *.xlsx (첨부 파일)
    │
    ├─ download_jpx_regulations.py
    │      └──→ JPX_rules/{TSE,JPX-R}/*.pdf
    │
    └─ (수동) ──→ data/pdfs/jpx_official/*.pdf

extract_pdf_text.py    ──→ JPX_rules/**/*.txt         (규정 전문)
extract_pdf_reasons.py ──→ data/pdf_reasons.json      (전체 PDF Reason 일괄 추출)

enrich_supervision_details.py (pdfplumber)
    │  감리종목 PDF 테이블에서 위반 기준(●) 추출
    └──→ current_stocks.json에 Refined_Details 추가

simplify_details.py
    │  Details 텍스트를 간결한 라벨로 분류
    └──→ current_stocks.json에 Simplified_Details 추가

data/*.json + pdf_reasons.json
    │
    ├─ JPX_통합보고서.html (JavaScript)
    │      fetch()로 JSON 로딩 → 3.1 TSE 트랙 현황을 동적 렌더링
    │
    └─ PROMPT_consolidated_report.md (LLM)
           └──→ data/JPX_Consolidated_Report.csv  (통합+분류)
```
