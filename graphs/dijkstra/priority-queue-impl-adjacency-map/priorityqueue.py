from vertex import Vertex


class PriorityQueue:
    def __init__(self):
        self.pq: list = [None]
        self._pointer: int = 0

    def is_empty(self) -> bool:
        return self._pointer == 0

    def insert(self, vertex: Vertex):
        self.pq.append(vertex)
        self._pointer += 1
        vertex.key = self._pointer
        self._perc_up(self._pointer)

    def _perc_up(self, pointer: int):
        while pointer // 2 > 0:
            if self.pq[pointer // 2].weight > self.pq[pointer].weight:
                self.pq[pointer // 2], self.pq[pointer] = self.pq[pointer], self.pq[pointer // 2]
                self.pq[pointer // 2].key = pointer // 2
                self.pq[pointer].key = pointer
            pointer = pointer // 2

    def decrease_key(self, pointer: int):
        self._perc_up(pointer)

    def delete_min(self) -> Vertex:
        if self.is_empty():
            raise Exception("Priority queue is empty")
        v: Vertex = self.pq[1]
        self.pq[1] = self.pq[self._pointer]
        self.pq[1].key = 1
        self.pq.pop()
        self._pointer -= 1
        self._perc_down(1)
        return v

    def _perc_down(self, pointer: int):
        while pointer * 2 <= self._pointer:
            min_index: int = self._find_swap_index(pointer)
            if self.pq[pointer].weight > self.pq[min_index].weight:
                self.pq[pointer], self.pq[min_index] = self.pq[min_index], self.pq[pointer]
                self.pq[pointer].key = pointer
                self.pq[min_index].key = min_index
            pointer = min_index

    def _find_swap_index(self, pointer: int) -> int:
        if pointer * 2 + 1 > self._pointer:
            return pointer * 2
        else:
            if self.pq[pointer * 2].weight <= self.pq[pointer * 2 + 1].weight:
                return pointer * 2
            else:
                return pointer * 2 + 1
