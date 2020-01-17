def reverseList(alist: list, start: int, end: int):
    if start < end:
        alist[start], alist[end] = alist[end], alist[start]
        reverseList(alist, start + 1, end - 1)


alist: list = [1, 2, 3, 4, 5]
print(alist)
reverseList(alist, 0, len(alist) - 1)
print(alist)