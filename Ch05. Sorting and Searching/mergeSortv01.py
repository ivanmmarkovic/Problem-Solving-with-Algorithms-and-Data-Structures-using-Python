
alist = [54,26,93,17,77,31,44,55,20]
print(alist)
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        leftList = alist[:mid]
        rightList = alist[mid:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = j = k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
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


mergeSort(alist)

print(alist)
        