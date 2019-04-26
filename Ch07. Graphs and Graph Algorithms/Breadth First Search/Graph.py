from Queue import Queue

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.distance = {}
        self.prev = {}

    def addVertex(self, label):
        self.vertices.append(label)
        self.adjacencyList[label] = []
        self.distance[label] = 0
        self.prev[label] = None

    def addEdge(self, label1, label2):
        self.adjacencyList[label1].append(label2)
        self.adjacencyList[label2].append(label1)

    def bfs(self, label_start, label_end):
        gray = [] # visited, not fully explored
        black = [] # explored
        queue = Queue()
        queue.enqueue(label_start)
        gray.append(label_start)
        found = False
        while not queue.isEmpty() and not found:
            dequeued_vertex = queue.dequeue()
            if dequeued_vertex == label_end:
                found = True
            else:
                for neighbour in self.adjacencyList[dequeued_vertex]:
                    if neighbour not in gray:
                        self.distance[neighbour] = self.distance[dequeued_vertex] + 1
                        self.prev[neighbour] = dequeued_vertex
                        gray.append(neighbour)
                        queue.enqueue(neighbour)
                black.append(dequeued_vertex)
        if found:
            print(self.printPath(label_end))
        else:
            print("Path not found")

    def printPath(self, label):
        if self.prev[label] is None:
            return label
        else:
            return self.printPath(self.prev[label]) + " -> " + label

    def toString(self):
        result = ""
        for vertex in self.vertices:
            result += ("Neigbours of " + vertex + ": ")
            for neighbour in self.adjacencyList[vertex]:
                result += (neighbour + ", ")
            result += "\n"
        return result


