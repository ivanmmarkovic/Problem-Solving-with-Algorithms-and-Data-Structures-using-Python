from vertex import Vertex

class Graph:
    def __init__(self, size: int = 10):
        self.vertices: list = []
        self.adjacencyMatrix = [[float("inf") for x in range(size)] for y in range(size)] 
        self.adjacencyList: dict = {}
        self.prev: dict = {}
        self.visited: dict = {}

    def addVertex(self, label: str, weight:int = float("inf")):
        vertex: Vertex = Vertex(label, weight)
        vertex.index = len(self.vertices)
        self.vertices.append(vertex)
        self.prev[label] = None
        self.adjacencyList[label] = []
        self.visited[label] = False

    def addEdge(self, label1: str, label2: str, weight: int):
        index1: int = self.findIndexByLabel(label1)
        index2: int = self.findIndexByLabel(label2)
        self.adjacencyMatrix[index1][index2] = weight
        
    def dijkstra(self, label: str):
        index: int = self.findIndexByLabel(label)
        current: Vertex = self.vertices[index]
        current.weight = 0
        while current is not None:
            for i in range(len(self.adjacencyMatrix[current.index])):
                if self.adjacencyMatrix[current.index][i] != float("inf"):
                    if current.weight + self.adjacencyMatrix[current.index][i] < self.vertices[i].weight:
                        self.vertices[i].weight = current.weight + self.adjacencyMatrix[current.index][i]
                        self.prev[self.vertices[i].label] = current.label
            self.visited[current.label] = True
            current: Vertex = self.findCheapestVertex()
            
    def findCheapestVertex(self)->Vertex:
        current: Vertex = None
        for vertex in self.vertices:
            if self.visited[vertex.label] == False:
                if current is None:
                    current = vertex
                elif current.weight > vertex.weight:
                    current = vertex
        return current
            
    def showPath(self, label: str)->str:
        if self.prev[label] is None:
            return label
        else:
            return self.showPath(self.prev[label]) + " -> " + label

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
        
