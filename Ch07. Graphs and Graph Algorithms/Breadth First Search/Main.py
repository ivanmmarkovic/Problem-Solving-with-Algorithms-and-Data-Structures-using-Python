from Graph import Graph


graph = Graph()

vertices = ["start", "a", "b", "c", "d", "e", "f", "g", "end"]
for vertex in vertices:
    graph.addVertex(vertex)


graph.addEdge("start", "a")
graph.addEdge("start", "c")
graph.addEdge("start", "d")
graph.addEdge("a", "b")
graph.addEdge("b", "end")
graph.addEdge("c", "end")
graph.addEdge("d", "e")
graph.addEdge("e", "f")
graph.addEdge("e", "g")


print(graph.toString())

graph.bfs("start", "f") # start -> d -> e -> f
print(graph.distance) # {'start': 0, 'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 2, 'f': 3, 'g': 3, 'end': 2}


