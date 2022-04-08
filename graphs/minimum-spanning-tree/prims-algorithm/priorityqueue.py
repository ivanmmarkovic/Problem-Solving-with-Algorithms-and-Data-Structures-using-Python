from typing import List

from vertex import Vertex


class PriorityQueue:


    def __init__(self) -> None:
        self.queue: List[Vertex] = [None]
        self.pointer:int = 0


    def is_empty(self) -> bool:
        return self.pointer == 0


    def insert(self, v:Vertex):
        self.queue.append(v)
        self.pointer += 1
        v.index = self.pointer
        self.perc_up(self.pointer)


    def perc_up(self, index:int):
        while index // 2 > 0:
            if self.queue[index].weight < self.queue[index // 2].weight:
                self.queue[index], self.queue[index // 2] = self.queue[index // 2], self.queue[index]
                self.queue[index].index = index 
                self.queue[index // 2].index = index // 2
            index = index // 2


    def decrease_key(self, key:int):
        self.perc_up(key)


    def get_min(self) -> Vertex:
        if self.is_empty():
            raise Exception('Priority queue is empty')
        return self.queue[1]


    def delete_min(self) -> Vertex:
        if self.is_empty():
            raise Exception('Priority queue is empty')
        v:Vertex = self.queue[1]
        self.queue[1] = self.queue[self.pointer]
        self.queue[1].index = 1
        self.queue.pop()
        self.pointer -= 1
        self.perc_down(1)
        return v


    def perc_down(self, index:int):
        while index * 2 <= self.pointer:
            min_index:int = self.find_min_index(index)
            if self.queue[index].weight > self.queue[min_index].weight:
                self.queue[index], self.queue[min_index] = self.queue[min_index], self.queue[index]
                self.queue[min_index].index = min_index 
                self.queue[index].index = index
            index = min_index



    def find_min_index(self, index:int) -> int:
        if index * 2 + 1 > self.pointer:
            return index * 2
        else:
            if self.queue[index * 2].weight <= self.queue[index * 2 + 1].weight:
                return index * 2
            else:
                return index * 2 + 1

