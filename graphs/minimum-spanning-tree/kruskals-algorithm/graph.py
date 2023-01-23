from typing import Set, Dict, List, Tuple

class Graph:

    def __init__(self) -> None:
        self.vertices:Set[str] = set()
        self.root:Dict[str, str] = dict()
        self.rank:Dict[str, int] = dict()
        self.edges:List[Tuple[str, str, int]] = list()
        self.mst:List[Tuple[str, str, int]] = list()


    def add_vertex(self, label:str) -> None:
        self.vertices.add(label)
        self.root[label] = label
        self.rank[label] = 0


    def add_edge(self, label1:str, label2:str, weight:int) -> None:
        self.edges.append((label1, label2, weight))


    def kruskal(self) -> None:
        self.edges.sort(key = lambda edge: edge[2])
        for l1, l2, weight in self.edges:

            root1:str = self._find_root(l1)
            root2:str = self._find_root(l2)

            if root1 != root2:
                if self.rank[root1] > self.rank[root2]:
                    self.root[root2] = root1
                    self.rank[root1] = self.rank[root1] + 1
                else:
                    self.root[root1] = root2
                    self.rank[root2] = self.rank[root2] + 1
                self.mst.append((l1, l2, weight))

        print(self.mst)


    def _find_root(self, label:str) -> str:
        if self.root[label] != label:
            self.root[label] = self._find_root(self.root[label])
        return self.root[label]
