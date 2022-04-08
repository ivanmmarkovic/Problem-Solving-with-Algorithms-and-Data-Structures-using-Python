class Vertex:

    def __init__(self, label:str=None, weight:int=float('inf'), index:int=None) -> None:
        self.label:str = label
        self.weight:int = weight
        self.index:int = index

