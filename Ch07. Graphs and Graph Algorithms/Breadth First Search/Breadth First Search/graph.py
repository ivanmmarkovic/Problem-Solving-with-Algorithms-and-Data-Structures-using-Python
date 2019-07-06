
from queue import Queue

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.prev: dict = {}
        self.distance: dict = {}
        self.colors: dict = {}
        self.adjacencyList: dict = {}

    def add_vertex(self, label: str):
        self.vertices.append(label)
        self.prev[label] = None
        self.distance[label] = float("inf")
        self.colors[label] = "white"
        self.adjacencyList[label]: list = []

    def add_edge(self, label1,  label2):
        self.adjacencyList[label1].append(label2)
        self.adjacencyList[label2].append(label1)

    def bfs(self, label_start:str, end_label: str):
        self.distance[label_start] = 0
        self.colors[label_start] = "gray"
        q = Queue()
        q.enqueue(label_start)
        while not q.isEmpty():
            dequeued = q.dequeue()
            for neighbour in self.adjacencyList[dequeued]:
                if self.colors[neighbour] == "white":
                    self.distance[neighbour] = self.distance[dequeued] + 1
                    self.prev[neighbour] = dequeued
                    self.colors[neighbour] = "gray"
                    q.enqueue(neighbour)
            self.colors[dequeued] = "black"

        print(self.print_path(end_label))

    def print_path(self, end_label)-> str:
        if self.prev[end_label] is None:
            return end_label
        else:
            return self.print_path(self.prev[end_label]) + " -> " + end_label

    def to_string(self):
        result = ""
        for vertex in self.vertices:
            result += ("Neigbours of " + vertex + ": ")
            for neighbour in self.adjacencyList[vertex]:
                result += (neighbour + ", ")
            result += "\n"
        return result
