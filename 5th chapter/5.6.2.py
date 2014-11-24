"""	Modify the hash function for strings to use positional weightings	"""


def hash(a_string, table_size):
	sum = 0
	for pos in range(len(a_string)-1,-1,-1):
		sum = sum + ord(a_string[pos]) * 10 ** pos
	print sum
	return sum % table_size

print hash('binoy', 10)
print hash('yonib', 10)
