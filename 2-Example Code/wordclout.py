from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from nltkcore import stemme,removestopwords
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
from loader import loadfolders,loadfiles
from filereader import readfile
from pdfreader3 import readpdf
from removeblanklines import removeemptylines,abstract

def wordclouder(files10):
    files = files10
    sentence = ""
    arr = []
    #for cases in files:
    #        arr+= removeemptylines(readpdf(cases))
    #print(arr)
    for ioo in files:
        sentence = sentence+removeemptylines(readpdf(ioo))+" "

    print(sentence)

    tokens = sentence.split(" ")
    lemmatizedwords = stemme(tokens,"ps")
    stopwordremovedwords = removestopwords(lemmatizedwords)
    accuratewords = []
    for new_word in stopwordremovedwords:
        if "no" in hasNumbers2(str(new_word)):
            accuratewords.append(new_word)
    tokens = accuratewords
    comment_words = ''

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        comment_words += " ".join(tokens)+" "

    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    min_font_size = 10).generate(comment_words)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

#files = []
#files.append("files/1.pdf")
#files.append("files/2.pdf")
#wordclouder(files)