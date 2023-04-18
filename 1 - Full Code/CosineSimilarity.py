# Program to measure similarity between
# two sentences using cosine similarity.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from filereader import readfile, readfile2
from task5core import gettfidfbyword,doctermfrequency,getbm25byword


def tfidf_cosine_similarity(query, document):
    X = query
    filer = readfile2(document)
    Y = filer[0]

    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    sw = stopwords.words('english')
    l1 =[];l2 =[]

    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set: l1.append(1/float(gettfidfbyword(w))) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0.0

    #cosine formula
    for i in range(len(rvector)):
            xi = float(l1[i])
            xo = float(l2[i])
            xn = xi*xo
            c+= round(float(xn),3)

    for i in range(0, len(l1)):
        l1[i] = float(l1[i])

    for i in range(0, len(l2)):
        l2[i] = float(l2[i])

    cosine = c / float((sum(l1)*sum(l2))**0.5)
    #print("similarity: ", cosine)
    return round(cosine,5)

def bm25_cosine_similarity(query, document):
    X = query
    filer = readfile2(document)
    Y = filer[0]

    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    sw = stopwords.words('english')
    l1 =[];l2 =[]

    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set: l1.append(1/float(getbm25byword(w))) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0.0

    #cosine formula
    for i in range(len(rvector)):
            xi = float(l1[i])
            xo = float(l2[i])
            xn = xi*xo
            c+= round(float(xn),3)

    for i in range(0, len(l1)):
        l1[i] = float(l1[i])

    for i in range(0, len(l2)):
        l2[i] = float(l2[i])

    cosine = c / float((sum(l1)*sum(l2))**0.5)
    #print("similarity: ", cosine)
    return round(cosine,5)


#query = input("Query: ").lower()
#Z = input("Document Path: ").lower()
#document = "files-clean/civil Appeal/C.A._3_2018.txt"
#print(str(tfidf_cosine_similarity(query,document)))
#print(str(bm25_cosine_similarity(query,document)))