class Stack:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def size(self):
		return len(self.items)

def rev_string(my_str):
	m = Stack()
	rev_str = []
	for char in my_str:
		m.push(char)
	while not m.is_empty():
		rev_str.append(m.pop())
	return ''.join(rev_str)


if __name__ == '__main__':
	print rev_string('binoy')
