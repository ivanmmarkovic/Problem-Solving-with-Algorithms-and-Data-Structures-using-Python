from graph import Graph

graph: Graph = Graph(20)

graph.add_vertex("START")
graph.add_vertex("A")
graph.add_vertex("C")
graph.add_vertex("B")
graph.add_vertex("D")
graph.add_vertex("END")

graph.add_edge("START", "A", 0)
graph.add_edge("START", "C", 2)
graph.add_edge("A", "B", 18)
graph.add_edge("A", "D", 15)
graph.add_edge("C", "B", 3)
graph.add_edge("C", "D", 10)
graph.add_edge("B", "END", 150)
graph.add_edge("D", "END", 15)
graph.dijkstra("START")

print(graph.return_path("END"))
