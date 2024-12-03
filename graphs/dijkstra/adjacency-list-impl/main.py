
from typing import List, Dict, Set

from vertex import Vertex


class Graph:

    def __init__(self, capacity :int =10):
        self.capacity :int = capacity
        self.vertices :Dict[str, Vertex] = dict()
        self.prev :Dict[str, str] = dict()
        self.adjacency_list :Dict[str, List[Vertex]] = dict()
        self.visited :Set[str] = set()



    def add_vertex(self, label :str, weight :int = float('inf')) -> None:
        v :Vertex = Vertex(label, weight)
        self.vertices[v.label] = v
        self.adjacency_list[label] = list()
        self.prev[label] = None


    def add_edge(self, label1 :str, label2 :str, weight :int) -> None:
        v :Vertex = Vertex(label2, weight)
        self.adjacency_list[label1].append(v)


    def dijkstra(self, label :str) -> None:
        v :Vertex = self.vertices[label]
        v.weight = 0

        while v is not None:
            for n in self.adjacency_list[v.label]:
                o :Vertex = self.vertices[n.label]
                if v.weight + n.weight < o.weight:
                    o.weight = v.weight + n.weight
                    self.prev[o.label] = v.label
            self.visited.add(v.label)
            v = self._find_cheapest_vertex()


    def show_path(self, label :str) -> str:
        if self.prev[label] is None:
            return label
        return self.show_path(self.prev[label]) + '->' + label


    def _find_cheapest_vertex(self) -> Vertex:
        vertex :Vertex = None
        for v in self.vertices.values():
            if v.label not in self.visited:
                if vertex is None:
                    vertex = v
                elif vertex.weight > v.weight:
                    vertex = v

        return vertex



graph: Graph = Graph()

graph.add_vertex("START")
graph.add_vertex("A")
graph.add_vertex("C")
graph.add_vertex("B")
graph.add_vertex("D")
graph.add_vertex("END")

graph.add_edge("START", "A", 0)
graph.add_edge("START", "C", 2)
graph.add_edge("A", "B", 18)
graph.add_edge("A", "D", 15)
graph.add_edge("C", "B", 3)
graph.add_edge("C", "D", 10)
graph.add_edge("B", "END", 150)
graph.add_edge("D", "END", 15)
graph.dijkstra("START")

print(graph.show_path("END"))





