
def sequentialSearch(alist: list, item: int)->bool:
    found: bool = False
    count: int = 0
    while count < len(alist) and not found:
        if alist[count] == item:
            found = True
        else:
            count += 1
    
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))