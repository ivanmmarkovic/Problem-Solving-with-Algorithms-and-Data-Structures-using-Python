from graph import Graph

g: Graph = Graph()
for i in range(9):
    g.add_vertex(str(i))

g.add_edge('0', '1')
g.add_edge('1', '2')
g.add_edge('2', '3')
g.add_edge('3', '0')
g.add_edge('2', '4')
g.add_edge('4', '5')
g.add_edge('5', '6')
g.add_edge('6', '4')
g.add_edge('7', '6')
g.add_edge('8', '7')

g.kosaraju()
