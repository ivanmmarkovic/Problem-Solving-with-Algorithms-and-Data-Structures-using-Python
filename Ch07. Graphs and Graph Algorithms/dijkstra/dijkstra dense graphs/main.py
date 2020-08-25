from graph import Graph

g: Graph = Graph()

g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_vertex("e")
g.add_vertex("f")

g.add_edge("a", "b", 6)
g.add_edge("a", "c", 3)
g.add_edge("c", "b", 2)
g.add_edge("c", "e", 20)
g.add_edge("b", "e", 10)
g.add_edge("b", "d", 2)
g.add_edge("e", "d", 10)
g.add_edge("e", "f", 100)
g.add_edge("d", "f", 20)

g.dijkstra("a")
print(g.return_path("f"))