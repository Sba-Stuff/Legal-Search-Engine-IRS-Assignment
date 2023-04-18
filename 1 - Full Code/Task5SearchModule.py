from loader import loadfolders,loadfiles
from CosineSimilarity import  tfidf_cosine_similarity,bm25_cosine_similarity
from filewriter import writefile
import sys
from removeblanklines import removeemptylines,abstract
from pdfreader3 import readpdf

folders = loadfolders("files-clean/")
xieon =""
#query = sys.argv[1]
query="judg hear thi"
results=[]
page = 1
#if(len(sys.argv)==3):
#    page = sys.argv[2]

for folder in folders:
    files = loadfiles("files-clean/"+folder+"/")
    for filegotten in files:
        x  = removeemptylines(readpdf("pdf/"+folder+"/"+filegotten.replace("txt","pdf")))

        #results.append(str(tfidf_cosine_similarity(query,"files-clean/"+folder+"/"+filegotten))+",""files-clean/"+folder+"/"+filegotten.replace("txt","pdf")+","+abstract(x))
        results.append("<table width=\"100%\" border=\"0\"><tr><td width=\"88%\">"+filegotten.replace("txt","pdf")+"</td><td width=\"12%\">&nbsp;</td></tr><tr><td>"+abstract(x)+"</td><td><a href='sds.html' target='_blank'>Read File</a></td></tr></table>")
res = sorted(results,reverse=True)
for g in range (10*int(page)-10,10*int(page)):
        if int(g)<145:
            xieon+=str(res[g+1])

print(xieon)

