def search(aList, e):
    
    def bSearch(aList, e, low, high):
        if low == high:
            return aList[low] == e
        mid = (low+high)//2
        if aList[mid] == e:
            return True
        if aList[mid] > e:
            if mid == low:
                return False
            return bSearch(aList, low, mid-1)
        else:
            return bSearch(aList, mid+1, high)
        
    if len(aList) == 0:
        return False
    else
        return bSearch(aList, e, 0, len(aList) -1)
