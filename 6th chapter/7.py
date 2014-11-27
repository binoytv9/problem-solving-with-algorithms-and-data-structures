"""	Clean up the print_exp function so that it does not include an 'extra' set of parentheses around each number.	"""


import build_parse_tree

def print_exp(tree):
	str_val = ""
	if tree:
		if tree.get_root_val() in ['+','-','*','/']:
			str_val = '(' + print_exp(tree.get_left_child())
		else:
			str_val = str_val + print_exp(tree.get_left_child())

		str_val = str_val + str(tree.get_root_val())

		if tree.get_root_val() in ['+','-','*','/']:
			str_val = str_val + print_exp(tree.get_right_child()) + ')'
		else:
			str_val = str_val + print_exp(tree.get_right_child())
	return str_val


pt = build_parse_tree.build_parse_tree("(3 + (4 * 5))")
print print_exp(pt)

