

from typing import Dict, List, Set

from stack import Stack

class Graph:

    def __init__(self) -> None:
        self.vertices: List[str] = []
        self.colors: Dict[str, str] = {}
        self.adjacency_list: Dict[str, Set[str]] = {}
        self.adjacency_list_reversed: Dict[str, Set[str]] = {}
        self.stack: Stack = Stack()
        self.components: List[List[str]] = []

    def add_vertex(self, label:str):
        self.vertices.append(label)
        self.colors[label] = 'white'
        self.adjacency_list[label] = set()
        self.adjacency_list_reversed[label] = set()

    def add_edge(self, label1:str, label2:str):
        self.adjacency_list[label1].add(label2)
        self.adjacency_list_reversed[label2].add(label1)

    def kosaraju(self):
        for label in self.vertices:
            if self.colors[label] == 'white':
                self.dfs(label)

        for color in self.colors:
            self.colors[color] = 'white'

        while not self.stack.is_empty():
            current:str = self.stack.pop()

            if self.colors[current] == 'white':
                connected_components: List[str] = []
                self.dfs_reversed(current, connected_components)

                self.components.append(connected_components)

        print(self.components)


    def dfs(self, label:str):
        self.colors[label] = 'gray'

        for n in self.adjacency_list[label]:
            if self.colors[n] == 'white':
                self.dfs(n)

        self.colors[label] = 'black'
        self.stack.push(label)

    def dfs_reversed(self, label: str, connected_components:List[str]):
        self.colors[label] = 'gray'

        for n in self.adjacency_list_reversed[label]:
            if self.colors[n] == 'white':
                self.dfs_reversed(n, connected_components)
        connected_components.append(label)
        self.colors[label] = 'black'





