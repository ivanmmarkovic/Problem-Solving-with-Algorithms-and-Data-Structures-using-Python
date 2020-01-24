

class Queue:
    def __init__(self, length: int = 10):
        self.length = length
        self.queue: list = [None] * self.length
        self.front = self.rear = -1
        self.__elements: int = 0

    def isEmpty(self)->bool:
        return self.front == -1
    
    def __full(self)->bool:
        return self.front == self.length - 1

    def size(self)->int:
        return self.__elements

    def enqueue(self, item):
        if self.__full():
            raise Exception('Queue is full')
        self.front += 1
        if self.rear == -1:
            self.rear += 1
        self.__elements += 1
        self.queue[self.front] = item
        

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        retValue = self.queue[self.rear]
        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.rear += 1
        self.__elements -= 1
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
