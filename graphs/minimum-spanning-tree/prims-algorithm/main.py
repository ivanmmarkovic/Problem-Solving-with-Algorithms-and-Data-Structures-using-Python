from graph import Graph


graph: Graph = Graph()

graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("f")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")

graph.add_edge("a", "b", 4)
graph.add_edge("a", "f", 2)
graph.add_edge("b", "c", 6)
graph.add_edge("f", "b", 3)
graph.add_edge("f", "c", 1)
graph.add_edge("f", "e", 4)
graph.add_edge("c", "d", 3)
graph.add_edge("d", "e", 2)
graph.prims("a")  # a -> f, f -> c, f -> b, c -> d, d -> e,
