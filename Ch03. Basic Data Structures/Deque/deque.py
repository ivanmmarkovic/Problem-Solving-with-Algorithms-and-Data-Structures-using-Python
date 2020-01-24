
class Deque:
    def __init__(self):
        self.deque: list = []

    def isEmpty(self)->bool:
        return len(self.deque) == 0

    def size(self)->int:
        return len(self.deque)

    def addFront(self, item):
        self.deque.insert(0, item)

    def addRear(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.deque.pop(0)

    def removeRear(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.deque.pop()

