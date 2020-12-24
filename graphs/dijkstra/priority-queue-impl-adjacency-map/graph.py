from vertex import Vertex
from priorityqueue import PriorityQueue


class Graph:
    def __init__(self):
        self._vertices: dict = {}
        self._adjacency_map: dict = {}
        self._prev: dict = {}

    def add_vertex(self, label: str):
        v: Vertex = Vertex(label)
        self._vertices[label] = v
        self._adjacency_map[label]: list = []
        self._prev[label] = None

    def add_edge(self, label1: str, label2: str, weight: int):
        self._adjacency_map[label1].append(Vertex(label2, weight))

    def dijkstra(self, label: str):
        self._vertices[label].weight = 0
        pq: PriorityQueue = PriorityQueue()
        for label in self._vertices:
            pq.insert(self._vertices[label])
        while not pq.is_empty():
            current: Vertex = pq.delete_min()
            for neighbour in self._adjacency_map[current.label]:
                v: Vertex = self._vertices[neighbour.label]
                if current.weight + neighbour.weight < v.weight:
                    v.weight = current.weight + neighbour.weight
                    self._prev[v.label] = current.label
                    pq.decrease_key(v.key)

    def show_path(self, label: str) -> str:
        if self._prev[label] is None:
            return label
        else:
            return self.show_path(self._prev[label]) + " -> " + label








