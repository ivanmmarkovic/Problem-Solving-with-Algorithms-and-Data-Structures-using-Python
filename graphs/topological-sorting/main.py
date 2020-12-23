from graph import Graph

graph = Graph()

vertices = ["a", "b", "c", "d", "e", "f"]
for vertex in vertices:
    graph.add_vertex(vertex)


graph.add_edge("a", "c")
graph.add_edge("c", "d")
graph.add_edge("c", "f")
graph.add_edge("b", "c")
graph.add_edge("b", "e")

graph.topsort()

