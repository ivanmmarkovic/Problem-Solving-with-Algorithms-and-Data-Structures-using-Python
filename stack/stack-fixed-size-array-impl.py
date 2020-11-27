class Stack:
    def __init__(self, length: int = 10):
        self._length: int = length
        self._stack: list = [None] * self._length
        self._pointer: int = -1

    def is_empty(self) -> bool:
        return self._pointer == -1

    def is_full(self) -> bool:
        return self._pointer == self._length - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self._pointer += 1
        self._stack[self._pointer] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        ret_value = self._stack[self._pointer]
        self._pointer -= 1
        return ret_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._stack[self._pointer]

    def size(self) -> int:
        return len(self._pointer) + 1


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


