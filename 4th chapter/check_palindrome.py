def check_palindrome(string):
	if len(string) <= 1:
		return True
	return string[0] == string[-1] and check_palindrome(string[1:-1])


string = 'Reviled did I live, said I, as evil I did deliver'
s = ''.join(i.lower() for i in string if i.isalpha())
print check_palindrome(s)
