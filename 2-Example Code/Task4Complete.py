from filereader import readfile,readfile2
from filewriter import writefile,writefilenonewline,createsubdirectories

def tfidfsum():
    sum = []
    lines = readfile2("tfidf.txt")
    for c in lines:
        lin1 = c.split(' ')
        sumi = 0.0
        for f in lin1:
            id = lin1[0]
            if ":" in f:
                g = f.split(":")
                sumi = float(sumi)+float(g[1])
        sum.append(str(id)+" "+str(round(sumi,3)))
    writefile("tfidfsum.txt",sum)

def bm25sum():
    sum = []
    lines = readfile2("bm25.txt")
    for c in lines:
        lin1 = c.split(' ')
        sumi = 0.0
        for f in lin1:
            id = lin1[0]
            if ":" in f:
                g = f.split(":")
                sumi = float(sumi)+float(g[1])
        sum.append(str(id)+" "+str(round(sumi,3)))
    writefile("bm25sum.txt",sum)

tfidfsum()
bm25sum()
print("Done")