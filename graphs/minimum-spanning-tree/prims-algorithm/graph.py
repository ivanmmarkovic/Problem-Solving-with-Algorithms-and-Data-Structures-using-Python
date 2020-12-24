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
        self._adjacency_map[label2].append(Vertex(label1, weight))

    def prims(self, label: str):
        result: str = ""
        self._vertices[label].weight = 0
        pq: PriorityQueue = PriorityQueue()
        for label in self._vertices:
            pq.insert(self._vertices[label])
        while not pq.is_empty():
            current: Vertex = pq.delete_min()
            if self._prev[current.label] is not None:
                result += self._prev[current.label] + " -> " + current.label + ", "
            for neighbour in self._adjacency_map[current.label]:
                v: Vertex = self._vertices[neighbour.label]
                if neighbour.weight < v.weight:
                    v.weight = neighbour.weight
                    self._prev[v.label] = current.label
                    pq.decrease_key(v.key)
        print(result)








