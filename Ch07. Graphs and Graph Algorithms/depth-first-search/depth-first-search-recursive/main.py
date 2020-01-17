from graph import Graph

graph = Graph()

myVertices = ['A','B','C','D','E','F','G','H','I']
# add vertices
for i in range(len(myVertices)):
    graph.addVertex(myVertices[i])

graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('A', 'D')
graph.addEdge('C', 'D')
graph.addEdge('C', 'G')
graph.addEdge('D', 'G')
graph.addEdge('D', 'H')
graph.addEdge('B', 'E')
graph.addEdge('B', 'F')
graph.addEdge('E', 'I')

graph.dfs("A")
print(graph.showPath("H"))