# PyPDF2 documentation : https://pypdf.readthedocs.io/en/stable/index.html

from pypdf import PdfWriter  # Import PDF writer

merger = PdfWriter()  # Create merger object
pdfs = []  # List to store PDF file names

# Get number of PDFs to merge
n = int(input("\nHow many PDFs do you want to merge?: "))
print('\n')

# Take input for each PDF file name
print("Enter the name of each PDF file (format: filename.pdf):")
for i in range(n):
    name = input(f"PDF {i+1}: ")
    pdfs.append(name)

# Add each PDF to the merger
for pdf in pdfs:
    merger.append(pdf)

# Write merged PDF to file
merger.write("merged-pdf.pdf")
merger.close()

print("Merged PDFs successfully.")
