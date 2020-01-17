
class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.distance: dict = {}
        self.prev: dict = {}
        self.colors: dict = {}
        self.entry: dict = {}
        self.exit: dict = {}
        self.time: int = 0

    def addVertex(self, label: str):
        self.vertices.append(label)
        self.adjacencyList[label]: list = []
        self.distance[label] = 0
        self.prev[label] = None
        self.colors[label] = "white"

    def addEdge(self, label1: str, label2: str):
        self.adjacencyList[label1].append(label2)
        self.adjacencyList[label2].append(label1)

    def dfs(self, label: str):
        self.colors[label] = "gray"
        self.time += 1
        self.entry[label] = self.time
        for neighbour in self.adjacencyList[label]:
            if self.colors[neighbour] == "white":
                self.colors[neighbour] = "gray"
                self.distance[neighbour] = self.distance[label] + 1
                self.prev[neighbour] = label
                self.time += 1
                self.entry[neighbour] = self.time
                self.dfs(neighbour)
        self.time += 1
        self.exit[label] = self.time
        self.colors[label] = "black"

    def showPath(self, end: str)->str:
        if self.prev[end] is None:
            return end
        else:
            return self.showPath(self.prev[end]) + " -> " + end




            


