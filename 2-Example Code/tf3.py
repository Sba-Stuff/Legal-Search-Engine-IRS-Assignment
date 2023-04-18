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

#for x in filer:
    #m = x.replace('\t',',',1)
    #l = m.split(',')
    #print(l[0])
    #files = loadfiles("files-clean/")
    #for j in files:
    #   filer = readfile("files-clean/"+j)
    #   words = []
    #   words+= readfile("files-clean/"+j)
    #   position = 1
    #   for xen in words:
    #    print(words)
    #    if l[1] in xen:
    #        print("files-clean/"+j+" "+l[1]+str(position))
    #        position = position+1

for x in filer:
    m = x.replace('\t',',',1)
    l = m.split(',')
    words = []
    words+= readfile("files-clean/1.txt")
    #print(words)
    position = 0
    for feo in words:
        position = position+1
        if feo in l[1]:
            print(l[0]+" "+l[1]+"at"+str(position))



