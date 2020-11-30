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
            self.tail.next = self.head
        else:
            self.head = Node(key, self.head)
            self.tail.next = self.head

    def addToTail(self, key):
        if self.isEmpty():
            self.head = self.tail = Node(key)
            self.tail.next = self.head
        else:
            self.tail.next = Node(key, self.head)
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
                current: Node = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = self.head
                self.tail = current
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
                else:
                    current = current.next
            self.tail = current
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
                    prev: Node = None
                    current: Node = self.head
                    count: int = 0
                    while count < index:
                        prev = current
                        current = current.next
                        count += 1
                    prev.next = current.next

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
                        current.next = Node(newElement, current.next)
                    current = current.next
                current = current.next

    def insertBefore(self, listElement, newElement):
        if self.isEmpty():
            return
        else:
            prev: Node = None
            current: Node = self.head
            stopped: bool = True
            while current != self.head or stopped:
                stopped = False
                if current.key == listElement:
                    if current == self.head:
                        self.addToHead(newElement)
                    else:
                        prev.next = Node(newElement, current)
                prev = current
                current = current.next

    def sort(self):
        if self.isEmpty():
            return
        else:
            swapped: bool = True
            current: Node
            while swapped:
                swapped = False
                current = self.head
                while current != self.tail:
                    if current.key > current.next.key:
                        tmp: int = current.key
                        current.key = current.next.key
                        current.next.key = tmp
                        swapped = True
                    current = current.next




        

            

        

        

