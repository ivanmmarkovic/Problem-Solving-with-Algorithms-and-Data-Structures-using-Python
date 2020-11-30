class Queue:
    def __init__(self, length: int = 10):
        self._length: int = length
        self._queue: list = [None] * self._length
        self._front = self._rear = -1
        self._count: int = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self._rear = (self._rear + 1) % self._length
        if self._front == -1:
            self._front += 1
        self._count += 1
        self._queue[self._rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        ret_value = self._queue[self._front]
        if self._front == self._rear:
            self._front = self._rear = -1
        else:
            self._front = (self._front + 1) % self._length
        self._count -= 1
        return ret_value

    def size(self) -> int:
        return self._count

    def is_empty(self) -> bool:
        return self._front == -1

    def is_full(self) -> bool:
        return (self._rear + 1) % self._length == self._front


def hot_potato(namelist, number):
    q = Queue(30)

    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

