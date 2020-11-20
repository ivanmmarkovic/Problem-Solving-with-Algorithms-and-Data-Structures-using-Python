from graph import Graph


g: Graph = Graph()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")

# a, b ||---|| c, d


g.add_edge("a", "c")
g.add_edge("a", "d")

g.add_edge("b", "c")
g.add_edge("b", "d")


# g.add_edge("a", "b")

print(g.bipartite_check())
