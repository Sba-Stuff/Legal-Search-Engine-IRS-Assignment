from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def stemme(wordarray,stemmer):
    stemmedwords = []
    if "ps" in stemmer:
        ps = PorterStemmer()
    # choose some words to be stemmed
        words = wordarray
        for w in words:
            stemmedwords.append(ps.stem(w))
    if "ls" in stemmer:
        ls = LancasterStemmer()
        # choose some words to be stemmed
        words = wordarray
        for w in words:
            stemmedwords.append(ls.stem(w))
    return stemmedwords
def removestopwords(wordarray):
    stop_words = set(stopwords.words('english'))
    word_tokens = wordarray                     #word_tokenize(example_sent)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def stemmebase(wordarray,stemmer):
    stemmedwords = []
    if "ps" in stemmer:
        ps = PorterStemmer()
    # choose some words to be stemmed
        words = wordarray
        for w in words:
            stemmedwords.append(w+","+ps.stem(w))
    if "ls" in stemmer:
        ls = LancasterStemmer()
        # choose some words to be stemmed
        words = wordarray
        for w in words:
            stemmedwords.append(w+","+ls.stem(w))
    return stemmedwords

def removestopwordsbase(wordarray):
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []
    for gi in wordarray:
        word_tokens = gi.split(',')
        kif = word_tokens[0]
        bif = word_tokens[1]
        if bif not in stop_words and len(bif)>2:
            filtered_sentence.append(kif+","+bif)
    return filtered_sentence

#words=[]
#words.append("these,this")
#words.append("melon,melon")
#words.append("chin,ci")
#words.append("isha,isa")
#print(removestopwordsbase(words))


#words=[]
#words.append("i")
#words.append("am")
#words.append("going")
#words.append("to")
#words.append("pakistan")
#words.append("buy")
#words.append("dolls")
#print("Complete Words")
#print(words)
#cleanwords = removestopwords(words)
#print("Words Without Stop Words")
#print(cleanwords)
#print("Words After PorterStemming")
#print(stemme(cleanwords,"ps"))