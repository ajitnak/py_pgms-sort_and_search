import operator
import string

def mergeSort(L, comp=operator.lt):
    if len(L) < 2:
        return L[:]
    mid = len(L)/2
    left = mergeSort(L[:mid], comp)
    right = mergeSort(L[mid:], comp)
    return merge(left, right, comp)

def merge(ll, rl, compare):
    result = []
    i,j = 0,0
    while i < len(ll) and j < len(rl):
        if compare(ll[i], rl[j]):
            result.append(ll[i])
            i = i+1
        else:
            result.append(rl[j])
            j = j+1
    while i < len(ll):
        result.append(ll[i])
        i = i+1

    while j < len(rl):
        result.append(rl[j])
        j = j+1
    return result

def lastNameFirstName(name1, name2):
    name1List = string.split(name1, ' ')
    name2List = string.split(name2, ' ')
    if name1List[1] !=  name2List[1]:
        return name1List[1] < name2List[1]
    else:
        return name1List[0] < name2List[0]

def firstNameLastName(name1, name2):
    name1List = string.split(name1, ' ')
    name2List = string.split(name2, ' ')
    if name1List[0] != name2List[0]:
        return name1List[0] < name2List[0]
    else:
        return name1List[1] < name2List[1]


print "sorted list:{}".format(mergeSort([9,6,3,10,35,33,77,45,1]))
print "sorted list:{}".format(mergeSort(['Ajit Nayak','Sunita Raj','Ayan Nayak','Anayanya Nayak', 'Steve Msdsds'], lastNameFirstName))


