from Stack import Stack

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacencyList: dict = {}
        self.prev: dict = {}
        self.distance: dict = {}
        self.gray: list = []  # visited
        self.black: list = []  # explored

    def add_vertex(self, label):
        self.vertices.append(label)
        self.adjacencyList[label] = []
        self.prev[label] = None
        self.distance[label] = 0

    def add_edge(self, label1, label2):
        self.adjacencyList[label1].append(label2)
        # self.adjacencyList[label2].append(label1) directed acyclic graph

    def top_sort(self):
        for vertex in self.vertices:
            if vertex not in self.black:
                self.dfs(vertex)

        self.black.reverse()
        print(self.black)

    def dfs(self, start_label):
        stack = Stack()
        stack.push(start_label)
        self.gray.append(start_label)
        while not stack.isEmpty():
            peeked_vertex = stack.peek()
            neighbour = self.get_neighbour(peeked_vertex)
            if neighbour is not None:
                stack.push(neighbour)
                self.gray.append(neighbour)
                self.distance[neighbour] = self.distance[peeked_vertex] + 1
                self.prev[neighbour] = peeked_vertex
            else:
                peeked_vertex = stack.pop()
                self.black.append(peeked_vertex)

    def get_neighbour(self, label):
        count: int = 0
        found: bool = False
        while count < len(self.adjacencyList[label]) and not found:
            if self.adjacencyList[label][count] not in self.gray:
                found = True
            else:
                count += 1
        if found:
            return self.adjacencyList[label][count]
        else:
            return None

    def toString(self):
        result = ""
        for vertex in self.vertices:
            result += ("Neigbours of " + vertex + ": ")
            for neighbour in self.adjacencyList[vertex]:
                result += (neighbour + ", ")
            result += "\n"
        return result


























