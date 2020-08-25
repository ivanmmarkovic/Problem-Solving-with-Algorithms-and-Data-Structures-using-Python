from priorityqueue import PriorityQueue
from vertex import Vertex

class Graph:
    def __init__(self):
        self.__vertices__: dict = {}
        self.__prev__: dict = {}
        self.__adjacency_map__: dict = {}

    def add_vertex(self, label: str):
        self.__vertices__[label] = Vertex(label)
        self.__prev__[label] = None
        self.__adjacency_map__[label]: dict = {}

    def add_edge(self, label1: str, label2: str, weight: int = float("inf")):
        self.__adjacency_map__[label1][label2] = Vertex(label2, weight)

    def prims(self, label: str):
        self.__vertices__[label].weight = 0
        pq: PriorityQueue = PriorityQueue()
        for label in self.__vertices__:
            pq.insert(self.__vertices__[label])
        
        result: str = ""
        while not pq.is_empty():
            v: Vertex = pq.delete_min()
            if self.__prev__[v.label] is not None:
                result += self.__prev__[v.label] + " - " + v.label + ", "
            for neighbour_label in self.__adjacency_map__[v.label]:
                neighbour: Vertex = self.__adjacency_map__[v.label][neighbour_label]
                vertex: Vertex = self.__vertices__[neighbour_label]
                if neighbour.weight < vertex.weight:
                    self.__prev__[neighbour_label] = v.label
                    vertex.weight = neighbour.weight
                    pq.decrease_key(vertex.key)

        print(result)
    
    

    