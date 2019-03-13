from Vertex import Vertex
from Queue import Queue

class Graph:
    def __init__(self, maxNumberOfVertices = 0):
        self.maxNumberOfVertices = maxNumberOfVertices
        self.vertices = [None] * maxNumberOfVertices
        self.currentNumberOfVertices = 0
        self.adjacencyMatrix = [[0 for x in range(maxNumberOfVertices)] for y in range(maxNumberOfVertices)]

    def addVertex(self, label):
        vertex = Vertex(label, self.currentNumberOfVertices)
        self.vertices[self.currentNumberOfVertices] = vertex
        self.adjacencyMatrix[self.currentNumberOfVertices][self.currentNumberOfVertices] = False
        self.currentNumberOfVertices += 1

    def addEdge(self, start, end):
        self.adjacencyMatrix[start][end] = True
        self.adjacencyMatrix[end][start] = True

    def breadthFirstSearch(self):
        queue = Queue()
        v1 = self.vertices[0]
        print("Visited : " + v1.label)
        for j in range(self.currentNumberOfVertices):
            if self.adjacencyMatrix[v1.index][j] == True:
                self.vertices[j].inserted = True
                queue.enqueue(self.vertices[j])
        v1.visited = True
        while not queue.isEmpty():
            vertex = queue.dequeue()
            vertex.visited = True
            print("Visited : " + vertex.label)
            for j in range(self.currentNumberOfVertices):
                if self.adjacencyMatrix[vertex.index][j] == True and self.vertices[j].visited == False and self.vertices[j].inserted == False:
                    self.vertices[j].inserted = True
                    queue.enqueue(self.vertices[j])


graph = Graph(10)

graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")

graph.addEdge(0, 1) # AB
graph.addEdge(0, 2) # AC
graph.addEdge(0, 3) # AD
graph.addEdge(1, 2) # BC
graph.addEdge(2, 1) # CB
graph.addEdge(2, 4) # CE
graph.addEdge(3, 4) # DE

graph.breadthFirstSearch()