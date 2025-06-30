# PDF Merger 

A Python script to merge multiple PDF files into a single PDF using the `pypdf` library.

## Features

- Accepts any number of PDF files from the user
- Merges them in the entered order
- Outputs a single PDF named `merged-pdf.pdf`

## How to Run

1. Install the required library:
```bash
pip install pypdf
```

2. Place the PDF files in the same directory as the script.

3. Run the script:
```bash
python main.py
```

4. Follow the prompts to enter the number of PDFs and their filenames (e.g., `file1.pdf`, `file2.pdf`, etc.).

## Example

```
How many PDFs do you want to merge?: 2

Enter the name of each PDF file (format: filename.pdf):
PDF 1: file1.pdf
PDF 2: file2.pdf

Merged PDFs successfully.
```

> ✅ Output: A new file named `merged-pdf.pdf` will be created.

## File Structure

```bash
pdf_merger/
├── main.py
└── README.md
```

## Author  
Namrata Tamboli
