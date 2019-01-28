from Node import Node

class QueueAsLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        tmp = self.head
        while tmp != None:
            count += 1
            tmp = tmp.next

        return count

    def print(self):
        result = ""
        tmp = self.head
        while tmp != None:
            result += str(tmp.payload)
            tmp = tmp.next
        print(result)

    def enqueue(self, payload):
        if self.isEmpty():
            self.head = Node(payload, self.head)
            self.tail = self.head
        else:    
            self.head = Node(payload, self.head)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            nodeToRemove = self.tail
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                tmp = self.head
                while tmp.next != self.tail:
                    tmp = tmp.next
                tmp.next = None
                self.tail = tmp
            return nodeToRemove.payload



q = QueueAsLinkedlList()
q.enqueue("string")
q.enqueue(12)
q.enqueue(100)

q.print()
while not q.isEmpty():
    print(q.dequeue())