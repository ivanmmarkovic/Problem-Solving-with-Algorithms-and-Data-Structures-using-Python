class Dequeue:
    def __init__(self):
        self.dequeue = []

    def addFront(self, item):
        self.dequeue.insert(0, item)

    def addRear(self, item):
        self.dequeue.append(item)

    def removeFront(self):
        return self.dequeue.pop(0)

    def removeRear(self):
        return self.dequeue.pop()

    def isEmpty(self):
        return self.dequeue == []

    def size(self):
        return len(self.dequeue)
