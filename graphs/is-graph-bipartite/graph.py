from queue import Queue


class Graph:
    def __init__(self):
        self._vertices: list = []
        self._colors: dict = {}
        self._adjacency_matrix: dict = {}

    def add_vertex(self, label: str):
        self._vertices.append(label)
        self._colors[label] = None
        self._adjacency_matrix[label]: list = []

    def add_edge(self, label1: str, label2: str):
        self._adjacency_matrix[label1].append(label2)
        self._adjacency_matrix[label2].append(label1)

    def bipartite_check(self) -> bool:
        for vertex in self._vertices:
            if self._colors[vertex] is not None:
                continue
            self._colors[vertex] = "red"
            q: Queue = Queue()
            q.enqueue(vertex)
            while not q.is_empty():
                v = q.dequeue()
                for neighbour in self._adjacency_matrix[v]:
                    if self._colors[neighbour] == self._colors[v]:
                        return False
                    if self._colors[neighbour] is None:
                        if self._colors[v] == "red":
                            self._colors[neighbour] = "blue"
                        else:
                            self._colors[neighbour] = "red"
                        q.enqueue(neighbour)
        return True





