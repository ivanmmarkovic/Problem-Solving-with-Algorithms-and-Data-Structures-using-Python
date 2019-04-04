from Stack import Stack

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.distance = {}
        self.previous = {}
        self.visited = []
        self.time = {}
        self.time_count = 0

    def add_vertex(self, v):
        self.vertices.append(v)
        self.adjacencyList[v] = []
        self.distance[v] = 0
        self.previous[v] = None
        self.time[v] = {}
        self.time[v]['start'] = 0
        self.time[v]['finished'] = 0

    def add_edge(self,v1, v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)

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
        

    def search_helper(self, vertex):
        if vertex in self.visited:
            return
        stack = Stack()
        stack.push(vertex)
        self.visited.append(vertex)
        self.time_count += 1
        self.time[vertex]['start'] = self.time_count
        while not stack.isEmpty():
            peeked_vertex = stack.peek()
            new_vertex = self.find_unvisited_neighbour(peeked_vertex)
            if new_vertex != None:
                self.previous[new_vertex] = peeked_vertex
                self.distance[new_vertex] = self.distance[peeked_vertex] + 1
                self.visited.append(new_vertex)
                self.time_count += 1
                self.time[new_vertex]['start'] = self.time_count
                stack.push(new_vertex)
            else:
                stack.pop()
                self.time_count += 1
                self.time[peeked_vertex]['finished'] = self.time_count

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
print(graph.time)


    