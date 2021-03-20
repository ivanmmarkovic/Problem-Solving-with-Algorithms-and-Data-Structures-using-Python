from vertex import Vertex


class Graph:

    def __init__(self):
        self.vertices: dict = {}
        self.edges: list = []

    def add_vertex(self, label: str = None):
        self.vertices[label] = Vertex(label)

    def add_edge(self, label1: str, label2: str):
        self.edges.append([label1, label2])

    def union_find(self):

        for edge in self.edges:
            label_one: str = edge[0]
            label_two: str = edge[1]
            vertex_one = self.vertices[label_one]
            vertex_two = self.vertices[label_two]

            root_one: Vertex = self.find_root(vertex_one)
            root_two: Vertex = self.find_root(vertex_two)

            if root_one != root_two:
                if root_one.rank > root_two.rank:
                    root_two.parent = root_one
                    root_one.rank = root_one.rank + 1
                else:
                    root_one.parent = root_two
                    root_two.rank = root_two.rank + 1

    def find_root(self, vertex: Vertex):
        if vertex.parent != vertex:
            vertex.parent = self.find_root(vertex.parent)
            return vertex.parent
        return vertex.parent
