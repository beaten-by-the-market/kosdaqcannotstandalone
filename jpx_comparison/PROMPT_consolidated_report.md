# JPX Consolidated Report 생성 프롬프트

아래 지시에 따라 JPX 시장조치 통합 보고서 CSV를 생성해주세요.

## 작업 개요

`data/` 폴더 하위의 모든 섹션별 CSV 파일과 `data/pdf_reasons.json`을 통합하여
하나의 `data/JPX_Consolidated_Report.csv`를 생성합니다.

## 입력 파일

| 소스 파일 | Section 값 | Status 값 |
|---|---|---|
| `data/supervision_delisting/current_stocks.json` | "Securities Under Supervision" 또는 "Securities to Be Delisted" (Section 컬럼 기준) | Current |
| `data/supervision_delisting/current_others.json` | Section 컬럼 기준 | Current |
| `data/supervision_delisting/history_stocks.json` | Section 컬럼 없음 → "Securities Under Supervision" | History |
| `data/supervision_delisting/history_others.json` | Section 컬럼 없음 → "Securities Under Supervision" | History |
| `data/improvement_period/companies_improvement_period.json` | "Improvement Period" | Current |
| `data/improvement_period/companies_transitional_measures.json` | "Improvement Period" | Current |
| `data/grace_period/current_stocks.json` | "Grace Period" | Current |
| `data/grace_period/history_stocks.json` | "Grace Period" | History |
| `data/grace_period/history_others.json` | "Grace Period" | History |
| `data/public_announcement/public_announcement.json` | "Public Announcement" | History |
| `data/violation_penalties/violation_penalties.json` | "Violation Penalty" | History |
| `data/improvement_reports/improvement_reports.json` | "Improvement Reports" | History |
| `data/special_alert/current.json` | "Securities on Special Alert" | Current |
| `data/special_alert/history.json` | "Securities on Special Alert" | History |
| `data/pdf_reasons.json` | Reason 텍스트 매칭용 | - |

## 출력 컬럼

```
Section, Status, Sub-Category, Code, Issue Name, Market Segment, Date, Period/Deadline, Reason, Remarks, Quant/Qual, Reason Category, Reason Sub-Category, Decision Authority
```

### 컬럼 매핑 규칙

- **Section**: 위 표의 Section 값. supervision_delisting의 current 파일은 원본 CSV의 `Section` 컬럼에 "Securities Under Supervision (Confirmation)", "Securities Under Supervision (Examination)", "Securities to Be Delisted" 등이 있음. 괄호 앞 부분만 Section으로 사용.
- **Sub-Category**: 괄호 안 부분 (Confirmation, Examination 등). 없으면 빈 값.
- **Code**: 종목 코드
- **Issue Name**: 종목명
- **Market Segment**: 시장 구분 (Prime, Standard, Growth 등)
- **Date**: 지정일/공표일/제출일 등 (원본 컬럼명이 다양함: Designation Date, Announcement Date 등)
- **Period/Deadline**: 기간 또는 기한 (있는 경우만)
- **Reason**: 사유 텍스트. 원본 JSON의 `Details` 필드에 PDF에서 추출된 Reason이 이미 포함되어 있음. 비어있는 경우 `pdf_reasons.json`에서 매칭.
- **Simplified_Reason**: `Simplified_Details` 필드 값 (간결한 라벨). `simplify_details.py`로 생성.
- **Refined_Reason**: `Refined_Details` 필드 값 (PDF 테이블에서 추출한 구체적 위반 기준). `enrich_supervision_details.py`로 생성. 해당 없으면 빈 값.
- **Remarks**: 비고

### 분류 컬럼 (LLM이 판단)

아래 3개 컬럼은 **Reason 텍스트 내용을 분석하여** 분류해야 합니다.

#### 1. Reason Category & Reason Sub-Category

Reason 텍스트를 읽고 아래 분류 체계에 따라 태깅하세요.

