from filereader import readfile,readfile2
from filewriter import writefile,writefilenonewline,createsubdirectories
from task3core import defgetwordbyid

def wordagainstid():
    lines = readfile2("Preprocessedlist.csv")
    sum = []
    sum.append("Terms"+"\t"+"TFIDF"+"\t"+"BM25")
    for c in lines:
        lin1 = c.split(',')
        for f in lin1:
            id = lin1[0]
            tfidf = lin1[1]
            bm25 = lin1[2]
            word =  defgetwordbyid(id)
        sum.append(word+"\t"+str(tfidf)+"\t"+bm25)
    writefile("finallist.txt",sum)

wordagainstid()
print("done")