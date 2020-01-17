
class BinaryHeap:
    def __init__(self):
        self.heap: list = [None]
        self.index: int = 0

    def isEmpty(self)->int:
        return self.index == 0

    def size(self)->int:
        return self.index

    def insert(self, value):
        self.heap.append(value)
        self.index += 1
        self.percUp(self.index)

    def percUp(self, index: int):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index//2]:
                self.heap[index], self.heap[index//2] = self.heap[index // 2], self.heap[index]
            index = index // 2

    def deleteMin(self):
        if self.isEmpty():
            return None
        else:
            retValue: int = self.heap[1]
            if self.index == 1:
                self.index = 0
                self.heap.pop()
            else:
                self.heap[1] = self.heap[self.index]
                self.heap.pop()
                self.index -= 1
                self.percDown(1) 
            return retValue

    def percDown(self, index):
        while index * 2 <= self.index:
            minIndex: int = self.getMinIndex(index)
            if self.heap[index] > self.heap[minIndex]:
                self.heap[index], self.heap[minIndex] = self.heap[minIndex], self.heap[index]
            index = minIndex

    def getMinIndex(self, index):
        if index * 2 + 1 > self.index:
            return index * 2
        else:
            if self.heap[index * 2] <= self.heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def findMin(self):
        if self.isEmpty():
            return None
        else:
            return self.heap[1]

    def buildHeap(self, arr: list):
        for element in arr:
            self.insert(element)


heap: BinaryHeap = BinaryHeap()
heap.insert(5)
heap.insert(1)

print(heap.heap)

heap.insert(3)

print(heap.heap)

heap.insert(0)

print(heap.heap)

while not heap.isEmpty():
    print(heap.deleteMin())

