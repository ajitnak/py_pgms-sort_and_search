def inSort(aList):
    for i in (1, len(aList)-1):
        val = aList[i]
        pos = i
        while pos > 0 and aList[pos-1] > curVal:
            aList[pos] = aList[pos-1]
            pos -= 1
        aList[pos] = val

    
     
