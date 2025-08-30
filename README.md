# PDF Utility

A simple, lightweight command-line utility in Python for managing PDF files. This script provides core functionalities for merging multiple PDFs into one and splitting a single PDF into a smaller file.

## Features

- **Merge PDFs**: Combines a list of PDF files into a single output file.
- **Split PDF**: Extracts a specific range of pages from a PDF and saves them to a new file.
- **Highly Portable**: The script is a single file with minimal dependencies.

## Requirements

This tool requires Python 3.x and the PyPDF2 library. You can install the dependency using pp:

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
