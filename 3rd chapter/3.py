"""	Implement a direct infix evaluator that combines the functionality of infix-to-postfix con-
*	version and the postfix evaluation algorithm. Your evaluator should process infix tokens
*	from left to right and use two stacks, one for operators and one for operands, to perform
*	the evaluation	
"""

def direct_infix_eval(infix_expr):
	prec = {}
	prec['^'] = 4
	prec['*'] = 3
	prec['/'] = 3
	prec['+'] = 2
	prec['-'] = 2
	prec['('] = 1

	operand_stack = Stack()
	operator_stack = Stack()

	token_list = infix_expr.split()

	for token in token_list:
		if validOperand(token):
			operand_stack.push(token)
		elif token == '(':
			operator_stack.push(token)
		elif token == ')':
			top_token = operator_stack.peek()
			while top_token != '(':
				do_math(operator_stack.pop(),operand_stack)
				top_token = operator_stack.pop()
		else:
			while (not operator_stack.is_empty()) and (prec[operator_stack.peek()] >= prec[token]):
				do_math(operator_stack.pop(),operand_stack)
			operator_stack.push(token)

	while not operator_stack.is_empty():
		do_math(operator_stack.pop(),operand_stack)

	return operand_stack.pop()

def validOperand(operand):
	for i in operand:
		if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and i not in "0123456789":
			return False
	return True

def do_math(operator,operand_stack):
	op2 = int(operand_stack.pop())
	op1 = int(operand_stack.pop())
	
	if operator == "^":
		result = op1 **  op2
	elif operator == "*":
		result = op1 * op2
	elif operator == "/":
		result = op1 / op2
	elif operator == "+":
		result = op1 + op2
	else:
		result = op1 - op2

	operand_stack.push(result)

from stack import *

if __name__ == '__main__':
	print direct_infix_eval("5 * 3 ^ ( 4 - 2 )")
	print direct_infix_eval("10 + 3 * 5 / ( 16 - 4 )")
