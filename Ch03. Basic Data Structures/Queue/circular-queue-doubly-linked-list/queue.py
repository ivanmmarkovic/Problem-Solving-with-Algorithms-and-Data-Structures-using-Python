from node import Node

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__elements: int = 0

    def isEmpty(self)->bool:
        return self.__head is None

    def size(self):
        return self.__elements

    def enqueue(self, item):
        if self.isEmpty():
            self.__head = self.__tail = Node(item)
            self.__head.prev = self.__tail
            self.__tail.next = self.__head
        else:
            self.__tail.next = Node(item, self.__tail, self.__head)
            self.__tail = self.__tail.next
            self.__head.prev = self.__tail
        self.__elements += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        item = self.__head.key
        if self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = self.__tail
            self.__tail.next = self.__head
        self.__elements -= 1
        return item


