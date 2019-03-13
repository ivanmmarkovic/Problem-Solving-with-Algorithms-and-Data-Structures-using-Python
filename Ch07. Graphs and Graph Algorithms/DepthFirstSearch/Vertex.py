class Vertex:
    def __init__(self, label = None, index = None):
        self.label = label
        self.index = index
        self.visited = False
        self.inserted = False
