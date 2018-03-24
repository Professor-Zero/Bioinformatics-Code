
#Counter - dict subclass for counting hashable objects
from collections import Counter

#createMultiSet() ~ reads a multiset string and returns a multiset(using counter and map makes into a mutliset)
def createMultiSet(string):
    return Counter(map(int,string.strip().split()))

#findSetLength() - uses nC_2 equation 
def findSetLength(multiSetlength):
    n = -1
    combination = multiSetlength*2
    for i in range(combination):
        equation = i * (i-1)
        if equation == combination:
            n = i
            break
    return n

#aims to find the set for multiSet
def findSet(multiSet):
    #initilize Set
    setX = {0}
    maxNum = max(multiSet)

    #--------------inner functions------------#
    #max1 = a maxium number from setX, set1 = a set
    #returna a new multi set
    def newMultiSet(max1, set1): 
        #print(max1, set1)
        return Counter(abs(max1-s) for s in set1) 
        #return Counter(abs(max1-s) for s in set1)

    # helper function for new mutliset
    def containment(newMultiS, multiS):
        for x in newMultiS:
            #print(x, "newMS-",newMultiS, "mS-",multiS)
            if newMultiS[x] > multiS[x]:
                return False
        return True
        #return all(newMultiS[x] <= multiS[x] for x in newMultiS)
    #--------------inner functions------------#        

    while (len(multiSet) > 0):
        currentMaxNum = max(multiSet)
        #print('set',sorted(list(setX)))
        if containment(newMultiSet(currentMaxNum, setX), multiSet):
            setX.update({currentMaxNum})
            multiSet -= newMultiSet(currentMaxNum, setX)
        else:
            setX.update({maxNum - currentMaxNum})
            multiSet -= newMultiSet(maxNum - currentMaxNum, setX)
    
    #sorted the set
    sortSet = sorted(list(setX))
    return sortSet

if __name__ == "__main__":
    multiSetString = open('dataRM.txt','r').read()
    multiSet = createMultiSet(multiSetString)
    #gets the total 
    setLength = findSetLength(len(multiSet))
    #print('multiSet:',multiSet)

    x = findSet(multiSet)
    setString = [str(a) for a in x]
    print(' '.join(setString))