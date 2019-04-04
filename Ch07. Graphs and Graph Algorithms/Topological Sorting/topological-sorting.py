from Stack import Stack
from collections import OrderedDict

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.distance = {}
        self.previous = {}
        self.visited = []

    def add_vertex(self, v):
        self.vertices.append(v)
        self.adjacencyList[v] = []
        self.distance[v] = 0
        self.previous[v] = None

    def add_edge(self,v1, v2):
        self.adjacencyList[v1].append(v2)
        #self.adjacencyList[v2].append(v1) DIRECTED ACYCLIC GRAPHS ONLY

    def to_string(self):
        result = ""
        for vertex in self.vertices:
            result += (vertex + " -> ")
            for neighbour in self.adjacencyList[vertex]:
                result += neighbour + " "
            result += "\n"
        return result

    def breadth_first_search(self):
        for vertex in self.vertices:
            self.search_helper(vertex)

        sorted_x = sorted(self.distance.items(), key=lambda kv: kv[1])
        sorted_dict = OrderedDict(sorted_x)
        print(sorted_dict)

    def search_helper(self, vertex):
        self.visited.append(vertex)
        stack = Stack()
        stack.push(vertex)
        self.visited.append(vertex)
        while not stack.isEmpty():
            peeked_vertex = stack.peek()
            new_vertex = self.find_unvisited_neighbour(peeked_vertex)
            if new_vertex != None:
                self.previous[new_vertex] = peeked_vertex
                self.distance[new_vertex] = self.distance[peeked_vertex] + 1
                self.visited.append(new_vertex)
                stack.push(new_vertex)
            else:
                stack.pop()

    def find_unvisited_neighbour(self, vertex):
        found = False
        count = 0
        while count < len(self.adjacencyList[vertex]) and not found:
            if self.adjacencyList[vertex][count] not in self.visited:
                found =True
            else:
                count +=1
        if found:
            return self.adjacencyList[vertex][count]
        else:
            return None

graph = Graph()


vertices = ['A', 'B', 'C', 'D', 'E']
# add vertices
for i in range(len(vertices)):
    graph.add_vertex(vertices[i])

graph.add_edge('A', 'B')
graph.add_edge('C', 'B')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')

print(graph.to_string())
print("##########################")
graph.breadth_first_search()
print(graph.distance)
print(graph.previous)
print(graph.distance)


    