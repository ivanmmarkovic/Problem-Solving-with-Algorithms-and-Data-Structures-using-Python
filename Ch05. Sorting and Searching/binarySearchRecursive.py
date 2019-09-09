
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        #index: int = (len(alist) - 1) // 2
        index = len(alist) // 2
        if alist[index] == item:
            return True
        else:
            if alist[index] > item:
                return binarySearch(alist[0:index], item)
            else:
                return binarySearch(alist[index + 1 :], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
