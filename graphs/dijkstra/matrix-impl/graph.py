from vertex import Vertex


class Graph:
    def __init__(self, matrix_size: int = 10):
        self._matrix_size: int = matrix_size
        self._vertices: list = [None] * self._matrix_size
        self._pointer: int = 0
        self._adjacency_matrix: list = [[None for i in range(self._matrix_size)] for j in range(self._matrix_size)]
        self._prev: dict = {}
        self._visited: dict = {}

    def add_vertex(self, label: str = None, weight: int = float("inf")):
        if self._pointer == self._matrix_size:
            return
        vertex: Vertex = Vertex(label, float("inf"), self._pointer)
        self._vertices[self._pointer] = vertex
        self._prev[label] = None
        self._pointer += 1

    def add_edge(self, label1: str, label2: str, weight: int):
        vertex1: Vertex = self._find_vertex_by_label(label1)
        vertex2: Vertex = self._find_vertex_by_label(label2)
        self._adjacency_matrix[vertex1.get_index()][vertex2.get_index()] = weight

    def dijkstra(self, label: str):
        vertex: Vertex = self._find_vertex_by_label(label)
        vertex.set_weight(0)
        while vertex is not None:
            index: int = vertex.get_index()
            for i in range(len(self._adjacency_matrix[index])):
                if self._adjacency_matrix[index][i] is not None:
                    neighbour: Vertex = self._vertices[i]
                    if neighbour.get_weight() > vertex.get_weight() + self._adjacency_matrix[index][i]:
                        self._prev[neighbour.get_label()] = vertex.get_label()
                        neighbour.set_weight(vertex.get_weight() + self._adjacency_matrix[index][i])
            self._visited[vertex.get_label()] = vertex
            vertex = self._find_minimum_weight_vertex()

    def return_path(self, end_label: str = None) -> str:
        if self._prev[end_label] is None:
            return end_label
        else:
            return self.return_path(self._prev[end_label]) + " -> " + end_label

    def _find_vertex_by_label(self, label: str) -> Vertex:
        vertex: Vertex = None
        i: int = 0
        found: bool = False
        while i <= self._pointer and not found:
            if self._vertices[i].get_label() == label:
                vertex = self._vertices[i]
                found = True
            else:
                i += 1
        return vertex

    def _find_minimum_weight_vertex(self):
        vertex: Vertex = None
        for i in range(0, self._pointer, +1):
            v: Vertex = self._vertices[i]
            if v.get_label() not in self._visited:
                if vertex is None:
                    vertex = v
                elif vertex.get_weight() > v.get_weight():
                    vertex = v
        return vertex
