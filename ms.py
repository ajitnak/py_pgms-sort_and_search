def mergeSort(aList, comp = operator.lt):
    if len(aList) < 2:
        return aList[:]
    mid = len(aList)//2
    left = mergeSort(aList[:mid], comp)
    right = mergeSort(aList[mid:], comp)
    return merge(left, right, comp)

def merge(left, right, comp):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if comp(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
    
        


    
    
