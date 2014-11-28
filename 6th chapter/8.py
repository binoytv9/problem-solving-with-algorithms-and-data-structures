"""	Using the build_heap method, write a sorting function that can sort a list in O(n log n) time.	"""


import BinHeap

def sort_using_binary_heap(a_list):
	s_list = []
	bh = BinHeap.BinHeap()
	bh.build_heap(a_list)
	while len(bh.heap_list) > 1:
		s_list.append(bh.del_min())
	return s_list


a_list = [3,6,1,2,9,7]
print sort_using_binary_heap(a_list)
