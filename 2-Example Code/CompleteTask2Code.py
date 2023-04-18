#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#filereader to read files
from filereader import readfile
#function that writes some file with given array.
from filewriter import writefile
#functions for stemming and stopwords removal
from nltkcore import stemme,removestopwords
#function to remove duplicate words and such words containing some number
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
#dynamic array to load all casses categories
case_categories = []

# dynamic array get words from all the corpus documents
words =  []

#load cases folders from pdf folder, load in case_categories array and print it out.
case_categories = loadfolders("txt/")
print(case_categories)

documentidentifier=1
idetifieddocuments=[]
#words extraction code.
for cases in case_categories:
    judgements = loadfiles("txt/"+cases+"/")
    #print(judgements)
    for file in judgements:
        print("Reading File To Extract Words "+file)
        words+= readfile("txt/"+cases+"/"+file)
        idetifieddocuments.append(str(documentidentifier)+"\t"+file)
        documentidentifier = documentidentifier+1
#print(documentidentifier)
#print(words)


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

accuratewords = []
for new_word in sortedwords:
    if "no" in hasNumbers2(str(new_word)):
        accuratewords.append(new_word)
    #else:
        #print(str(new_word)+"ignored")
#print(accuratewords)

identifier = 1
identifiedwords = []
for wordstoidentify in accuratewords:
     if len(wordstoidentify) >=3:
        identifiedwords.append(str(identifier)+"\t"+wordstoidentify)
        identifier = identifier+1
print(identifiedwords)

writefile("casedocuments.txt",idetifieddocuments)
writefile("vocabulary.txt",identifiedwords)






