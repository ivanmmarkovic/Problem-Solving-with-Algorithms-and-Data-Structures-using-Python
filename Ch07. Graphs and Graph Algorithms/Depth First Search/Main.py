


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

graph.dfs("start", "end") # start -> a -> b -> end
print(graph.distance) # {'start': 0, 'a': 1, 'b': 2, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'end': 3}


