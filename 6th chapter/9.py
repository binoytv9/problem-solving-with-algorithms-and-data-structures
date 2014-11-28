"""	Write a function that takes a parse tree for a mathematical expression and calculates the
derivative of the expression with respect to some variable.	"""


import operator
from stack import *
from binary_tree import *

def build_parse_tree(fp_exp):
	fp_list = splitExpr(fp_exp)
	p_stack = Stack()
	e_tree = BinaryTree('')
	p_stack.push(e_tree)
	current_tree = e_tree
	for i in fp_list:
		if i == '(':
			current_tree.insert_left('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_left_child()
		elif i not in ['+', '-', '*', '/', ')']:
			if type(i) == int:
				current_tree.set_root_val(int(i))
			else:
				current_tree.set_root_val(i)
			parent = p_stack.pop()
			current_tree = parent
		elif i in ['+', '-', '*', '/']:
			current_tree.set_root_val(i)
			current_tree.insert_right('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_right_child()
		elif i == ')':
			current_tree = p_stack.pop()
		else:
			raise ValueError
	return e_tree

def return_exp(tree):
	str_val = ""
	if tree:
		if tree.get_root_val() in ['+','-','*','/']:
			str_val = '(' + return_exp(tree.get_left_child())
		else:
			str_val = str_val + return_exp(tree.get_left_child())

		str_val = str_val + str(tree.get_root_val())

		if tree.get_root_val() in ['+','-','*','/']:
			str_val = str_val + return_exp(tree.get_right_child()) + ')'
		else:
			str_val = str_val + return_exp(tree.get_right_child())
	return str_val

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
		elif ele.isalpha():
			start = index
			stop = None
			while ele.isalpha():
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
			
				
if __name__ == '__main__':
	pt = build_parse_tree("(x + (2*y))")
	expr = return_exp(pt)
	print expr
