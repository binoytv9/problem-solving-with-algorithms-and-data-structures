"""	Write a program that prints out Pascal's triangle. Your program should accept a parameter
that tells how many rows of the triangle to print	"""


def pascalTri(n,row=0,col = 0):
	if row == n-1:
		return
	if row > col:
		return '\n'
	aNr = fact(row)/(fact(row-col)*fact(col))
	print aNr,' ',pascalTri(n,row,col+1)
	pascalTri(n,row+1)

def fact(n):
	if n <= 0:
		return 1
	return n * fact(n-1)

print pascalTri(5)
