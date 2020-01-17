
alist: list = [54,26,93,17,77,31,44,55,20]

def mergeSort(alist: list):
    if len(alist) >= 2:
        midpoint: int = len(alist) // 2
        leftList: list = alist[0:midpoint]
        rightList: list = alist[midpoint:]
        mergeSort(leftList)
        mergeSort(rightList)

        i = j = k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] <= rightList[j]:
                alist[k] = leftList[i]
                i += 1
            else:
                alist[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            alist[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            alist[k] = rightList[j]
            j += 1
            k += 1

print(alist)
mergeSort(alist)
print(alist)
        