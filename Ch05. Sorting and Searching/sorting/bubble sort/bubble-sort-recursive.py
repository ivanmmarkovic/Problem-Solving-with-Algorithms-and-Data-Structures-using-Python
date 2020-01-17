
alist: list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def bubbleSort(alist, n: int):
    if n < 2:
        return
    for i in range(n):
        if alist[i] > alist[i + 1]:
            alist[i], alist[i + 1] = alist[i + 1], alist[i]
    bubbleSort(alist, n - 1)


print(alist)
bubbleSort(alist, len(alist) - 1)
print(alist)
