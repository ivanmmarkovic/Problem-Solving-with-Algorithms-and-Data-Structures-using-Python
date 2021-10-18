
from typing import Any, List


class Deque:

    def __init__(self, capacity: int = 10) -> None:
        self.capacity: int = capacity
        self.length: int = 0
        self._deque: List[Any] = [None] * self.capacity
        self.front: int = -1
        self.rear: int = -1

    def is_empty(self) -> bool:
        return self.front == -1

    def is_full(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front

    def size(self) -> int:
        return self.length

    def add_front(self, item: Any):
        if self.is_full():
            raise Exception('Deque is full')
        if self.is_empty(): # self.rear == -1
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.capacity - 1
        else:
            self.front -= 1
        self._deque[self.front] = item
        self.length += 1

    def add_rear(self, item: Any):
        if self.is_full():
            raise Exception('Deque is full')
        if self.is_empty(): # self.rear == -1
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self._deque[self.rear] = item
        self.length += 1

    def remove_front(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        item: Any = self._deque[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.length -= 1
        return item

    def remove_rear(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        item: Any = self._deque[self.rear]
        if self.rear == self.front:
            self.rear = self.front = -1
        elif self.rear == 0:
            self.rear = self.capacity - 1
        else:
            self.rear -= 1
        self.length -= 1
        return item

    def get_front(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._deque[self.front]

    def get_rear(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._deque[self.rear]


def is_palindrome(string:str='') -> bool:
    d: Deque = Deque()

    for character in string:
        d.add_rear(character)

    palindrome: bool = True
    while d.size() > 1 and palindrome:
        if d.remove_front() != d.remove_rear():
            palindrome = False
    
    return palindrome

print(is_palindrome('radar'))
print(is_palindrome('radr'))
print(is_palindrome('r'))
print(is_palindrome(''))
