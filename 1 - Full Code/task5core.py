from filereader import readfile,readfile2
from filewriter import writefile,writefilenonewline,createsubdirectories

def gettfidfbyword(word):
    f = open("finallist.txt", "r")
    lines = f.readlines()
    for line in lines:
        list = line.split('\t')
        if list[0] in word:
            return list[1].strip()

#print(gettfidfbyword("per"))

def getbm25byword(word):
    f = open("finallist.txt", "r")
    lines = f.readlines()
    for line in lines:
        list = line.split('\t')
        if list[0] in word:
            return list[2].strip()

def doctermfrequency(word, doc):
    count = 0
    stro = readfile(doc)
    #print(stro)
    for j in stro:
        if word == j:
            count=count+1
    return count


#doctermfrequency("suprem","files-clean/civil Appeal/C.A._3_2018.txt")