
class Queue:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.queue: list = [None] * self.capacity
        self.front = self.rear = -1
        self.length = 0

    def size(self)->int:
        return self.length

    def isEmpty(self)->bool:
        return self.rear == -1

    def isFull(self)->bool:
        return self.front == self.capacity - 1

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.front += 1
        self.queue[self.front] = item
        if self.rear == -1:
            self.rear += 1
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            retValue = self.queue[self.rear]
            if self.rear == self.front:
                self.rear = self.front = -1
            else:
                self.rear += 1
            self.length -= 1
            return retValue


q = Queue(5)

q.enqueue(101)
q.enqueue(202)
print(q.size()) # 2

for i in range(5):
    q.enqueue(i)

while not q.isEmpty():
    print(q.dequeue())

print(q.size()) # 0