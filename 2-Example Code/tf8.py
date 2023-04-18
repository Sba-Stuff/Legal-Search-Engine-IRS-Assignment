#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile,readfile2
#function that writes some file with given array.
from filewriter import writefile,writefilenonewline
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
#task3core
from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency,getdocumentbyid,logtermfrequency,TF_IDF

filer = readfile2("vocabulary.txt")
indexer = []
folders = loadfolders("files-clean/")
for x in filer:
    stringer = ""
    m = x.replace('\t',',',1)
    l = m.split(',')
            #print(l[0])
    for folder in folders:
        files = loadfiles("files-clean/"+folder+"/")
        for j in files:
            jij = str(l[1]).strip()
            stringer += str(getidbydocument(j))+":"+str(TF_IDF(jij,"files-clean/"+folder+"/"+j))+" "
    print(l[0]+" "+stringer)
    indexer.append(l[0]+" "+stringer.strip())

print(indexer)
writefile("tfidf.txt",indexer)
#stringer += str(getidbydocument(j))+":"+str(logtermfrequency(jij,"files-clean/"+folder+"/"+j))+" "





