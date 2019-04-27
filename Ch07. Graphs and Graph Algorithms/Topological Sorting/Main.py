


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
graph.add_edge("F", "B")
graph.add_edge("F", "G")

graph.top_sort()


