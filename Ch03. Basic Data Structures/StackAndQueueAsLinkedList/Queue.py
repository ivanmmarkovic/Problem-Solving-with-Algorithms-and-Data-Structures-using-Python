from Node import Node

class Queue:
	def __init__(self):
		self.head = self.tail = None

	def isEmpty(self):
		return self.head == None

	def size(self):
		tmp = self.head
		count = 0
		while tmp!= None:
			tmp = tmp.next
			count += 1
		return count

	def enqueue(self, payload):
		self.head = Node(payload, self.head)
		if self.tail == None:
			self.tail = self.head

	def dequeue(self):
		if self.isEmpty():
			return None
		else:
			payload  = self.tail.payload
			deleteMe = self.tail
			if self.head == self.tail:
				self.head = self.tail
			else:
				tmp = self.head
				while tmp.next != self.tail:
					tmp = tmp.next
				tmp.next = None
				self.tail = tmp
			deleteMe = None
			return payload