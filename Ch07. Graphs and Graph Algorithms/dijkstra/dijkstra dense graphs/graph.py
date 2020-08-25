from vertex import Vertex

class Graph:
    def __init__(self):
        self.__vertices__: dict = {}
        self.__prev__: dict = {}
        self.__adjacency_map__: dict = {}
        self.__visited__: dict = {}

    def add_vertex(self, label: str):
        self.__vertices__[label] = Vertex(label)
        self.__prev__[label] = None
        self.__adjacency_map__[label]: dict = {}

    def add_edge(self, label1: str, label2: str, weight: int = float("inf")):
        self.__adjacency_map__[label1][label2] = Vertex(label2, weight)

    def dijkstra(self, label: str):
        current: Vertex = self.__vertices__[label]
        current.weight = 0
        while current is not None:
            for neighbour_label in self.__adjacency_map__[current.label]:
                neighbour: Vertex = self.__adjacency_map__[current.label][neighbour_label]
                vertex: Vertex = self.__vertices__[neighbour_label]
                if current.weight + neighbour.weight < vertex.weight:
                    self.__prev__[vertex.label] = current.label
                    vertex.weight = current.weight + neighbour.weight
            self.__visited__[current.label] = current.label
            current = self.__find_vertex__()

    def __find_vertex__(self):
        vertex: Vertex = None
        for label in self.__vertices__:
            if label not in self.__visited__:
                if vertex is None:
                    vertex = self.__vertices__[label]
                else:
                    tmp: Vertex = self.__vertices__[label]
                    if tmp.weight < vertex.weight:
                        veretx = tmp
        return vertex

    def return_path(self, label: str) -> str:
        if self.__prev__[label] is None:
            return label
        else:
            return self.return_path(self.__prev__[label]) + " -> " + label



        
    
    

    