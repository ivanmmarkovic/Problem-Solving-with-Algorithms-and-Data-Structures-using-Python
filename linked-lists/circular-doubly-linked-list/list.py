from node import Node

class List:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def isEmpty(self):
        return self.head is None

    def numberOfElements(self)->int:
        if self.isEmpty():
            return 0
        else:
            current: Node = self.head
            stopped: bool = True
            count: int = 0
            while current != self.head or stopped:
                stopped = False
                count += 1
                current = current.next
            return count

    def printAll(self):
        if self.isEmpty():
            return
        else:
            current: Node = self.head
            stopped: bool = True
            while current != self.head or stopped:
                stopped = False
                print(current.key, end=", ")
                current = current.next
            print("")

    def addToHead(self, key):
        if self.isEmpty():
            self.head = self.tail = Node(key)
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            self.head = Node(key, self.tail, self.head)
            self.head.next.prev = self.head
            self.tail.next = self.head

    def addToTail(self, key):
        if self.isEmpty():
            self.head = self.tail = Node(key)
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            self.tail.next = Node(key, self.tail, self.head)
            self.tail = self.tail.next
            self.head.prev = self.tail

    def deleteFromHead(self):
        if self.isEmpty():
            return None
        else:
            retValue = self.head.key
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            return retValue

    def deleteFromTail(self):
        if self.isEmpty():
            return None
        else:
            retValue = self.tail.key
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.head.prev = self.tail
                self.tail.next = self.head
            return retValue

    def deleteNodesWithValue(self, value):
        if self.isEmpty():
            return
        else:
            current: Node = self.head
            stopped: bool = True
            while current.next != self.head or stopped:
                stopped = False
                if current.next.key == value:
                    current.next = current.next.next
                    current.next.prev = current
                else:
                    current = current.next
            self.tail = current
            self.tail.next = self.head
            self.head.prev = self.tail
            if self.head.key == value:
                self.deleteFromHead()

    def deleteOnIndex(self, index: int):
        if self.isEmpty():
            return 
        else:
            lastIndex = self.numberOfElements() - 1
            if index < 0 or index > lastIndex:
                print("Index out of range")
                return
            else:
                if index == 0:
                    self.deleteFromHead()
                elif index == lastIndex:
                    self.deleteFromTail()
                else:
                    current: Node = self.head
                    count: int = 0
                    while count < index:
                        current = current.next
                        count += 1
                    current.prev.next = current.next
                    current.next.prev = current.prev

    def insertAfter(self, listElement: int, newElement: int):
        if self.isEmpty():
            return
        else:
            current: Node = self.head
            stopped: bool = True
            while current != self.head or stopped:
                stopped = False
                if current.key == listElement:
                    if current == self.tail:
                        self.addToTail(newElement)
                    else:
                        newNode = Node(newElement, current, current.next)
                        newNode.prev.next = newNode
                        newNode.next.prev = newNode
                    current = current.next
                current = current.next

    def insertBefore(self, listElement, newElement):
        if self.isEmpty():
            return
        else:
            current: Node = self.head
            stopped: bool = True
            while current != self.head or stopped:
                stopped = False
                if current.key == listElement:
                    if current == self.head:
                        self.addToHead(newElement)
                    else:
                        newNode = Node(newElement, current.prev, current)
                        newNode.prev.next = newNode
                        newNode.next.prev = newNode
                current = current.next

    def sort(self):
        if self.isEmpty():
            return
        else:
            outer: Node
            inner: Node
            while outer != self.tail:
                inner = self.tail
                while inner != outer:
                    if inner.prev.key > inner.key:
                        tmp: int = inner.key
                        inner.key = inner.prev.key
                        inner.prev.key = tmp
                    inner = inner.prev
                outer = outer.next




        

            

        

        

