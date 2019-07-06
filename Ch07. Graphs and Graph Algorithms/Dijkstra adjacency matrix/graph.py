from vertex import Vertex

class Graph:
    def __init__(self, size: int):
        self.vertices: list = []
        self.adjacencyMatrix = [[float("inf") for x in range(size)] for y in range(size)] 
        self.previous: dict = {}
        self.visited: list = []

    def addVertex(self, label: str):
        self.vertices.append(Vertex(label, float("inf"), len(self.vertices)))
        self.previous[label]: str = None

    def addEdge(self, label1: str, label2: str, weight: int):
        index1: int = self.findIndexByLabel(label1)
        index2: int = self.findIndexByLabel(label2)
        self.adjacencyMatrix[index1][index2] = weight

    def dijkstra(self, label_start: str, label_end: str):
        index: int = self.findIndexByLabel(label_start)
        current: Vertex = self.vertices[index]
        current.weight = 0
        while current is not None:
            for i in range(len(self.adjacencyMatrix[current.index])):
                if self.adjacencyMatrix[current.index][i] != float("inf"):
                    if current.weight + self.adjacencyMatrix[current.index][i] < self.vertices[i].weight:
                        self.previous[self.vertices[i].label] = current.label
                        self.vertices[i].weight = current.weight + self.adjacencyMatrix[current.index][i]
            self.visited.append(current)
            current = self.findCheapestVertex()

        print(self.returnPath(label_end))

    def returnPath(self, labelEnd: str):
        if self.previous[labelEnd] is  None:
            return labelEnd
        else:
            return self.returnPath(self.previous[labelEnd]) + " -> " + labelEnd


    def findCheapestVertex(self)-> Vertex:
        cheapest: Vertex = None
        for vertex in self.vertices:
            if vertex not in self.visited:
                if cheapest is None:
                    cheapest = vertex
                else:
                    if vertex.weight < cheapest.weight:
                        cheapest = vertex
        return cheapest  

    def findIndexByLabel(self, label: str):
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
