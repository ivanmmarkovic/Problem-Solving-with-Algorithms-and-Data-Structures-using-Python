from priorityqueue import PriorityQueue
from vertex import Vertex

class Graph:
    def __init__(self):
        self.__vertices__: dict = {}
        self.__prev__: dict = {}
        self.__distance__: dict = {}
        self.__adjacency_map__: dict = {}

    def add_vertex(self, label: str):
        self.__vertices__[label] = Vertex(label)
        self.__prev__[label] = None
        self.__distance__[label] = 0
        self.__adjacency_map__[label]: dict = {}

    def add_edge(self, label1: str, label2: str, weight: int = float("inf")):
        self.__adjacency_map__[label1][label2] = Vertex(label2, weight)

    def dijkstra(self, label: str):
        self.__vertices__[label].weight = 0
        pq: PriorityQueue = PriorityQueue()
        for label in self.__vertices__:
            pq.insert(self.__vertices__[label])
        
        while not pq.is_empty():
            v: Vertex = pq.delete_min()
            for neighbour_label in self.__adjacency_map__[v.label]:
                neighbour: Vertex = self.__adjacency_map__[v.label][neighbour_label]
                vertex: Vertex = self.__vertices__[neighbour_label]
                if v.weight + neighbour.weight < vertex.weight:
                    self.__prev__[neighbour_label] = v.label
                    self.__distance__[neighbour_label] = self.__distance__[v.label] + 1
                    vertex.weight = v.weight + neighbour.weight
                    pq.decrease_key(vertex.key)
    
    def show_path(self, end: str) -> str:
        if self.__prev__[end] is None:
            return end
        else:
            return self.show_path(self.__prev__[end]) + " -> " + end

    