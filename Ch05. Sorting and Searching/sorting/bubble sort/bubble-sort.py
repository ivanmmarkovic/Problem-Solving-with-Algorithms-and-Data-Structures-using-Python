
array = [54,26,93,17,77,31,44,55,20]

def bubbleSort(alist: list):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1, i, -1):
            if alist[j - 1] > alist[j]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]

print(array)
bubbleSort(array)
print(array)