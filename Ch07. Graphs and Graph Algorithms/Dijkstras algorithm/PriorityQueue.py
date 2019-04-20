class PriorityQueue:
    def __init__(self):
        self.queue = [None]
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, vertex):
        self.queue.append(vertex)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, index):
        while index // 2 > 0:
            if self.queue[index // 2].weight > self.queue[index].weight:
                tmp = self.queue[index // 2]
                self.queue[index // 2] = self.queue[index]
                self.queue[index] = tmp
            index = index // 2

    def deleteMin(self):
        ret_vertex = self.queue[1]
        self.queue[1] = self.queue[self.size]
        self.size -= 1
        self.percDown(1)
        return ret_vertex

    def percDown(self, index):
        while index * 2 <= self.size:
            min_index = self.getMinIndex(index)
            if self.queue[index].weight < self.queue[min_index].weight:
                tmp = self.queue[index]
                self.queue[index] = self.queue[min_index]
                self.queue[min_index] = tmp
            index = min_index

    def getMinIndex(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.queue[index * 2].weight < self.queue[index * 2 + 1].weight:
                return index * 2
            else:
                return index * 2 + 1

    def getMin(self):
        return self.queue[1]

    def build_heap(self, vertex_list):
        for vertex in vertex_list:
            self.insert(vertex)


