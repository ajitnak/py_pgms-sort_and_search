def search(L, e):
    """Assume L is is a sorted list in ascending order  
       Rturns True if e is in L else reurns False"""
    def bSearch(L, e, low, high):
        print "l={}, h={}".format(low, high)
        if low == high:
            print "e={}  el={}".format(e, L[low])
            return (L[low] == e)
        mid = (low+high) / 2
        if L[mid] == e:
            return True
        if L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L, e, low, mid-1)
        else:
            return bSearch(L, e, mid+1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


ml = [9,10,34,55,77,90,100,701, 1000]

print "Found 9 in list: {}".format(search(ml, 9))
