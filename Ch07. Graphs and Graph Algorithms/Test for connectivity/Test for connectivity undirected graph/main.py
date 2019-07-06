from graph import Graph

graph = Graph()

myVertices = ['A','B','C','D','E','F','G','H','I']
# add vertices
for i in range(len(myVertices)):
    graph.add_vertex(myVertices[i])



# uncomment line below and output will be false
# graph.add_vertex("P")

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

print("Graph is connected :", graph.is_connected("A"))