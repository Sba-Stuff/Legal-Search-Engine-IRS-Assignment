#filereader to read files
from filereader import readfile,readfile2
from loader import loadfolders,loadfiles
#for taking logs and math stuff
import math
#for N.
from loader import loadfolders,loadfiles

def getidbydocument(document):
    filer = readfile2("casedocuments.txt")
    for x in filer:
        m = x.replace('\t',',',1)
        l = m.split(',')
        if document in l[1]:
            return l[0]

def getdocumentbyid(id):
    filer = readfile2("casedocuments.txt")
    for x in filer:
        m = x.replace('\t',',',1)
        l = m.split(',')
        if str(id) in str(l[0]):
            return l[1]

def defgetwordbyid(id):
    filer = readfile2("vocabulary.txt")
    for x in filer:
        m = x.replace('\t',',',1)
        l = m.split(',')
        if str(id) in str(l[0]):
            return l[1]


def defgetidbyword(word):
    filer = readfile2("vocabulary.txt")
    for x in filer:
        m = x.replace('\t',',',1)
        l = m.split(',')
        if word in l[1]:
            return l[0]

def rawtermfrequency(termname,documentname):
    f = open(documentname, "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        g = line.split(' ')
        for h in g:
            if str(termname) in str(h):
                count = count+1
    return count

def logtermfrequency(term,document):
       tf = rawtermfrequency(term,document)
       if tf>0:
        ltf = 1+math.log10(tf)
        return ltf
       else:
        return 0

def NumberOfTermsinDocument(documentname):
    f = open(documentname, "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        g = line.split(' ')
        for h in g:
            if h is not "":
                count = count+1
    return count

def loadN(path):
    folders = loadfolders(path)
    count = 0
    for fold in folders:
        files = loadfiles(path+fold)
        for xi in files:
            count = count+1
    return count

def IDF(term,document):
    N = loadN("files-clean/")
    df = rawtermfrequency(term,document)
    if N is not 0 and df is not 0:
        nbydf = N/df
        ans = math.log10(nbydf)
        return ans
    else:
        return 0
def TF_IDF(term,document):
    tf =logtermfrequency(term,document)
    idf = IDF(term,document)
    return tf*idf

def compute_K(k1,b,dl, avdl):
	return k1 * ((1-b) + b * (float(dl)/float(avdl)))

def average_document_length(documentspath):
    N = loadN(documentspath)
    count = 0
    folders = loadfolders(documentspath)
    for fold in folders:
        docs = loadfiles(documentspath+fold)
        for documents in docs:
            f = open(documentspath+fold+"/"+documents, "r")
            lines = f.readlines()
            for line in lines:
                words = line.split(' ')
                for g in words:
                    if g is not "":
                        count = count+1
                    else:
                        count = count+0
    return count/N

def BM25(term,document,documentroot):
    k1=1.5
    b=0.75
    idf = IDF(term,document)
    tf = rawtermfrequency(term,document)
    N = loadN(documentroot)
    K = compute_K(k1,b,N,average_document_length(documentroot))
    denominator = (tf+1)*K
    numerator = tf*(k1+1)
    ans = numerator/denominator
    ans2 = tf*ans
    #print(str(ans))
    return ans2













#from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency
#print(str(defgetidbyword("waji")))
#print(defgetwordbyid(6))
#print(getidbydocument("4.txt"))
#from task3core import defgetidbyword,defgetwordbyid,getdocumentbyid,getidbydocument
#print(str(rawtermfrequency("hay","files-clean/1.txt")))
#print(str(logtermfrequency("waji","files-clean/1.txt")))
#print(NumberOfTermsinDocument("files-clean/1.txt"))
#print(TF_IDF("gya","files-clean/2.txt"))
#print(loadN("files-clean/"))
#print()
#average_document_length("files-clean/")
#BM25("waji","files-clean/1/1.txt","files-clean/")


#print(defgetwordbyid(9582))
#print(defgetwordbyid(8783))
#print(defgetwordbyid(4855))
#print(defgetwordbyid(5894))
#print(defgetwordbyid(2729))
#print(defgetwordbyid(10233))
#print(defgetwordbyid(5884))
#print(defgetwordbyid(5882))
#print(defgetwordbyid(8288))
#print(defgetwordbyid(11134))

##print(defgetwordbyid(2253))
##print(defgetwordbyid(10820))
##print(defgetwordbyid(8846))
##print(defgetwordbyid(2522))
##print(defgetwordbyid(6907))
##print(defgetwordbyid(3370))
##print(defgetwordbyid(8714))
##print(defgetwordbyid(11496))
##print(defgetwordbyid(8381))
##print(defgetwordbyid(5842))



