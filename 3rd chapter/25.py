"""	Implement a doubly linked list, in which each node has a reference
to the next node (commonly called next) as well as a reference to the preceding node
(commonly called back). The head reference also contains two references, one to the
first node in the linked list and one to the last.	"""


class Node:
	def __init__(self,init_data):
		self.data = init_data
		self.next = None
		self.back = None

	def get_data(self):
		return self.data

	def set_data(self,new_data):
		self.data = new_data

	def get_next(self):
		return self.next

	def set_next(self,new_next):
		self.next = new_next

	def get_back(self):
		return self.back

	def set_back(self,new_back):
		self.back = new_back


class UnorderedDoublyLinkedList:
	def __init__(self):
		self.head = [None,None]
		self.length = 0

	def is_empty(self):
		return self.head == [None,None]

	def add(self,item):
		tmp = Node(item)
		self.length += 1
		if self.is_empty():
			self.head[1] = tmp
		else:
			self.head[0].set_back(tmp)
		tmp.set_next(self.head[0])
		self.head[0] = tmp

	def size(self):
		return self.length

	def search(self,item):
		current,last = self.head
		for i in range((self.size() + 1)/2):
			if (current.get_data() == item) or (last.get_data() == item):
				return True
			current = current.get_next()
			last = last.get_back()
		return False

	def remove(self,item):
		current = self.head[0]
		if self.is_empty():
			print 'linked list is empty!!!'
			return
		while current != None:
			if current.get_data() == item:
				break
			current = current.get_next()
		if current == None:
			print '%d not found' %item
			return
		self.length -= 1
		if current.get_next() == None:
			self.head[1] = current.get_back()
			self.head[1].set_next(None)
		if current.get_back() == None:
			self.head[0] = current.get_next()
			self.head[0].set_back(None)
		else:
			current.get_back().set_next(current.get_next())
			current.get_next().set_back(current.get_back())

	def append(self,item):
		tmp = Node(item)
		self.length += 1
		if self.head[1] == None:
			self.head[0] = tmp
		else:
			self.head[1].set_next(tmp)
			tmp.set_back(self.head[1])
		self.head[1] = tmp

	def __str__(self):
		string = []
		current = self.head[0]
		while current != None:
			string.append(current.get_data())
			current = current.get_next()
		return str(string)

	def index(self,item):
		i = 0
		j = self.size() - 1
		current,last = self.head
		for k in range((self.size() + 1)/2):
			if current.get_data() == item:
				return i
			if last.get_data() == item:
				return j
			i += 1
			j -= 1
			current = current.get_next()
			last = last.get_back()
		return '%d not found' %item

	def insert(self,pos,item):
		tmp = Node(item)
		if pos > self.size()-1:
			self.append(item)
			return
		self.length += 1
		index = 0
		current = self.head[0]
		while current.get_next() != None:
			if index == pos:
				break
			index += 1
			current = current.get_next()
		if current.get_back() == None:
			tmp.set_next(current)
			self.head[0] = tmp
			tmp.set_back(None)
			current.set_back(tmp)
			
		else:
			current.get_back().set_next(tmp)
			tmp.set_next(current)
			tmp.set_back(current.get_back())
			current.set_back(tmp)


	def pop(self,pos=None):
		index = 0
		self.length -= 1
		current = self.head[0]
		if current == None:
			print 'cannot pop on empty list'
			return
		if (pos == None) or (pos >= self.size()-1):
			data = self.head[1].get_data()
			self.head[1] = self.head[1].get_back()
			self.head[1].set_next(None)
			return data
			
		while current.get_next() != None:
			if (pos != None) and (pos == index):
				break
			index += 1
			current = current.get_next()

		data = current.get_data()
		if current.get_back() == None:
			self.head[0] = current.get_next()
			current.set_back(None)
		else:
			current.get_back().set_next(current.get_next())
			current.get_next().set_back(current.get_back())
		return data


class OrderedDoublyLinkedList:
	def __init__(self):
		self.head = [None,None]
		self.length = 0

	def is_empty(self):
		return self.head == [None,None]

	def add(self,item):
		tmp = Node(item)
		current = self.head[0]
		self.length += 1
		if current == None:
			self.head = [tmp,tmp]
			return
		while current.get_next() != None:
			if current.get_data() > item:
				break
			current = current.get_next()
		if (current.get_next() == None) and (current.get_data() <= item):
			self.head[1] = tmp
			current.set_next(tmp)
			tmp.set_back(current)
			return
		prev_node = current.get_back()
		if prev_node == None:
			tmp.set_next(current)
			current.set_back(tmp)
			self.head[0] = tmp
			tmp.set_back(None)
		else:
			prev_node.set_next(tmp)
			tmp.set_next(current)
			current.set_back(tmp)
			tmp.set_back(prev_node)

	def size(self):
		return self.length

	def search(self,item):
		current,last = self.head
		for i in range((self.size()+1)/2):
			cdata = current.get_data()
			ldata = last.get_data()
			if cdata == item or ldata == item:
				return True
			elif cdata > item or ldata < item:
				return False
			current = current.get_next()
			last = last.get_back()

	def remove(self,item):
		current = self.head[0]
		if current == None:
			print 'linked list empty!!!'
			return
		while current != None:
			if current.get_data() == item:
				break
			current = current.get_next()
		if current == None:
			print '%d not found'%item
			return
		self.length -= 1
		prev_node = current.get_back()
		if current.get_next() == None:
			self.head[1] = prev_node
			prev_node.set_next(current.get_next())
			return
			
		if prev_node == None:
			self.head[0] = current.get_next()
			self.head[0].set_back(None)
		else:
			prev_node.set_next(current.get_next())
			current.get_next().set_back(prev_node)

	def __str__(self):
		string = []
		current = self.head[0]
		while current != None:
			string.append(current.get_data())
			current = current.get_next()
		return str(string)

	def index(self,item):
		i = 0
		j = self.size() - 1
		current,last = self.head
		for k in range((self.size() + 1)/2):
			if current.get_data() == item:
				return i
			if last.get_data() == item:
				return j
			i += 1
			j -= 1
			current = current.get_next()
			last = last.get_back()
		return '%d not found' %item

	def pop(self,pos=None):
		index = 0
		self.length -= 1
		current = self.head[0]
		if current == None:
			print 'cannot pop on empty list'
			return
		if (pos == None) or (pos >= self.size()-1):
			data = self.head[1].get_data()
			self.head[1] = self.head[1].get_back()
			self.head[1].set_next(None)
			return data
			
		while current.get_next() != None:
			if (pos != None) and (pos == index):
				break
			index += 1
			current = current.get_next()

		data = current.get_data()
		if current.get_back() == None:
			self.head[0] = current.get_next()
			current.set_back(None)
		else:
			current.get_back().set_next(current.get_next())
			current.get_next().set_back(current.get_back())
		return data


if __name__ == '__main__':
	a = OrderedDoublyLinkedList()
	a.add(10)
	a.add(20)
	a.add(40)
	a.add(70)
	a.add(1)
	a.add(60)
	print a
	print a.size()

	a.remove(70)
	print a
	print a.size()

	a.remove(10)
	print a
	print a.size()

	print a.search(40)
	print a.index(40)

	print a.pop()
	print a
	print a.size()
