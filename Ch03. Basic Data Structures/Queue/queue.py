
class Queue:
    def __init__(self):
        self.queue: list = []

    def size(self):
        return len(self.queue)

    def isEmpty(self)->bool:
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    