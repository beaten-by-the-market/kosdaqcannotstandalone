# pdfs/ — 출처 매핑

모든 서브폴더는 JPX 영문 사이트 **Market Alerts** 페이지와 1:1 대응합니다.

**Base URL**: `https://www.jpx.co.jp/english/listing/market-alerts/`

| 폴더 | JPX 페이지 URL | 내용 | 수집일 |
|---|---|---|---|
| `improvement_period/` | [improvement-period/](https://www.jpx.co.jp/english/listing/market-alerts/improvement-period/index.html) | Improvement Period 엑셀 원본 | 2026-03-18 |
| `improvement_reports/` | [improvement-reports/](https://www.jpx.co.jp/english/listing/market-alerts/improvement-reports/index.html) | 개선보고서 PDF (23건) | 2026-03-23 |
| `violation_penalties/` | [violation-penalties/](https://www.jpx.co.jp/english/listing/market-alerts/violation-penalties/index.html) | 위약금 부과 PDF (18건) | 2026-03-23 |
| `public_announcement/` | [public-announcement/](https://www.jpx.co.jp/english/listing/market-alerts/public-announcement/index.html) | 공표조치 PDF (17건) | 2026-03-23 |
| `supervision_delisting/` | [supervision-delisting/](https://www.jpx.co.jp/english/listing/market-alerts/supervision/index.html) | 감리종목/상장폐지 PDF (46건) | 2026-03-23 |
| `special_alert/` | [special-alert/](https://www.jpx.co.jp/english/listing/market-alerts/special-alert/index.html) | 특별경고 PDF (9건) | 2026-03-23 |
| `grace_period/` | [grace-period/](https://www.jpx.co.jp/english/listing/market-alerts/grace-period/index.html) | 유예기간 PDF (3건) | 2026-03-23 |

## jpx_official/ — JPX 공식 보고서 (개별 출처)

| 파일 | 출처 | 설명 |
|---|---|---|
| `E_20250130_1.pdf` | JPX 독립이사 조사위원회 보고서 (2025.01.30 공표) | 내부자거래 사건 조사보고서 — TSE 조직/인원/정보관리 체계 상세 |
| `E_20250130_2.pdf` | JPX 독립이사 조사위원회 보고서 별첨 (2025.01.30 공표) | 조사보고서 별첨 자료 |
| `JPX-R_Annual_Report_2025_E.pdf` | [JPX-R Annual Report](https://www.jpx.co.jp/english/regulation/outline/about/index.html) | JPX-R 연차보고서 2025 (FY2024 실적) |

## 파일명 규칙

- `improvement_reports/`: `{종목코드}_{회사명}.pdf`
- `violation_penalties/`: `{연도}_{종목코드}_{회사명}.pdf`
- `public_announcement/`: `{연도}_{종목코드}_{회사명}.pdf`
- `supervision_delisting/`: `SUP_{종목코드}_{회사명}.pdf` (감리) / `DEL_{종목코드}_{회사명}.pdf` (상장폐지)
- `special_alert/`: `{종목코드}_{회사명}.pdf`
- `grace_period/`: `{종목코드}_{회사명}.pdf`
