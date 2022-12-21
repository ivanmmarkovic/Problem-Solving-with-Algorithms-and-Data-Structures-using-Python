class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._queue.pop()

    def size(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return len(self._queue) == 0


def hot_potato(namelist, number):
    q = Queue()

    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
