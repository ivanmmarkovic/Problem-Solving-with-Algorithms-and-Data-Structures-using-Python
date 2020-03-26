from vertex import Vertex

class Graph:
    def __init__(self, size: int = 10):
        self.vertices: list = []
        self.prev: dict = {}
        self.adjacencyMatrix: list = [[None for x in range(size)] for y in range(size)] 
        self.visited: dict = {}

    def addVertex(self, label: str):
        vertex: Vertex = Vertex(label, float("inf"), len(self.vertices))
        self.vertices.append(vertex)
        self.prev[label] = None
        self.visited[label] = False

    def addEdge(self, label1: str, label2: str, weight: int):
        index1: int = self.findIndexByLabel(label1)
        index2: int = self.findIndexByLabel(label2)
        self.adjacencyMatrix[index1][index2] = weight

    def dijkstra(self, label: str):
        index: int = self.findIndexByLabel(label)
        self.vertices[index].weight = 0
        tmpVertex: Vertex = self.vertices[index]
        neighbour: Vertex
        while tmpVertex is not None:            
            for neighbourIndex in range(len(self.adjacencyMatrix[tmpVertex.index])):
                if self.adjacencyMatrix[tmpVertex.index][neighbourIndex] is not None:
                    neighbour = self.vertices[neighbourIndex]
                    if tmpVertex.weight + self.adjacencyMatrix[tmpVertex.index][neighbour.index] < neighbour.weight:
                        self.prev[neighbour.label] = tmpVertex.label
                        neighbour.weight = tmpVertex.weight + self.adjacencyMatrix[tmpVertex.index][neighbour.index]
            self.visited[tmpVertex.label] = True
            tmpVertex = self.findUnvisitedVertexWithMinWeight()
        
    def returnPath(self, label: str)->str:
        if self.prev[label] is None:
            return label
        else:
            return self.returnPath(self.prev[label]) + " -> " + label

    def findUnvisitedVertexWithMinWeight(self)->Vertex:
        unvisitedVertex: Vertex = None
        for vertex in self.vertices:
            if not self.visited[vertex.label]:
                if unvisitedVertex is None:
                    unvisitedVertex = vertex
                elif unvisitedVertex.weight > vertex.weight:
                    unvisitedVertex = vertex
        return unvisitedVertex


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
            raise Exception("Can't find vertex with label " + label)




