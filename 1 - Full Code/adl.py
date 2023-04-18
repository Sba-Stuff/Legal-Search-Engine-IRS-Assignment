#filereader to read files
from filereader import readfile,readfile2
from loader import loadfolders,loadfiles
#for taking logs and math stuff
import math
#for N.
from loader import loadfolders,loadfiles

def average_document_length(documentspath):
    N = 146
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

print(str(average_document_length("files-clean/")))