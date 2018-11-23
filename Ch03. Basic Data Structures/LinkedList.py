from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def addToHead(self, data):
        self.head = Node(data, self.head)
        if self.tail == None:
            self.tail = self.head

    def addToTail(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data) 
            self.tail = self.tail.next

    def deleteFromHead(self):
        if self.isEmpty():
            return None
        else:
            tmp = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return tmp

    def deleteFromTail(self):
        if self.isEmpty():
            return None
        else:
            tmp = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                currentNode = self.head
                while(currentNode.next != self.tail):
                    currentNode = currentNode.next
                currentNode.next = None
                self.tail = currentNode
            return tmp

    def deleteItemsWithValue(self, value):
        if self.isEmpty():
            return
        # check all nodes except head
        elif self.head != self.tail: # two or more Nodes
            currentNode = self.head
            while currentNode.next != None:
                if currentNode.next.data == value:
                    if currentNode.next.next == None:
                        currentNode.next = None
                    else:
                        currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next
            self.tail = currentNode
        # check head only
        if self.head.data == value:
            if self.tail == self.head:
                self.head = self.tail = None
            else:
                self.head = self.head.next

    def sort(self):
        outer = self.head
        while outer != None:
            swapped = True
            while swapped == True:
                swapped = False
                inner = self.head
                while inner.next != None:
                    if inner.data > inner.next.data:
                        tmp = inner.data
                        inner.data = inner.next.data
                        inner.next.data = tmp
                        swapped = True
                    inner = inner.next
            outer = outer.next

    def printAll(self):
        result = ""
        currentNode = self.head
        while(currentNode != None):
            result += (str(currentNode.data) + ", ")
            currentNode = currentNode.next
        print(result)

    def size(self):
        counter = 0
        currentNode = self.head
        while(currentNode != Node):
            counter += 1
            currentNode = currentNode.next
        return counter

    


