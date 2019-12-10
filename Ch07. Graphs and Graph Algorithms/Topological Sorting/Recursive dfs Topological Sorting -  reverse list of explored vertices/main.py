from graph import Graph


graph: Graph = Graph()

myVertices: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

for i in myVertices:
    graph.addVertex(i)

graph.addEdge('A', 'B')
graph.addEdge('B', 'C')
graph.addEdge('C', 'D')
graph.addEdge('C', 'E')
graph.addEdge('F', 'B')
graph.addEdge('F', 'G')

graph.topsort()

print(graph.prev)
print(graph.entry)
print(graph.exit)