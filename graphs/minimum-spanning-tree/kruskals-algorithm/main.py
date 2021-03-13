from graph import Graph

g: Graph = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('d')
g.add_vertex('c')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'f', 4)
g.add_edge('a', 'b', 23)

g.add_edge('b', 'd', 17)
g.add_edge('b', 'c', 3)
g.add_edge('c', 'd', 41)

g.add_edge('c', 'f', 2)
g.add_edge('f', 'e', 1)

g.kruskal()
