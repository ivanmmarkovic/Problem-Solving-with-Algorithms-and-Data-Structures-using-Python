class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.colors: dict = {}
        self.previous: dict = {}
        self.distance: dict = {}
        self.time: int = 0
        self.entry: dict = {}
        self.exit: dict = {}
        self.no_incoming_edges: dict = {} # to avoid looking through whole list
        self.explored: list = []

    def addVertex(self, label: str):
        self.vertices.append(label)
        self.adjacencyList[label]: list = []
        self.colors[label] = "white"
        self.distance[label] = 0
        self.previous[label] = None
        self.no_incoming_edges[label] = label

    def addEdge(self, label1: str, label2: str):
        self.adjacencyList[label1].append(label2)
        if label2 in self.no_incoming_edges:
            del self.no_incoming_edges[label2] # remove vertex, it has incoming edge

    def topsort(self):
        # perform depth first search on vertices with no incoming edges
        for label in self.no_incoming_edges:
            self.dfs(label)
        self.explored.reverse()
        print(self.explored)

    def dfs(self, start: str):
        self.time += 1
        self.entry[start] = self.time
        self.colors[start] = "gray"
        for neighbour in self.adjacencyList[start]:
            if self.colors[neighbour] == "white":
                self.previous[neighbour] = start
                self.distance[neighbour] = self.distance[neighbour] + 1
                self.dfs(neighbour)
        self.time += 1
        self.exit[start] = self.time
        self.colors[start] = "black"
        self.explored.append(start)

    def showPath(self, label: str)->str:
        if self.previous[label] is None:
            return label
        else:
            return self.showPath(self.previous[label]) + " -> " + label

