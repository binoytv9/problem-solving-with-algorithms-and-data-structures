"""	Implement the __str__ method in the UnorderedList class. What would be a good string
representation for a list	"""


class Node:
	def __init__(self,init_data):
		self.data = init_data
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self,new_data):
		self.data = new_data

	def set_next(self,new_next):
		self.next = new_next

class UnorderedList:
	def __init__(self):
		self.head = None
		self.lastNode = None
		self.length = 0

	def is_empty(self):
		return self.head == None

	def add(self,item):
		tmp = Node(item)
		if self.is_empty():
			self.lastNode = tmp
		tmp.set_next(self.head)
		self.head = tmp
		self.length += 1

	def size(self):
		return self.length

	def search(self,item):
		current = self.head
		while current != None:
			if current.get_data() == item:
				return True
			current = current.get_next()
		return False

	def remove(self,item):
		current = self.head
		prev_node = None
		if current == None:
			print '%d not found' %item
			return
		while current != None:
			if current.get_data() == item:
				break
			prev_node = current
			current = current.get_next()
		if current.get_next() == None:
			self.lastNode = prev_node
		if prev_node == None:
			self.head = self.head.get_next()
		else:
			prev_node.set_next(current.get_next())
		self.length -= 1

	def append(self,item):
		tmp = Node(item)
		self.lastNode.set_next(tmp)
		self.lastNode = tmp
		self.length += 1

	def __str__(self):
		string = ''
		current = self.head
		while current != None:
			string += '%d --> '%current.get_data()
			current = current.get_next()
		string += 'None'
		return string


if __name__ == '__main__':
	mylist = UnorderedList()
	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)
	print mylist.size()
	print mylist.lastNode.get_data()
	mylist.remove(31)
	print mylist.search(31)
	mylist.append(30)
	print mylist.size()
	print mylist.lastNode.get_data()
	print mylist
