import PyPDF2
# pdf file object
# you can find find the pdf file with complete code in below
def readpdf(path):

    pdfFileObj = open(path, 'rb')
# pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
    #print(pdfReader.numPages)
# a page object
    pageObj = pdfReader.getPage(0)
# extracting text from page.
# this will print the text you can also save that into String
    return pageObj.extractText()