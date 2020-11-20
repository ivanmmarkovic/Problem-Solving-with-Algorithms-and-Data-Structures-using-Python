from vertex import Vertex


class PriorityQueue:
    def __init__(self):
        self._queue: list = [None]
        self._pointer: int = 0

    def is_empty(self) -> bool:
        return self._pointer == 0

    def insert(self, vertex: Vertex):
        self._queue.append(vertex)
        self._pointer += 1
        vertex.set_key(self._pointer)
        self._perc_up(self._pointer)

    def _perc_up(self, index: int):
        while index // 2 > 0:
            if self._queue[index].get_weight() < self._queue[index // 2].get_weight():
                self._queue[index], self._queue[index // 2] = self._queue[index // 2], self._queue[index]
                self._queue[index].set_key(index)
                self._queue[index // 2].set_key(index // 2)
            index = index // 2

    def decrease_key(self, key: int):
        self._perc_up(key)

    def delete_min(self) -> Vertex:
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        vertex_to_delete: Vertex = self._queue[1]
        self._queue[1] = self._queue[self._pointer]
        self._queue[1].set_key(1)
        self._pointer -= 1
        self._queue.pop()
        self._perc_down(1)
        return vertex_to_delete

    def _perc_down(self, index: int):
        while index * 2 <= self._pointer:
            swap_index: int = self._find_swap_index(index)
            if self._queue[index].get_weight() > self._queue[swap_index].get_weight():
                self._queue[index], self._queue[swap_index] = self._queue[swap_index], self._queue[index]
                self._queue[index].set_key(index)
                self._queue[swap_index].set_key(swap_index)
            index = swap_index

    def _find_swap_index(self, index) -> int:
        if index * 2 + 1 > self._pointer:
            return index * 2
        else:
            if self._queue[index * 2].get_weight() <= self._queue[index * 2 + 1].get_weight():
                return index * 2
            else:
                return index * 2 + 1



