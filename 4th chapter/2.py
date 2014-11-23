"""	Write a recursive function to reverse a list	"""

def reverse(lst):
	if lst == []:
		return lst
	if len(lst) == 1:
		return [lst[0]]
	return reverse(lst[1:]) + [lst[0]]

print reverse([1,2,3,4,5])
print reverse([])
