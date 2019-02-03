from random import randint

alist = [24, 16, 117, 3, 81, 14, 94]
print(alist)

'''
def quicksort(alist):
    if len(alist) < 2:
        return alist
    else:
        pivotElement = alist[0]
        leftList = []
        rightlist = []
        for item in alist[1:]:
            if item <= pivotElement:
                leftList.append(item)
            else:
                rightlist.append(item)
        return quicksort(leftList) + [pivotElement] + quicksort(rightlist)
'''
def quicksort(alist):
    if len(alist) < 2:
        return alist
    else:
        pivot = randint(0, len(alist) - 1)
        leftList = []
        rightList = []
        for index in range(len(alist)):
            if index != pivot:
                if alist[index] <= alist[pivot]:
                    leftList.append(alist[index])
                else:
                    rightList.append(alist[index])
        return quicksort(leftList) + [alist[pivot]] + quicksort(rightList)

sorted = quicksort(alist)
print(sorted)