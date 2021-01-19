class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.input_stack: Stack = Stack()
        self.output_stack: Stack = Stack()

    def is_empty(self) -> bool:
        return self.input_stack.is_empty()

    def size(self) -> int:
        return self.input_stack.size()

    def enqueue(self, item):
        self.input_stack.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        while not self.input_stack.is_empty():
            self.output_stack.push(self.input_stack.pop())
        ret_value = self.output_stack.pop()
        while not self.output_stack.is_empty():
            self.input_stack.push(self.output_stack.pop())
        return ret_value


def hot_potato(people: list, num: int) -> str:
    q: Queue = Queue()
    for person in people:
        q.enqueue(person)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))