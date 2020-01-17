from vertex import Vertex
from priorityqueue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.prev: dict = {}

    def addVertex(self, label: str, weight:int = float("inf")):
        vertex: Vertex = Vertex(label, weight)
        vertex.index = len(self.vertices)
        self.vertices.append(vertex)
        self.prev[label] = None
        self.adjacencyList[label] = []

    def addEdge(self, label1: str, label2: str, weight: int):
        vertex: Vertex = Vertex(label2, weight)
        index: int = self.findIndexByLabel(label2)
        vertex.index = index
        self.adjacencyList[label1].append(vertex)

        vertex = Vertex(label1, weight)
        index: int = self.findIndexByLabel(label1)
        vertex.index = index
        self.adjacencyList[label2].append(vertex)

    def prims(self, label: str):
        result: str = ""
        index: int = self.findIndexByLabel(label)
        self.vertices[index].weight = 0
        pq = PriorityQueue()
        pq.buildHeap(self.vertices)
        current: Vertex
        while not pq.isEmpty():
            current = pq.deleteMin()
            print(current.label)
            if self.prev[current.label] is not None:
                result += self.prev[current.label] + " -> " + current.label + ", "
            for neighbour in self.adjacencyList[current.label]:
                if neighbour.weight < self.vertices[neighbour.index].weight:
                    self.prev[self.vertices[neighbour.index].label] = current.label
                    self.vertices[neighbour.index].weight = neighbour.weight
                    pq.decreaseKey(self.vertices[neighbour.index].key)
        print(result)

    def findIndexByLabel(self, label: str)->int:
        found: bool = False
        count: int = 0
        while count < len(self.vertices) and not found:
            if self.vertices[count].label == label:
                found = True
            else:
                count += 1
        if found:
            return count
        else:
            return None
        
