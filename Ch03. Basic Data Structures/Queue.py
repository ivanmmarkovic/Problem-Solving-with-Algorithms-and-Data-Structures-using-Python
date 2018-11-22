class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)
