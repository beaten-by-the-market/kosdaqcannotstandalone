# JPX 상장기업 시장조치 현황 보고서
## — TSE 트랙 / JPX-R 트랙별 분류 —

> **기준일**: 2026-03-23 (Current 데이터) / History 데이터: 2021~2026
> **데이터 출처**: JPX 영문 웹사이트 HTML 및 PDF, TDnet, Companies in Improvement Period 엑셀
> **총 228건** (Current 170건 + History 58건)

---

## 1. 전체 구조

TSE의 시장조치는 **판단 주체**에 따라 두 개의 트랙으로 나뉜다.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      TSE 트랙 (Quantitative)                            │
│                TSE가 규칙 기반으로 자체 판단·집행                         │
│                                                                          │
│  [유동성 기준 미달]     [재무 기준 미달]     [기업행위/감사의견]           │
│   주주수, 유통시총,      순자산               주식병합, TOB, 캐시아웃,    │
│   유통비율, 매매대금,                         감사의견 미표명 등          │
│   시가총액 등                                                            │
│        │                     │                      │                    │
│        ▼                     ▼                      │                    │
│  Improvement Period (개선기간, ~1년)                 │ ← Imp. Period 없음 │
│  104종목 (Liquidity)   6종목 (Financial)             │                    │
│              + 3종목 (복합)                          │                    │
│        │                     │                      │                    │
│        │ 미충족 시            │ 미충족 시             │                    │
│        ▼                     ▼                      ▼                    │
│  Securities Under Supervision (감리종목)                                 │
│        │                                                                 │
│        ▼                                                                 │
│  Securities to Be Delisted (정리종목) → 상장폐지                         │
│                                                                          │
│  ※ 참고: KRX는 유동성 기준 = 유예기간 부여, 재무 기준 = 즉시 조치.        │
│    TSE는 유동성·재무 모두 Improvement Period(유예기간)를 부여하는 구조.     │
└──────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                   JPX-R 트랙 (Qualitative)                          │
│            JPX-R이 독립 심사 후 결정, TSE 명의로 집행                 │
│                                                                     │
│  [공시 위반, 거버넌스 위반, 서약서 위반 등]                           │
│        │                                                             │
│        ▼                                                             │
│   JPX-R Listed Company Compliance Dept 심사                         │
│        │                                                             │
│        ├── Public Announcement (공표조치)                            │
│        ├── Violation Penalty (위약금 부과)                           │
│        ├── Improvement Report (개선보고서 징구)                      │
│        ├── Security on Special Alert (특별주의시장종목 지정)          │
│        └── Grace Period (유예기간 지정)                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. TSE 트랙 — 현황 (159건)

TSE가 수치 기준 또는 기업행위 발생 여부를 기반으로 **규칙에 따라 자동 판단·집행**한다.

### 2.1 Improvement Period (개선기간) — 113종목

수치 기준 미달 시 개선 기한을 부여하는 단계. 개별 PDF 없이 **엑셀 목록으로만 게시**된다.
KRX와 달리 TSE는 **유동성·재무 기준 모두** Improvement Period(유예기간)를 부여한다.

| 구분 | 미달 기준 | 종목 수 |
|---|---|---:|
| **Liquidity** | Tradable Share Mkt Cap (유통시총) | 60 |
| | Tradable Share Ratio (유통비율) | 21 |
| | Market Capitalization (시가총액) | 17 |
| | 유통비율 + 유통시총 복합 | 3 |
| | 유통시총 + 매매대금 복합 | 2 |
| | 주주수 + 유통시총 복합 | 1 |
| | **소계** | **104 (92%)** |
| **Financial** | Net Assets (순자산) | 6 |
| | **소계** | **6 (5%)** |
| **Liquidity + Financial** | 유통시총 + 순자산 동시 미달 | **3 (3%)** |

| 시장별 | Prime | Standard | Growth | 합계 |
|---|---:|---:|---:|---:|
| 종목 수 | 33 | 53 | 27 | **113** |

