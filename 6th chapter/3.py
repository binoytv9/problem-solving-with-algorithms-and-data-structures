"""	Using the find_successor method, write a non-recursive inorder traversal for a binary search tree	"""

import BinarySearchTree

def inorder_using_find_successor(tree):
	current = tree.root.find_min()
	while current != None:
		print '%d : %s' %(current.key,current.payload)
		current = current.find_successor()


my_tree = BinarySearchTree.BinarySearchTree()
my_tree[3] = "red"
my_tree[4] = "blue"
my_tree[6] = "yellow"
my_tree[2] = "at"

inorder_using_find_successor(my_tree)
