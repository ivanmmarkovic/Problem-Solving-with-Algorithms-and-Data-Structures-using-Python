from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def printAll(self):
        result = ""
        currentNode = self.head
        while currentNode != None:
            result += (str(currentNode.payload) + ", ")
            currentNode = currentNode.next
        print(result)

    def size(self):
        counter = 0
        currentNode = self.head
        while currentNode != None:
            counter += 1
            currentNode = currentNode.next
        return counter

    def addToHead(self, payload):
        if self.isEmpty():
            self.head = self.tail = Node(payload, None, None)
        else:
            self.head = Node(payload, None, self.head)
            self.head.next.previous = self.head

    def addToTail(self, payload):
        if self.isEmpty():
            self.head = self.tail = Node(payload, None, None)
        else:
            self.tail.next = Node(payload, self.tail, None)
            self.tail = self.tail.next

    def removeFromHead(self):
        if self.isEmpty():
            return None
        else:
            payloadToReturn = self.head.payload
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
            return payloadToReturn

    def removeFromTail(self):
        if self.isEmpty():
            return None
        else:
            payloadToReturn = self.tail.payload
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
            return payloadToReturn

    def deleteNodeOnIndex(self, index):
        if(index >= self.size() or index < 0 or self.isEmpty()):
            return 
        else:
            counter = 0
            prevNode = None
            currentNode = self.head
            while counter < index:
                prevNode = currentNode
                currentNode = currentNode.next
                counter += 1
            if prevNode == None: # delete self.head
                if self.head == self.tail:
                    self.tail = self.head = None
                else:
                    self.head = self.head.next
                    self.head.previous = None
            else:
                prevNode.next = currentNode.next
                if prevNode.next == None:
                    self.tail = prevNode
                else:
                    prevNode.next.previous = prevNode
                currentNode = None

    def deleteNodesWithValue(self, payload):
        if self.isEmpty():
            return
        elif self.head != self.tail: # two or more Nodes
            currentNode = self.head
            while currentNode.next != None:
                if currentNode.next.payload == payload:
                    currentNode.next = currentNode.next.next
                    if currentNode.next != None:
                        currentNode.next.previous = currentNode
                else:
                    currentNode = currentNode.next
            self.tail = currentNode
        # check self.head
        if self.head.payload == payload:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None

    def sort(self):
        outer = self.head
        while outer != None:
            inner = self.tail
            while inner != outer:
                if inner.previous.payload > inner.payload:
                    tmp = inner.previous.payload
                    inner.previous.payload = inner.payload
                    inner.payload = tmp
                inner = inner.previous
            outer = outer.next
        

