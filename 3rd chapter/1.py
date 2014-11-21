"""	Modify the infix-to-postfix algorithm so that it can handle errors.	"""


def infix_to_postfix(infix_expr):
	prec = {}
	prec['^'] = 4
	prec['*'] = 3
	prec['/'] = 3
	prec['+'] = 2
	prec['-'] = 2
	prec['('] = 1

	op_stack = Stack()
	postfix_list = []
	token_list = infix_expr.split()

	for token in token_list:
		if validOperand(token):
			postfix_list.append(token)
		elif token == '(':
			op_stack.push(token)
		elif token == ')':
			top_token = op_stack.pop()
			while top_token != '(':
				postfix_list.append(top_token)
				top_token = op_stack.pop()
		elif validOperator(token):
			while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
				postfix_list.append(op_stack.pop())
			op_stack.push(token)
		else:
			print 'Invalid operator/operand : %s' %(token)
			print 'Exiting... \n'
			sys.exit(1)

	while not op_stack.is_empty():
		postfix_list.append(op_stack.pop())

	return ' '.join(postfix_list)


def validOperator(token):
	if token not in '(-+/*^':
			return False
	return True

def validOperand(token):
	for t in token:
		if t not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and t not in "0123456789":
			return False
	return True

from stack import *
import sys

if __name__ == '__main__':
	print(infix_to_postfix("A * B + C * D"))
	print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
