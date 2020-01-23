
class Stack:
    def __init__(self, length: int = 10):
        self.length = length
        self.stack: list = [None] * self.length
        self.pointer = -1
    
    def isEmpty(self)->bool:
        return self.pointer == -1

    def size(self)->int:
        return self.pointer + 1

    def push(self, item):
        if self.pointer < self.length - 1:
            self.pointer += 1
            self.stack[self.pointer] = item
        else:
            raise Exception('Stack is full')

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            retValue = self.stack[self.pointer]
            self.pointer -= 1
            return retValue

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            return self.stack[self.pointer]
    
