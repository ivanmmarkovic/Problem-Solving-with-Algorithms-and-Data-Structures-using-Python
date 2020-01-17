
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            retValue = self.head.value
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
            return retValue







