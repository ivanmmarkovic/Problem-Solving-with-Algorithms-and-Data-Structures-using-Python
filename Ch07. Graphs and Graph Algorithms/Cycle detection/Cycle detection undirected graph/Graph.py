
class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.prev: dict = {}
        self.colors: dict = {}
        self.explored: list = []

    def add_vertex(self, label):
        self.vertices.append(label)
        self.adjacencyList[label] = []
        self.prev[label] = None
        self.colors[label] = "white"

    def add_edge(self, label1, label2):
        self.adjacencyList[label1].append(label2)
        self.adjacencyList[label2].append(label1)

    def dfs(self, label: str, prev = None):
        if self.colors[label] == "gray" and prev is not None and label not in self.adjacencyList[prev]:
            print("Cycle", prev, label)
            return
        if self.colors[label] != "white": # only black will fall there
            return 
        self.prev[label] = prev
        self.colors[label] = "gray"
        for neighbour in self.adjacencyList[label]:
            self.dfs(neighbour, label)
        self.colors[label] = "black"

    def print_path(self, label: str)-> str:
        if self.prev[label] is None:
            return label
        else:
            return self.print_path(self.prev[label]) + " -> " + label



























