#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile,readfile2
#function that writes some file with given array.
from filewriter import writefile,writefilenonewline,createsubdirectories
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
#task3core
from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency,getdocumentbyid,logtermfrequency,TF_IDF,BM25,IDF
import math

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
                rrr = IDF(jij,"files-clean/"+folder+"/"+j)
                if rrr is not 0:
                    stringer += str(getidbydocument(j))+":"+str(rrr)+" "
        print(l[0]+" "+stringer)
        indexer.append(l[0]+" "+stringer.strip())


print(indexer)
writefile("idf.txt",indexer)



#N = 146
#df = rawtermfrequency("aadab","files-clean/Suo Moto Case/S.M.C._7_2017_06022019.txt")
#print(str(df))
#if N is not 0 and df is not 0:
#    nbydf = N/df
#    print(str(nbydf))
#    ans = math.log10(nbydf)
#    print(str(ans))