> 주요 종목: Japan Display (6740, Prime, 유통주식수 ~2028.03), AKEBONO BRAKE (7238, Prime, 유통주식수 ~2030.03), TV Asahi Holdings (9409, Prime, 유통주식수 ~2026.03)

> **KRX 비교**: KRX는 재무 기준(자본잠식 등) 미달 시 즉시 관리종목/상장폐지 절차에 진입하지만, TSE는 재무 기준(순자산 미달 6건) 역시 Improvement Period를 부여하여 개선 기회를 먼저 제공하는 구조. TSE에서 Financial 기준에 해당하는 것은 **Net Assets(순자산)만** 6건(5%)이며, 나머지 107건(95%)은 유동성 기준.

### 2.2 Securities Under Supervision (감리종목) — 37종목

| 경로 | 구분 | 사유 | 종목 수 |
|---|---|---|---:|
| **Improvement Period 경유** | Liquidity | 유통시총 미달 (기한 내 미충족) | 2 |
| | Liquidity + Financial | 시가총액 + 순자산 미달 (기한 내 미충족) | 1 |
| | **소계** | | **3** |
| **직행 (Imp. Period 없음)** | Corporate Actions | Reverse Stock Split (주식병합) | 20 |
| | Corporate Actions | Board Resolution (취득결의) | 14 |
| | Audit Opinion | 감사의견 미표명/부적정 | 0 |
| | 기타 | 유가증권보고서 미제출, 은행거래 정지 등 | 0 |
| | **소계** | | **34** |

직행 34건은 회사가 TDnet에 공시한 **당일 즉시** TSE가 감리종목으로 지정 (시차 0일).

<details>
<summary>Improvement Period 경유 3종목</summary>

| Code | Issue Name | Market | 미달 기준 |
|------|-----------|--------|----------|
| 9914 | Uematsu Shokai Co.,Ltd. | Standard | Tradable Share Mkt Cap |
| 7719 | TOKYO KOKI CO.LTD. | Standard | Tradable Share Mkt Cap |
| 6173 | Aqualine Ltd. | Growth | Market Cap + Net Assets |

</details>

<details>
<summary>Corporate Actions 직행 34종목 (최근순)</summary>

| Code | Issue Name | Market | 지정일 | 사유 |
|------|-----------|--------|--------|------|
| 9914 | Uematsu Shokai | Standard | Mar. 21, 2026 | - |
| 1776 | SUMIKEN MITSUI ROAD | Standard | Mar. 09, 2026 | TOB 동의 |
| 2540 | YOMEISHU SEIZO | Prime | Feb. 25, 2026 | TOB 동의 |
| 2692 | ITOCHU-SHOKUHIN | Prime | Feb. 25, 2026 | TOB 동의·응모추천 |
| 4659 | AJIS | Standard | Feb. 19, 2026 | 주식병합 결의 |
| 4464 | SOFT99 | Standard | Feb. 17, 2026 | 주식병합 |
| 9338 | INFORICH | Growth | Feb. 13, 2026 | 주식병합 |
| 9927 | WATT MANN | Standard | Feb. 13, 2026 | 주식병합 결의 |
| 4974 | TAKARA BIO | Prime | Feb. 13, 2026 | 주식병합 |
| 3546 | Alleanza Holdings | Prime | Feb. 13, 2026 | 주식병합 결의 |
| 2344 | HEIAN CEREMONY SERVICE | Standard | Feb. 10, 2026 | 주식병합 결의 |
| 4556 | KAINOS Laboratories | Standard | Feb. 06, 2026 | 주식병합 결의 |
| 6670 | MCJ | Standard | Feb. 05, 2026 | 주식병합 |
| 6403 | SUIDO KIKO KAISHA | Standard | Feb. 05, 2026 | 주식병합 결의 |
| 1726 | Br.Holdings | Prime | Feb. 04, 2026 | 주식병합 |
| 7999 | MUTOH HOLDINGS | Standard | Feb. 04, 2026 | 주식병합 |
| 7922 | SANKO SANGYO | Standard | Feb. 03, 2026 | 주식병합 |
| 4690 | NIPPON PALLET POOL | Standard | Jan. 30, 2026 | 주식병합 |
| 202A | MAMEZO | Growth | Jan. 23, 2026 | 주식병합 |
| 8209 | FRIENDLY | Standard | Jan. 19, 2026 | 주식병합 결의 |
| 6201 | TOYOTA INDUSTRIES | Prime | Jan. 14, 2026 | TOB 동의 |
| 4530 | HISAMITSU PHARMACEUTICAL | Prime | Jan. 06, 2026 | TOB 동의 |
| 3541 | Nousouken | Growth | Dec. 25, 2025 | 주식병합 결의 |
| 6901 | SAWAFUJI ELECTRIC | Standard | Dec. 19, 2025 | 주식병합 결의 |
| 3593 | HOGY MEDICAL | Prime | Dec. 17, 2025 | 주식병합 |
| 3902 | Medical Data Vision | Prime | Dec. 15, 2025 | 주식병합 결의 |
| 7317 | Matsuya R&D | Growth | Dec. 15, 2025 | 주식병합 |
| 4384 | RAKSUL | Prime | Dec. 11, 2025 | 주식병합 |
| 9067 | MARUWN | Standard | Nov. 13, 2025 | 주식병합 결의 |
| 7088 | Forum Engineering | Prime | Nov. 10, 2025 | 주식병합 결의 |
| 7105 | Mitsubishi Logisnext | Standard | Sep. 30, 2025 | 주식병합 결의 |
| 4917 | MANDOM | Prime | Sep. 10, 2025 | 주식병합 결의 |
| 7229 | YUTAKA GIKEN | Standard | Aug. 29, 2025 | 주식병합 결의 |
| 7250 | PACIFIC INDUSTRIAL | Prime | Jul. 25, 2025 | 주식병합 결의 |
| 6135 | Makino Milling Machine | Prime | Jun. 03, 2025 | 주식병합 |

