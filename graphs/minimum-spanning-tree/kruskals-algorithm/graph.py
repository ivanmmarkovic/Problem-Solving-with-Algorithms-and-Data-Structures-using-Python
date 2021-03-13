from vertex import Vertex

def find_root(vertex: Vertex = None) -> Vertex:
    while vertex.root != vertex:
        vertex = vertex.root
    return vertex

def sort_edges_by_weight_increasingly(edges: list) -> list:
    # edges [[label1, label2, weight], [label1, label2, weight]]
    if len(edges) < 2:
        return edges
        
    pivot_index: int = len(edges) // 2
    pivot_value = edges[pivot_index][2] 
    left_list: list = []
    right_list: list = []
    for i in range(len(edges)):
        if i != pivot_index:
            if edges[i][2] < pivot_value:
                left_list.append(edges[i])
            else:
                right_list.append(edges[i])
        
    return sort_edges_by_weight_increasingly(left_list) + [edges[pivot_index]] + sort_edges_by_weight_increasingly(right_list)



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
        self.edges.append([vertex_2_label, vertex_1_label, weight])

    def kruskal(self):
        # sort edges by weight increasingly
        self.edges = sort_edges_by_weight_increasingly(self.edges)
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