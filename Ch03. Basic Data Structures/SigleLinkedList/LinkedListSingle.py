from Node import Node

class LinkedListSingle:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        counter = 0
        tmp = self.head
        while tmp != None:
            counter += 1
            tmp = tmp.next
        return counter

    def printAll(self):
        result = ""
        tmp = self.head
        while tmp != None:
            result += str(tmp.payload)
            tmp = tmp.next
        print(result)

    def addToHead(self, payload):
        self.head = Node(payload, self.head)
        if self.tail == None:
            self.tail = self.head
    
    def addToTail(self, payload):
        if self.isEmpty():
            self.head = self.tail = Node(payload)
        else:
            self.tail.next = Node(payload)
            self.tail = self.tail.next

    def deleteFromHead(self):
        if self.isEmpty():
            return
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head =self.head.next

    def deleteFromTail(self):
        if self.isEmpty():
            return None
        else:
            toReturn = self.tail.payload
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                tmp = self.head
                while tmp.next != self.tail:
                    tmp = tmp.next 
                tmp.next = None
                self.tail = tmp
            return toReturn

    def sort(self):
        outer = self.head
        while outer!= None:
            swapped = True
            while swapped == True:
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

    def deleteOnIndex(self, index):
        size = self.size()
        if index < 0 or index > size or self.isEmpty():
            return 
        else:
            if index == 0:
                self.deleteFromHead()
            elif index == size - 1:
                self.deleteFromTail()
            else:
                prev = None
                current = self.head
                counter = 0
                while counter < index:
                    prev = current
                    current = current.next
                    counter += 1
                prev.next = current.next

    def deleteNodesWithValue(self, value):
        prev = None
        tmp = self.head
        while tmp != None:
            if tmp.payload == value:
                if tmp == self.head:
                    self.deleteFromHead()
                elif tmp == self.tail:
                    self.deleteFromTail()
                else:
                    prev.next = tmp.next
                    tmp = prev
            else:
                prev = tmp
            
            tmp = tmp.next

    def insertAfter(self, listPayload, newPayload):
        tmp = self.head
        while tmp != None:
            if tmp.payload == listPayload:
                if tmp == self.tail:
                    self.addToTail(newPayload)
                else:
                    newNode = Node(newPayload, tmp.next)
                    tmp.next = newNode
                tmp = tmp.next
            tmp = tmp.next

    def insertBefore(self, listPayload, newPayload):
        prev = None
        tmp = self.head
        while tmp != None:
            if tmp.payload == listPayload:
                if tmp == self.head:
                    self.addToHead(newPayload)
                else:
                    newNode = Node(newPayload, tmp)
                    prev.next = newNode
            prev = tmp
            tmp = tmp.next


