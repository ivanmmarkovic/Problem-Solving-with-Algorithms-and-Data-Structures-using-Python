
class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.colors: dict = {}
        self.explored: list = []

    def addVertex(self, label: str):
        self.vertices.append(label)
        self.adjacencyList[label]: list = []
        self.colors[label] = "white"

    def addEdge(self, label1: str, label2: str):
        self.adjacencyList[label1].append(label2)

    def topsort(self):
        for vertex in self.vertices:
            if self.colors[vertex] == "white":
                self.dfs(vertex)
        self.explored.reverse()
        print(self.explored)
        
    def dfs(self, label: str):
        self.colors[label] = "gray"
        for neighbour in self.adjacencyList[label]:
            if self.colors[neighbour] == "white":
                self.colors[neighbour] = "gray"
                self.dfs(neighbour)
        self.explored.append(label)
        self.colors[label] = "black"





            


