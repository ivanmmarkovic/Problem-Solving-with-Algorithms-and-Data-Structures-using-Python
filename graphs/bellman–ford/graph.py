
#  Bellman-Ford algorithm
#  Find shortest paths from one vertex,
#  to all other vertices in weighted graph.
#  Runtime O(V*E)

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.edges: list = []
        self.distance: dict = {}
        self.prev: dict = {}

    def add_vertex(self, label: str):
        self.vertices.append(label)
        self.distance[label] = None
        self.prev[label] = None

    def add_edge(self, label1: str, label2: str, weight: int):
        self.edges.append([label1, label2, weight])

    def bellman_ford(self, source: str):
        self.distance[source] = 0

        for _ in range(len(self.vertices)):

            for edge in self.edges:
                label1: str = edge[0]
                label2: str = edge[1]
                weight: int = edge[2]

                if self.distance[label1] is None:
                    continue
                if self.distance[label2] is None:
                    self.distance[label2] = self.distance[label1] + weight
                    self.prev[label2] = label1
                    continue
                if self.distance[label1] + weight < self.distance[label2]:
                    self.distance[label2] = self.distance[label1] + weight
                    self.prev[label2] = label1
                    continue

    def print_distances(self, source: str):
        for v in self.vertices:
            if v != source:
                distance: int = self.distance[v]
                print(f'Distance from {source} to {v} is {distance}')