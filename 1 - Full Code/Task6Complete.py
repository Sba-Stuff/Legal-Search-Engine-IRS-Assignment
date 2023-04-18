from task3core import getidbydocument
from filereader import readfile2
from aps import tfidf_ap,bm25_ap
from filewriter import writefile
def tfidf_rankcalculator(ranks):
    rank = ""
    for x in range(0,100):
        df = ranks[x].split(",")
        dfi = df[0].replace(".pdf",".txt")
        #print(dfi)
        rank = rank +" "+ str(getidbydocument(dfi)) +" "
        #+"["+str(x+1)+"]"+" "
    return rank

def bm25_rankcalculator(ranks):
    rank = ""
    for x in range(0,130):
        df = ranks[x].split(",")
        dfi = df[0].replace(".pdf",".txt")
        #print(dfi)
        rank = rank +" "+ str(getidbydocument(dfi)) +" "
        #+"["+str(x+1)+"]"+" "
    return rank

def accuracy(p, r):
    ans1 = p*r
    ans2 = p+r
    ans3 = ans1/ans2
    ans4 = 2*ans3
    return ans4

def average_precision(arr1,d):
    c = 0.0
    for f in arr1:
        c+=float(f)
    return c/d

def mean_average_precision(arr1,d):
    c = 0
    for f in arr1:
        c+=float(f)
    return c/d

tfidfq1lines = readfile2("Assignment Task5 Artifacts\PreProcessing\TFIDF Q1.csv")
tfidfq2lines = readfile2("Assignment Task5 Artifacts\PreProcessing\TFIDF Q2.csv")
tfidfq3lines = readfile2("Assignment Task5 Artifacts\PreProcessing\TFIDF Q3.csv")
tfidfq4lines = readfile2("Assignment Task5 Artifacts\PreProcessing\TFIDF Q4.csv")
tfidfq5lines = readfile2("Assignment Task5 Artifacts\PreProcessing\TFIDF Q5.csv")

rank1tfidf = tfidf_rankcalculator(tfidfq1lines)
rank2tfidf = tfidf_rankcalculator(tfidfq2lines)
rank3tfidf = tfidf_rankcalculator(tfidfq3lines)
rank4tfidf = tfidf_rankcalculator(tfidfq4lines)
rank5tfidf = tfidf_rankcalculator(tfidfq5lines)

#print(rank1tfidf)
#print(rank2tfidf)
#print(rank3tfidf)
#print(rank4tfidf)
#print(rank5tfidf)

bm25q1lines = readfile2("Assignment Task5 Artifacts\PreProcessing\BM25 Q1.csv")
bm25q2lines = readfile2("Assignment Task5 Artifacts\PreProcessing\BM25 Q2.csv")
bm25q3lines = readfile2("Assignment Task5 Artifacts\PreProcessing\BM25 Q3.csv")
bm25q4lines = readfile2("Assignment Task5 Artifacts\PreProcessing\BM25 Q4.csv")
bm25q5lines = readfile2("Assignment Task5 Artifacts\PreProcessing\BM25 Q5.csv")

rank1bm25 = bm25_rankcalculator(bm25q1lines)
rank2bm25 = bm25_rankcalculator(bm25q2lines)
rank3bm25 = bm25_rankcalculator(bm25q3lines)
rank4bm25 = bm25_rankcalculator(bm25q4lines)
rank5bm25 = bm25_rankcalculator(bm25q5lines)

#print(rank1bm25)
#print(rank2bm25)
#print(rank3bm25)
#print(rank4bm25)
#print(rank5bm25)

tfidfprecisionq1 =  .03
tfidfrecallq1 =     .20
tfidfprecisionq2 =  .02
tfidfrecallq2 =     .22
tfidfprecisionq3 =  .04
tfidfrecallq3 =     .80
tfidfprecisionq4 =  .12
tfidfrecallq4 =     .38
tfidfprecisionq5 =  .03
tfidfrecallq5 =     .38

#print(str(accuracy(tfidfprecisionq1,tfidfrecallq1)))
#print(str(accuracy(tfidfprecisionq2,tfidfrecallq2)))
#print(str(accuracy(tfidfprecisionq3,tfidfrecallq3)))
#print(str(accuracy(tfidfprecisionq4,tfidfrecallq4)))
#print(str(accuracy(tfidfprecisionq5,tfidfrecallq5)))
ifdif1a = accuracy(tfidfprecisionq1,tfidfrecallq1)
ifdif2a = accuracy(tfidfprecisionq2,tfidfrecallq2)
ifdif3a = accuracy(tfidfprecisionq3,tfidfrecallq3)
ifdif4a = accuracy(tfidfprecisionq4,tfidfrecallq4)
ifdif5a =  accuracy(tfidfprecisionq5,tfidfrecallq5)

bm25precisionq1 =  .09
bm25recallq1 =     .16
bm25precisionq2 =  .06
bm25recallq2 =     .60
bm25precisionq3 =  .05
bm25recallq3 =     1.0
bm25precisionq4 =  .26
bm25recallq4 =     .81
bm25precisionq5 =  .06
bm25recallq5 =     .75

