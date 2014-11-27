"""	Modify the build_parse_tree and evaluate functions to handle boolean statements (and, or, and not).	"""


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
		elif i == ')':
			current_tree = p_stack.pop()
		elif i in ['False', 'True']:
			current_tree.set_root_val(i == 'True')
			parent = p_stack.pop()
			current_tree = parent
		elif i not in ['and', 'or', 'not']:
			current_tree.set_root_val(int(i))
			parent = p_stack.pop()
			current_tree = parent
		elif i in ['and', 'or', 'not']:
			if  i == 'not':
				current_tree = p_stack.pop()
			current_tree.set_root_val(i)
			current_tree.insert_right('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_right_child()
		else:
			raise ValueError
	return e_tree

def evaluate(parse_tree):
	left = parse_tree.get_left_child()
	right = parse_tree.get_right_child()
	if left and right:
		fn = parse_tree.get_root_val()
		if fn == 'not':
			return not evaluate(right)
		elif fn == 'and':
			return evaluate(left) and evaluate(right)
		else:
			return evaluate(left) or evaluate(right)
	else:
		return parse_tree.get_root_val()

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
			
				

print evaluate(build_parse_tree("(not 3)"))
print evaluate(build_parse_tree("(not False)"))
