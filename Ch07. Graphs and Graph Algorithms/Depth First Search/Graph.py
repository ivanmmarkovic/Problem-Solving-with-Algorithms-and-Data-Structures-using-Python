

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.distance = {}
        self.prev = {}
        self.gray = []
        self.black = []

    def addVertex(self, label):
        self.vertices.append(label)
        self.adjacencyList[label] = []
        self.distance[label] = 0
        self.prev[label] = None

    def addEdge(self, label1, label2):
        self.adjacencyList[label1].append(label2)
        self.adjacencyList[label2].append(label1)

    def dfs(self, label_start, label_end):
        stack = Stack()
        stack.push(label_start)
        self.gray.append(label_start)
        found = False
        while not stack.isEmpty() and not found:
            peeked_vertex = stack.peek()
            print("Visiting ", peeked_vertex)
            if peeked_vertex == label_end:
                found = True
            else:
                neighbour = self.findUnvisitedNeighbour(peeked_vertex)
                if neighbour is not None:
                    self.prev[neighbour] = peeked_vertex
                    self.distance[neighbour] = self.distance[peeked_vertex] + 1
                    self.gray.append(neighbour)
                    stack.push(neighbour)
                else:
                    self.black.append(stack.pop())

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

    def findUnvisitedNeighbour(self, label):
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

