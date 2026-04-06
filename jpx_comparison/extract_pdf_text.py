#!/usr/bin/env python3
"""
Extract text from PDF files using pymupdf (fitz).
Saves extracted text as .txt files in the same directory.
"""

import fitz  # pymupdf
import os
from pathlib import Path

# Directory containing the PDF files
pdf_dir = Path("JPX_rules")

# List of PDF files to process
pdf_files = [
    "jpx-r_business_regs_20250228.pdf",
    "jpx-r_business_regulations_enforcement_rules_2013-07-16.pdf",
    "listed_company_compliance_20250401.pdf",
    "listing_exam_guidelines_20251208.pdf",
    "listing_regs_20251208.pdf",
    "listing_regs_ER_20251208.pdf",
]

def extract_text_from_pdf(pdf_path, output_path):
    """
    Extract text from a PDF file and save it to a .txt file.

    Args:
        pdf_path: Path to the PDF file
        output_path: Path where the text file should be saved
    """
    try:
        print(f"Processing: {pdf_path.name}")

        # Open the PDF file
        doc = fitz.open(pdf_path)

        # Extract text from all pages
        text = ""
        for page_num in range(len(doc)):
            page = doc[page_num]
            text += page.get_text()
            print(f"  Extracted page {page_num + 1}/{len(doc)}")

        # Save the extracted text to a .txt file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"  Saved: {output_path.name}")
        print(f"  Total characters: {len(text)}\n")

        # Close the PDF document
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

    # Check if directory exists
    if not pdf_dir.exists():
        print(f"ERROR: Directory '{pdf_dir}' does not exist!")
        return

    # Process each PDF file
    successful = 0
    failed = 0

    for pdf_filename in pdf_files:
        pdf_path = pdf_dir / pdf_filename

        # Check if file exists
        if not pdf_path.exists():
            print(f"WARNING: File not found: {pdf_path}\n")
            failed += 1
            continue

        # Generate output path (same name but .txt extension)
        txt_filename = pdf_filename.rsplit('.', 1)[0] + '.txt'
        output_path = pdf_dir / txt_filename

        # Extract text
        if extract_text_from_pdf(pdf_path, output_path):
            successful += 1
        else:
            failed += 1

    # Print summary
    print("=" * 60)
    print(f"Summary: {successful} successful, {failed} failed")
    print("=" * 60)

if __name__ == "__main__":
    main()
