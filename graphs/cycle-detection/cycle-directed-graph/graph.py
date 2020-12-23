
class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacency_list: dict = {}
        self.prev: dict = {}
        self.distance: dict = {}
        self.colors: dict = {}
        self.entry: dict = {}
        self.exit: dict = {}
        self.time: int = 0

    def add_vertex(self, label: str):
        self.vertices.append(label)
        self.adjacency_list[label]: list = []
        self.prev[label] = None
        self.distance[label] = 0
        self.colors[label] = "white"

    def add_edge(self, label1: str, label2: str):
        self.adjacency_list[label1].append(label2)

    def dfs(self, label: str):
        self.colors[label] = "gray"
        self.time += 1
        self.entry[label] = self.time
        for neighbour in self.adjacency_list[label]:
            if self.colors[neighbour] == "white":
                self.prev[neighbour] = label
                self.distance[neighbour] = self.distance[label] + 1
                self.dfs(neighbour)
            if self.colors[neighbour] == "gray":
                print("Cycle", label, " - ", neighbour)
        self.colors[label] = "black"
        self.time += 1
        self.exit[label] = self.time

    def return_path(self, label: str) -> str:
        if self.prev[label] is None:
            return label
        else:
            return self.return_path(self.prev[label]) + " -> " + label
