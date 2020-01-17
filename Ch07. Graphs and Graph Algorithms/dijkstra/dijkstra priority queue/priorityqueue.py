from vertex import Vertex

class PriorityQueue:
    def __init__(self, size: int = 0):
        self.heap: list = [None]
        self.size = size

    def isEmpty(self)->bool:
        return self.size == 0

    def insert(self, vertex: Vertex):
        self.size += 1
        vertex.key = self.size
        self.heap.append(vertex)
        self.percUp(self.size)

    def percUp(self, index: int):
        while index // 2 > 0:
            if self.heap[index].weight < self.heap[index//2].weight:
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
                self.heap[index].key = index
                self.heap[index//2].key = index // 2
            index = index // 2

    def decreaseKey(self, index):
        self.percUp(index)

    def deleteMin(self)->Vertex:
        if self.isEmpty():
            return None
        else:
            tmp: Vertex = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap[1].key = 1
            self.heap.pop()
            self.size -= 1
            self.percDown(1)
            return tmp

    def percDown(self, index: int):
        while index * 2 <= self.size:
            minIndex: int = self.getMinIndex(index)
            if self.heap[index].weight > self.heap[minIndex].weight:
                self.heap[index], self.heap[minIndex] = self.heap[minIndex], self.heap[index]
                self.heap[index].key = index
                self.heap[minIndex].key = minIndex 
            index = minIndex

    def getMinIndex(self, index: int):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap[index * 2].weight <= self.heap[index * 2 + 1].weight:
                return  index * 2
            else:
                return index * 2 + 1
    
    def buildHeap(self, vertices: list):
        for vertex in vertices:
            self.insert(vertex)
