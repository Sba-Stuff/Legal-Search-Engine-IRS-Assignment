import sys
from operator import add
import numpy as np
from collections import OrderedDict
#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile,readfile2
#function that writes some file with given array.
from filewriter import writefile
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency,getdocumentbyid,logtermfrequency,TF_IDF,BM25

a = sys.argv[1]
words = a.split(" ")
lemmatizedwords = stemme(words,"ps")
print("Porter Stemmer Lemmatization Applied")
#print(lemmatizedwords)

stopwordremovedwords = removestopwords(lemmatizedwords)
print("Stopwords Removed")
#print(stopwordremovedwords)

singlewords = removeduplicate(stopwordremovedwords)
print("Duplicates Removed")
#print(singlewords)

sortedwords = sorted(singlewords)
print("Words Sorted")
#print(sortedwords)

wordids= []
for neon in sortedwords:
     wordids.append(defgetidbyword(neon))

#print(wordids)

searchings=[]
filer = readfile2("tfidf.txt")
for x in filer:
    stringer = ""
    m = x.replace(' ',',',1)
    l = m.split(',')
    for wids in wordids:
        if wids in l[0]:
            sf = l[1].split(' ')
            searchings.append(sf)
#print(searchings)

##scores = []
##for score in searchings:
##    ls = score
##    for df in ls:
##        mengal = df.split(":")
##        for j in range(4):
##            soc = ""
##            if str(j+1) in mengal[0]:
##                scores.append(mengal[1])

scores = []
for score in searchings:
    ls = score
    slist = [e[2:] for e in ls]
    scores.append(slist)

scores2 = []
for item in scores:
    #scores2.append([float(i[1:]) for i in item])
    for i in item:
        if ":" in str(i):
            print(i)
            scores2.append(float(i[1:]))
        else:
            print(i)
            scores2.append(float(i))


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def ranker(scores2):
    scores3 = []
    if len(scores2) is 1:
            scores3.append(scores2[0])

    if len(scores2) is 2:
        for a, b in zip(scores2[0], scores2[1]):
            scores3.append(float(a)+float(b))

    if len(scores2) is 3:
        for a, b, c in zip(scores2[0], scores2[1], scores[2]):
            scores3.append(float(a)+float(b)+float(c))

    if len(scores2) is 4:
        for a, b, c,d in zip(scores2[0], scores2[1], scores[2],scores[3]):
            scores3.append(float(a)+float(b)+float(c)+float(d))

    if len(scores2) is 5:
        for a, b, c,d,e in zip(scores2[0], scores2[1], scores[2],scores[3],scores[4]):
            scores3.append(float(a)+float(b)+float(c)+float(d)+float(e))

    if len(scores2) is 6:
        for a, b, c,d,e,f in zip(scores2[0], scores2[1], scores[2],scores[3],scores[4],scores[5]):
            scores3.append(float(a)+float(b)+float(c)+float(d)+float(e)+float(f))

    if len(scores2) is 7:
        for a, b, c,d,e,f,g in zip(scores2[0], scores2[1], scores[2],scores[3],scores[4],scores[5],scores[6]):
            scores3.append(float(a)+float(b)+float(c)+float(d)+float(e)+float(f)+float(g))

    if len(scores2) is 8:
        for a,b,c,d,e,f,g,h in zip(scores2[0], scores2[1], scores[2],scores[3],scores[4],scores[5],scores[6],scores[7]):
            scores3.append(float(a)+float(b)+float(c)+float(d)+float(e)+float(f)+float(g)+float(h))

    if len(scores2) is 9:
        for a, b, c,d,e,f,g,h,i in zip(scores2[0], scores2[1], scores[2],scores[3],scores[4],scores[5],scores[6],scores[7],scores[8]):
            scores3.append(float(a)+float(b)+float(c)+float(d)+float(e)+float(f)+float(g)+float(h)+float(i))

    if len(scores2) is 10:
        for a, b, c,d,e,f,g,h,i,j in zip(scores2[0], scores2[1], scores[2],scores[3],scores[4],scores[5],scores[6],scores[7],scores[8],scores[9]):
            scores3.append(float(a)+float(b)+float(c))
            scores3.append(float(a)+float(b)+float(c)+float(d)+float(e)+float(f)+float(g)+float(h)+float(i)+float(j))

    scores4 = []
    count = 1
    for sc in scores3:
        scores4.append(str(count))
        scores4.append(str(sc))
        count = count+1

    #print(Convert(scores4))
    score5 = Convert(scores4)

    sort_orders = sorted(score5.items(), key=lambda x: x[1], reverse=True)
    beo = []
    for i in sort_orders:
    	beo.append(i[0]+":"+i[1])
    return beo

print(ranker(scores2))