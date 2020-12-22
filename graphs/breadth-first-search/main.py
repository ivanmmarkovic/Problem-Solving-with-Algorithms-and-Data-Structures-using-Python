from graph import Graph

graph = Graph()

my_vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# add vertices
for i in range(len(my_vertices)):
    graph.add_vertex(my_vertices[i])

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'G')
graph.add_edge('D', 'G')
graph.add_edge('D', 'H')
graph.add_edge('B', 'E')
graph.add_edge('B', 'F')
graph.add_edge('E', 'I')

graph.bfs("A")
print(graph.return_path("H"))
