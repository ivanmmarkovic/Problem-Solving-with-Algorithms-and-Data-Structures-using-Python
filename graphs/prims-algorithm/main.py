from graph import Graph

graph: Graph = Graph()

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")


g.add_edge("A", "B", 4)
g.add_edge("A", "F", 2)
g.add_edge("B", "C", 6)
g.add_edge("F", "B", 3)
g.add_edge("F", "C", 1)
g.add_edge("F", "E", 4)
g.add_edge("C", "D", 3)
g.add_edge("D", "E", 2)

g.prims("A")
