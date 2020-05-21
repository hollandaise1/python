"""To write a function that count the odd occurence of integers in an array """
arr = [2,2,4,3,5,4,5,4,5,3,2,2]

#Solution 1:
def getOccurance(myArray):
    counterDict = {}
    for item in myArray:
        if item in counterDict:
            counterDict[item] += 1
        else:
            counterDict[item] = 1
    return counterDict
    
def oddMod(myDict):
    newDict = {}
    for k,v in myDict.items():
        if v%2 != 0:
            newDict[k]=v
            newDict.update()
        else:
            pass
    return newDict

#Expected Results: {4: 3, 5: 3}

#Solution 2:
import collections
arr = [2,2,4,3,5,4,5,4,5,3,2,2]
num2count = collections.Counter(arr)
print(num2count)
odd_nums = [x for x in num2count if num2count[x]%2]
print(odd_nums)

#Counter({2: 4, 4: 3, 5: 3, 3: 2})
#[4, 5]

