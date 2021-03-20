from graph import Graph
from vertex import Vertex

g: Graph = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b')
g.add_edge('c', 'd')
g.add_edge('d', 'e')
g.add_edge('c', 'f')
g.add_edge('f', 'b')

g.union_find()

for label in g.vertices:
    vertex: Vertex = g.vertices[label]
    print(f'{vertex.label} parent is {vertex.parent.label}, rank is {vertex.parent.rank}')




