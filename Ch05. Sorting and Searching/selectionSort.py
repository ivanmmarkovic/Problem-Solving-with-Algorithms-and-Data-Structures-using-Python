alist = [15, 3, 437, 59, 1, 117, 500, 19]
print(alist)

def selectionSort(alist):
    for i in range(len(alist)):
        min = i

        for j in range(i + 1, len(alist)):
            if alist[min] > alist[j]:
                min = j

        if min != i:
            tmp = alist[i]
            alist[i] = alist[min]
            alist[min] = tmp


selectionSort(alist)
print(alist)