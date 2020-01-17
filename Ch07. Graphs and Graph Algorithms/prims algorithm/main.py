from graph import Graph

graph = Graph()

g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")


g.addEdge("A", "B", 4)
g.addEdge("A", "F", 2)
g.addEdge("B", "C", 6)
g.addEdge("F", "B", 3)
g.addEdge("F", "C", 1)
g.addEdge("F", "E", 4)
g.addEdge("C", "D", 3)
g.addEdge("D", "E", 2)

g.prims("A")