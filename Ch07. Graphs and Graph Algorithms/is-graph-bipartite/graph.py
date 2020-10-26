from queue import Queue

class Graph:
    def __init__(self):
        self.__vertices__: list = []
        self.__adjacency_list__: dict = {}
        self.__colors__: dict = {}

    def add_vertex(self, label: str):
        self.__vertices__.append(label)
        self.__adjacency_list__[label]: list = []

    def add_edge(self, label1: str, label2: str):
        self.__adjacency_list__[label1].append(label2)
        self.__adjacency_list__[label2].append(label1)

    def is_bipartite(self) -> bool:
        for vertex in self.__vertices__:
            if vertex not in self.__colors__:
                self.__colors__[vertex] = "red"
                q: Queue = Queue()
                q.enqueue(vertex)

                current: str = None
                while not q.is_empty():
                    current = q.dequeue()
                    for neighbour in self.__adjacency_list__[current]:
                        if neighbour not in self.__colors__:
                            if self.__colors__[current] == "red":
                                self.__colors__[neighbour] = "blue"
                            else:
                                self.__colors__[neighbour] = "red"
                            q.enqueue(neighbour)
                        else:
                            if self.__colors__[neighbour] == self.__colors__[current]:
                                return False
        return True
                            
