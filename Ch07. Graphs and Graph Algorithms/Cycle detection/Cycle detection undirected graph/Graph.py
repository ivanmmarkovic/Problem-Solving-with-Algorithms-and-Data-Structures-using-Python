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
        self.adjacencyList[label2].append(label1)

    def dfs(self, start: str):
        self.colors[start] = "gray"
        self.entry[start] = self.time
        self.time += 1
        for neighbour in self.adjacencyList[start]:
            if self.colors[neighbour] == "white":
                self.distance[neighbour] = self.distance[start] + 1
                self.prev[neighbour] = start 
                self.dfs(neighbour)
            if self.colors[neighbour] == "gray" and self.prev[start] != neighbour:
                print("Cycle", start, "->", neighbour)
            
        self.colors[start] = "black"
        self.exit[start] = self.time 
        self.time + 1
        self.explored.append(start)

    def printPath(self, label: str)-> str:
        if self.prev[label] is None:
            return label
        else:
            return self.printPath(self.prev[label]) + " -> " + label

