"""	Write a function that takes a string as a parameter and returns a new string that is the reverse of
the old string	"""

def reverse(string):
	if len(string) <= 1:
		return string
	return reverse(string[1:]) + string[0]

print reverse('binoy')
print reverse('b')
print reverse('')
