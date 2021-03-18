import PyPDF2

# Reader & Writer Example:
# open pdf in binary mode
with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)  # returns page index in this case page 1
    # a few interesting memebrs such as rotate and scale can be found
    page.rotateClockwise(90)

    # the original document is not modify we neeed a writer objec:
    writer = PyPDF2.PdfFileWriter()
    # writer.insertPage(page,0) # insert page in specific index
    # writer.insertBlankPage() # insert a blank page
    writer.addPage(page)  # adds page to the end of file
    with open("rotated.pdf", "wb") as output:  # write in binary
        writer.write(output)

# Merger Example:
merger = PyPDF2.PdfFileMerger()
# in real would you would scan a directory for pdfsand create a list:
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
