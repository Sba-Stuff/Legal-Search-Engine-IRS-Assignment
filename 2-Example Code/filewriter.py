from pathlib import Path

def writefile(filename, arraytowrite):
    with open(filename, 'w', encoding="utf-8") as f:
        for item in arraytowrite:
            if item is not "":
                f.write("%s\n" % item)

def writefilenonewline(filename, arraytowrite):
    with open(filename, 'w+', encoding="utf-8") as f:
        for item in arraytowrite:
            if item is not "":
                f.write("%s " % item)

def createsubdirectories(path,subdirectories):
    for dirs in subdirectories:
        Path(path+"/"+dirs).mkdir(parents=True, exist_ok=True)

def appendfile(filename, arraytowrite):
    with open(filename, 'a', encoding="utf-8") as f:
        for item in arraytowrite:
            if item is not "":
                f.write("%s\n" % item)


#text = []
#text.append("hello")
#text.append("world")
#writefile("waji.txt",text)