

alist: list = [54,26,93,17,77,31,44,55,20]

def selectionSort(alist: list):
    for i in range(len(alist)):
        min: int = i
        for j in range(i + 1, len(alist), +1):
            if alist[j] < alist[min]:
                min = j
        if min != i:
            alist[min], alist[i] = alist[i], alist[min]
    
print(alist)
selectionSort(alist)
print(alist)