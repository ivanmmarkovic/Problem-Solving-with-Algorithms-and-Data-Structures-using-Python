
def binarySearch(alist: list, item: int)->bool:
    start: int = 0
    end: int = len(alist) - 1
    found: bool = False

    while start <= end and not found:
        midpoint: int = start + (end - start) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                end = midpoint - 1
            else:
                start = midpoint + 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42 ,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))