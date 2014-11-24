"""	Write a program that prints out Pascal's triangle. Your program should accept a parameter
that tells how many rows of the triangle to print	"""


def pascalTri(n,row=0):
	if row == n:
		return
	print ' ' * (n-row-1),val(row,0)
	pascalTri(n,row+1)

def val(r,c):
	if r < c:
		return ''
	key = str(r)+str(c)
	if key not in d:
		k1 = str(r-1)+str(c)
		k2 = str(r-1)+str(c-1)
		d[key] = d.get(k1,0) + d.get(k2,0)
	return str(d[key]) + ' ' + val(r,c+1)

d = {}
d['00'] = 1
n = raw_input('enter no of rows : ')
pascalTri(int(n))
