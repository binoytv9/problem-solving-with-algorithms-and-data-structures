"""	Implement the binary search using recursion without the slice operator.	"""

def binary_search(a_list, item,start=0, stop=None):
	if stop == None:
		stop = len(a_list)
	if stop-start == 0:
		return False
	else:
		midpoint = (start + stop) // 2
	print a_list[midpoint]
	if a_list[midpoint] == item:
		return True
	else:
		if item < a_list[midpoint]:
			return binary_search(a_list, item,start,midpoint)
		else:
			return binary_search(a_list, item,midpoint+1,stop)


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
print(binary_search(test_list, 19))
