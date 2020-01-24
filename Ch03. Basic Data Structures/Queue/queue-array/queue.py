
class Queue:
    def __init__(self):
        self.queue: list = []

    def isEmpty(self)->bool:
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.queue.pop(0)