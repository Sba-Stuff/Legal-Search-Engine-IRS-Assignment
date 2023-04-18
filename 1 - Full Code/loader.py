from os import listdir
from os.path import isfile, join

def loadfolders(mypath):
 folders = [f for f in listdir(mypath)]
 return folders

def loadfiles(mypath):
 files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
 return files

#print(loadfolders("pdf/"))
#print(loadfiles("pdf/civil Appeal/"))