from graph import Graph

graph = Graph()

vertices = ["a", "b", "c", "d", "e", "f", "g"]
for vertex in vertices:
    graph.addVertex(vertex)


graph.addEdge("a", "c")
graph.addEdge("c", "d")
graph.addEdge("c", "f")
graph.addEdge("a", "b")
graph.addEdge("d", "e")
graph.addEdge("b", "c")
graph.addEdge("b", "g")

graph.topsort()
