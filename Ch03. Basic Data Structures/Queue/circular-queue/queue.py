

class Queue:
    def __init__(self, length: int = 10):
        self.length = length
        self.queue: list = [None] * self.length
        self.front = self.rear = -1
        self.__elements: int = 0

    def isEmpty(self)->bool:
        return self.front == -1
    
    def __full(self)->bool:
        return (self.front + 1) % self.length == self.rear

    def size(self)->int:
        return self.__elements

    def enqueue(self, item):
        if self.__full():
            raise Exception('Queue is full')
        self.front = (self.front + 1) % self.length
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
            self.rear = (self.rear +1) % self.length
        self.__elements -= 1
        return retValue


