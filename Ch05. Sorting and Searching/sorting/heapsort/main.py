
from binaryheap import BinaryHeap

alist: list = [54,26,93,17,77,31,44,55,20]

bh = BinaryHeap()
bh.buildHeap(alist)

sortedList: list = [None] * bh.size()
pointer: int = 0

while not bh.isEmpty():
    sortedList[pointer] = bh.deleteMin()
    pointer += 1

print(sortedList)