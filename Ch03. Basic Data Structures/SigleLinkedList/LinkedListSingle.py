from Node import Node

class LinkedListSingle:
    def __init__(self):
        self.head = None
        self.tail = None

    def printAll(self):
        result = ""
        tmp = self.head 
        while tmp != None:
            result += (str(tmp.payload) + ", ")
            tmp = tmp.next
        print(result)

    def size(self):
        count = 0
        tmp = self.head
        while tmp != None:
            count += 1
            tmp = tmp.next
        return count

    def isEmpty(self):
        return self.head == None

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
                self.head = self.head.next
    
    def deleteFromTail(self):
        if self.isEmpty():
            return
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                tmp = self.head
                while tmp.next != self.tail:
                    tmp = tmp.next
                self.tail = tmp
                self.tail.next = None

    def deleteOnIndex(self, index):
        size = self.size()
        if index < 1 or index > size:
            return
        else:
            if index == 1:
                self.deleteFromHead()
            elif index == size:
                self.deleteFromTail()
            else:
                prev = self.head
                count = 1
                while count < index - 1:
                    prev = prev.next
                    count += 1
                prev.next = prev.next.next

    def deleteNodesWithValue(self, value):
        tmp = self.head
        prev = None
        while tmp != None:
            if tmp.payload == value:
                if tmp == self.head:
                    self.deleteFromHead()
                elif tmp == self.tail:
                    self.deleteFromTail()
                else:
                    prev.next = prev.next.next
                    tmp = prev
            else:
                prev = tmp
            tmp = tmp.next

    def insertAfter(self, listElement, newElement):
        tmp = self.head
        while tmp != None:
            if tmp.payload == listElement:
                if tmp == self.tail:
                    self.addToTail(newElement)
                else:
                    newNode = Node(newElement, tmp.next)
                    tmp.next = newNode
                tmp = tmp.next
            tmp = tmp.next

    def insertBefore(self, listElement, newElement):
        tmp = self.head
        prev = None
        while tmp != None:
            if tmp.payload == listElement:
                if tmp == self.head:
                    self.addToHead(newElement)
                else:
                    newNode = Node(newElement, tmp)
                    prev.next = newNode
            prev = tmp
            tmp = tmp.next

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

