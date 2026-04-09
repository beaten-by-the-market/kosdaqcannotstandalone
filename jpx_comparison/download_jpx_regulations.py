"""
JPX 규정 PDF 자동 수집 스크립트
- TSE: Securities Listing Regulations and Related Rules 섹션
- JPX-R: 전체 규정
다운로드 위치: JPX_rules/TSE_Listing_Regulations/, JPX_rules/JPX-R/
파일명: 표에 있는 규정 이름 사용 (날짜 정보 포함)
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.jpx.co.jp"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_BASE = os.path.join(SCRIPT_DIR, "JPX_rules")


def sanitize_filename(name: str) -> str:
    """표에 있는 규정 이름을 파일명으로 변환 (날짜 정보 유지)"""
    # 파일명에 사용할 수 없는 문자 치환
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    # 연속 공백 정리
    name = re.sub(r"\s+", " ", name).strip()
    return name + ".pdf"


def download_pdf(url: str, save_path: str) -> bool:
    """PDF 다운로드"""
    if os.path.exists(save_path):
        print(f"  [SKIP] 이미 존재: {os.path.basename(save_path)}")
        return True

    try:
        r = requests.get(url, headers=HEADERS, timeout=60)
        r.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(r.content)
        size_kb = len(r.content) / 1024
        print(f"  [OK] {os.path.basename(save_path)} ({size_kb:.0f} KB)")
        return True
    except Exception as e:
        print(f"  [FAIL] {os.path.basename(save_path)}: {e}")
        return False


def fetch_page(path: str) -> BeautifulSoup:
    """페이지 HTML 파싱"""
    url = urljoin(BASE_URL, path)
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def collect_tse_listing_regulations(soup: BeautifulSoup) -> list[tuple[str, str]]:
    """TSE 페이지에서 Securities Listing Regulations and Related Rules 섹션 PDF 수집"""
    results = []

    # 'Securities Listing Regulations and Related Rules' 제목 span 찾기
    target_span = None
    for span in soup.find_all("span"):
        if span.get_text(strip=True) == "Securities Listing Regulations and Related Rules":
            target_span = span
            break

    if not target_span:
        print("[WARN] 'Securities Listing Regulations and Related Rules' 섹션을 찾지 못했습니다.")
        return results

    # 이 span 다음에 오는 테이블에서 PDF 추출
    table = target_span.find_next("table")
    if not table:
        return results

    for row in table.find_all("tr"):
        th = row.find("th")
        link = row.find("a", href=lambda h: h and ".pdf" in str(h))
        if th and link:
            name = th.get_text(strip=True)
            href = urljoin(BASE_URL, link["href"])
            results.append((name, href))

    return results


def collect_jpxr_regulations(soup: BeautifulSoup) -> list[tuple[str, str]]:
    """JPX-R 페이지에서 전체 규정 PDF 수집"""
    results = []

    for row in soup.find_all("tr"):
        th = row.find("th")
        link = row.find("a", href=lambda h: h and ".pdf" in str(h))
        if th and link:
            name = th.get_text(strip=True)
            href = urljoin(BASE_URL, link["href"])
            results.append((name, href))

    return results


def main():
    # === TSE: Securities Listing Regulations and Related Rules ===
    print("=" * 60)
    print("TSE - Securities Listing Regulations and Related Rules")
    print("=" * 60)

    tse_dir = os.path.join(OUTPUT_BASE, "TSE_Listing_Regulations")
    os.makedirs(tse_dir, exist_ok=True)

    tse_soup = fetch_page("/english/rules-participants/rules/regulations/index.html")
    tse_pdfs = collect_tse_listing_regulations(tse_soup)
    print(f"발견된 PDF: {len(tse_pdfs)}개\n")

    for name, url in tse_pdfs:
        filename = sanitize_filename(name)
        save_path = os.path.join(tse_dir, filename)
        print(f"  다운로드: {name}")
        download_pdf(url, save_path)

    # === JPX-R: 전체 규정 ===
    print()
    print("=" * 60)
    print("JPX-R - 전체 규정")
    print("=" * 60)

    jpxr_dir = os.path.join(OUTPUT_BASE, "JPX-R")
    os.makedirs(jpxr_dir, exist_ok=True)

    jpxr_soup = fetch_page("/english/rules-participants/rules/regulations/02.html")
    jpxr_pdfs = collect_jpxr_regulations(jpxr_soup)
    print(f"발견된 PDF: {len(jpxr_pdfs)}개\n")

    for name, url in jpxr_pdfs:
        filename = sanitize_filename(name)
        save_path = os.path.join(jpxr_dir, filename)
        print(f"  다운로드: {name}")
        download_pdf(url, save_path)

    # === 요약 ===
    print()
    print("=" * 60)
    print("다운로드 완료 요약")
    print("=" * 60)
    print(f"TSE Listing Regulations: {len(tse_pdfs)}개 -> {tse_dir}")
    print(f"JPX-R Regulations:       {len(jpxr_pdfs)}개 -> {jpxr_dir}")


if __name__ == "__main__":
    main()
