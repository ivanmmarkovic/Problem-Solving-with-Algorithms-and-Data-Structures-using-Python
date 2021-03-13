from graph import Graph

g: Graph = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('d')
g.add_vertex('c')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'f')
g.add_edge('a', 'b')

g.add_edge('b', 'd')
g.add_edge('b', 'c')
g.add_edge('c', 'd')

g.add_edge('c', 'f')
g.add_edge('f', 'e')

g.kruskal()
