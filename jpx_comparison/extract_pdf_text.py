#!/usr/bin/env python3
"""
Extract text from PDF files using pymupdf (fitz).
Saves extracted text as .txt files in the same directory.
JPX_rules 하위 폴더(TSE_Listing_Regulations, JPX-R)의 모든 PDF를 자동 탐색.
"""

import fitz  # pymupdf
from pathlib import Path

# Directory containing the PDF files
pdf_dir = Path("JPX_rules")


def extract_text_from_pdf(pdf_path, output_path):
    """
    Extract text from a PDF file and save it to a .txt file.
    """
    try:
        print(f"Processing: {pdf_path.relative_to(pdf_dir)}")

        doc = fitz.open(pdf_path)

        text = ""
        for page_num in range(len(doc)):
            page = doc[page_num]
            text += page.get_text()
            print(f"  Extracted page {page_num + 1}/{len(doc)}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"  Saved: {output_path.relative_to(pdf_dir)}")
        print(f"  Total characters: {len(text)}\n")

        doc.close()
        return True
    except Exception as e:
        print(f"ERROR processing {pdf_path.name}: {e}\n")
        return False


def main():
    """Main function to process all PDF files."""
    print("=" * 60)
    print("PDF Text Extraction Tool")
    print("=" * 60 + "\n")

    if not pdf_dir.exists():
        print(f"ERROR: Directory '{pdf_dir}' does not exist!")
        return

    # 하위 폴더 포함 모든 PDF 자동 탐색
    pdf_files = sorted(pdf_dir.rglob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_files)} PDF files.\n")

    successful = 0
    failed = 0

    for pdf_path in pdf_files:
        txt_path = pdf_path.with_suffix('.txt')
        if extract_text_from_pdf(pdf_path, txt_path):
            successful += 1
        else:
            failed += 1

    print("=" * 60)
    print(f"Summary: {successful} successful, {failed} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
