
from loader import loadfolders,loadfiles
from CosineSimilarity import  tfidf_cosine_similarity,bm25_cosine_similarity
from filewriter import writefile
import sys
from removeblanklines import removeemptylines,abstract
from pdfreader3 import readpdf
from wordclout import wordclouder2
import io


static_url="http://127.0.0.1:5000/"
def tfidfsearcher(queri,pagi):
    folders = loadfolders("files-clean/")
    xieon =""
    #query = sys.argv[1]
    query=queri
    results=[]
    if(pagi=="" and pagi=="Search"):
        page = 1
    else:
        page = int(pagi)

    for folder in folders:
        files = loadfiles("files-clean/"+folder+"/")
        for filegotten in files:
            x  = removeemptylines(readpdf("pdf/"+folder+"/"+filegotten.replace("txt","pdf")))
            y=abstract(x)
            #results.append(str(tfidf_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten))+",""files-clean/"+folder+"/"+filegotten.replace("txt","pdf")+","+abstract(x))
            results.append(str(tfidf_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten))+"~"+"<table width=\"100%\" border=\"1\"><tr><td width=\"88%\">"+filegotten.replace("txt","pdf")+"</td><td width=\"12%\">&nbsp;</td></tr><tr><td>"+y+"</td><td><a href='"+static_url+"static/pdf/"+folder+"/"+filegotten.replace("txt","pdf")+"' target='_blank'>Read File</a></td></tr></table><br/>"+"~"+y)
    res = sorted(results,reverse=True)
    sentencebulk = ""
    for g in range (10*int(page)-10,10*int(page)):
            if int(g)<145:
                ming = res[g+1].split("~")
                xieon+=str(ming[1])
                sentencebulk = sentencebulk+" "+ming[2]+" "
    sio = wordclouder2(sentencebulk)
    return xieon+"</td><td rowspan=\"2\" width=\"100%\" align=\"left\" valign=\"top\">"+sio+"</td>"

def bm25searcher(queri,pagi):
    folders = loadfolders("files-clean/")
    xieon =""
    #query = sys.argv[1]
    query=queri
    results=[]
    page = pagi
    if(pagi==""):
        page = 1

    for folder in folders:
        files = loadfiles("files-clean/"+folder+"/")
        for filegotten in files:
            x  = removeemptylines(readpdf("pdf/"+folder+"/"+filegotten.replace("txt","pdf")))
            y=abstract(x)
            #results.append(str(tfidf_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten))+",""files-clean/"+folder+"/"+filegotten.replace("txt","pdf")+","+abstract(x))
            results.append(str(bm25_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten))+"~"+"<table width=\"100%\" border=\"1\"><tr><td width=\"88%\">"+filegotten.replace("txt","pdf")+"</td><td width=\"12%\">&nbsp;</td></tr><tr><td>"+y+"</td><td><a href='"+static_url+"static/pdf/"+folder+"/"+filegotten.replace("txt","pdf")+"' target='_blank'>Read File</a></td></tr></table><br/>"+"~"+y)
    res = sorted(results,reverse=True)
    sentencebulk = ""
    for g in range (10*int(page)-10,10*int(page)):
            if int(g)<145:
                ming = res[g+1].split("~")
                xieon+=str(ming[1])
                sentencebulk = sentencebulk+" "+ming[2]+" "
    sio = wordclouder2(sentencebulk)
    return xieon+"</td><td rowspan=\"2\" width=\"100%\" align=\"left\" valign=\"top\">"+sio+"</td>"
