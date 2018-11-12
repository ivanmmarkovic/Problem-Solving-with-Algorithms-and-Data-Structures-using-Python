alist = [15, 3, 437, 59, 1, 117, 500, 19]
print(alist)

# def insertionSort(alist):
#     for i in range(1, len(alist)):
#         index = i - 1
#         current = alist[i]
#         while index >= 0 and alist[index] > current:
#             alist[index + 1] = alist[index]
#             index -= 1
#         alist[index  + 1] = current

def insertionSort(alist):
    for i in range(1, len(alist)):

        position = i
        currentNumber = alist[position]

        while position > 0 and alist[position - 1] > currentNumber:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentNumber


insertionSort(alist)
print(alist)
