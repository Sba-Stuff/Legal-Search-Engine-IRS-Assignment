from nltkcore import stemme,removestopwords
from duplicateremover import removeduplicate
def readfile(filepath):
    words = []
    f = open(filepath, "r")
    lines = f.readlines()
    for line in lines:
        list = line.split(' ')
        for tokens in list:
            stringly = ''.join(e for e in tokens if e.isalnum())
            words.append(stringly.lower())
    while '' in words:
        words.remove('')
    return words

def readfile2(filepath):
    words = []
    f = open(filepath, "r")
    lines = f.readlines()
    for line in lines:
            words.append(line)
    return words

#words= readfile("check.txt")
#print("File Readed These Are Words")
#print(words)

#print("Porter Stemmer Lemmatization Applied, These are the Words")
#lemmatizedwords = stemme(words,"ps")
#print(lemmatizedwords)

#print("Stopwords These Are The Words")
#stopwordremovedwords = removestopwords(lemmatizedwords)
#print(stopwordremovedwords)

#print("Duplicates Removed These Are The Words")
#singlewords = removeduplicate(stopwordremovedwords)
#print(singlewords)

#print("Words Sorted")
#sortedwords = sorted(singlewords)
#print(sortedwords)


