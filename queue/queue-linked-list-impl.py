
class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class Queue:
    def __init__(self):
        self._head = self._tail = None
        self._count: int = 0

    def enqueue(self, item):
        if self.is_empty():
            self._head = self._tail = Node(item)
        else:
            self._tail.next = Node(item)
            self._tail = self._tail.next
        self._count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        ret_value: Node = self._head
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self._count -= 1
        return ret_value.key

    def size(self) -> int:
        return self._count

    def is_empty(self) -> bool:
        return self._head is None


def hot_potato(namelist, number):
    q: Queue = Queue()
    for person in namelist:
        q.enqueue(person)
    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

