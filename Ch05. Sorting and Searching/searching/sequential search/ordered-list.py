
def orderedSequentialSearch(alist: list, item: int)->bool:
    found: bool = False
    stopped: bool = False
    count: int = 0
    while count < len(alist) and not found and not stopped:
        if alist[count] == item:
            found = True
        else:
            if alist[count] > item:
                stopped = True
            else:
                count += 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))