#print(str(accuracy(bm25precisionq1,bm25recallq1)))
#print(str(accuracy(bm25precisionq2,bm25recallq2)))
#print(str(accuracy(bm25precisionq3,bm25recallq3)))
#print(str(accuracy(bm25precisionq4,bm25recallq4)))
#print(str(accuracy(bm25precisionq5,bm25recallq5)))
bm251a = accuracy(bm25precisionq1,bm25recallq1)
bm252a = accuracy(bm25precisionq2,bm25recallq2)
bm253a = accuracy(bm25precisionq3,bm25recallq3)
bm254a = accuracy(bm25precisionq4,bm25recallq4)
bm255a = accuracy(bm25precisionq5,bm25recallq5)

tfidfq1ap = average_precision(tfidf_ap(),15.0)
tfidfq2ap = average_precision(tfidf_ap(),9.0)
tfidfq3ap = average_precision(tfidf_ap(),5.0)
tfidfq4ap = average_precision(tfidf_ap(),32.0)
tfidfq5ap = average_precision(tfidf_ap(),8.0)

bm25q1ap = average_precision(bm25_ap(),15.0)
bm25q2ap = average_precision(bm25_ap(),9.0)
bm25q3ap = average_precision(bm25_ap(),5.0)
bm25q4ap = average_precision(bm25_ap(),32.0)
bm25q5ap = average_precision(bm25_ap(),8.0)

tfidftotalap = []
tfidftotalap.append(tfidfq1ap)
tfidftotalap.append(tfidfq2ap)
tfidftotalap.append(tfidfq3ap)
tfidftotalap.append(tfidfq4ap)
tfidftotalap.append(tfidfq5ap)

bm25totalap = []
bm25totalap.append(bm25q1ap)
bm25totalap.append(bm25q2ap)
bm25totalap.append(bm25q3ap)
bm25totalap.append(bm25q4ap)
bm25totalap.append(bm25q5ap)

tfidfmap = mean_average_precision(tfidftotalap,5)
bm25ap = mean_average_precision(bm25totalap,5)

xprinter = []
xprinter.append("Query Terms \t\t\t Weighting \t\t\t P \t\t\t R \t\t\t F \t\t\t AP")
xprinter.append(str(1) + "\t\t\t TFIDF \t\t\t "+str(round(tfidfprecisionq1,2))+" \t\t\t "+str(round(tfidfrecallq1,2))+" \t\t\t "+str(round(ifdif1a,2))+" \t\t\t "+str(round(tfidfq1ap,2)))
xprinter.append(str(2) + "\t\t\t TFIDF \t\t\t "+str(round(tfidfprecisionq2,2))+" \t\t\t "+str(round(tfidfrecallq2,2))+" \t\t\t "+str(round(ifdif2a,2))+" \t\t\t "+str(round(tfidfq2ap,2)))
xprinter.append(str(3) + "\t\t\t TFIDF \t\t\t "+str(round(tfidfprecisionq3,2))+" \t\t\t "+str(round(tfidfrecallq3,2))+" \t\t\t "+str(round(ifdif3a,2))+" \t\t\t "+str(round(tfidfq3ap,2)))
xprinter.append(str(4) + "\t\t\t TFIDF \t\t\t "+str(round(tfidfprecisionq4,2))+" \t\t\t "+str(round(tfidfrecallq4,2))+" \t\t\t "+str(round(ifdif4a,2))+" \t\t\t "+str(round(tfidfq4ap,2)))
xprinter.append(str(5) + "\t\t\t TFIDF \t\t\t "+str(round(tfidfprecisionq5,2))+" \t\t\t "+str(round(tfidfrecallq5,2))+" \t\t\t "+str(round(ifdif5a,2))+" \t\t\t "+str(round(tfidfq5ap,2)))
xprinter.append("___________________________________________________________________________________________________________________________________")
xprinter.append("Mean Average Precision for 5 queries = "+str(round(tfidfmap,2)))
yprinter = []
yprinter.append("Query Terms \t\t\t Weighting \t\t\t P \t\t\t R \t\t\t F \t\t\t AP")
yprinter.append(str(1) + "\t\t\t BM25 \t\t\t "+str(round(bm25precisionq1,2))+" \t\t\t "+str(round(bm25recallq1,2))+" \t\t\t "+str(round(bm251a,2))+" \t\t\t "+str(round(bm25q1ap,2)))
yprinter.append(str(2) + "\t\t\t BM25 \t\t\t "+str(round(bm25precisionq2,2))+" \t\t\t "+str(round(bm25recallq2,2))+" \t\t\t "+str(round(bm252a,2))+" \t\t\t "+str(round(bm25q2ap,2)))
yprinter.append(str(3) + "\t\t\t BM25 \t\t\t "+str(round(bm25precisionq3,2))+" \t\t\t "+str(round(bm25recallq3,2))+" \t\t\t "+str(round(bm253a,2))+" \t\t\t "+str(round(bm25q3ap,2)))
yprinter.append(str(4) + "\t\t\t BM25 \t\t\t "+str(round(bm25precisionq4,2))+" \t\t\t "+str(round(bm25recallq4,2))+" \t\t\t "+str(round(bm254a,2))+" \t\t\t "+str(round(bm25q4ap,2)))
yprinter.append(str(5) + "\t\t\t BM25 \t\t\t "+str(round(bm25precisionq5,2))+" \t\t\t "+str(round(bm25recallq5,2))+" \t\t\t "+str(round(bm255a,2))+" \t\t\t "+str(round(bm25q5ap,2)))
yprinter.append("___________________________________________________________________________________________________________________________________")
yprinter.append("Mean Average Precision for 5 queries = "+str(round(bm25ap,2)))

writefile("Task6TFIDF.txt",xprinter)
writefile("Task6BM25.txt",yprinter)