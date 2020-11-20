class Vertex:
    def __init__(self, label: str = None, weight: int = float("inf"), index: int = None):
        self._label: str = label
        self._weight: int = weight
        self._index: int = index

    def get_index(self):
        return self._index

    def get_label(self) -> str:
        return self._label

    def set_label(self, label: str):
        self._label = label

    def get_weight(self) -> int:
        return self._weight

    def set_weight(self, weight: int = float("inf")):
        self._weight = weight
