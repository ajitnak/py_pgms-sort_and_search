import random

class intDict(object):
    """ A dict with int keys"""
    def __init__(self, numBkts):
        self.numBkts = numBkts
        self.buckets = []
        for i in range(numBkts):
            self.buckets.append([])
    
    def addEntry(self, key, val):
        bkt = self.buckets[key%self.numBkts]
        for i in range(len(bkt)):
            if bkt[i][0] == key:
                bkt[i][1] = value 
                return
        bkt.append((key, val))
    
    def getVal(self, key):
        bkt = self.buckets[key%self.numBkts]
        for e in bkt:
            if e[0] == key:
                return e[1]
        return None

D = intDict(29)
for i in range(20):
    key = random.randint(0,10**4)
    D.addEntry(key, i)
print D.buckets

