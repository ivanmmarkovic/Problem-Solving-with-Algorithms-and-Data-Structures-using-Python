from Queue import Queue

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.distance = {}
        self.previous = {}

    def add_vertex(self, v):
        self.vertices.append(v)
        self.adjacencyList[v] = []
        self.distance[v] = 0
        self.previous[v] = None

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
        queue = Queue()
        startVertex = self.vertices[0]
        gray = [] # visited, not fully explored
        black = [] # explored
        gray.append(startVertex)
        queue.enqueue(startVertex)
        while not queue.isEmpty():
            dequeued = queue.dequeue()
            if dequeued not in black:
                for neighbour in self.adjacencyList[dequeued]:
                    if neighbour not in gray:
                        queue.enqueue(neighbour)
                        gray.append(neighbour)
                        self.distance[neighbour] = self.distance[dequeued] + 1
                        self.previous[neighbour] = dequeued
            black.append(dequeued)
            print("Explored " + dequeued, end = " ")
        print("")

    def showPath(self, vertex):
        if self.previous[vertex] == None:
            return vertex
        else:
            return self.showPath(self.previous[vertex]) + " -> " + vertex

graph = Graph()


vertices = ['A', 'B', 'C', 'D', 'E', 'F']
# add vertices
for i in range(len(vertices)):
    graph.add_vertex(vertices[i])

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')
graph.add_edge('D', 'F')

print(graph.to_string())
print("##########################")
graph.breadth_first_search()
print(graph.distance)
print(graph.previous)
print(graph.showPath("F"))

    