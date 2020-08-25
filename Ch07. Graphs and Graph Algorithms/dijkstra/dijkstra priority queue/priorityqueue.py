from vertex import Vertex

class PriorityQueue:
    def __init__(self):
        self.__queue__: list = [None]
        self.__pointer__: int = 0

    def is_empty(self) -> bool:
        return self.__pointer__ == 0

    def insert(self, vertex: Vertex):
        self.__pointer__ += 1
        self.__queue__.append(vertex)
        vertex.key = self.__pointer__
        self.__perc_up__(self.__pointer__)

    def __perc_up__(self, pointer: int):
        while pointer // 2 > 0:
            if self.__queue__[pointer].weight < self.__queue__[pointer // 2].weight:
                self.__queue__[pointer], self.__queue__[pointer // 2] = self.__queue__[pointer // 2], self.__queue__[pointer]
                self.__queue__[pointer].key = pointer
                self.__queue__[pointer // 2].key = pointer // 2
            pointer = pointer // 2

    def decrease_key(self, key: int):
        self.__perc_up__(key)

    def get_min(self) -> Vertex:
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return self.__queue__[1]

    def delete_min(self) -> Vertex:
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        min_vertex: Vertex = self.__queue__[1]
        self.__queue__[1] = self.__queue__[self.__pointer__]
        self.__queue__[1].key = 1
        self.__pointer__ -= 1
        self.__queue__.pop()
        self.__perc_down__(1)
        return min_vertex

    def __perc_down__(self, index: int):
        while index * 2 <= self.__pointer__:
            min_index: int = self.__min_index__(index)
            if self.__queue__[index].weight > self.__queue__[min_index].weight:
                self.__queue__[index], self.__queue__[min_index] = self.__queue__[min_index], self.__queue__[index]
                self.__queue__[index].key = index
                self.__queue__[min_index].key = min_index
            index = min_index

    def __min_index__(self, index: int) -> int:
        if index * 2 + 1 > self.__pointer__:
            return index * 2
        else:
            if self.__queue__[index * 2].weight <= self.__queue__[index * 2 + 1].weight:
                return index * 2
            else:
                return index * 2 + 1



