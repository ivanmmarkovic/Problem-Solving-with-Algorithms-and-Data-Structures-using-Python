from stack import Stack


class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacency_list: dict = {}
        self.adjacency_list_reversed: dict = {}
        self.time = 0
        self.visited: dict = {}
        self.entry: dict = {}
        self.exit: dict = {}
        self.stack: Stack = Stack()
        self.connected_components: list = []

    def add_vertex(self, label: str):
        self.vertices.append(label)
        self.adjacency_list[label]: list = []
        self.adjacency_list_reversed[label]: list = []
        self.visited[label] = False

    def add_edge(self, label1: str, label2: str):
        self.adjacency_list[label1].append(label2)
        self.adjacency_list_reversed[label2].append(label1)

    def kosaraju(self):
        for vertex in self.vertices:
            if not self.visited[vertex]:
                self.dfs(vertex)
        for vertex in self.visited:
            self.visited[vertex] = False
        while not self.stack.is_empty():
            vertex = self.stack.pop()
            components: list = []
            if not self.visited[vertex]:
                self.dfs_reversed_edges(vertex, components)
            if len(components) > 0:
                self.connected_components.append(components)
        print(self.connected_components)

    def dfs(self, label: str):
        self.visited[label] = True
        self.time += 1
        self.entry[label] = self.time
        for neighbour in self.adjacency_list[label]:
            if not self.visited[neighbour]:
                self.dfs(neighbour)
        self.time += 1
        self.exit[label] = self.time
        self.stack.push(label)

    def dfs_reversed_edges(self, label: str, components: list = None):
        self.visited[label] = True
        for neighbour in self.adjacency_list_reversed[label]:
            if not self.visited[neighbour]:
                self.dfs_reversed_edges(neighbour, components)
        components.append(label)





