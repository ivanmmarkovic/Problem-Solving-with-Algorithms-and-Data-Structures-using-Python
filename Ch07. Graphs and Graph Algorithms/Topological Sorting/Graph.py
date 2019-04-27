
from collections import OrderedDict

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.distance = {}
        self.prev = {}
        self.gray = []
        self.black = []

    def add_vertex(self, label):
        self.vertices.append(label)
        self.adjacencyList[label] = []
        self.distance[label] = 0
        self.prev[label] = None

    def add_edge(self, label1, label2):
        self.adjacencyList[label1].append(label2)
        # self.adjacencyList[label2].append(label1)

    def top_sort(self):
        for vertex in self.vertices:
            self.dfs(vertex)

        sorted_x = sorted(self.distance.items(), key=lambda kv: kv[1])
        sorted_dict = OrderedDict(sorted_x)
        print(sorted_dict)

    def dfs(self, label):
        stack = Stack()
        stack.push(label)
        self.gray.append(label)
        while not stack.isEmpty():
            peeked_vertex = stack.peek()
            neighbour = self.find_unvisited_neighbour(peeked_vertex)
            if neighbour is not None:
                self.prev[neighbour] = peeked_vertex
                self.distance[neighbour] = self.distance[peeked_vertex] + 1
                self.gray.append(neighbour)
                stack.push(neighbour)
            else:
                self.black.append(stack.pop())


    def to_string(self):
        result = ""
        for vertex in self.vertices:
            result += ("Neigbours of " + vertex + ": ")
            for neighbour in self.adjacencyList[vertex]:
                result += (neighbour + ", ")
            result += "\n"
        return result

    def find_unvisited_neighbour(self, label):
        found = False
        count = 0
        while count < len(self.adjacencyList[label]) and not found:
            if self.adjacencyList[label][count] not in self.gray:
                found = True
            else:
                count += 1
        if found:
            return self.adjacencyList[label][count]
        else:
            return None

