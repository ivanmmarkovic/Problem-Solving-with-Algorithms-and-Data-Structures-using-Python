class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._queue.pop()

    def size(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return len(self._queue) == 0
        
    def peek(self) -> int:
    	if self.is_empty():
            raise Exception("Queue is empty")
    	return self._queue[len(self._queue) - 1]

class MyStack:

    def __init__(self):
        self.input = Queue()
        self.output = Queue()

    def empty(self) -> bool:
        return self.input.is_empty()

    def push(self, item):
        self.input.enqueue(item)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        while self.input.size() > 1 :
            self.output.enqueue(self.input.dequeue())
        
        val = self.input.dequeue()
        while not self.output.is_empty():
            self.input.enqueue(self.output.dequeue())
        
        return val

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        while self.input.size() > 1 :
            self.output.enqueue(self.input.dequeue())
        
        val = self.input.peek()
        self.output.enqueue(self.input.dequeue())
        while not self.output.is_empty():
            self.input.enqueue(self.output.dequeue())
        
        return val

    def size(self) -> int:
        return self.input.size()

        

