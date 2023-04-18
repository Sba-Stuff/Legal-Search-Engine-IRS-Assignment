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
    folders = loadfolders("files/")
    muja = []
    words = []
    for f in folders:
        createsubdirectories("files-clean/",f)

    for folder in folders:
        files = loadfiles("files/"+folder)
        for filer in files:
            words+= readfile("files/"+folder+"/"+filer)
    words = stemmebase(words,"ps")
    dupli = removeduplicate(words)
    dupli.append("ali,ai")
    #print(dupli)
    rsd = removestopwordsbase(dupli)
    writefile("lemits.txt",rsd)

create_clean_corpus()

