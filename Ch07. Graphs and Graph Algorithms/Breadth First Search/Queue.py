from Node import Node

class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def isEmpty(self):
        return self.head == None

    def enqueue(self, vertex):
        self.head = Node(vertex, self.head)
        if self.tail == None:
            self.tail = self.head

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            toReturn = self.tail
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                tmp = self.head
                while tmp.next != self.tail:
                    tmp = tmp.next
                self.tail = tmp
                tmp.next = None
            return toReturn.payload
