from queue import Queue


class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacency_list: dict = {}
        self.color: dict = {}

    def add_vertex(self, label: str = None):
        self.vertices.append(label)
        self.adjacency_list[label]: list = []
        self.color[label] = None

    def add_edge(self, label1: str = None, label2: str = None):
        self.adjacency_list[label1].append(label2)
        self.adjacency_list[label2].append(label1)

    def is_bipartite(self) -> bool:
        for vertex in self.vertices:
            if self.color[vertex] is not None:
                continue
            q: Queue = Queue()
            self.color[vertex] = "red"
            q.enqueue(vertex)
            while not q.is_empty():
                tmp: str = q.dequeue()
                for neighbour in self.adjacency_list[tmp]:
                    if self.color[neighbour] == self.color[tmp]:
                        return False
                    if self.color[neighbour] is None:
                        if self.color[tmp] == "red":
                            self.color[neighbour] = "blue"
                        else:
                            self.color[neighbour] = "red"
                        q.enqueue(neighbour)
        return True






