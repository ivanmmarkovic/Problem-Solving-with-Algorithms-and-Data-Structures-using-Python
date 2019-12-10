from stack import Stack

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.distance: dict = {}
        self.prev: dict = {}
        self.adjacencyList: dict = {}
        self.colors: dict = {}
        self.entry: dict = {}
        self.exit: dict = {}
        self.time: int = 0
        self.explored: list = []

    def addVertex(self, label: str):
        self.vertices.append(label)
        self.distance[label] = 0
        self.prev[label] = None
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
            
    def dfs(self, start: str):
        self.colors[start] = "gray"
        self.entry[start] = self.time
        self.time += 1
        for neighbour in self.adjacencyList[start]:
            if self.colors[neighbour] == "white":
                self.distance[neighbour] = self.distance[start] + 1
                self.prev[neighbour] = start 
                self.dfs(neighbour)
        self.colors[start] = "black"
        self.exit[start] = self.time 
        self.time + 1
        self.explored.append(start)


