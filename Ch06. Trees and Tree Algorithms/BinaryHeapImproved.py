# removed unnecessary iterations in percUp and percDown

class BinaryHeap:
    def __init__(self):
        self.size = 0
        self.heap = [0]

    def isEmpty(self):
        return self.size == 0

    def insert(self, item):
        self.size += 1
        self.heap.append(item)
        self.percUp(self.size)

    def percUp(self, index):
        swap = True
        while index // 2 > 0 and swap:
            swap = False
            if self.heap[index] < self.heap[index//2]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[index // 2]
                self.heap[index//2] = tmp
                swap = True
            index = index // 2

    def deleteMin(self):
        toReturn = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.percDown(1)
        return toReturn

    def percDown(self, index):
        swap = True
        while index * 2 <= self.size and swap:
            swap = False
            minIndex = self.getMinIndex(index)
            if self.heap[index] > self.heap[minIndex]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[minIndex]
                self.heap[minIndex] = tmp
                swap = True
            index = minIndex

    def getMinIndex(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap[index * 2] < self.heap[index * 2 + 1]:
                return index* 2
            else:
                return index * 2 + 1

    def getMin(self):
        if self.isEmpty():
            return None
        else:
            return self.heap[1]

    def buildHeap(self, alist):
        for item in alist:
            self.insert(item)

    def show(self):
        print(self.heap)

bh = BinaryHeap()
bh.insert(9)
bh.insert(7)
bh.show()
bh.insert(1)
bh.show()
#bh.insert(3)
bh.show()

while not bh.isEmpty():
    print(bh.deleteMin())

