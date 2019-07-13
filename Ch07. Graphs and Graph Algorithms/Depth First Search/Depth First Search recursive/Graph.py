from Stack import Stack

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
        # self.adjacencyList[label2].append(label1) directed acyclic graph

    
    def dfs(self, label):
        self.colors[label] = "gray"
        for neighbour in  self.adjacencyList[label]:
            if self.colors[neighbour] == "white":
                self.colors[neighbour] = "gray"
                self.prev[neighbour] = label
                self.dfs(neighbour)
        self.colors[label] = "black"

    def print_path(self, end_label)-> str:
        if self.prev[end_label] is None:
            return end_label
        else:
            return self.print_path(self.prev[end_label]) + " -> " + end_label

    def get_neighbour(self, label)-> str:
        count: int = 0
        found: bool = False
        while count < len(self.adjacencyList[label]) and not found:
            if self.colors[self.adjacencyList[label][count]] == "white":
                found = True
            else:
                count += 1
        if found:
            return self.adjacencyList[label][count]
        else:
            return None

    def toString(self):
        result = ""
        for vertex in self.vertices:
            result += ("Neigbours of " + vertex + ": ")
            for neighbour in self.adjacencyList[vertex]:
                result += (neighbour + ", ")
            result += "\n"
        return result


























