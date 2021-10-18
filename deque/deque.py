
from typing import Any, List


class Deque:

    def __init__(self) -> None:
        self._deque: List[Any] = []

    def is_empty(self) -> bool:
        return len(self._deque) == 0

    def size(self) -> int:
        return len(self._deque)

    def add_front(self, item: Any):
        self._deque.insert(0, item)

    def add_rear(self, item: Any):
        self._deque.append(item)

    def remove_front(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._deque.pop(0)

    def remove_rear(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._deque.pop()



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
