def readfile2(filepath):
    words = []
    f = open(filepath, "r")
    lines = f.readlines()
    for line in lines:
            words.append(line)
    return words

lines = readfile2("DocsKeywords.txt")

#print(lines)
xt = []
for x in lines:
    y = x.split(' ')
    docid = y[0]
    print(docid)
    ft = []
    for j in range(1,len(y)):
        fr = y[j].split(":")
        ft.append(fr[0])
    for df in ft:
        xt.append(docid+" "+df)

#print(xt)