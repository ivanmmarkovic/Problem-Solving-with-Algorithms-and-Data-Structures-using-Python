class Vertex:
    def __init__(self, label = None, parent = None, weight= float("inf")):
        self.label = label
        self.parent = parent
        self.weight = weight