</details>

### 2.3 Securities to Be Delisted (정리종목) — 9종목

| Code | Issue Name | Market | 지정일 | 사유 |
|------|-----------|--------|--------|------|
| 7739 | CANON ELECTRONICS | Prime | Mar. 19, 2026 | Reverse Stock Split |
| 7092 | Fast Fitness Japan | Prime | Mar. 19, 2026 | Reverse Stock Split |
| 7450 | SUNDAY | Standard | Mar. 12, 2026 | Share Cash-Out |
| 5352 | KROSAKI HARIMA | Prime | Mar. 11, 2026 | Share Cash-Out |
| 1841 | SANYU CONSTRUCTION | Standard | Mar. 06, 2026 | Reverse Stock Split |
| 7455 | PARIS MIKI HOLDINGS | Standard | Mar. 06, 2026 | Reverse Stock Split |
| 7635 | SUGITA ACE | Standard | Mar. 03, 2026 | Reverse Stock Split |
| 7923 | TOIN CORPORATION | Standard | Feb. 27, 2026 | Share Cash-Out |
| 7116 | DAIWA TSUSHIN | Standard | Feb. 25, 2026 | Reverse Stock Split |

> 9건 전부 Corporate Actions 기반. 수치 기준 미달로 인한 상장폐지는 현재 0건.

---

## 3. JPX-R 트랙 — 현황 (69건)

JPX-R Listed Company Compliance Dept가 **독립 심사** 후 결정하고, **TSE 명의로 집행**한다.
PDF에 *"This decision is based on the results of the examination by Japan Exchange Regulation"* 명기.

### 3.1 조치 절차와 단계

JPX-R 조치는 위반의 심각도에 따라 단계적으로 적용된다:

```
  위반 발생 (허위공시, 적시공시 위반, 거버넌스 위반 등)
       │
       ▼
  JPX-R 심사
       │
       ├─ 경미 ─────── Public Announcement (공표조치)
       │
       ├─ 중간 ─────── Violation Penalty (위약금 부과)
       │                + Improvement Report (개선보고서 징구)
       │
       ├─ 심각 ─────── Security on Special Alert (특별주의시장종목)
       │                → 개선 실패 시 상장폐지
       │
       └─ 서약 위반 ── Grace Period (유예기간)
                        → 유예기간 내 미해소 시 상장폐지
```

