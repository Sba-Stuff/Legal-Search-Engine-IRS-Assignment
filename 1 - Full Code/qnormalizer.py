from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
from nltkcore import stemme,removestopwords

def querynormalizer(quer):
    query = quer.lower()
    q = query.split(" ")
    normalizedquery=""
    words=[]
    singlewords=[]
    lemmatizedwords = []
    for qa in q:
        words.append(qa)
    lemmatizedwords = stemme(words,"ps")
    stopwordremovedwords = removestopwords(lemmatizedwords)
    singlewords = removeduplicate(stopwordremovedwords)
    #print(singlewords)
    for qi in singlewords:
        normalizedquery+=qi+" "
    return normalizedquery[:-1]

#print(querynormalizer("judge hearing thief"))


