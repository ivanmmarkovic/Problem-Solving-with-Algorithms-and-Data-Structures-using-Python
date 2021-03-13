from vertex import Vertex

def find_root(vertex: Vertex = None) -> Vertex:
    while vertex.root != vertex:
        vertex = vertex.root
    return vertex


class Graph:
    def __init__(self):
        self.vertices: dict = {}
        self.edges: list = []

    def add_vertex(self, label: str = None):
        self.vertices[label] = Vertex(label)

    def add_edge(self, vertex_1_label: str = None, vertex_2_label: str = None, weight: int = float("inf")):
        if vertex_1_label not in self.vertices or vertex_2_label not in self.vertices:
            raise Exception("Invalid label name")
        self.edges.append([vertex_1_label, vertex_2_label, weight])

    def kruskal(self):
        # sort edges by weight increasingly
        minimum_spanning_tree: list = []
        for edge_list in self.edges:
            vertex_one: Vertex = self.vertices[edge_list[0]]
            vertex_two: Vertex = self.vertices[edge_list[1]]

            root_one: Vertex = find_root(vertex_one)
            root_two: Vertex = find_root(vertex_two)

            if root_one != root_two:
                root_one.root = root_two
                minimum_spanning_tree.append([vertex_one.label, vertex_two.label])

        print(minimum_spanning_tree)