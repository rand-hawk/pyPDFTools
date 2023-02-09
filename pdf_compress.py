from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

page_no = 1
print(f'please wait, processing pages...')
for page in reader.pages:
    print(f'...{page_no}')
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)
    page_no = page_no + 1

with open("compressed_output.pdf", "wb") as f:
    writer.write(f)