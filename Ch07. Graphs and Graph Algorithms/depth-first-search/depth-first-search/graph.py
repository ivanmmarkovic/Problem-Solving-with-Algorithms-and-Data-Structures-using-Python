from stack import Stack

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
        s = Stack()
        s.push(label)
        self.colors[label] = "gray"
        self.time += 1
        self.entry[label] = self.time
        current: str  
        neighbour: str
        while not s.isEmpty():
            current = s.peek()
            neighbour = self.findUnvisitedNeighbour(current)
            if neighbour is not None:
                    self.colors[neighbour] = "gray"
                    self.distance[neighbour] = self.distance[current] + 1
                    self.prev[neighbour] = current
                    self.time += 1
                    self.entry[neighbour] = self.time
                    s.push(neighbour)
            else:
                s.pop()
                self.time += 1
                self.exit[current] = self.time
                self.colors[current] = "black"

    def findUnvisitedNeighbour(self, label: str):
        count: int = 0
        found: bool = False
        neighbour: str = None
        while count < len(self.adjacencyList[label]) and not found:
            if self.colors[self.adjacencyList[label][count]] == "white":
                found = True
                neighbour = self.adjacencyList[label][count]
            else:
                count += 1
        return neighbour


    def showPath(self, end: str)->str:
        if self.prev[end] is None:
            return end
        else:
            return self.showPath(self.prev[end]) + " -> " + end




            


