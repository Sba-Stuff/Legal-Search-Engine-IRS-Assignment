from filereader import readfile,readfile2
from filewriter import writefile,writefilenonewline,createsubdirectories

def gettfidfbyword(word):
    f = open("qories.txt", "r")
    lines = f.readlines()
    for line in lines:
        list = line.split('\t')
        if word in list[0]:
            return list[1]

print(gettfidfbyword("sent"))