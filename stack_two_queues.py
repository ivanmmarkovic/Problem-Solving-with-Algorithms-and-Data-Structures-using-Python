from typing import Any, List


class Queue:

    def __init__(self) -> None:
        self.queue:List[Any] = []

    def size(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def enqueue(self, item:Any) -> None:
        self.queue.insert(0, item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue.pop()



class Stack:

    def __init__(self):
        self.input: Queue = Queue()
        self.output:Queue = Queue()
        

    def push(self, x: Any) -> None:
        self.input.enqueue(x)
        

    def pop(self) -> Any:
        if self.input.is_empty():
            raise Exception('Queue is empty')
        
        while self.input.size() > 1:
            self.output.enqueue(self.input.dequeue())
            
        item:Any = self.input.dequeue()

        while not self.output.is_empty():
            self.input.enqueue(self.output.dequeue())
            
        return item


    def peek(self) -> Any:
        if self.input.is_empty():
            raise Exception('Queue is empty')
            
        while self.input.size() > 1:
            self.output.enqueue(self.input.dequeue())
            
        item:Any = self.input.dequeue()
        self.output.enqueue(item)
        
        while not self.output.is_empty():
            self.input.enqueue(self.output.dequeue())
        return item
        

    def is_empty(self) -> bool:
        return self.input.is_empty()
