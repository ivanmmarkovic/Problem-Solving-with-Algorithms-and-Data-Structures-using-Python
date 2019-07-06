
from stack import Stack

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

    def dfs(self, label_start:str, end_label: str):
        self.distance[label_start] = 0
        self.colors[label_start] = "gray"
        stack = Stack()
        stack.push(label_start)
        while not stack.isEmpty():
            peeked = stack.peek()
            neighbour: str = self.find_unvisited_neighbour(peeked)
            if neighbour is None:
                stack.pop()
                self.colors[peeked] = "black"
            else:
                self.distance[neighbour] = self.distance[peeked] + 1
                self.prev[neighbour] = peeked
                self.colors[neighbour] = "gray"
                stack.push(neighbour)

        print(self.print_path(end_label))

    def print_path(self, end_label)-> str:
        if self.prev[end_label] is None:
            return end_label
        else:
            return self.print_path(self.prev[end_label]) + " -> " + end_label

    def find_unvisited_neighbour(self, label)-> str:
        found: bool = False
        count: int = 0
        neighbour: str = ""
        while count < len(self.adjacencyList[label]) and not found:
            neighbour = self.adjacencyList[label][count]
            if self.colors[neighbour] == "white":
                found = True
            else:
                count += 1
        if found:
            return neighbour
        else:
            return None


    def to_string(self):
        result = ""
        for vertex in self.vertices:
            result += ("Neigbours of " + vertex + ": ")
            for neighbour in self.adjacencyList[vertex]:
                result += (neighbour + ", ")
            result += "\n"
        return result
