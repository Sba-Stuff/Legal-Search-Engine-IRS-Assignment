#functions that loads folders and files within a directory
from loader import loadfolders,loadfiles
#function that counts files within a given folder
from filecounter import filesinafoldercounter
#function that writes some file with given array.
from filewriter import writefile
#function to read abstracts from pdf files abstract: first 20 lines.
from pdfreader3 import readpdf
#remove blank lines an fetching abstract function core.
from removeblanklines import removeemptylines,abstract

#dynamic array to load all casses categories
case_categories = []

#dynamic array for cases abstracts
abstracts =  []

#first value of bastract must be header
abstracts.append("Category / Class\t\t\tName S.No.\t\t\tAbstract of Judgments")
abstracts.append("______________________________________________")


#dynamic array to count number of cases within all case categories.
case_count = []

#first value of case count must be header.
case_count.append("Category / Class\t\t\tName Number of Judgments")


#load cases folders from pdf folder, load in case_categories array and print it out.
case_categories = loadfolders("pdf/")
print(case_categories)

#case abstract code.
for cases in case_categories:
    judgements = loadfiles("pdf/"+cases+"/")
    judgementid = 1
    #print(judgements)
    for file in judgements:
        print(file)
        x  = removeemptylines(readpdf("pdf/"+cases+"/"+file))
        #print(x)
        abstracts.append(cases+"\t\t\t"+str(judgementid)+"\t\t\t"+abstract(x))
        abstracts.append("______________________________________________")
        judgementid = judgementid + 1

writefile("abstracts.txt",abstracts)


#count files within all cases folders and save in case_count array.
for cases in case_categories:
    #print(filesinafoldercounter("pdf/"+cases+"/"))
    case_count.append(cases+"\t\t\t"+str(filesinafoldercounter("pdf/"+cases+"/")))
print(case_count)

writefile("casescount.txt",case_count)