
class BinaryHeap:
    def __init__(self):
        self.heap: list = [None]
        self.pointer: int = 0

    def isEmpty(self)->bool:
        return self.pointer == 0

    def size(self)->int:
        return self.pointer

    def getMin(self):
        if self.isEmpty():
            return None
        else:
            return self.heap[self.pointer]

    def insert(self, item):
        self.heap.append(item)
        self.pointer += 1
        self.percUp(self.pointer)

    def percUp(self, index):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index//2]:
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
            index = index // 2

    def deleteMin(self):
        if self.isEmpty():
            return None
        else:
            retValue = self.heap[1]
            self.heap[1] = self.heap[self.pointer]
            self.pointer -= 1
            self.heap.pop()
            self.percDown(1)
            return retValue
    
    def percDown(self, index: int):
        while index * 2 <= self.pointer:
            minIndex: int = self.getMinIndex(index)
            if self.heap[index] > self.heap[minIndex]:
                self.heap[index], self.heap[minIndex] = self.heap[minIndex], self.heap[index]
            index = minIndex

    def getMinIndex(self, index: int):
        if index * 2 + 1 > self.pointer:
            return index * 2
        else:
            if self.heap[index * 2] <= self.heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def buildHeap(self, alist: list):
        for item in alist:
            self.insert(item)


