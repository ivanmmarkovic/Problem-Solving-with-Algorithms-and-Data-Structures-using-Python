from vertex import Vertex
from priorityQueue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.prev: dict = {}
        self.adjacencyList: dict = {}

    def addVertex(self, label: str):
        vertex: Vertex = Vertex(label)
        self.vertices.append(vertex)
        vertex.index = len(self.vertices) - 1
        self.prev[label]: str = None
        self.adjacencyList[label]:list = []

    def addEdge(self, label:str, label1:str, weight: int):
        index:int = self.findVertexByLabel(label1).index
        self.adjacencyList[label].append(Vertex(label1, weight, None, index))

    def prim(self, labelStart: str):
        result: str = ""
        startVertex: Vertex = self.findVertexByLabel(labelStart)
        startVertex.weight = 0
        pq = PriorityQueue()
        for vertex in self.vertices:
            pq.insert(vertex)
        while not pq.isEmpty():
            min: Vertex = pq.deleteMin()
            if self.prev[min.label] is not None:
                result +=  self.prev[min.label] + " -> " + min.label + ", "
            for neighbour in self.adjacencyList[min.label]:
                # loop through self.vertices avoided, O(1) instead of O(V)
                # tmp: Vertex = self.findVertexByLabel(neighbour.label)
                tmp: Vertex = self.vertices[neighbour.index]
                if neighbour.weight < tmp.weight:
                    self.prev[neighbour.label] = min.label
                    tmp.weight = neighbour.weight
                    pq.decreaseKey(tmp.key)
        
        print(result)

    def showPath(self, label: str):
        if self.prev[label] is None:
            return label
        else:
            return self.showPath(self.prev[label]) + " -> " + label

    def findVertexByLabel(self,label):
        found: bool = False
        count: int = 0
        while count < len(self.vertices) and not found:
            if self.vertices[count].label == label:
                found = True
            else:
                count += 1
        if found:
            return self.vertices[count]
        else:
            return None

        