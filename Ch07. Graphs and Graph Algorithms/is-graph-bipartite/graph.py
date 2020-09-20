from queue import Queue

class Graph:
    def __init__(self):
        self.__vertices__:dict = {}
        self.__adjacency_map__: dict = {}
        self.__colors__: dict = {}
        self.__colors__["red"]: list = []
        self.__colors__["blue"]: list = []


    def add_vertex(self, vertex: str):
        self.__vertices__[vertex] = vertex
        self.__adjacency_map__[vertex]:list = []

    def add_edge(self, vertex1: str, vertex2: str):
        self.__adjacency_map__[vertex1].append(vertex2)
        self.__adjacency_map__[vertex2].append(vertex1)

    def bipartite_check(self, vertex) -> bool:
        q: Queue = Queue()
        for vertex in self.__vertices__:
            if vertex in self.__colors__["red"] or vertex in self.__colors__["blue"]:
                continue
            self.__colors__["red"].append(vertex)
            q.enqueue(vertex)

            while not q.is_empty():
                tmp: str = q.dequeue()
                if tmp in self.__colors__["red"]:
                    current_color = "red"
                    opposite_color = "blue"
                else:
                    current_color = "blue"
                    opposite_color = "red"
                for neighbour in self.__adjacency_map__[tmp]:
                    if neighbour in self.__colors__[current_color]:
                        return False
                    if neighbour not in self.__colors__[opposite_color]:
                        self.__colors__[opposite_color].append(neighbour)
                        q.enqueue(neighbour)
        return True


    