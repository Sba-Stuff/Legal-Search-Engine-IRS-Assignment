#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile
#function that writes some file with given array.
from filewriter import writefile,writefilenonewline,createsubdirectories
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2

folders = loadfolders("files/")

for f in folders:
        createsubdirectories("files-clean/",f)

for folder in folders:
    files = loadfiles("files/"+folder)
    for filer in files:
        words = []
        words+= readfile("files/"+folder+"/"+filer)
        lemmatizedwords = stemme(words,"ps")
        stopwordremovedwords = removestopwords(lemmatizedwords)
        cleanwords = []
        for eachword in stopwordremovedwords:
            cleanwords.append(eachword)
        #print(cleanwords)
        writefilenonewline("files-clean/"+folder+"/"+filer,cleanwords)



