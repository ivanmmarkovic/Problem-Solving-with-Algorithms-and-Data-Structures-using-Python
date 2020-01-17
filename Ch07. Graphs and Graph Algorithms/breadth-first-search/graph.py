from queue import Queue

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.distance: dict = {}
        self.prev: dict = {}
        self.colors: dict = {}

    def addVertex(self, label: str):
        self.vertices.append(label)
        self.adjacencyList[label]: list = []
        self.distance[label] = 0
        self.prev[label] = None
        self.colors[label] = "white"

    def addEdge(self, label1: str, label2: str):
        self.adjacencyList[label1].append(label2)
        self.adjacencyList[label2].append(label1)

    def bfs(self, label: str):
        q = Queue()
        q.enqueue(label)
        self.colors[label] = "gray"
        current: str  
        while not q.isEmpty():
            current = q.dequeue()
            for neighbour in self.adjacencyList[current]:
                if self.colors[neighbour] == "white":
                    self.colors[neighbour] = "gray"
                    self.distance[neighbour] = self.distance[current] + 1
                    self.prev[neighbour] = current
                    q.enqueue(neighbour)
            self.colors[current] = "black"

    def showPath(self, end: str)->str:
        if self.prev[end] is None:
            return end
        else:
            return self.showPath(self.prev[end]) + " -> " + end




            


