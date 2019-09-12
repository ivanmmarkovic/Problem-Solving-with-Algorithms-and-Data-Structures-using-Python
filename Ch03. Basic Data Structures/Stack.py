class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        # not checking if stack is empty
        # https://github.com/ivanmmarkovic/Problem-Solving-with-Algorithms-and-Data-Structures-using-Python/issues/1
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)
