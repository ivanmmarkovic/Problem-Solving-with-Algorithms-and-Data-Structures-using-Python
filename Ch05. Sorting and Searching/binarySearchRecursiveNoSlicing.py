
def binarySearchRecursiveNoSlicing(alist: list, item: int, start: int, end: int)-> bool:
    if start > end:
        return False
    else:
        midpoint: int = (start + end) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch(alist, item, start, midpoint - 1)
            else:
                return binarySearch(alist, item, midpoint + 1, end)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 54]
print(binarySearchRecursiveNoSlicing(testlist, 3, 0, len(testlist) - 1))
print(binarySearchRecursiveNoSlicing(testlist, 13, 0, len(testlist) - 1))

print(binarySearchRecursiveNoSlicing(testlist, 54, 0, len(testlist) - 1))
print(binarySearchRecursiveNoSlicing(testlist, 0, 0, len(testlist) - 1))

