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

filer = readfile2("vocabulary.txt")
folders = loadfolders("files-clean/")

for folder in folders:
    for x in filer:
        m = x.replace('\t',',',1)
        l = m.split(',')
        #print(l[0])
        files = loadfiles("files-clean/"+folder)
        for j in files:
            words = []
            words+= readfile("files-clean/"+folder+"/"+j)
        position = 0
        for feo in words:
            position = position+1
            if feo in l[1]:
                print(l[0]+" "+l[1]+"at"+str(position))

#for x in filer:
#    m = x.replace('\t',',',1)
#    l = m.split(',')
#    words = []
#    words+= readfile("files-clean/1.txt")
#    #print(words)
#    position = 0
#    for feo in words:
#        position = position+1
#        if feo in l[1]:
#            print(l[0] l[1]+"at"+str(position))



