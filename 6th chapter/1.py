"""	Extend the build_parse_tree function to handle mathematical expressions that do not have spaces between every character.	"""

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
			current_tree.set_root_val(int(i))
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

def evaluate(parse_tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul,'/':operator.truediv}
	left = parse_tree.get_left_child()
	right = parse_tree.get_right_child()
	if left and right:
		fn = opers[parse_tree.get_root_val()]
		return fn(evaluate(left),evaluate(right))
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
				ele = expr[index]
			stop = index
			exprList.append(expr[start:stop])
			index -= 1
		else:
			exprList.append(ele)
		index += 1
	return  exprList
			
				
if __name__ == '__main__':
	pt = build_parse_tree("((10+5)*3)")
	print evaluate(pt)
	pt = build_parse_tree("(3 + (4 * 5))")
	print evaluate(pt)
