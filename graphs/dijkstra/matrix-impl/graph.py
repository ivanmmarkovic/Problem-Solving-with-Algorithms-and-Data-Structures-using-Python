from vertex import Vertex


class Graph:
    def __init__(self, size: int = 10):
        self.size: int = size
        self.index: int = 0
        self.vertices_list: list = [None] * self.size
        self.vertices: dict = {}
        self.adjacency_matrix: list = [[None for i in range(self.size)] for j in range(self.size)]
        self.prev: dict = {}
        self.visited: dict = {}

    def add_vertex(self, label: str):
        if self.index == self.size:  # matrix is full
            return
        vertex: Vertex = Vertex(label, float("inf"), self.index)
        self.vertices_list[self.index] = vertex
        self.vertices[vertex.label] = vertex
        self.index += 1
        self.prev[vertex.label] = None
        self.visited[vertex.label] = False

    def add_edge(self, label1: str, label2: str, weight: int):
        index1: int = self.vertices[label1].index
        index2: int = self.vertices[label2].index
        self.adjacency_matrix[index1][index2] = weight

    def dijkstra(self, label: str):
        current_vertex: Vertex = self.vertices[label]
        current_vertex.weight = 0
        while current_vertex is not None:
            self.visited[current_vertex.label] = True
            for i in range(self.index):
                if self.adjacency_matrix[current_vertex.index][i] is not None:
                    weight: int = self.adjacency_matrix[current_vertex.index][i]
                    neighbour: Vertex = self.vertices_list[i]
                    if current_vertex.weight + weight < neighbour.weight:
                        neighbour.weight = current_vertex.weight + weight
                        self.prev[neighbour.label] = current_vertex.label
            current_vertex = self.find_minimum_weight_vertex()

    def return_path(self, label: str) -> str:
        if self.prev[label] is None:
            return label
        else:
            return self.return_path(self.prev[label]) + " -> " + label

    def find_minimum_weight_vertex(self):
        vertex: Vertex = None
        for label in self.vertices:
            if not self.visited[label]:
                if vertex is None:
                    vertex = self.vertices[label]
                else:
                    if vertex.weight > self.vertices[label].weight:
                        vertex = self.vertices[label]
        return vertex