> 하나의 사안에 대해 **복수 조치가 동시 부과**되는 경우가 많다 (예: 공표조치 + 위약금 + 개선보고서 징구).

### 3.2 조치별 현황

#### Public Announcement (공표조치) — 17건 (History, 2023~2025)

| 사유 | 건수 |
|------|---:|
| False Statements (허위공시) | 14 |
| MSCB Issuance Rule Violation | 1 |
| Corporate Conduct: Outside Director | 1 |
| Delayed Disclosure (지연공시) | 1 |

#### Violation Penalty (위약금 부과) — 18건 (History, 2023~2026)

| 사유 | 건수 |
|------|---:|
| Timely Disclosure Violation (적시공시 위반) | 9 |
| False Statements (허위공시) | 3 |
| Audit Opinion Not Expressed (감사의견 미표명) | 2 |
| Written Oath Violation (서약서 위반) | 3 |
| Corporate Conduct: Internal Management | 1 |

#### Improvement Reports (개선보고서 징구) — 23건 (History, 2021~2025)

| 사유 | 건수 |
|------|---:|
| False Statements (허위공시) | **23** (전건) |

> 개선보고서 징구는 전건이 허위공시 사유. 검사기간 5년 (최장 2030년까지).

#### Securities on Special Alert (특별주의시장종목) — 8종목 (Current)

| Code | Issue Name | Market | 지정일 | 사유 | 상태 |
|------|-----------|--------|--------|------|------|
| 3856 | Abalance Corporation | Standard | Jan. 31, 2026 | Audit Disclaimer | 개선 중 |
| 6548 | TABIKOBO Co.Ltd. | Growth | Nov. 22, 2025 | Timely Disclosure | 개선 중 |
| 9444 | TOSHIN HOLDINGS | Standard | Nov. 22, 2025 | Audit Opinion | 개선 중 |
| 6594 | NIDEC CORPORATION | Prime | Oct. 28, 2025 | Audit Opinion | 개선 중 |
| 4813 | ACCESS CO.,LTD. | Prime | Aug. 27, 2025 | Timely Disclosure | 개선 중 |
| 5856 | Life Intelligent Enterprise | Standard | Mar. 27, 2025 | Corp. Conduct | 개선 중 |
| 6173 | Aqualine Ltd. | Growth | Jan. 29, 2025 | Timely Disclosure | 개선 중 |
| 7831 | Wellco Holdings | Standard | Oct. 26, 2024 | Timely Disclosure | **후속관찰** |

#### Grace Period (유예기간) — 3종목 (Current)

| Code | Issue Name | Market | 유예기간 | 사유 |
|------|-----------|--------|----------|------|
| 7116 | DAIWA TSUSHIN | Standard | Jun. 19, 2025 ~ Jun. 19, 2026 | Written Oath (IPO) |
| 9229 | SUNWELS | Prime | Apr. 30, 2025 ~ Apr. 30, 2026 | Written Oath (Segment Transfer) |
| 8887 | SYLA Holdings | Standard | Jun. 1, 2025 ~ May 31, 2029 | Not Substantial Surviving Co. (Merger) |

---

## 4. 종합 요약

### 4.1 판단주체별 요약

| | TSE 트랙 (Quantitative) | JPX-R 트랙 (Qualitative) |
|---|---:|---:|
| **Current 종목** | 159 | 11 |
| **History 건수** | — | 58 |
| **합계** | **159** | **69** |

### 4.2 사유 분류별 요약 (전체 228건)

| 대분류 | 사유 | 건수 |
|--------|------|---:|
| **Quantitative** | Listing Criteria — Liquidity (유통시총, 유통비율, 시가총액 등) | 106 |
| | Listing Criteria — Financial (순자산) | 6 |
| | Listing Criteria — Liquidity + Financial 복합 | 4 |
| | Corporate Actions (주식병합, 캐시아웃, 합병) | 44 |
| | Audit Opinion (감사의견 미표명) | 5 |
| | **소계** | **165 (72%)** |
| **Qualitative** | Disclosure Violation (허위공시, 적시공시, 지연공시) | 53 |
| | Governance Violation (내부관리, MSCB, 사외이사) | 5 |
| | Listing Integrity Violation (서약서 위반) | 5 |
| | **소계** | **63 (28%)** |

