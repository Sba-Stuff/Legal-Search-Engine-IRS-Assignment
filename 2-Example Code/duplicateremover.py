def removeduplicate(list):
    final_list = []
    for value in list:
        if value not in final_list:
            final_list.append(value)
    return final_list

def hasNumbers(inputString):
    return any(i.isdigit() for i in inputString)

def hasNumbers2(inputString):
    if any(i.isdigit() for i in inputString):
        return "yes"
    else:
        return "no"

#list = []
#list.append('Muhammad Wajeeh Uz Zaman')
#list.append('Muhammad Wajeeh Ul Hassan')
#list.append('Muhammad Wajeeh Uz Zaman')
#print(removeduplicate(list))

#what = str(hasNumbers("Wajeeh9"))
#what = str(hasNumbers("Wajeeh"))
#if "True" in what:
#    print("yeah")
#else:
#   print("nope")