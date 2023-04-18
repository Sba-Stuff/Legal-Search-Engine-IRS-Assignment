from loader import loadfolders,loadfiles
from CosineSimilarity import  tfidf_cosine_similarity,bm25_cosine_similarity
from filewriter import writefile

folders = loadfolders("files-clean/")

tfidfweighting = []
bm25weighting = []
query_terms = []
query_terms.append("judg hear thi")
query_terms.append("judg juri")
query_terms.append("suprem court hear")
query_terms.append("present court")
query_terms.append("suprem court juri")

for quer in query_terms:
    print("Query Term: "+quer)
    tfidfweighting.append("Query Term: "+quer)
    print("Weighting Scheme: "+"TFIDF")
    tfidfweighting.append("Weighting Scheme: "+"TFIDF")
    for folder in folders:
        query = quer
        files = loadfiles("files-clean/"+folder+"/")
        for filegotten in files:
            print(filegotten.replace("txt","pdf")+"\t"+str(tfidf_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten)))
            tfidfweighting.append(filegotten.replace("txt","pdf")+"\t"+str(tfidf_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten)))
    print("\n")
    tfidfweighting.append("\n")

for quer in query_terms:
    print("Query Term: "+quer)
    bm25weighting.append("Query Term: "+quer)
    print("Weighting Scheme: "+"BM25")
    bm25weighting.append("Weighting Scheme: "+"BM25")
    for folder in folders:
        query = quer
        files = loadfiles("files-clean/"+folder+"/")
        for filegotten in files:
            print(filegotten.replace("txt","pdf")+"\t"+str(bm25_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten)))
            bm25weighting.append(filegotten.replace("txt","pdf")+"\t"+str(bm25_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten)))
    print("\n")
    bm25weighting.append("\n")

writefile("task5TFIDFweights",tfidfweighting)
writefile("task5BM25weights",bm25weighting)

