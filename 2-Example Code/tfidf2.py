#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile,readfile2
#function that writes some file with given array.
from filewriter import writefile,writefilenonewline,appendfile
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
#task3core
from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency,getdocumentbyid,logtermfrequency,TF_IDF,BM25

tf = readfile2("rtf.txt")
idf = readfile2("ltf.txt")

def normalizeefile(iden,path,savepath):
    tf = readfile2(path)
    stringer = str(iden)
    arr = []
    stringer2=""
    for l in tf:
        if str(iden) in str(l):
            doc = l
            x=0
            doc2 = doc.split(" ")
            for fd in doc2:
                if ":" in fd:
                    stringer2+=fd+" "
                else:
                    stringer2+=fd+";"
    arr.append(stringer+";"+stringer2.strip())
    writefile(savepath,arr)


def get_tf(termid,docid):
    tf = readfile2("rtf.txt")
    for l in tf:
        if str(termid) in str(l):
            doc = l
            doc2 = doc.split(" ")
            for fd in doc2:
                if ":" in fd:
                    g = fd
                    g2 = g.split(":")
                    if str(docid) in str(g2[0]):
                        return(g2[1])

def get_idf(termid,docid):
    tf = readfile2("ltf.txt")
    for l in tf:
        if str(termid) in str(l):
            doc = l
            doc2 = doc.split(" ")
            for fd in doc2:
                if ":" in fd:
                    g = fd
                    g2 = g.split(":")
                    if str(docid) in str(g2[0]):
                        return(g2[1])

def tf_idf(termid,docid):
    return float(get_tf(termid,docid))*float(get_idf(termid,docid))

for x in range(6):
    normalizeefile(x+1,"rtf.txt","rtf2.txt")


