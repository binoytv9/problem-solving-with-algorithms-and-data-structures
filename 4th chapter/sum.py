def sum(lst):
	if len(lst) == 0:
		return 0
	elif len(lst) == 1:
		return lst[0]
	return lst[0] + sum(lst[1:])

print sum([1,2,3,4,5])
