"""	Implement the Queue ADT, using a list such that the rear of the queue is at the end of the
list	"""


class Queue:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def enqueue(self,item):
		self.items.append(item)
	def dequeue(self):
		self.items.pop(0)
	def size(self):
		return len(self.items)
