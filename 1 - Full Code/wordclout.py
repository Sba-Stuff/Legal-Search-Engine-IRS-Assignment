from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from nltkcore import stemme,removestopwords
from duplicateremover import removeduplicate,hasNumbers,hasNumbers2
from loader import loadfolders,loadfiles
from filereader import readfile
from pdfreader3 import readpdf
from removeblanklines import removeemptylines,abstract
import io
import base64

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

def wordclouder2(sentencei):
    sentence = sentencei
    print(sentence)

    tokens = sentence.split(" ")
    #lemmatizedwords = stemme(tokens,"ps")
    stopwordremovedwords = removestopwords(tokens)
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
    #plt.show()
    figfile = io.BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = base64.b64encode(figfile.getvalue())
    return "<img src='data:image/png;base64,"+str(figdata_png.decode('utf8'))+"' height='200px' width='200px'>"
#files = []
#files.append("files/1.pdf")
#files.append("files/2.pdf")
#wordclouder(files)