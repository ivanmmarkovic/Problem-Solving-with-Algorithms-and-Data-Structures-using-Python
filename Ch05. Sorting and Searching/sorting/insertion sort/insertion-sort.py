
alist: list = [54,26,93,17,77,31,44,55,20]

def insertionSort(alist: list):
    for i in range(1, len(alist)):
        current:int = alist[i]
        pointer: int = i
        while pointer > 0 and alist[pointer - 1] > current:
            alist[pointer] = alist[pointer - 1]
            pointer -= 1
        alist[pointer] = current


print(alist)
insertionSort(alist)
print(alist)
