import PyPDF2

# Get the page number to be deleted from the user
page_number = int(input("Enter the page number to be deleted: "))

# Open the PDF file for reading
with open('input.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Check if the page number is valid
    if page_number < 1 or page_number > num_pages:
        print("Invalid page number")
        exit()

    # Create a PDF file writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through all pages in the PDF file, except for the page to be deleted
    for i in range(num_pages):
        if i != page_number - 1:
            page = pdf_reader.pages[i]
            pdf_writer.add_page(page)

    # Write the modified PDF file to a new file named "output.pdf"
    with open('output.pdf', 'wb') as file:
        pdf_writer.write(file)
