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
            self.head = Node(item, self.head)

    def addToTail(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
        else:
            self.tail.next = Node(item)
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
            return retValue

    def deleteFromTail(self):
        if self.isEmpty():
            return None
        else:
            retValue = self.tail.key
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                current: Node = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
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
                prev: Node = None
                current: Node = self.head
                while count < index:
                    count += 1
                    prev = current
                    current = current.next
                prev.next = current.next

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
                        current.next = Node(newElement, current.next)
                    current = current.next
                current = current.next

    def insertBefore(self, listElement, newElement):
        if self.isEmpty():
            return 
        else:
            prev: Node = None
            current: Node = self.head
            while current is not None:
                if current.key == listElement:
                    if current == self.head:
                        self.addToHead(newElement)
                    else:
                        prev.next = Node(newElement, current)
                prev = current
                current = current.next

    def sort(self):
        swapped: bool = True
        while swapped:
            swapped = False
            current: Node = self.head
            while current != self.tail:
                if current.key > current.next.key:
                    tmp: int = current.key
                    current.key = current.next.key
                    current.next.key = tmp
                    swapped = True






