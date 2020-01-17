from graph import Graph

graph = Graph()

graph.addVertex("START")
graph.addVertex("A")
graph.addVertex("C")
graph.addVertex("B")
graph.addVertex("D")
graph.addVertex("END")

graph.addEdge("START", "A", 0)
graph.addEdge("START", "C", 2)
graph.addEdge("A", "B", 18)
graph.addEdge("A", "D", 15)
graph.addEdge("C", "B", 3)
graph.addEdge("C", "D", 10)
graph.addEdge("B", "END", 150)
graph.addEdge("D", "END", 15)
graph.dijkstra("START")

print(graph.showPath("END"))