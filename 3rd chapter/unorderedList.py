"""	The Unordered List Abstract Data Type	"""


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
	def is_empty(self):
		return self.head == None
	def add(self,item):
		tmp = Node(item)
		tmp.set_next(self.head)
		self.head = tmp
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
			if current.get_data() == item:
				return True
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

if __name__ == '__main__':
	temp = Node(93)
	print temp.get_data()
	mylist = UnorderedList()
	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)
	print mylist.search(17)
	mylist.remove(17)
	print mylist.search(17)
	print mylist.size()