### 4.3 핵심 시사점

1. **TSE 트랙의 대부분은 Going Private**: 감리종목 37건 중 34건(92%)이 기업의 자발적 상장폐지(MBO/TOB). 수치 기준 미달로 인한 감리종목은 3건(8%)에 불과.

2. **Improvement Period의 92%가 유동성 기준**: 113종목 중 Liquidity 104종목(92%), Financial(순자산) 6종목(5%)에 불과. 유통시총 미달 60건이 최다. 2022년 시장구분 재편 이후 유통성 기준 강화의 영향.

3. **JPX-R 트랙의 핵심은 허위공시**: 개선보고서 23건 전건, 공표조치 17건 중 14건(82%)이 허위공시 사유.

4. **동시 다중 조치**: TOSHIN HOLDINGS(9444)는 공표조치 + 위약금 + 개선보고서 + 특별경고가 모두 부과된 사례.

---

## 5. TSE Listing Dept 업무부하 분석

> **인원 출처**: `E_20250130_1.pdf` pp.16–18 (기준일: 2024.10.1)
> **업무량 출처**: JPX 웹사이트 데이터 (기준일: 2026.03.23)

### 5.1 담당 조직과 인원

TSE Listing Department는 총 82명으로, 업무 성격에 따라 **4개 기능 단위**로 분산되어 있다.

```
TSE Listing Department (총 82명)
│
├── Listing Department Director (1명) + Section Director (1명)
│
├─── [직할 3개 그룹] (26명)
│    ├── Planning Group (10명)
│    │     └─ 상장규칙 전반 기획
│    ├── Listed Company Support Group (4명)
│    │     └─ 상장기업 IR활동 지원, 공시 교육
│    └── Administration Group (12명)
│          └─ 추가상장·변경상장 등 상장주식수 관리, 상장수수료 청구
│
└─── Corporate Disclosure Office (55명)
     │  Office장 (1명)
     │
     ├── Planning & Coordination Group (22명)
     │     ├─ 적시공시 규칙 기획
     │     ├─ Improvement Period 목록 관리·갱신
     │     ├─ 감리종목(Under Supervision) 지정·공표
     │     └─ 상폐종목(To Be Delisted) 지정·공표
     │
     ├── LC Services Group 1 — Prime (12명)  ┐
     ├── LC Services Group 2 — Standard (13명)├ 공시 접수·검토·승인·배포
     └── LC Services Group 3 — Growth (7명)  ┘  (Disclosure Supervisors 29명)
```

### 5.2 업무 범위 — KRX 공시부와의 비교

KRX의 경우 공시부 실무진이 일상 공시 검토부터 상장폐지 검토까지 **전 과정을 일괄 수행**하지만, TSE는 동일 업무 범위가 **부서 내 그룹 간**, 그리고 **TSE와 JPX-R 간**에 분산되어 있다.

<table>
<tr>
  <th>KRX 공시부 업무</th>
  <th>JPX 담당</th>
  <th>JPX 인원</th>
  <th>비고</th>
</tr>
<tr>
  <td>일상 공시 검토·승인·배포</td>
  <td>TSE LC Services Group 1~3</td>
  <td align="right">32명</td>
  <td>Disclosure Supervisors 29명 포함</td>
</tr>
<tr>
  <td>상장사 대상 공시 교육, IR 지원</td>
  <td>TSE Listed Company Support Group</td>
  <td align="right">4명</td>
  <td>직할 그룹 소속</td>
</tr>
<tr>
  <td>추가상장·변경상장 (상장주식수 관리)</td>
  <td>TSE Administration Group</td>
  <td align="right">12명</td>
  <td>직할 그룹 소속</td>
