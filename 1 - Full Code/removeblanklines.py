def removeemptylines(string_with_empty_lines):
	lines = string_with_empty_lines.split("\n")
	non_empty_lines = [line for line in lines if line.strip() != ""]
	string_without_empty_lines = ""
	for line in non_empty_lines:
      		string_without_empty_lines += line + "\n"
	return string_without_empty_lines

def abstract(firstpagetext):
    abstract = ""
    lines = firstpagetext.split("\n")
    for xxeodar in range(20):
        if(xxeodar!=0 and xxeodar!=1 and xxeodar!=2 and xxeodar!=3 and xxeodar!=4):
            abstract += lines[xxeodar] + "\n"
    return removeemptylines(abstract)

#strin = "My Name is Wajeeh  \n   \n    \n     \nThere were Three empty lines"
#print(strin)


#print("outut by removeeimptylines function")
#print(removeemptylines(strin))


#print("Random Alot of text")
#strin2 = "My Name is Wajeeh  \n   \n    \n     \nThere were Three empty lines My Name is Wajeeh  \n   \n    \n     \nThere were Three empty lines My Name is Wajeeh  \n   \n    \n     \nThere were Three empty lines My Name is Wajeeh  \n   \n    \n     \nThere were Three empty lines My Name is Wajeeh  \n   \n    \n     \nThere were Three empty lines"
#print(strin2)

#print("Abstract of Random text")
#print(abstract(strin2))
