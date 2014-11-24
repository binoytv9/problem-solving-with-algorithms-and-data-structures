"""	We used a hash function for strings that weighted the characters by position. Devise an
alternative weighting scheme.	"""


def hash(a_string,table_size):
	sum = 1
	pos = 0
	l = len(a_string)
	while pos < l:
		sum += ord(a_string[pos%l]) * ord(a_string[(pos+1)%l]) * 10 ** pos
		pos += 1
	print sum
	return sum % table_size

print hash('binoy', 10)
print hash('yonib', 10)
