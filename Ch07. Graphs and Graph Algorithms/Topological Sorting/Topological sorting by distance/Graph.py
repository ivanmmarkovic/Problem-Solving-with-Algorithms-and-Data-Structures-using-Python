from Stack import Stack
from collections import OrderedDict


class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.previous = {}
        self.distance = {}
        self.visited = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        self.adjacencyList[vertex] = []
        self.previous[vertex] = None
        self.distance[vertex] = 0

    def add_edge(self, vertex1, vertex2):
        self.adjacencyList[vertex1].append(vertex2)

    def top_sort(self):
        for vertex in self.vertices:
            self.top_sort_help(vertex)

        sorted_x = sorted(self.distance.items(), key=lambda kv: kv[1])
        sorted_dict = OrderedDict(sorted_x)
        print(sorted_dict)

    def top_sort_help(self, vertex):
        stack = Stack()
        self.visited.append(vertex)
        stack.push(vertex)
        while not stack.isEmpty():
            vertex_peeked = stack.peek()
            neighbour = self.find_unvisited_neighbour(vertex_peeked)
            if neighbour != None:
                stack.push(neighbour)
                self.previous[neighbour] = vertex_peeked
                self.distance[neighbour] = self.distance[vertex_peeked] + 1
                self.visited.append(neighbour)
            else:
                stack.pop()


    def find_unvisited_neighbour(self, vertex):
        found = False
        count = 0
        neighbour = None
        while count < len(self.adjacencyList[vertex]) and not found:
            neighbour = self.adjacencyList[vertex][count]
            if neighbour not in self.visited:
                found = True
            else:
                count += 1
        if found:
            return neighbour
        else:
            return None


