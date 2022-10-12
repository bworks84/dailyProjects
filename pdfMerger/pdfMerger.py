import PyPDF2
import os

# using library to call merge func
merger = PyPDF2.PdfFileMerger()

# loop through files in current directory,
# make sure it is a pdf  file,
# append one to the other, write new file
#
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write("combinedTest.pdf")
