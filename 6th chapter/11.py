"""	Using the BinaryHeap class, implement a new class called PriorityQueue . Your
PriorityQueue class should implement the constructor, plus the enqueue and
dequeue methods.	"""



import BinHeap

class PriorityQueue:
	def __init__(self):
		self.bh = BinHeap.BinHeap()

	def enqueue(self,item):
		self.bh.insert(item)

	def dequeue(self):
		self.bh.del_min()

	def __str__(self):
		return str(self.bh.heap_list)

if __name__ == '__main__':
	pq = PriorityQueue()
	pq.enqueue(5)
	pq.enqueue(7)
	pq.enqueue(3)
	pq.enqueue(1)
	pq.enqueue(11)
	pq.enqueue(10)

	print pq
	pq.dequeue()
	print pq
	pq.dequeue()
	print pq
	pq.dequeue()
	print pq
