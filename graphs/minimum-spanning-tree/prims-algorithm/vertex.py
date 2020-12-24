class Vertex:
    def __init__(self, label: str = None, weight: int = float("inf"), key: int = None):
        self.label: str = label
        self.weight: int = weight
        self.key: int = key
