
from Node import Node

class Stack:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def size(self):
		tmp = self.head
		count = 0
		while tmp != None:
			tmp = tmp.next
			count += 1
		return count

	def push(self, payload):
		self.head = Node(payload, self.head)

	def pop(self):
		if self.isEmpty():
			return None
		else:
			payload = self.head.payload
			deleteMe = self.head
			if self.head.next == None:
				self.head = None
			else:
				self.head = self.head.next
			deleteMe = None
			return payload
