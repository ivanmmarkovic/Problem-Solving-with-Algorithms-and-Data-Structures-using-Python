
#  Bellman-Ford algorithm
#  Find shortest paths from one vertex,
#  to all other vertices in weighted graph.
#  Runtime O(V*E)

from typing import Set, Dict, List, Tuple


class Graph:


    def __init__(self) -> None:
        self.vertices:Set[str] = set()
        self.edges:List[Tuple[str, str, int]] = list()
        self.prev:Dict[str, str] = dict()
        self.distances:Dict[str, int] = dict()


    def add_vertex(self, label:str) -> None:
        self.vertices.add(label)
        self.prev[label] = None
        self.distances[label] = None


    def add_edge(self, v1:str, v2:str, distance:int) -> None:
        self.edges.append((v1, v2, distance))


    def bellman_ford(self, label:str) -> None:
        self.distances[label] = 0

        for _ in range(len(self.vertices) - 1):

            for v1, v2, distance in self.edges:
                if self.distances[v1] is None:
                    continue
                if self.distances[v2] is None or self.distances[v2] > self.distances[v1] + distance:
                    self.distances[v2] = self.distances[v1] + distance
                    self.prev[v2] = v1

        # Check for negative-weight cycles
        for v1, v2, distance in self.edges:
            if self.distances[v1] is not None and self.distances[v2] > self.distances[v1] + distance:
                raise ValueError("Graph contains a negative-weight cycle")

        self._print_paths(label)


    def _print_paths(self, label:str) -> None:
        for v in self.vertices:
            if v == label:
                continue
            if self.distances[v] is not None:
                print(f'Path from {label} to {v} is {self._return_path(v)} and distance is {self.distances[v]}')
            else:
                print(f'No path from {label} to {v}')


    def _return_path(self, label:str) -> str:
        if self.prev[label] is None:
            return label
        return self._return_path(self.prev[label]) + ' -> ' + label
    


g = Graph()
for v in ['A', 'B', 'C', 'D']:
    g.add_vertex(v)

g.add_edge('A', 'B', 1)
g.add_edge('B', 'C', 3)
g.add_edge('A', 'C', 10)
g.add_edge('C', 'D', 2)
g.add_edge('D', 'B', 4)

g.bellman_ford('A')

