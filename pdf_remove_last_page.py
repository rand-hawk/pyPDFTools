import PyPDF2

# Open the PDF file for reading
with open('956.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Create a PDF file writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through all pages in the PDF file, except for the last one
    for i in range(num_pages - 1):
        page = pdf_reader.pages[i]
        pdf_writer.add_page(page)

    # Write the modified PDF file to a new file named "output.pdf"
    with open('output.pdf', 'wb') as file:
        pdf_writer.write(file)
