class Deque:
    def __init__(self, length: int = 10):
        self._length: int = length
        self._deque: list = [None] * self._length
        self._front = self._rear = -1
        self._count: int = 0

    def add_front(self, item):
        if self.is_full():
            raise Exception("Deque is full")
        if self.is_empty():
            self._front = self._rear = 0
        elif self._front == 0:
            self._front = self._length - 1
        else:
            self._front -= 1
        self._deque[self._front] = item
        self._count += 1

    def add_rear(self, item):
        if self.is_full():
            raise Exception("Deque is full")
        if self.is_empty():
            self._front = self._rear = 0
        else:
            self._rear = (self._rear + 1) % self._length
        self._deque[self._rear] = item
        self._count += 1

    def remove_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        ret_value = self._deque[self._front]
        if self._front == self._rear:
            self._front = self._rear = -1
        else:
            self._front = (self._front + 1) % self._length
        self._count -= 1
        return ret_value

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        ret_value = self._deque[self._rear]
        if self._front == self._rear:
            self._front = self._rear = -1
        elif self._rear == 0:
            self._rear = self._length - 1
        else:
            self._rear = self._rear - 1
        self._count -= 1
        return ret_value

    def get_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._deque[self._front]

    def get_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._deque[self._rear]

    def is_full(self) -> bool:
        return (self._rear + 1) % self._length == self._front

    def is_empty(self) -> bool:
        return self._front == -1

    def size(self) -> int:
        return self._count


def is_palindrome(string: str) -> bool:
    d: Deque = Deque(len(string))
    for character in string:
        d.add_rear(character)

    palindrome: bool = True
    while d.size() > 1 and palindrome:
        if d.remove_front() != d.remove_rear():
            palindrome = False
    return palindrome


print(is_palindrome("radar"))
print(is_palindrome("radr"))


