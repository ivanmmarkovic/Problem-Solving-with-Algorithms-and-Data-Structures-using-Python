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
        if self.isEmpty():
            raise Exception('Stack is empty')
        # not checking if stack is empty
        # https://github.com/ivanmmarkovic/Problem-Solving-with-Algorithms-and-Data-Structures-using-Python/issues/1
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

        
'''
this solution is slower
previous
############
1. pop - pop() - O(1)
2. push - append() - O(1)
this
############
1. pop - pop(i) - O(k)
2. push - insert(i) - O(n)
class Stack:
    def __init__(self):
        self.stack: list = []
    def isEmpty(self)->bool:
        return len(self.stack) == 0
    def size(self)->int:
        return len(self.stack)
    def push(self, item):
        self.stack.insert(0, item)
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.stack.pop(0)
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.stack[0]
'''
