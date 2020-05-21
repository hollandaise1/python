"""To write a function that count the odd occurence of integers in an array """
arr = [2,2,4,4,3,5,4,5,4,5,3,2,2]

def getOccurance(myArray):
    counterDict = {}

    for item in myArray:
        if item in counterDict:
            counterDict[item] += 1
        else:
            counterDict[item] = 1
    return counterDict
    
def oddMod(myDict):
    for k,v in myDict.items():
        newDict = {}
        if v%2 != 0:
            newDict[k]=v
        else:
            pass
    return newDict