| Reason Category | Reason Sub-Category | 판단 기준 (Reason 텍스트 키워드/패턴) |
|---|---|---|
| **Listing Criteria (Liquidity)** | `Tradable Share Mkt Cap` | "tradable share market capitalization" 미달 |
| | `Tradable Share Ratio` | "tradable share ratio" 미달 |
| | `Market Capitalization` | "market capitalization" 미달 (tradable 아닌 전체) |
| | `Shareholders, Tradable Share Mkt Cap` | 주주수 + 유통시가총액 복합 미달 |
| | `Tradable Share Mkt Cap, Trading Value` | 유통시가총액 + 거래대금 복합 미달 |
| | `Tradable Share Ratio, Tradable Share Mkt Cap` | 유통비율 + 유통시가총액 복합 미달 |
| | `Failed to Meet: Tradable Share Mkt Cap` | improvement period 내 기준 미충족 |
| **Listing Criteria (Financial)** | `Net Assets` | "net assets" 미달 |
| **Listing Criteria (Liquidity + Financial)** | `Liquidity + Financial Criteria` | 유동성 + 재무 복합 미달 |
| | `Net Assets, Market Capitalization` | 순자산 + 시가총액 복합 |
| | `Failed to Meet: Market Capitalization + Net Assets` | improvement period 내 복합 기준 미충족 |
| **Corporate Actions** | `Reverse Stock Split (Going Private)` | "reverse stock split", "shares owned by shareholders other than a specified party will be less than one share", "demand the sale of shares" |
| | `Share Cash-Out (Squeeze Out)` | "share cash-out", "squeeze out", "tender offer" 후 완전자회사화 |
| | `Not a Substantial Surviving Company (Merger)` | "substantial surviving company", "merger" |
| **Disclosure Violation** | `False Statements` | "false statements", "inappropriate accounting" |
| | `Timely Disclosure Violation` | "violated the provisions of timely disclosure" |
| | `Delayed Disclosure` | "delayed disclosure", "not expected to be able to submit" |
| **Audit Opinion** | `Audit Opinion Not Expressed / Disclaimer` | "disclaimer of opinion", "audit opinion not expressed", "disclaimer of conclusion" |
| **Governance Violation** | `Corporate Conduct: Internal Management` | "Code of Corporate Conduct" + "internal management" |
| | `Corporate Conduct: Outside Director` | "independent outside director" |
| | `Internal Management Deficiency (Follow-up)` | follow-up 관련 governance 위반 |
| | `MSCB Issuance Rule Violation` | "MSCB", "moving strike convertible bonds" |
| **Listing Integrity Violation** | `Written Oath Violation (IPO)` | "written oath" + "initial listing" |
| | `Written Oath Violation (Segment Transfer)` | "written oath" + "segment transfer" / "reassignment" |
| | `Written Oath Violation (General)` | "written oath" (일반) |

#### 2. Quant/Qual

| 값 | 기준 |
|---|---|
| `Quantitative` | 수치 기준 미달 (유통주식, 시가총액, 순자산, 주주수 등) 또는 기업행위(주식병합, 스퀴즈아웃) |
| `Qualitative` | 공시 위반, 거버넌스 위반, 내부관리체계 부실 등 정성적 사유 |

#### 3. Decision Authority

| 값 | 기준 |
|---|---|
| `TSE` | 상장유지기준 미달, 기업행위 관련 → TSE Listing Department가 직접 판단 |
| `JPX-R` | 공시 위반, 내부관리 부실, 서약서 위반 등 심사가 필요한 건 → "based on the results of the examination by Japan Exchange Regulation" 문구가 PDF에 있는 경우. Special Alert, Violation Penalty, Public Announcement, Improvement Reports 섹션은 기본적으로 JPX-R |

### Improvement Period 특수 처리

Improvement Period 데이터(`companies_improvement_period.json`, `companies_transitional_measures.json`)는 xlsx에서 추출된 것으로, 컬럼 구조가 다릅니다.
- Reason 텍스트가 없는 경우가 많으며, 대신 어떤 기준을 위반했는지 컬럼으로 표시되어 있을 수 있습니다 (예: Tradable Share Ratio, Net Assets 등의 컬럼에 체크 표시).
- 이 경우 해당 컬럼들을 종합하여 Reason Category/Sub-Category를 추론하세요.

## 실행 방법

1. `scrape_jpx_market_alerts.py` 실행하여 최신 CSV 확보
2. `extract_pdf_reasons.py` 실행하여 `pdf_reasons.json` 생성
3. 이 프롬프트와 함께 위 파일들을 LLM에 제공하여 통합 CSV 생성

## 품질 검증

- 모든 입력 CSV의 행이 빠짐없이 포함되었는지 확인
- Reason Category가 빈 값인 행이 없는지 확인
- 동일 종목이 여러 섹션에 중복 등장하는 것은 정상 (예: Supervision + Violation Penalty)
