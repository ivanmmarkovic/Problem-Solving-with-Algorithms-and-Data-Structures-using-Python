
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        # index: int = startIndex + (endIndex - startIndex) // 2
        # index: int = 0 + ((len(alist) - 1) - 0) // 2
        # endIndex = len(alist) - 1
        index = (len(alist) - 1) // 2
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
