import PyPDF2
pdf_water = open('wtr.pdf', mode='rb')
pdfwtr = PyPDF2.PdfFileReader(pdf_water)
water_mark = pdfwtr.getPage(0)
pdf_super = open('super.pdf', mode='rb')
pdf = PyPDF2.PdfFileReader(pdf_super)
writer = PyPDF2.PdfFileWriter()
pages = pdf.getNumPages()
for i in range(0, pages):
    page = pdf.getPage(i)
    page.mergePage(water_mark)
    writer.addPage(page)
new_file = open('waterpdf.pdf', mode='wb')
writer.write(new_file)
