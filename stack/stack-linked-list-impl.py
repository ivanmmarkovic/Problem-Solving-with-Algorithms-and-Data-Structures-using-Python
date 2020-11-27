class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class Stack:
    def __init__(self):
        self._head: Node = None
        self._count: int = 0

    def is_empty(self) -> bool:
        return self._head is None

    def push(self, item):
        self._head = Node(item, self._head)
        self._count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        ret_value = self._head.key
        self._head = self._head.next
        self._count -= 1
        return ret_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head.key

    def size(self) -> int:
        return len(self._count)


def reverse_string(s: str) -> str:
    stack: Stack = Stack()
    for character in s:
        stack.push(character)

    result: str = ""
    while not stack.is_empty():
        result += stack.pop()

    return result


string: str = "This string will be reversed ..."
print(reverse_string(string)) # ... desrever eb lliw gnirts sihT