</tr>
<tr>
  <td>상장유지기준(정량) 미달 → 개선기간 관리</td>
  <td rowspan="2">TSE Planning &amp; Coordination Group</td>
  <td rowspan="2" align="right">22명 내</td>
  <td>Improvement Period 엑셀 갱신</td>
</tr>
<tr>
  <td>관리종목 지정, 상장폐지 사유 해당여부 검토 (정량 기준)</td>
  <td>기업행위, 감사의견 등 규칙 기반</td>
</tr>
<tr>
  <td>공시지연·불이행·변경에 대한 심사, 벌점 부여</td>
  <td rowspan="2"><b>JPX-R</b> Listed Co. Compliance Dept</td>
  <td rowspan="2" align="right">26명+ <sup>※</sup></td>
  <td>TSE가 아닌 JPX-R 소관</td>
</tr>
<tr>
  <td>상폐 해당여부 심사 (정량 기준: 감사의견 미표명 등)</td>
  <td>감리종목 지정 '후' 상폐 확정 심사</td>
</tr>
</table>

> ※ JPX-R Listed Co. Compliance Dept 26명+는 조사보고서(`E_20250130_1.pdf` p.20)상 변경 전 미공개정보 수령 등록인원 25명(부장 제외 전 부원) + 부장 1명에서 역산한 **최소 추정치**. 실제 인원은 이보다 많을 수 있음.

> **핵심 차이**:
> - KRX는 공시부가 공시 접수·검토에서 정량 기준 **상장폐지 사유 발생 검토·해당여부 검토·개선기간 부여**, 공시 위반에 대한 **심사·벌점 부여**까지 일괄 수행한다.
> - TSE는 이 업무가 분리: ① 공시 접수·검토는 LC Services Group, ② 위반 심사·벌점·상폐 확정 판단은 **JPX-R**. TSE Listing Dept는 감리종목 지정 등 **행정 공표만** 수행하고 심사·판단 업무는 갖고 있지 않다.

### 5.3 TSE Listing Dept의 시장조치 업무 — 단계별 분석

#### (A) Improvement Period — 예측 가능, 정기 갱신

| 항목 | 내용 |
|------|------|
| **현재 종목 수** | 113종목 |
| **갱신 주기** | 유통시총·유통비율 등 = **주 1회** / 시가총액(Growth) = **월 1회** / 매매대금(Prime) = **연 1회** (매년 1월 5영업일경) |
| **산출물** | 엑셀 파일 1개 (개별 PDF 없음) |
| **End Date 분포** | 아래 표 참조 |

| 기한까지 잔여 기간 | 종목 수 | 비율 |
|---|---:|---:|
| 이미 만료 (overdue) | 4 | 3% |
| 이번 달 (2026.03) | **53** | **43%** |
| 1~3개월 후 | 8 | 7% |
| 4~12개월 후 | 54 | 44% |
| 13개월 이상 | 3 | 2% |

> **3월 집중 현상**: 122개 기한 항목 중 53건(43%)이 2026년 3월 말 만료. 이는 대부분의 상장기업이 3월 결산이므로 record date가 3월 31일에 집중되기 때문. 다만 이 시점의 업무는 **수치 확인 후 목록 갱신**이며, 기한 만료 종목은 Under Supervision으로 이관하는 정형화된 처리.

#### (B) Securities Under Supervision — 이벤트 드리븐, 즉시 대응

| 항목 | 내용 |
|------|------|
| **현재 종목 수** | 37종목 |
| **트리거** | 기업이 TDnet에 Corporate Action 공시 → **당일 즉시** 감리종목 지정 |
| **월간 발생 빈도** | 2025.6~2026.3 기준 월 0~15건 (2026.2월에 15건으로 피크) |
| **산출물** | 종목별 TSE Urgent Notice PDF 1건 |
| **업무 내용** | 공시 확인 → 상폐기준 해당 여부 판단 → PDF 작성·공표 |

| 기간 | 지정 건수 |
|------|---:|
| 2025.06~2025.09 | 5건 (월 1.3건) |
| 2025.10~2025.12 | 8건 (월 2.7건) |
| 2026.01 | 5건 |
| 2026.02 | **15건** |
| 2026.03 (23일까지) | 2건 |

