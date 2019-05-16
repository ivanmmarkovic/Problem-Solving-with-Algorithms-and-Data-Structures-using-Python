class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.isEmpty():
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def push(self, item):
        self.stack.append(item)
