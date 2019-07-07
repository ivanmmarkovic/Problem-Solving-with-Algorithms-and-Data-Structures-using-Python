

class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self)-> bool:
        return self.stack == []

    def size(self)-> int:
        return len(self.stack) - 1

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]