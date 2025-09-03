import sys
import argparse
import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter, errors
from tqdm import tqdm # type: ignore
import fitz  # type: ignore # PyMuPDF

def merge_pdfs(input_files, output_file, optimize=False, password=None):
    """
    Merges multiple PDF files into a single output file.
    """
    if os.path.exists(output_file):
        print(f"Error: Output file '{output_file}' already exists. Use the --force flag to overwrite.")
        return

    print(f"Starting to merge {len(input_files)} files.")
    merger = PdfMerger()

    try:
        # Use a progress bar for the merging loop
        for filename in tqdm(input_files, desc="Merging Files", unit="file"):
            if not os.path.exists(filename):
                print(f"\nError: Input file '{filename}' not found. Aborting.")
                merger.close()
                return
            
            reader = PdfReader(filename)
            if reader.is_encrypted:
                if password:
                    reader.decrypt(password)
                else:
                    print(f"\nError: File '{filename}' is password protected. Use --password.")
                    merger.close()
                    return
                    
            merger.append(reader)
        
        if password:
            merger.encrypt(password) # pyright: ignore[reportAttributeAccessIssue]

        merger.write(output_file)
        merger.close()
        
        print(f"Successfully merged files into {output_file}.")
        
        # Optimization step
        if optimize:
            optimize_pdf(output_file)

    except errors.PdfReadError:
        print(f"\nError: One of the files is not a valid PDF or a password issue occurred.")
    except Exception as e:
        print(f"\nAn unexpected error occurred during merging: {e}")

def split_pdfs(input_file, start_page, end_page, output_file, optimize=False, password=None):
    """
    Splits a single PDF file, extracting a range of pages.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return
    
    if os.path.exists(output_file):
        print(f"Error: Output file '{output_file}' already exists. Use the --force flag to overwrite.")
        return

    print(f"Starting to split file: {input_file}")
    
    try:
        reader = PdfReader(input_file)
        if reader.is_encrypted:
            if password:
                reader.decrypt(password)
            else:
                print(f"\nError: File '{input_file}' is password protected. Use --password.")
                return
                
        writer = PdfWriter()
        total_pages = len(reader.pages)

        if start_page < 1 or end_page > total_pages or start_page > end_page:
            print(f"Error: Invalid page range. Your PDF has {total_pages} pages.")
            return

        for page_num in tqdm(range(start_page - 1, end_page), desc="Splitting Pages", unit="page"):
            writer.add_page(reader.pages[page_num])
        
        if password:
            writer.encrypt(password)

        with open(output_file, 'wb') as f:
            writer.write(f)
            
        print(f"Successfully split pages into {output_file}.")
        
        if optimize:
            optimize_pdf(output_file)

    except errors.PdfReadError:
        print(f"\nError: The input file is not a valid PDF or a password issue occurred.")
    except Exception as e:
        print(f"An unexpected error occurred during splitting: {e}")

def rotate_pdfs(input_file, output_file, rotation_degrees=0, optimize=False, password=None):
    """
    Rotates all pages in a PDF by a specified degree.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    if os.path.exists(output_file):
        print(f"Error: Output file '{output_file}' already exists. Use the --force flag to overwrite.")
        return
    
    if rotation_degrees not in [90, 180, 270]:
        print("Error: Rotation degrees must be 90, 180, or 270.")
        return

    print(f"Rotating pages in '{input_file}' by {rotation_degrees} degrees.")

    try:
        reader = PdfReader(input_file)
        if reader.is_encrypted:
            if password:
                reader.decrypt(password)
            else:
                print(f"\nError: File '{input_file}' is password protected. Use --password.")
                return

        writer = PdfWriter()
        total_pages = len(reader.pages)

        for page_num in tqdm(range(total_pages), desc="Rotating Pages", unit="page"):
            page = reader.pages[page_num]
            page.rotate(rotation_degrees)
            writer.add_page(page)

        if password:
            writer.encrypt(password)

        with open(output_file, 'wb') as f:
            writer.write(f)
            
        print(f"Successfully rotated pages and saved to {output_file}.")

        if optimize:
            optimize_pdf(output_file)

    except Exception as e:
        print(f"An error occurred during rotation: {e}")

