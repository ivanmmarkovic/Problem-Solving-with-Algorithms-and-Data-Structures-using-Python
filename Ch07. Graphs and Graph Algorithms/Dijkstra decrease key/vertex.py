
class Vertex:
    def __init__(self, label: str, weight: int = float("inf"), key: int = None, index: int = None):
        self.label = label
        self.weight = weight
        self.key = key # key in priority queue
        self.index = index # index created when add vertex in graph
        # index - to avoid loop through vertices when updating weight

