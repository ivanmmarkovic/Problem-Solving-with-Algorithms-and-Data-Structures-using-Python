class Stack:
    def __init__(self):
        self.stack: list = []

    def isEmpty(self)->bool:
        return len(self.stack) == 0

    def size(self)->int:
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

