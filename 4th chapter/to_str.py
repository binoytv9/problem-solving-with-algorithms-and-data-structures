def to_str(n,base):
	convert_str = '0123456789ABCDEF'
	if n < base:
		return convert_str[n]
	return to_str(n/base,base) + convert_str[n%base]

print to_str(123,10)
print to_str(123,16)
print to_str(123,8)
print to_str(123,2)
