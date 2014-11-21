"""	Postfix Evaluation	"""

def postfix_eval(postfix_expr):
	token_list = postfix_expr.split()
	operand_stack = Stack()

	for token in token_list:
		if validOperand(token):
			operand_stack.push(int(token))
		else:
			op2 = operand_stack.pop()
			op1 = operand_stack.pop()
			result = do_math(token,op1,op2)
			operand_stack.push(result)
	return operand_stack.pop()

def validOperand(token):
	for t in token:
		if t not in "0123456789":
			return False
	return True

def do_math(op, op1, op2):
	if op == "^":
		return op1 **  op2
	elif op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2

from stack import  *

if __name__ == '__main__':
	from infix_to_postfix import *
	print(postfix_eval('7 8 + 3 2 + /'))
	print(postfix_eval(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )")))
	print(postfix_eval(infix_to_postfix("5 * 3 ^ ( 4 - 2 )")))
