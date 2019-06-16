from vertex import Vertex

class PriorityQueue:
    def __init__(self):
        self.queue: list = [None]
        self.size: int = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, vertex: Vertex):
        self.size += 1
        vertex.key = self.size
        self.queue.append(vertex)
        self.percUp(self.size)

    def percUp(self, index: int):
        while index // 2 > 0:
            if self.queue[index // 2].weight > self.queue[index].weight:
                tmp: Vertex = self.queue[index // 2]
                self.queue[index // 2] = self.queue[index]
                self.queue[index] = tmp
                self.queue[index // 2].key = index // 2
                self.queue[index].key = index
            index = index // 2

    def deleteMin(self):
        if not self.isEmpty():
            min: Vertex = self.queue[1]
            self.queue[1] = self.queue[self.size]
            self.queue[1].key = 1
            self.queue.pop()
            self.size -= 1
            self.percDown(1)
            return min
        else:
            return None

    def percDown(self, index: int):
        while index * 2 <= self.size:
            minIndex: int = self.getMinIndex(index)
            if self.queue[index].weight > self.queue[minIndex].weight:
                tmp: Vertex = self.queue[index]
                self.queue[index] = self.queue[minIndex]
                self.queue[minIndex] = tmp
                self.queue[index].key = index
                self.queue[minIndex].key = minIndex
            index = minIndex

    def getMinIndex(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.queue[index * 2].weight < self.queue[index * 2 + 1].weight:
                return index * 2
            else:
                return index * 2 + 1

    def decreaseKey(self, index: int):
        self.percUp(index)

    def buildHeap(self, vertices: list):
        for vertex in vertices:
            self.insert(vertex)

    def getMin(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[1]

