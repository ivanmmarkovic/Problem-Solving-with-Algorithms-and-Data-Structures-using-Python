

from typing import Dict, List, Set

from stack import Stack

class Graph:


    def __init__(self) -> None:
        self.vertices:Set[str] = set()
        self.adjacency_list:Dict[str, Set[str]] = dict()
        self.adjacency_list_reversed:Dict[str, Set[str]] = dict()
        self.visited:Set[str] = set()
        self.stack:Stack = Stack()


    def add_vertex(self, label:str) -> None:
        self.vertices.add(label)
        self.adjacency_list[label] = set()
        self.adjacency_list_reversed[label] = set()


    def add_edge(self, label1:str, label2:str) -> None:
        if label1 not in self.vertices or label2 not in self.vertices:
            raise Exception('Vertices are not added')
        self.adjacency_list[label1].add(label2)
        self.adjacency_list_reversed[label2].add(label1)


    def kosaraju(self) -> List[List[str]]:
        for v in self.vertices:
            if v not in self.visited:
                self._dfs(v)

        self.visited.clear()

        connected_components:List[List[str]] = list()

        while not self.stack.is_empty():
            v:str = self.stack.pop()
            if v not in self.visited:
                connected:List[str] = list()
                self._dfs_reversed(v, connected)

                if len(connected) > 0:
                    connected_components.append(connected)

        return list(connected_components)



    def _dfs(self, label:str) -> None:
        self.visited.add(label)

        for n in self.adjacency_list[label]:
            if n not in self.visited:
                self._dfs(n)

        self.stack.push(label)


    def _dfs_reversed(self, v:str, connected:List[str]) -> None:
        connected.append(v)
        self.visited.add(v)
        for n in self.adjacency_list_reversed[v]:
            if n not in self.visited:
                self._dfs_reversed(n, connected)




