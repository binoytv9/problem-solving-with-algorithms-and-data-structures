"""	Implement a slice method for the UnorderedList class. It should take two parameters,
start and stop, and return a copy of the list starting at the start position and going up to
but not including the stop position	"""


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
			print 'linked list is empty!!!'
			return
		while current != None:
			if current.get_data() == item:
				break
			prev_node = current
			current = current.get_next()
		if current == None:
			print '%d not found' %item
			return
		if current.get_next() == None:
			self.lastNode = prev_node
		if prev_node == None:
			self.head = self.head.get_next()
		else:
			prev_node.set_next(current.get_next())
		self.length -= 1

	def append(self,item):
		tmp = Node(item)
		if self.lastNode == None:
			self.head = tmp
		else:
			self.lastNode.set_next(tmp)
		self.lastNode = tmp
		self.length += 1

	def __str__(self):
		string = []
		current = self.head
		while current != None:
			string.append(current.get_data())
			current = current.get_next()
		return str(string)

	def index(self,item):
		indx = 0
		current = self.head
		while current != None:
			if current.get_data() == item:
				return indx
			indx += 1
			current = current.get_next()
		return '%d not found' %item

	def insert(self,pos,item):
		tmp = Node(item)
		index = 0
		prev_node = None
		current = self.head
		while current != None:
			if index == pos:
				break
			index += 1
			prev_node = current
			current = current.get_next()
		if current == None:
			self.lastNode = prev_node
		if prev_node == None:
			tmp.set_next(self.head)
			self.head = tmp
		else:
			prev_node.set_next(tmp)
			tmp.set_next(current)
		self.length += 1

	def pop(self,pos=None):
		index = 0
		prev_node = None
		current = self.head
		if current == None:
			print 'cannot pop on empty list'
			return
		while current.get_next() != None:
			if (pos != None) and (pos == index):
				break
			index += 1
			prev_node = current
			current = current.get_next()

		if current.get_next() == None:
			self.lastNode = prev_node
		data = current.get_data()
		if prev_node == None:
			self.head = current.get_next()
		else:
			prev_node.set_next(current.get_next())
		self.length -= 1
		return data

	def slice(self,start=0,stop=None):
		index = 0
		startCopy = False
		current = self.head
		newlist = UnorderedList()
		while current != None:
			if index == start:
				startCopy = True
			if index == stop:
				break
			if startCopy:
				newlist.append(current.get_data())
			index += 1
			current = current.get_next()
		return newlist


if __name__ == '__main__':
	mylist = UnorderedList()
	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)
	print mylist
	print mylist.slice(1,100)
