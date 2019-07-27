import heapq

class Value:
	def __init__(self, data):
		self.data = data

	def __cmp__(self, other):
		return -cmp(self.data, other.data)


def kth_closest(nums, k):
	vals=[Value(n) for n in nums]
	print vals
	
	max_heap=vals[:k]
	heapq.heapify(max_heap)
	#max_heap=[]
	#for pt in points_with_d[:k]:
	#	heapq.heappush(max_heap, pt)

	#while max_heap:
	#	pt = heapq.heappop(max_heap)
	#	print pt.point, pt.dist

	for val in vals[k:]:
		if val.data < max_heap[0].data:
			print "replace", max_heap[0].data, "with",  val.data
			heapq.heapreplace(max_heap, val)

	#print "results"	
	while max_heap:
		ptd = heapq.heappop(max_heap)
		print ptd.data



#kth_closest((0,0), [(7,7), (1,-1), (3,3),(10,10), (2,-2), (5,5)], 3)
kth_closest([5,4,2,9,6,3,7,4,10,0,-1,60], 4)


 
