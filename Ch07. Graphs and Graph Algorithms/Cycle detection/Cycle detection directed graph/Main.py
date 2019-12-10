from graph import Graph


graph: Graph = Graph()


vertices = ["a", "b", "c", "d"]
for vertex in vertices:
    graph.addVertex(vertex)


graph.addEdge("a", "b")
graph.addEdge("b", "c")
graph.addEdge("c", "d")
graph.addEdge("d", "b")

graph.dfs("a")


print(graph.prev)
print(graph.entry)
print(graph.exit)
