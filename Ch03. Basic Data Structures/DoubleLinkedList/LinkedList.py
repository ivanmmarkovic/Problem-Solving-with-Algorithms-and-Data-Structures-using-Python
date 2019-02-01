
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        return self.head == None

    def numberOfElements(self):
        count = 0
        tmp = self.head
        while tmp != None:
            count += 1
            tmp = tmp.next

        return count

    def printAll(self):
        result = ""
        tmp = self.head
        while tmp != None:
            result += str(tmp.payload) + ", "
            tmp = tmp.next
        return result

    def addToHead(self, payload):
        if self.isEmpty():
            self.head = self.tail = Node(payload)
        else:
            self.head = Node(payload, None, self.head)
            self.head.next.prev = self.head

    def addToTail(self, payload):
        if self.isEmpty():
            self.head = self.tail = Node(payload)
        else:
            self.tail.next = Node(payload, self.tail)
            self.tail = self.tail.next

    def removeFromHead(self):
        if self.isEmpty():
            return None
        else:
            returnValue = self.head.payload
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                nodeToDelete = self.head
                self.head =self.head.next
                self.head.prev = None
                nodeToDelete = None
            return returnValue

    def removeFromTail(self):
        if self.isEmpty():
            return None
        else:
            returnValue = self.tail.payload
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                nodeToDelete = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                nodeToDelete = None
            return returnValue

    def deleteNodesWithValue(self, value):
        if self.isEmpty():
            return
        else:
            currentNode = self.head
            while currentNode.next != None:
                if currentNode.next.payload == value:
                    if currentNode.next.next == None:
                        currentNode.next = None
                    else:
                        currentNode.next = currentNode.next.next
                        currentNode.next.prev = currentNode
                else:
                    currentNode = currentNode.next
            self.tail = currentNode
        if self.head.payload == value:
            self.removeFromHead()

    def deleteOnIndex(self, index):
        size = self.numberOfElements()
        if self.isEmpty():
            pass
        elif index < 0 or index >= size:
            pass
        else:
            if index == 0:
                self.removeFromHead()
            elif index == size - 1:
                self.removeFromTail()
            else:
                counter = 1
                nodeToDelete = self.head.next
                while counter < index:
                    nodeToDelete = nodeToDelete.next
                    counter += 1

                nodeToDelete.prev.next = nodeToDelete.next
                nodeToDelete.next.prev = nodeToDelete.prev

    def insertBefore(self, listValue, newValue):
        tmp = self.head
        while tmp != None:
            if tmp.payload == listValue:
                if tmp == self.head:
                    self.addToHead(newValue)
                else:
                    newNode = Node(newValue, tmp.prev, tmp)
                    tmp.prev.next = newNode
                    tmp.prev = newNode
            tmp = tmp.next

    def insertAfter(self, listValue, newValue):
        tmp = self.head
        while tmp != None:
            if tmp.payload == listValue:
                if tmp == self.tail:
                    self.addToTail(newValue)
                else:
                    newNode = Node(newValue, tmp, tmp.next)
                    tmp.next.prev = newNode
                    tmp.next = newNode
                tmp = tmp.next
            tmp = tmp.next

    def sort(self):
        outer = self.head
        while outer != self.tail:
            inner = self.tail
            while inner != outer:
                if inner.prev.payload > inner.payload:
                    tmp = inner.prev.payload
                    inner.prev.payload = inner.payload
                    inner.payload = tmp
                inner = inner.prev
            outer = outer.next


l = LinkedList()

for i in range(1, 6):
    l.addToHead(i)

l.addToHead(5)
l.addToHead(5)
l.addToHead(5)

for i in range(5, 10):
    l.addToHead(i)


l.addToTail(5)
l.addToTail(5)
l.addToTail(5)
l.addToHead(5)
l.addToHead(5)
l.addToHead(5)

print(l.printAll())
l.deleteNodesWithValue(5)
print(l.printAll())
