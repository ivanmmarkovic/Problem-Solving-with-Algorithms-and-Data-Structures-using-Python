alist = [1, 2, 3, 4, 5]

def sum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + sum(alist[1:])


result = sum(alist)
print(result)