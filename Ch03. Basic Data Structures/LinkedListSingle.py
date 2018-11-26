from NodeSingle import NodeSingle

class LinkedListSingle:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def addToHead(self, payload):
        self.head = NodeSingle(payload, self.head)
        if self.tail == None:
            self.tail = None

    def addToTail(self, payload):
        if self.isEmpty():
            self.head = self.tail = NodeSingle(payload) 
        else:
            self.tail.next = NodeSingle(payload)
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
            return payloadToReturn

    def removeFromTail(self):
        if self.isEmpty():
            return None
        else:
            payloadToReturn = self.tail.payload
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                currentNode = self.head
                while currentNode.next != self.tail:
                    currentNode = currentNode.next
                currentNode.next = None
                self.tail = currentNode
            return payloadToReturn

    def deleteAllNodeSinglesWithValue(self, value):
        if self.isEmpty():
            return
        # check if list contains more than one NodeSingle
        # check all, except self.head
        elif self.head != self.tail:
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
        # check self.head
        if self.head.payload == value:
            if self.head.next == None:
                self.head = self.tail = None
            else:
                self.head = self.head.next

    def deleteOnIndex(self,index):
        listSize = self.size()
        if index >= listSize or self.isEmpty():
            return
        else:
            counter = 0
            prevNode = None
            currentNode = self.head
            while counter < index:
                counter += 1
                prevNode = currentNode
                currentNode= currentNode.next
            if prevNode == None:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
            else:
                # not a self.tail
                if currentNode.next != None:
                    prevNode.next = currentNode.next
                    currentNode = None
                # is a self.tail
                else:
                    prevNode.next = None
                    self.tail = prevNode
                    currentNode = None

    def sortShortBubble(self):
        outer = self.head
        inner = self.head
        swapped = True
        while outer != None:
            swapped = True
            while swapped:
                swapped = False
                inner = self.head
                while inner.next != None:
                    if inner.payload > inner.next.payload:
                        tmp = inner.payload
                        inner.payload = inner.next.payload
                        inner.next.payload = tmp
                        swapped = True
                    inner = inner.next
            outer = outer.next

    def size(self):
        if self.isEmpty():
            return 0
        else:
            counter = 0
            currentNode = self.head
            while currentNode != None:
                counter += 1
                currentNode = currentNode.next
            return counter

    def printAll(self):
        result = ""
        currentNode = self.head
        while currentNode != None:
            result += (str(currentNode.payload) + ", ")
            currentNode = currentNode.next
        print(result)

