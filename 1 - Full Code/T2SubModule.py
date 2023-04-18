#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile,readfile2
#function that writes some file with given array.
from filewriter import writefile,writefilenonewline,createsubdirectories
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords,stemmebase,removestopwordsbase
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
#task3core
from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency,getdocumentbyid,logtermfrequency,TF_IDF,BM25


#Creating Clean Corpus, That have stopwords removed, lemmatized words.
def create_clean_corpus():
    folders = loadfolders("txt/")
    muja = []
    words = []
    for folder in folders:
        files = loadfiles("txt/"+folder)
        for filer in files:
            words+= readfile("txt/"+folder+"/"+filer)
    words = stemmebase(words,"ps")
    dupli = removeduplicate(words)
    #print(dupli)
    jaga=[]
    rsd = removestopwordsbase(dupli)
    mnd = sorted(rsd)
    for fd in mnd:
        if "no" in hasNumbers2(fd):
            jaga.append(fd)
    identifier = 1
    identifiedwords = []
    for wordstoidentify in jaga:
        if len(wordstoidentify) >=3:
            identifiedwords.append(str(identifier)+"\t"+wordstoidentify)
            identifier = identifier+1
    writefile("lemits.txt",identifiedwords)

create_clean_corpus()

