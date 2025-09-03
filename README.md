# PDF-Utility

A simple yet powerful command-line tool for managing PDF files, built with Python.

This utility is designed to be fast, reliable, and easy to use for common PDF tasks directly from your terminal.

## ✨ Features

* **Merge:** Combine multiple PDF files into a single document.
* **Split:** Extract a specific range of pages from a PDF into a new file.
* **Rotate:** Rotate all pages in a PDF by 90, 180, or 270 degrees.
* **Crop:** Crop a specific page of a PDF to a custom size.
* **Optimization:** Reduce the file size of the output PDF to save storage.
* **Password Handling:** Work with password-protected PDF files.
* **Robustness:** Includes checks for file existence and invalid arguments to prevent errors.
* **User Experience:** Provides a clear, user-friendly interface and a real-time progress bar for long tasks.

## ⚙️ Installation

First, ensure you have Python installed. Then, use `pip` to install the required libraries:

```bash
pip install PyPDF2 tqdm PyMuPDF
```
## Usage
Use the pdf_tool.py script with the appropriate command (merge, split, rotate, crop) followed by its specific arguments.

## Merge PDFs
# Combine multiple PDFs into one.
```bash
python pdf_tool.py merge <input_file1> <input_file2> ... <output_file> [OPTIONS]
```
# Example:
```bash
python pdf_tool.py merge doc1.pdf doc2.pdf report.pdf
```
# With options:
```bash
python pdf_tool.py merge report.pdf confidential.pdf final.pdf --optimize --password mysecret
```
## Split PDFs
# Extract a range of pages from a single PDF.
```bash
python pdf_tool.py split <input_file> <start_page> <end_page> <output_file> [OPTIONS]
```
# Example:
```bash
python pdf_tool.py split big_book.pdf 10 20 excerpt.pdf
```
## Rotate PDFs
# Rotate all pages of a PDF by a specified amount.
```bash
python pdf_tool.py rotate <input_file> <degrees> <output_file> [OPTIONS]
```
degrees can be 90, 180, or 270.

# Example:
```bash
python pdf_tool.py rotate sideways_doc.pdf 90 rotated_doc.pdf --optimize
```
## Crop PDFs
# Crop a specific page of a PDF. Coordinates are in points (72 points per inch).
```bash
python pdf_tool.py crop <input_file> <page_number> <x0> <y0> <x1> <y1> <output_file> [OPTIONS]
```
(x0, y0): Top-left corner coordinates.

(x1, y1): Bottom-right corner coordinates.

# Example:
```bash
python pdf_tool.py crop invoice.pdf 1 100 100 400 600 cropped_invoice.pdf
```