
array = [54,26,93,17,77,31,44,55,20]

def shortBubble(alist: list):
    swapped: bool = True
    while swapped:
        swapped = False
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True
        

print(array)
shortBubble(array)
print(array)
'''
def shortBubble(alist: list):
    swapped: bool = True
    dec: int = len(alist) - 1
    while swapped:
        swapped = False
        for i in range(dec):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True
        dec -= 1

print(array)
shortBubble(array)
print(array)
'''