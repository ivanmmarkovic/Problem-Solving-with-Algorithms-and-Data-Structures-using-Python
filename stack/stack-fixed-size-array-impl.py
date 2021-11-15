from typing import Any, List


class Stack:

    def __init__(self, capacity: int = 1) -> None:
        self.capacity: int = capacity
        self.stack: List[Any] = [None] * self.capacity
        self.pointer: int = -1

    def size(self) -> int:
        return self.pointer + 1

    def is_empty(self) -> bool:
        return self.pointer == -1

    def is_full(self) -> bool:
        return self.pointer == self.capacity - 1

    def push(self, item:Any):
        if self.is_full():
            raise Exception('Stack is full')
        self.pointer += 1
        self.stack[self.pointer] = item

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception('Stack is empty')
        item = self.stack[self.pointer]
        self.pointer -= 1
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack[self.pointer]


def reverse_string(s: str) -> str:
    stack: Stack = Stack(len(s))
    for character in s:
        stack.push(character)

    result: str = ""
    while not stack.is_empty():
        result += stack.pop()

    return result


string: str = "This string will be reversed ..."
print(reverse_string(string)) # ... desrever eb lliw gnirts sihT


