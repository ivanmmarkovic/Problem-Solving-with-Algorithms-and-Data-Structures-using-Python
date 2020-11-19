from vertex import Vertex
from priorityqueue import PriorityQueue


class Graph:
    def __init__(self):
        self._vertices: dict = {}
        self._prev: dict = {}
        self._adjacency_map: dict = {}

    def add_vertex(self, label: str = None, weight: int = float("inf")):
        self._vertices[label] = Vertex(label)
        self._prev[label] = None
        self._adjacency_map[label]: dict = {}

    def add_edge(self, label1: str = None, label2: str = None, weight: int = float("inf")):
        self._adjacency_map[label1][label2] = Vertex(label2, weight)

    def dijkstra(self, label: str):
        self._vertices[label].set_weight(0)
        pq: PriorityQueue = PriorityQueue()
        for vertex_label in self._vertices:
            pq.insert(self._vertices[vertex_label])
        while not pq.is_empty():
            vertex: Vertex = pq.delete_min()
            for neighbour_label in self._adjacency_map[vertex.get_label()]:
                neighbour_from_adjacency_map: Vertex = self._adjacency_map[vertex.get_label()][neighbour_label]
                neighbour_from_vertices: Vertex = self._vertices[neighbour_label]
                if neighbour_from_vertices.get_weight() > \
                        vertex.get_weight() + neighbour_from_adjacency_map.get_weight():
                    neighbour_from_vertices.set_weight(vertex.get_weight() + neighbour_from_adjacency_map.get_weight())
                    self._prev[neighbour_from_vertices.get_label()] = vertex.get_label()
                    pq.decrease_key(neighbour_from_vertices.get_key())

    def return_path(self, end_label: str = None) -> str:
        if self._prev[end_label] is None:
            return end_label
        else:
            return self.return_path(self._prev[end_label]) + " -> " + end_label







