
from typing import Dict, List

from vertex import Vertex
from priorityqueue import PriorityQueue

class Graph:

    def __init__(self) -> None:
        self.vertices: Dict[str, Vertex] = dict()
        self.adjacency_map: Dict[str, List[Vertex]] = dict()
        self.prev:Dict[str, str] = dict()


    def add_vertex(self, label:str, weight:int=float('inf')):
        self.vertices[label] = Vertex(label)
        self.adjacency_map[label] = []
        self.prev[label] = None


    def add_edge(self, label1:str, label2:str, weight:int):
        self.adjacency_map[label1].append(Vertex(label2, weight))
        self.adjacency_map[label1].append(Vertex(label1, weight))

    
    def prims(self, label:str):
        res:str = ''
        v:Vertex = self.vertices[label]
        v.weight = 0

        pq:PriorityQueue = PriorityQueue()
        for k in self.vertices:
            vertex = self.vertices[k]
            pq.insert(vertex)

        while not pq.is_empty():
            v = pq.delete_min()
            print('Min is ', v.label)
            if self.prev[v.label] is not None:
                res += f'{self.prev[v.label]} -> {v.label}, '
            for neighbour in self.adjacency_map[v.label]:
                vertex:Vertex = self.vertices[neighbour.label]
                if neighbour.weight < vertex.weight:
                    vertex.weight = neighbour.weight
                    self.prev[vertex.label] = v.label
                    pq.decrease_key(vertex.index)

        print(res)
