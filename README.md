<<<<<<< HEAD
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
=======
# PDF Utility

A simple, lightweight command-line utility in Python for managing PDF files. This script provides core functionalities for merging multiple PDFs into one and splitting a single PDF into a smaller file.

## Features

- **Merge PDFs**: Combines a list of PDF files into a single output file.
- **Split PDF**: Extracts a specific range of pages from a PDF and saves them to a new file.
- **Highly Portable**: The script is a single file with minimal dependencies.

## Requirements

This tool requires Python 3.x and the PyPDF2 library. You can install the dependency using pip:

```bash
pip install PyPDF2
```
# Clone the repository
```bash
git clone https://github.com/your-username/pdf_tool.git
```
# Go into the project folder
```bash
cd pdf_tool
```

# (Optional) Create a virtual environment
```bash
python -m venv venv
```

# Activate the virtual environment

# Windows
```bash
venv\Scripts\activate
```
# Mac/Linux
```bash
source venv/bin/activate
```

# Install dependencies
```bash
pip install PyPDF2
```

# Run the script
```bash
python pdf_tool.py
```

# How to Use

To use this tool, place the pdf_tool.py script and your PDF files in the same directory.

You can modify the example code within the if __name__ == "__main__": block to perform the action you need.

## Example 1: Merging PDFs

To merge two files, report1.pdf and report2.pdf, into a new file named combined_reports.pdf:

To use this, uncomment the line below and replace with your file names
```bash
merge_pdfs(["report1.pdf", "report2.pdf"], "combined_reports.pdf")
```
## Example 2: Splitting a PDF

To split a file named long_document.pdf and save pages 1 through 3 to a new file named first_three_pages.pdf:

To use this, uncomment the line below and replace with your file names and page numbers
```bash
split_pdf("long_document.pdf", 1, 3, "first_three_pages.pdf")
```

# Contributing

Feel free to fork this repository, suggest improvements, or submit pull requests. All contributions are welcome!
>>>>>>> c0d389cec584639dcb4141f81fe72d17814337ad
