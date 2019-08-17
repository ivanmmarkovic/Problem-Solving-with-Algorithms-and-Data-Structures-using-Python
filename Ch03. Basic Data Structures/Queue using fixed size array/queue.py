

class Queue:
    def __init__(self, size: int):
        self.size = size
        self.queue: list = [None] * self.size
        self.front = -1
        self.rear = -1

    def getFirst(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[self.front]        

    def isEmpty(self)-> bool:
        return self.front == -1 and self.rear == -1

    def enqueue(self, item):
        if self.rear == len(self.queue) - 1:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        returnValue = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return returnValue

    