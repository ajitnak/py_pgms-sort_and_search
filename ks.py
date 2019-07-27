def kthSmallest(arr, low, high, k): 
  
    # If k is smaller than number of  
    # elements in array 
    if (k >= 0 and k <= high - low ): 
      
        # Partition the array around last  
        # element and get position of pivot 
        # element in sorted array 
        pos = partition(arr, low, high) 
  
        # If position is same as k 
	#print pos, low,k
        if (pos - low == k ): 
            return arr[pos] 
        if (pos - low > k ): # If position is more,  
            return kthSmallest(arr, low, pos - 1, k) 
  
        # Else recur for right subarray 
        return kthSmallest(arr, pos + 1, high, 
                           k - pos + low - 1) 
  
    # If k is more than number of 
    # elements in array 
    return None
  
# Standard partition process of QuickSort().  
# It considers the last element as pivot and 
# moves all smaller element to left of it 
# and greater elements to right 
def partition(arr, low, high): 
  
    x = arr[high] 
    i = low 
    for j in range(low, high): 
        if (arr[j] <= x): 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[high] = arr[high], arr[i] 
    return i 
  

def smallest(list, k):
	return kthSmallest(list, 0, len(list) - 1, k-1)
arr = [12, 3, 5, 7, 4, 19, 26] 
n = len(arr) 
k = 3
print smallest(arr, 1)
print smallest(arr, 2)
print kthSmallest(arr, 0, n - 1, 3-1) 
print kthSmallest(arr, 0, n - 1, 4-1) 
print kthSmallest(arr, 0, n - 1, 5-1) 
print kthSmallest(arr, 0, n - 1, 6-1) 
print kthSmallest(arr, 0, n - 1, 7-1) 


