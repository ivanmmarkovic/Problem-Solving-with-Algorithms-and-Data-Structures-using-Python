
alist = [15, 3, 437, 59, 1, 117, 500, 19]
print(alist)

# range([start], stop[, step])

# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.


def bubbleSort(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - 1, i, -1):
            if alist[j - 1] > alist[j]:
                tmp = alist[j - 1]
                alist[j - 1] = alist[j]
                alist[j] = tmp

bubbleSort(alist)

print(alist)