class Queue:
    def __init__(self):
        self.__queue__: list = []

    def is_empty(self) -> bool:
        return len(self.__queue__) == 0

    def enqueue(self, vertex: str):
        self.__queue__.append(vertex)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.__queue__.pop(0)

    