import os
import PyPDF2

# Get a list of all PDF files in the current directory
pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]

# Sort the list of PDF files in ascending order
pdf_files.sort()

# Create a PDF file merger object
merger = PyPDF2.PdfMerger()

# Iterate through all PDF files, opening each one and adding it to the merger
for pdf in pdf_files:
    with open(pdf, 'rb') as file:
        merger.append(file)

# Write the combined PDF file to a new file named "combined.pdf"
with open('form_956_combined.pdf', 'wb') as file:
    merger.write(file)
