class intDict(object):
    def __init__(self, numBkts):
        self.nBkts = numBkts
        sekf.bkts = []
        for i in range(numBkts):
            self.bkts.append([])

    def addEntry(self, k, v):
        bkt = self.bkts[k % numBkts]
        for i in len bkt:
            if bkt[i][0] == key:
                bkt[i][1] = val
        bkt.append((k, v))
    def getEntry(self, k):
        bkt = self.bkts[k % numBkts]
        for e in bkt:
            if e[0] == key:
                return e[1]
        return None
            
