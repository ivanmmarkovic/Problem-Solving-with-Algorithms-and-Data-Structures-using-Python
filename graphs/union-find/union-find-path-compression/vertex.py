class Vertex:

    def __init__(self, label: str = None):
        self.label = label
        self.parent: 'Vertex' = self
        self.rank: int = 0

