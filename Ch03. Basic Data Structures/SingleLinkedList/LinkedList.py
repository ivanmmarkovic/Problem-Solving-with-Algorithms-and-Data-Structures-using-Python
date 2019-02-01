
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
            self.head = Node(payload, self.head)

    def addToTail(self, payload):
        if self.isEmpty():
            self.head = self.tail = Node(payload)
        else:
            self.tail.next = Node(payload)
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
                tmp = self.head
                while tmp.next != self.tail:
                    tmp= tmp.next
                tmp.next = None
                self.tail = tmp
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
                prevNode = self.head
                nodeToDelete = self.head.next
                while counter < index:
                    prevNode = nodeToDelete
                    nodeToDelete = nodeToDelete.next
                    counter += 1

                prevNode.next = nodeToDelete.next
                nodeToDelete = None

    def insertBefore(self, listValue, newValue):
        prevNode = None
        tmp = self.head
        while tmp != None:
            if tmp.payload == listValue:
                if tmp == self.head:
                    self.addToHead(newValue)
                else:
                    newNode = Node(newValue, tmp)
                    prevNode.next = newNode
            prevNode = tmp
            tmp = tmp.next

    def insertAfter(self, listValue, newValue):
        tmp = self.head
        while tmp != None:
            if tmp.payload == listValue:
                if tmp == self.tail:
                    self.addToTail(newValue)
                else:
                    newNode = Node(newValue, tmp.next)
                    tmp.next = newNode
                tmp = tmp.next
            tmp = tmp.next

    def sort(self):
        outer = self.head
        while outer != None:
            swapped = True
            while swapped:
                swapped = False
                inner = self.head
                while inner.next != None:
                    if inner.payload > inner.next.payload:
                        tmp = inner.next.payload
                        inner.next.payload = inner.payload
                        inner.payload = tmp
                        swapped = True
                    inner = inner.next

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


