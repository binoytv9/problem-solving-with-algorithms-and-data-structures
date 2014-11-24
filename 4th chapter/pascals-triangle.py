"""	Write a program that prints out Pascal's triangle. Your program should accept a parameter
that tells how many rows of the triangle to print	"""


def pascalTri(n,row=0):
        if row == n:
                return
        print ' '*(n-1-row),aNr(row,0)
        pascalTri(n,row+1)

def aNr(row,col):
        if row < col:
                return '\n'
        anr = fact(row)/(fact(row-col)*fact(col))
        return str(anr) + ' ' + aNr(row,col+1)

def fact(n):
        if n <= 0:
                return 1
        return n * fact(n-1)

n = raw_input('enter no of rows : ')
pascalTri(int(n))
