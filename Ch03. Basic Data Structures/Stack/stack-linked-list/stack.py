from node import Node

class Stack:
    def __init__(self):
        self.head: Node = None
        self.length: int = 0

    def isEmpty(self):
        return self.head is None
        # self.length == 0

    def size(self):
        # avoid linked list traversal
        return self.length

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            return self.head.key

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            retNode: Node = self.head
            self.head = self.head.next
            self.length -= 1
            return retNode.key

    def push(self, item):
        self.length += 1
        self.head = Node(item, self.head)


s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
