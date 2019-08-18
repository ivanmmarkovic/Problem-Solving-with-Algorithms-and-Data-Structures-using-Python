
class Queue:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def isEmpty(self)-> bool:
        return self.front == -1
    
    def isFull(self)-> bool:
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1 ) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            toReturn = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            self.front = (self.front + 1) % self.size
            return toReturn

    def showFirst(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.queue[self.front]

    def printAll(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            if self.front <= self.rear:
                for i in range(self.front, self.rear + 1, + 1):
                    print(self.queue[i], end=", ")
            else:
                for i in range(self.front, self.size, +1):
                    print(self.queue[i], end=", ")
                for j in range(self.rear + 1):
                    print(self.queue[j], end=", ")
            print("")