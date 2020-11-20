class Queue:
    def __init__(self):
        self._queue: list = []

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def enqueue(self, vertex: str):
        self._queue.append(vertex)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._queue.pop(0)
