from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from removeblanklines import removeemptylines,abstract

def readpdf(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 1
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

#print(readpdf("pdf/civil Appeal/C.A._3_2018.pdf"))
#x  = removeemptylines(readpdf("pdf/civil Appeal/C.A._3_2018.pdf"))
#print(abstract(x))
#y  = removeemptylines(readpdf("pdf/civil Appeal/C.A._3_2018_dt-14-9-2018.pdf"))
#print(abstract(y))