> 2026년 2월의 15건 집중은 MBO/TOB 붐 시기와 일치. 다만 Corporate Actions 기반 지정은 **정형화된 PDF 템플릿** 사용 (공시 내용 확인 후 코드·종목명·사유를 삽입하는 수준).

#### (C) Securities to Be Delisted — Under Supervision 후속, 소량

| 항목 | 내용 |
|------|------|
| **현재 종목 수** | 9종목 |
| **갱신 주기** | 수시 (Under Supervision → To Be Delisted 전환 시) |
| **산출물** | 종목별 TSE Urgent Notice PDF 1건 |

### 5.4 업무부하 평가

| 평가 항목 | 분석 |
|-----------|------|
| **업무 분산** | KRX 공시부에 집중된 업무가 TSE에서는 **4개 단위**로 분산: 공시 접수(LC Services 32명), 규칙·시장조치(P&C 22명), IR·교육(Support 4명), 주식수 관리(Admin 12명). 또한 심사·징계는 **JPX-R**(26명+)이 별도 수행. |
| **예측 가능성** | Improvement Period는 end date가 수개월~1년 전부터 확정되어 있어 **업무량 예측 가능**. 3월 결산 집중은 연간 반복 패턴이므로 사전 대비 가능. |
| **즉시 대응 부하** | Under Supervision 지정은 공시 당일 즉시이나, Corporate Actions은 **정형 템플릿 처리**이며 판단 재량이 적음. 월 최대 15건(2026.2) 수준. |
| **심사 부하 부재** | 공시 위반 심사, 벌점 부여, 상폐 확정 판단, 위약금 부과 등 **재량적 판단이 필요한 심사 업무는 전부 JPX-R 소관**. TSE P&C Group은 JPX-R의 심사 결과를 받아 공표만 수행. |
| **인원 대비 업무량** | P&C Group 22명이 113종목 목록 관리 + 월 수 건의 감리/상폐 지정 PDF 처리. 규칙 기획 업무를 감안해도 **현재 수준에서 과부하 징후는 낮음**. |
| **참고: JPX-R 대비** | JPX-R Listed Company Compliance Dept(26명+)는 FY2024 상폐심사 106건 + Special Alert 4건 + 개선보고서 7건 등 **비정형 심층 심사**를 수행. TSE의 정형적 행정 처리와 성격이 근본적으로 다름. |

### 5.5 결론

TSE Listing Dept의 시장조치 업무는 다음 특성으로 인해 **현 인원 체제에서 과부하 없이 처리 가능한 수준**으로 판단된다:

1. **업무 분산 구조**: KRX가 공시부 단일 부서에서 수행하는 업무가 TSE에서는 Listing Dept 내 4개 그룹(82명) + JPX-R(26명+)에 분산. 특히 **심사·판단 업무가 JPX-R로 완전 분리**되어 있어, TSE에는 규칙 기반 행정 처리만 남음.
2. **정형화**: Improvement Period는 엑셀 갱신, Under Supervision/To Be Delisted는 템플릿 PDF — 모두 재량적 판단이 최소화된 규칙 기반 처리
3. **예측 가능**: end date가 사전 확정되어 있어 업무량 예측·사전 대비 가능
4. **즉시 대응의 단순성**: Corporate Actions 공시 → 감리종목 지정은 당일 즉시이나, 공시 내용 확인 후 정형 PDF 작성이므로 건당 소요 시간이 짧음
5. **심사 부하 제로**: 공시 위반 여부 판단, 조치 수준 결정, 상폐 확정 심사 등 전문적 심사는 JPX-R이 전담하므로, TSE Listing Dept에는 심사에 따른 업무 부하가 발생하지 않음

---

> **참고 자료**
> - `JPX_JPX-R_TSE_조직및역할분석.md` — 조직·역할 분담 분석
> - `JPX_Consolidated_Report_v3.csv` — 전체 228건 상세 데이터
> - `pdfs/` — 개별 조치 PDF 116건
> - `Companies_ImprovementPeriod_EN_260318.xlsx` — Improvement Period 원본 엑셀
