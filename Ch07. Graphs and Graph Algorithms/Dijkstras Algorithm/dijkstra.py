
class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacencyList = {}
        self.previous = {}
        self.weight = {}
        self.visited = []

    def addVertex(self, label, weight = 0):
        self.vertices.append({"label": label, "weight": weight})
        self.adjacencyList[label] = []
        self.previous[label] = None
        self.weight[label] = weight

    def addEdge(self, label, neighbour_label, neighbour_weight):
        self.adjacencyList[label].append({'label': neighbour_label, 'weight': neighbour_weight})
        self.previous[neighbour_label] = label

    def dijkstra(self, start_vertex_label, end_vertex_label):
        cheapest_node = self.find_cheapest_node(start_vertex_label)
        while cheapest_node != None:
            neighbours = self.adjacencyList[cheapest_node["label"]]
            for neighbour in neighbours:
                if cheapest_node["weight"] + neighbour["weight"] < self.weight[neighbour["label"]]:
                    self.previous[neighbour["label"]] = cheapest_node["label"]
                    self.weight[neighbour["label"]] = self.weight[cheapest_node["label"]] + neighbour["weight"]
            self.visited.append(cheapest_node)
            cheapest_node = self.find_cheapest_node(start_vertex_label)
                
        print(self.print_path(end_vertex_label))

    def print_path(self, end_vertex_label):
        if self.previous[end_vertex_label] == None:
            return end_vertex_label
        else:
            return self.print_path(self.previous[end_vertex_label]) + " -> " + end_vertex_label

    def find_cheapest_node(self, vertex_label):
        cheapest_node = {"label": None, "weight": float("inf")}
        for node in self.adjacencyList[vertex_label]:
            if node not in self.visited and node["weight"] < cheapest_node["weight"]:
                cheapest_node = node
        if cheapest_node["label"] == None:
            return None
        else:
            #self.visited.append(cheapest_node)
            return cheapest_node

graph = Graph()

graph.addVertex("START", 0)
graph.addVertex("A", 0)
graph.addVertex("B", 10)
graph.addVertex("END", 15)
graph.addVertex("C", 2)
graph.addVertex("D", 10)


graph.addEdge("START", "A", 0)
graph.addEdge("START", "C", 2)

graph.addEdge("A", "B", 10)
graph.addEdge("A", "D", 15)

graph.addEdge("C", "B", 3)
graph.addEdge("C", "D", 10)


graph.addEdge("B", "END", 15)
graph.addEdge("D", "END", 10)

graph.dijkstra("START", "END")