def crop_pdfs(input_file, output_file, page_number, x0, y0, x1, y1, optimize=False, password=None):
    """
    Crops a specified page of a PDF to a given rectangle.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    if os.path.exists(output_file):
        print(f"Error: Output file '{output_file}' already exists. Use the --force flag to overwrite.")
        return

    print(f"Cropping page {page_number} of '{input_file}' to create '{output_file}'...")

    try:
        doc = fitz.open(input_file)
        if doc.is_encrypted:
            if password:
                doc.authenticate(password)
            else:
                print(f"Error: File '{input_file}' is password protected. Use --password.")
                return

        page_index = page_number - 1
        if not 0 <= page_index < len(doc):
            print(f"Error: Invalid page number. The PDF has {len(doc)} pages.")
            return

        page = doc[page_index]
        rect = fitz.Rect(x0, y0, x1, y1)
        page.set_cropbox(rect)

        # Create a new document with just the cropped page
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=page_index, to_page=page_index)
        
        new_doc.save(output_file)
        new_doc.close()
        doc.close()
        
        print(f"Successfully cropped page {page_number} and saved to {output_file}.")

        if optimize:
            optimize_pdf(output_file)
    except Exception as e:
        print(f"An error occurred during cropping: {e}")

def optimize_pdf(file_path):
    """
    Optimizes a PDF file to reduce its size using PyMuPDF.
    """
    try:
        doc = fitz.open(file_path)
        doc.ez_save(file_path, garbage=4, clean=True)
        print(f"Successfully optimized {file_path}.")
    except Exception as e:
        print(f"Failed to optimize PDF: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple command-line utility for managing PDF files."
    )
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Merge command parser
    merge_parser = subparsers.add_parser('merge', help='Merge multiple PDFs into one')
    merge_parser.add_argument('input_files', nargs='+', help='List of input PDF files')
    merge_parser.add_argument('output_file', help='The name of the output PDF file')
    merge_parser.add_argument('-o', '--optimize', action='store_true', help='Optimize the output PDF to reduce size')
    merge_parser.add_argument('-p', '--password', help='Password for encrypted PDFs')
    merge_parser.add_argument('-f', '--force', action='store_true', help='Force overwrite existing output file')

    # Split command parser
    split_parser = subparsers.add_parser('split', help='Split a single PDF into a smaller file')
    split_parser.add_argument('input_file', help='The name of the PDF to split')
    split_parser.add_argument('start_page', type=int, help='The starting page number (inclusive)')
    split_parser.add_argument('end_page', type=int, help='The ending page number (inclusive)')
    split_parser.add_argument('output_file', help='The name of the output PDF file')
    split_parser.add_argument('-o', '--optimize', action='store_true', help='Optimize the output PDF to reduce size')
    split_parser.add_argument('-p', '--password', help='Password for encrypted PDFs')
    split_parser.add_argument('-f', '--force', action='store_true', help='Force overwrite existing output file')

    # Rotate command parser
    rotate_parser = subparsers.add_parser('rotate', help='Rotate all pages in a PDF')
    rotate_parser.add_argument('input_file', help='The name of the PDF to rotate')
    rotate_parser.add_argument('rotation', type=int, help='Rotation degrees (90, 180, or 270)')
    rotate_parser.add_argument('output_file', help='The name of the output PDF file')
    rotate_parser.add_argument('-o', '--optimize', action='store_true', help='Optimize the output PDF to reduce size')
    rotate_parser.add_argument('-p', '--password', help='Password for encrypted PDFs')
    rotate_parser.add_argument('-f', '--force', action='store_true', help='Force overwrite existing output file')

    # Crop command parser
    crop_parser = subparsers.add_parser('crop', help='Crop a specific page of a PDF')
    crop_parser.add_argument('input_file', help='The input PDF file')
    crop_parser.add_argument('page_number', type=int, help='The page number to crop (1-based)')
    crop_parser.add_argument('x0', type=float, help='x-coordinate of the top-left corner')
    crop_parser.add_argument('y0', type=float, help='y-coordinate of the top-left corner')
    crop_parser.add_argument('x1', type=float, help='x-coordinate of the bottom-right corner')
    crop_parser.add_argument('y1', type=float, help='y-coordinate of the bottom-right corner')
    crop_parser.add_argument('output_file', help='The output PDF file')
    crop_parser.add_argument('-o', '--optimize', action='store_true', help='Optimize the output PDF to reduce size')
    crop_parser.add_argument('-p', '--password', help='Password for encrypted PDFs')
    crop_parser.add_argument('-f', '--force', action='store_true', help='Force overwrite existing output file')

    args = parser.parse_args()

    # Before calling the function, handle the overwrite logic
    if args.command in ['merge', 'split', 'rotate', 'crop']:
        if os.path.exists(args.output_file) and not args.force:
            print(f"Error: The output file '{args.output_file}' already exists. Use the --force flag to overwrite it.")
            sys.exit(1)

    if args.command == 'merge':
        merge_pdfs(args.input_files, args.output_file, args.optimize, args.password)
    elif args.command == 'split':
        split_pdfs(args.input_file, args.start_page, args.end_page, args.output_file, args.optimize, args.password)
    elif args.command == 'rotate':
        rotate_pdfs(args.input_file, args.output_file, args.rotation, args.optimize, args.password)
    elif args.command == 'crop':
        crop_pdfs(args.input_file, args.output_file, args.page_number, args.x0, args.y0, args.x1, args.y1, args.optimize, args.password)
    else:
        parser.print_help()