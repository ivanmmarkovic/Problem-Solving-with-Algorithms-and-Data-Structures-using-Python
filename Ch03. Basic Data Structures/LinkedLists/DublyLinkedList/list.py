from node import Node

class List:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def isEmpty(self)->bool:
        return self.head is None

    def numberOfElements(self)->int:
        if self.isEmpty():
            return 0
        else:
            current: Node = self.head
            count: int = 0
            while current is not None:
                count += 1
                current = current.next
            return count

    def addToHead(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
        else:
            self.head = Node(item, None, self.head)
            self.head.next.prev = self.head

    def addToTail(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
        else:
            self.tail.next = Node(item, self.tail, None)
            self.tail = self.tail.next

    def deleteFromHead(self):
        if self.isEmpty():
            return None
        else:
            retValue = self.head.key
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
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
                self.tail.next = None
            return retValue

    def deleteOnIndex(self, index: int):
        lastIndex: int = self.numberOfElements() - 1
        if index < 0 or index > lastIndex:
            print("Index out of range")
            return
        else:
            if index == 0:
                self.deleteFromHead()
            elif index == lastIndex:
                self.deleteFromTail()
            else:
                count: int = 0
                current: Node = self.head
                while count < index:
                    count += 1
                    current = current.next
                current.prev.next = current.next
                current.next.prev = current.prev

    def deleteNodesWithValue(self, value):
        retValue = None
        if self.isEmpty():
            return retValue
        else:
            current: Node = self.head
            while current.next is not None:
                if current.next.key == value:
                    retValue = current.next.key
                    current.next = current.next.next
                    if current.next is not None:
                        current.next.prev = current
                else:
                    current = current.next
            self.tail = current
            if self.head.key == value:
                retValue = self.head.key
                self.deleteFromHead()
            return retValue

    def insertAfter(self, listElement, newElement):
        if self.isEmpty():
            return
        else:
            current: Node = self.head
            while current is not None:
                if current.key == listElement:
                    if current == self.tail:
                        self.addToTail(newElement)
                    else:
                        newNode = Node(newElement, current, current.next)
                        current.next = newNode
                        newNode.next.prev = newNode
                    current = current.next
                current = current.next

    def insertBefore(self, listElement, newElement):
        if self.isEmpty():
            return 
        else:
            current: Node = self.head
            while current is not None:
                if current.key == listElement:
                    if current == self.head:
                        self.addToHead(newElement)
                    else:
                        newNode = Node(newElement, current.prev, current)
                        newNode.prev.next = newNode
                        newNode.next.prev = newNode
                current = current.next

    def sort(self):
        outer: Node = self.head
        while outer != self.tail:
            inner: Node = self.tail
            while inner != outer:
                if inner.prev.key > inner.key:
                    tmp: int = inner.prev.key
                    inner.prev.key = inner.key
                    inner.key = tmp
                inner = inner.prev
            outer = outer.next







