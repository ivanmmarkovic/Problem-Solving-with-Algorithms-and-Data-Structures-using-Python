
from typing import List, Set, Dict, Tuple

class Graph:


    def __init__(self) -> None:
        self.vertices:Set[str] = set()
        self.roots:Dict[str, str] = dict()
        self.sizes:Dict[str, int] = dict()
        self.edges:List[Tuple[str, str, int]] = list()
        self.mst:List[Tuple[str, str, int]] = list()

    
    def add_vertex(self, label:str) -> None:
        self.vertices.add(label)
        self.roots[label] = label
        self.sizes[label] = 1


    def add_edge(self, label1:str, label2:str, weight:int) -> None:
        if label1 not in self.vertices or label2 not in self.vertices:
            raise Exception("Vertices must be added before connecting them")
        self.edges.append((label1, label2, weight))


    def kruskal(self) -> List[Tuple[str, str, int]]:
        self.mst.clear()
        self.edges.sort(key = lambda edge: edge[2])

        for v1, v2, weight in self.edges:

            root1:str = self._find_root(v1)
            root2:str = self._find_root(v2)

            if root1 != root2:
                if self.sizes[root1] >= self.sizes[root2]:
                    self.roots[root2] = root1
                    self.sizes[root1] += self.sizes[root2]
                else:
                    self.roots[root1] = root2
                    self.sizes[root2] += self.sizes[root1]
                self.mst.append((v1, v2, weight))

        return list(self.mst)
    
    def _find_root(self, label:str) -> str:
        if self.roots[label] != label:
            self.roots[label] = self._find_root(self.roots[label])
        return self.roots[label]



