def reverseList(alist: list, start: int, end: int):
    while start < end - 1:
        alist[start], alist[end] = alist[end], alist[start]
        start += 1
        end -= 1


alist: list = [1, 2, 3, 4, 5]
print(alist)
reverseList(alist, 0, len(alist) - 1)
print(alist)
