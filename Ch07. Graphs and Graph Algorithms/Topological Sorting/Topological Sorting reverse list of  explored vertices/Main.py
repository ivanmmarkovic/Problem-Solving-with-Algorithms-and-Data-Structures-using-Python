from Graph import Graph

graph = Graph()

vertices = ["a", "b", "c", "d", "e", "f", "g"]
for vertex in vertices:
    graph.add_vertex(vertex)


graph.add_edge("a", "c")
graph.add_edge("c", "d")
graph.add_edge("c", "f")
graph.add_edge("a", "b")
graph.add_edge("d", "e")
graph.add_edge("b", "c")
graph.add_edge("b", "g")

graph.top_sort()


