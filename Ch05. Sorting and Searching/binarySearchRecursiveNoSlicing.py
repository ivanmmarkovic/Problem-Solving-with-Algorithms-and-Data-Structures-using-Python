
def binarySearch(alist, item, start, end):
    if start > end:
        return False
    else:
        midpoint = (start + end) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch(alist, item, start, midpoint - 1)
            else:
                return binarySearch(alist, item, midpoint+ 1, end)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3, 0, len(testlist)))
print(binarySearch(testlist, 13, 0, len(testlist)))
