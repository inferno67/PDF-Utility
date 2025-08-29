import PyPDF2

# -------- Merge PDFs --------
def merge_pdfs(pdf_list, output_file):
    """
    Merges a list of PDF files into a single output file.
    
    Args:
        pdf_list (list): A list of paths to the PDF files to merge.
        output_file (str): The path for the merged output PDF.
    """
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    
    with open(output_file, "wb") as f:
        merger.write(f)
    
    merger.close()
    print(f"Merged PDFs saved as '{output_file}'")

# -------- Split PDF --------
def split_pdf(input_file, start_page, end_page, output_file):
    """
    Splits a PDF, saving a specific page range to a new file.
    
    Args:
        input_file (str): The path to the input PDF file.
        start_page (int): The starting page number (1-indexed).
        end_page (int): The ending page number (inclusive).
        output_file (str): The path for the split output PDF.
    """
    reader = PyPDF2.PdfReader(input_file)
    writer = PyPDF2.PdfWriter()
    
    # Pages in PyPDF2 are zero-indexed, so we subtract 1
    for i in range(start_page - 1, end_page):
        # Check if the page number is valid
        if 0 <= i < len(reader.pages):
            writer.add_page(reader.pages[i])
        else:
            print(f"Warning: Page {i + 1} is out of range for the input PDF.")
            
    if writer.pages:
        with open(output_file, "wb") as f:
            writer.write(f)
        print(f"Split PDF saved as '{output_file}'")
    else:
        print("No pages were written to the output file.")

# -------- Main Execution Block --------
# This code will only run when the script is executed directly.
if __name__ == "__main__":
    # Example usage:
    # NOTE: To run this, you need to have files like 'report1.pdf' and 'report2.pdf'
    # in the same folder as this script.
    
    # Example 1: Merge two PDFs
    # merge_pdfs(["report1.pdf", "report2.pdf"], "combined_reports.pdf")

    # Example 2: Split a PDF
    # This will create a new PDF containing pages 1-3 from 'long_document.pdf'.
    # split_pdf("long_document.pdf", 1, 3, "first_three_pages.pdf")
    
    print("PDF tool functions are ready to use.")
    print("To use the examples, uncomment the function calls above.")