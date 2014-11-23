"""	Implement a queue using linked lists	"""


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

class LinkedList:
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
			print 'linked list is empty!!!' %item
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
		self.length += 1
		prev_node = None
		current = self.head
		if current == None:
			self.head = self.lastNode = tmp
			return
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


class Deque:
	def __init__(self):
		self.mylist = LinkedList()

	def is_empty(self):
		return self.mylist.head == None

	def add_front(self,item):
		self.mylist.append(item)

	def add_rear(self,item):
		self.mylist.insert(0,item)

	def remove_front(self):
		return self.mylist.pop()

	def remove_rear(self):
		return self.mylist.pop(0)

	def size(self):
		return self.mylist.size()


if __name__ == '__main__':
	d = Deque()
	print d.is_empty()
	d.add_rear(4)
	d.add_rear('dog')
	d.add_front('cat')
	d.add_front(True)
	print d.size()
	print d.is_empty()
	d.add_rear(8.4)
	print d.remove_rear()
	print d.remove_front()
