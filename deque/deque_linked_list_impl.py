

from typing import List, Any


class ListNode:

    def __init__(self, key:Any = None, prev:'ListNode' = None, next:'ListNode' = None):
        self.key:Any = key
        self.prev:'ListNode' = prev
        self.next:'ListNode' = next


class Deque:

    def __init__(self):
        self._head:ListNode = None
        self._tail:ListNode = None
        self._length:int = 0


    def size(self) -> int:
        return self._length
    

    def is_empty(self) -> bool:
        return self._length == 0
    

    def add_front(self, e:Any) -> None:
        if self.is_empty():
            self._head = self._tail = ListNode(e)
        else:
            self._head = ListNode(e, None, self._head)
            self._head.next.prev = self._head
        self._length += 1


    def add_rear(self, e:Any) -> None:
        if self.is_empty():
            self._head = self._tail = ListNode(e)
        else:
            self._tail.next = ListNode(e, self._tail, None)
            self._tail = self._tail.next
        self._length += 1


    def remove_front(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        e:Any = self._head.key
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._length -= 1
        return e
    

    def remove_rear(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        e:Any = self._tail.key
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._length -= 1
        return e
    

    def get_front(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._head.key
    

    def remove_rear(self) -> Any:
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._tail.key
