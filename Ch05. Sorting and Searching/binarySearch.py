
def binarySearch(alist, item):
    start = 0
    end = len(alist) - 1
    found = False

    while start <= end and not found:
        index = (end + start) // 2
        if alist[index] == item:
            found = True
        else:
            if alist[index] > item:
                end = index -1
            else:
                start = index + 1

        return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))