#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile,readfile2
#function that writes some file with given array.
from filewriter import writefile,writefilenonewline,createsubdirectories
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
#task3core
from task3core import getidbydocument,defgetwordbyid,defgetidbyword,rawtermfrequency,getdocumentbyid,logtermfrequency,TF_IDF,BM25


#Creating Clean Corpus, That have stopwords removed, lemmatized words.
def create_clean_corpus():
    folders = loadfolders("files/")

    for f in folders:
        createsubdirectories("files-clean/",f)

    for folder in folders:
        files = loadfiles("files/"+folder)
        for filer in files:
            words = []
            words+= readfile("files/"+folder+"/"+filer)
            lemmatizedwords = stemme(words,"ps")
            stopwordremovedwords = removestopwords(lemmatizedwords)
            cleanwords = []
            for eachword in stopwordremovedwords:
                cleanwords.append(eachword)
            #print(cleanwords)
            writefilenonewline("files-clean/"+folder+"/"+filer,cleanwords)

#Calculator Raw Term Frequency or TF And Save in RTF.txt
def calculate_raw_term_frequency():
    filer = readfile2("vocabulary.txt")
    indexer = []
    folders = loadfolders("files-clean/")
    for x in filer:
        stringer = ""
        m = x.replace('\t',',',1)
        l = m.split(',')
                #print(l[0])
        for folder in folders:
            files = loadfiles("files-clean/"+folder+"/")
            for j in files:
                jij = str(l[1]).strip()
                rrr = rawtermfrequency(jij,"files-clean/"+folder+"/"+j)
                if rrr is not 0:
                    stringer += str(getidbydocument(j))+":"+str(rawtermfrequency(jij,"files-clean/"+folder+"/"+j))+" "
        print(l[0]+" "+stringer)
        indexer.append(l[0]+" "+stringer.strip())

    print(indexer)
    writefile("rtf.txt",indexer)

#Calculator Log Frequency or IDF And Save in IDF.txt
def calculate_log_frequency():
    filer = readfile2("vocabulary.txt")
    indexer = []
    folders = loadfolders("files-clean/")
    for x in filer:
        stringer = ""
        m = x.replace('\t',',',1)
        l = m.split(',')
                #print(l[0])
        for folder in folders:
            files = loadfiles("files-clean/"+folder+"/")
            for j in files:
                jij = str(l[1]).strip()
                rrr = logtermfrequency(jij,"files-clean/"+folder+"/"+j)
                if rrr is not 0:
                    dfi = round(logtermfrequency(jij,"files-clean/"+folder+"/"+j),3)
                    stringer += str(getidbydocument(j))+":"+str(dfi)+" "
        print(l[0]+" "+stringer)
        indexer.append(l[0]+" "+stringer.strip())

    print(indexer)
    writefile("ltf.txt",indexer)

#Calculator TF X IDF And Save in tfidf.txt
def calculate_tf_idf():
    filer = readfile2("vocabulary.txt")
    indexer = []
    folders = loadfolders("files-clean/")
    for x in filer:
        stringer = ""
        m = x.replace('\t',',',1)
        l = m.split(',')
                #print(l[0])
        for folder in folders:
            files = loadfiles("files-clean/"+folder+"/")
            for j in files:
                jij = str(l[1]).strip()
                rrr = TF_IDF(jij,"files-clean/"+folder+"/"+j)
                if rrr is not 0:
                    dfi = str(round(TF_IDF(jij,"files-clean/"+folder+"/"+j),3))
                    stringer += str(getidbydocument(j))+":"+dfi+" "
        print(l[0]+" "+stringer)
        indexer.append(l[0]+" "+stringer.strip())

    print(indexer)
    writefile("tfidf.txt",indexer)

#Calculator BM25 And Save in BM25.txt
def calculate_BM25():
    filer = readfile2("vocabulary.txt")
    indexer = []
    folders = loadfolders("files-clean/")
    for x in filer:
        stringer = ""
        m = x.replace('\t',',',1)
        l = m.split(',')
                #print(l[0])
        for folder in folders:
            files = loadfiles("files-clean/"+folder+"/")
            for j in files:
                jij = str(l[1]).strip()
                rrr = BM25(jij,"files-clean/"+folder+"/"+j,"files-clean/")
                if rrr is not 0:
                    dfi = str(round(BM25(jij,"files-clean/"+folder+"/"+j,"files-clean/"),2))
                    stringer += str(getidbydocument(j))+":"+dfi+" "
        print(l[0]+" "+stringer)
        indexer.append(l[0]+" "+stringer.strip())

    print(indexer)
    writefile("BM25.txt",indexer)

#Calling All Above Functions
#print("Cleaning Corpus")
#create_clean_corpus()
print("Calculating TF")
calculate_raw_term_frequency()
print("Calculating iDF")
calculate_log_frequency()
print("Calculating TF-IDF")
calculate_tf_idf()
print("Calculating BM25")
calculate_BM25()
print("Done")

