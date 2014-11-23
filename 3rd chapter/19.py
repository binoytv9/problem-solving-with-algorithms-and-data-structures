"""	Implement the remaining operations defined in the OrderedList ADT	"""


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

class OrderedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def add(self,item):
		tmp = Node(item)
		prev_node = None
		current = self.head
		if current == None:
			self.head = tmp
			return
		while current != None:
			if current.get_data() > item:
				break
			prev_node = current
			current = current.get_next()
		if prev_node == None:
			tmp.set_next(current)
			self.head = tmp
		else:
			tmp.set_next(current)
			prev_node.set_next(tmp)

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.get_next()
		return count

	def search(self,item):
		current = self.head
		while current != None:
			data = current.get_data()
			if data == item:
				return True
			elif data > item:
				return False
			current = current.get_next()
		return False

	def remove(self,item):
		current = self.head
		prev_node = None
		while current != None:
			if current.get_data() == item:
				break
			prev_node = current
			current = current.get_next()
		if prev_node == None:
			self.head = self.head.get_next()
		else:
			prev_node.set_next(current.get_next())

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
			data = current.get_data()
			if data == item:
				return indx
			elif data > item:
				return '%d not found' %item
			indx += 1
			current = current.get_next()
		return '%d not found' %item

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

		data = current.get_data()
		if prev_node == None:
			self.head = current.get_next()
		else:
			prev_node.set_next(current.get_next())
		return data

if __name__ == '__main__':
	mylist = OrderedList()
	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)
	print mylist
	print mylist.search(17)
	mylist.remove(17)
	print mylist.search(17)
	print mylist
