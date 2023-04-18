from os import listdir
from os.path import isfile, join

def filesinafoldercounter(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return len(files)

#print(str(filesinafoldercounter("pdf/civil Appeal/")))