
class Queue:
    def __init__(self, capacity: int = 10):
        self.capacity: int = capacity
        self.queue: list = [None] * self.capacity
        self.rear: int = -1
        self.front: int = -1
        self.length: int = 0

    def size(self)->int:
        return self.length

    def isEmpty(self)->bool:
        return self.rear == -1

    def isFull(self):
        return (self.front + 1) % self.capacity == self.rear

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.front = (self.front + 1) % self.capacity
        self.queue[self.front] = item
        if self.rear == -1:
            self.rear += 1
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        retValue = self.queue[self.rear]
        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.length -= 1
        return retValue

    def toString(self)->str:
        if self.isEmpty():
            return None
        else:
            result: str = ""
            if self.rear <= self.front:
                for i in range(self.rear, self.front + 1, +1):
                    result += str(self.queue[i]) + ", "
            else:
                for i in range(self.rear, self.capacity, +1):
                    result += str(self.queue[i]) + ", "
                for i in range(0, self.front, +1):
                     result += str(self.queue[i]) + ", "
            return result

queue = Queue(5)

queue.enqueue(1221)
queue.enqueue(13)
print(queue.toString())

for i in range(5):
    queue.enqueue(i)

print(queue.toString())


print(queue.dequeue())
print(queue.dequeue())

queue.enqueue(777)
queue.enqueue(5555)
queue.enqueue(121212)


print(queue.toString())
print(queue.queue)


    

    

