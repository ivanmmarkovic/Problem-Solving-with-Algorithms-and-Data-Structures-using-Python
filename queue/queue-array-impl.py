class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.insert(0, item)

    def dequeue(self):
        return self._queue.pop()

    def size(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return len(self._queue) == 0
