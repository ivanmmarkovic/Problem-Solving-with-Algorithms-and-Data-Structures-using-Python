
class Deque:

    def __init__(self):
        self.deque: list = []

    def size(self)->int:
        return len(self.deque)

    def isEmpty(self):
        return len(self.deque) == 0

    def addFront(self, item):
        self.deque.insert(0, item)

    def addRear(self, item):
        self.deque.append(item)

    def removeFront(self):
        return self.deque.pop(0)

    def removeRear(self):
        return self.deque.pop()


