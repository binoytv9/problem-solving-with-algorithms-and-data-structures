"""	Turn your direct infix evaluator from the previous problem into a calculator	"""

from stack import *

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

	token_list = splitExpr(infix_expr)

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

def splitExpr(expr):
	index = 0
	exprList = []
	while index < len(expr):
		ele = expr[index]
		if ele == ' ':
			pass
		elif ele.isdigit():
			start = index
			stop = None
			while ele.isdigit():
				index += 1
				if index < len(expr):
					ele = expr[index]
				else:
					ele = 'st0p'
			stop = index
			exprList.append(expr[start:stop])
			index -= 1
		else:
			exprList.append(ele)
		index += 1
	return  exprList

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

def calculator():
	print '\t\tCALCULATOR'
	print '\t    =================='
	while True:
		expr = raw_input('>>> ')
		if expr == 'Q' or expr =='q':
			print '\n\tquiting calculator...Good bye\n\n'
			break
		try :
			print direct_infix_eval(expr)
		except :
			print 'input expression and press <ENTER> to see output'
			print "input 'Q' or 'q' and hit <ENTER> to quit\n\n"

if __name__ == '__main__':
	calculator()
