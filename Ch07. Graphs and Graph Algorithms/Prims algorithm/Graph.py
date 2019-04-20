from Vertex import Vertex
from PriorityQueue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices = [] # list of Vertex objects
        self.adjacencyList = {} # label -> list(String) of neighbours(types of Vertex)
        self.path = ""

    def add_vertex(self, vertex_label): # vertex_label is string
        vertex = Vertex(vertex_label)
        self.vertices.append(vertex)
        self.adjacencyList[vertex.label] = [] # this list contains Vertex objects

    def add_edge(self, label1, label2, weight):
        self.adjacencyList[label1].append(Vertex(label2, None, weight))

    def prim(self, start_label):
        start_vertex = self.find_vertex_by_label(start_label)
        start_vertex.weight = 0
        pq = PriorityQueue()
        #for vertex in self.vertices:
        #    pq.insert(vertex)
        pq.build_heap(self.vertices)
        while not pq.isEmpty():
            min_vertex = pq.getMin() # return Vertex object
            if min_vertex.parent is not None:
                self.path += (min_vertex.parent + " -> " + min_vertex.label + ", ")
            for neighbour_vertex in self.adjacencyList[min_vertex.label]:
                tmp_vertex = self.find_vertex_by_label(neighbour_vertex.label) # vertex object from self.vertices
                if neighbour_vertex.weight < tmp_vertex.weight:
                    tmp_vertex.parent = min_vertex.label
                    tmp_vertex.weight = neighbour_vertex.weight
            pq.deleteMin()
        print(self.path)

    def find_vertex_by_label(self,label):
        found = False
        count = 0
        while count < len(self.vertices) and not found:
            if self.vertices[count].label == label:
                found = True
            else:
                count += 1
        if found:
            return self.vertices[count]
        else:
            return None


