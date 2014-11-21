"""	General Infix-to-Postfix Conversion	"""

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
		else:
			while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
				postfix_list.append(op_stack.pop())
			op_stack.push(token)

	while not op_stack.is_empty():
		postfix_list.append(op_stack.pop())

	return ' '.join(postfix_list)

def validOperand(token):
	for t in token:
		if t not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and t not in "0123456789":
			return False
	return True

from stack import *

if __name__ == '__main__':
	print(infix_to_postfix("A * B + C * D"))
	print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
