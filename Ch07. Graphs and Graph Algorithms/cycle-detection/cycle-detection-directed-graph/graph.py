
class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.colors: dict = {}
        self.previous: dict = {}

    def addVertex(self, label: str):
        self.vertices.append(label)
        self.adjacencyList[label]: list = []
        self.colors[label] = "white"
        self.previous[label] = None

    def addEdge(self, label1: str, label2: str):
        self.adjacencyList[label1].append(label2)

    def dfs(self, label: str):
        self.colors[label] = "gray"
        for neighbour in self.adjacencyList[label]:
            if self.colors[neighbour] == "gray":
                print("Cycle", label, " -> ", neighbour)
            elif self.colors[neighbour] == "white":
                self.previous[neighbour] = label
                self.colors[neighbour] = "gray"
                self.dfs(neighbour)
        self.colors[label] = "black"





            


