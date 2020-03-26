
from graph import Graph

g: Graph = Graph()

g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addVertex("f")

g.addEdge("a", "b", 6)
g.addEdge("a", "c", 3)
g.addEdge("c", "b", 2)
g.addEdge("c", "e", 20)
g.addEdge("b", "e", 10)
g.addEdge("b", "d", 2)
g.addEdge("e", "d", 10)
g.addEdge("e", "f", 100)
g.addEdge("d", "f", 20)

g.dijkstra("a")
print(g.returnPath("f"))


