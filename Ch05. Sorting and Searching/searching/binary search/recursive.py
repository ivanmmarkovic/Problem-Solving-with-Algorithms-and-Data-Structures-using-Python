
def binarySearch(alist: list, item: int)->bool:
    if len(alist) == 0:
        return False
    else:
        midpoint: int = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch(alist[0:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42 ,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))