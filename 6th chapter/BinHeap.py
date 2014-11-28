"""	Binary Heap Implementation	"""


class BinHeap:
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0

	def insert(self, k):
		self.heap_list.append(k)
		self.current_size = self.current_size + 1
		self.perc_up(self.current_size)

	def perc_up(self, i):
		while i // 2 > 0:
			if self.heap_list[i] < self.heap_list[i // 2]:
				tmp = self.heap_list[i // 2]
				self.heap_list[i // 2] = self.heap_list[i]
				self.heap_list[i] = tmp
			i = i // 2

	def del_min(self):
		ret_val = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size = self.current_size - 1
		self.heap_list.pop()
		self.perc_down(1)
		return ret_val

	def perc_down(self, i):
		while (i * 2) <= self.current_size:
			mc = self.min_child(i)
			if self.heap_list[i] > self.heap_list[mc]:
				tmp = self.heap_list[i]
				self.heap_list[i] = self.heap_list[mc]
				self.heap_list[mc] = tmp
			i = mc

	def min_child(self, i):
		if i * 2 + 1 > self.current_size:
			return i * 2
		else:
			if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def build_heap(self, a_list):
		i = len(a_list) // 2
		self.current_size = len(a_list)
		self.heap_list = [0] + a_list[:]
		while (i > 0):
			self.perc_down(i)
			i = i - 1


if __name__ == '__main__':
	bh = BinHeap()
	bh.insert(5)
	bh.insert(7)
	bh.insert(3)
	bh.insert(11)
	print(bh.del_min())
	print(bh.del_min())
	print(bh.del_min())
	print(bh.del_min())
