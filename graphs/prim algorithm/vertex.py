class Vertex:
    def __init__(self, label: str = None, weight: int = float("inf"), key: int = None):
        self._label: str = label
        self._weight: int = weight
        self._key: int = key

    def get_label(self) -> str:
        return self._label

    def set_key(self, key: int):
        self._key = key

    def get_key(self) -> int:
        return self._key

    def set_weight(self, weight: int = float("inf")):
        self._weight = weight

    def get_weight(self) -> int:
        return self._weight
