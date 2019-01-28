from Node import Node

class StackAsLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        tmp = self.head
        while tmp != None:
            count += 1
            tmp = tmp.next

        return count

    def push(self, payload):
        self.head = Node(payload, self.head)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            nodeToRemove = self.head
            self.head = self.head.next
            return nodeToRemove.payload

def reverseString(string):
    s = StackAsLinkedList()
    for character in string:
        s.push(character)
    
    result = ""
    while not s.isEmpty():
        result += s.pop()

    return result

print(reverseString("This is a string!"))
