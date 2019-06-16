from vertex import Vertex

class Graph:
    def __init__(self, size: int):
        self.vertices: list = []
        self.visited: list = []
        self.prev: dict = {}
        self.adjacencyMatrix = [[float("inf") for x in range(size)] for y in range(size)] 

    def addVertex(self, label: str):
        vertex: Vertex = Vertex(label)
        self.vertices.append(vertex)
        vertex.index = len(self.vertices) - 1
        self.prev[label]: str = None

    def addEdge(self, label1:str, label2:str, weight: int):
        index1:int = self.findVertexByLabel(label1).index
        index2:int = self.findVertexByLabel(label2).index
        self.adjacencyMatrix[index1][index2] = weight

    def dijkstra(self, labelStart: str, labelEnd: str):
        currentVertex = self.findVertexByLabel(labelStart)
        currentVertex.weight = 0
        while currentVertex is not None:
            for index in range(len(self.adjacencyMatrix)):
                if self.adjacencyMatrix[currentVertex.index][index] != float("inf"):
                    tmp: Vertex = self.vertices[index]
                    if currentVertex.weight + self.adjacencyMatrix[currentVertex.index][index] < tmp.weight:
                        tmp.weight = currentVertex.weight + self.adjacencyMatrix[currentVertex.index][index]
                        self.prev[tmp.label] = currentVertex.label
            self.visited.append(currentVertex)
            currentVertex = self.findCheapestVertex()

        print(self.returnPath(labelEnd))

    def returnPath(self, labelEnd: str):
        if self.prev[labelEnd] is  None:
            return labelEnd
        else:
            return self.returnPath(self.prev[labelEnd]) + " -> " + labelEnd
    

    def findCheapestVertex(self):
        cheapestVertex = Vertex("None", float("inf"))
        for vertex in self.vertices:
            if vertex not in self.visited:
                if vertex.weight < cheapestVertex.weight:
                    cheapestVertex = vertex
        if cheapestVertex.label == "None":
            return None
        else:
            return cheapestVertex

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

        