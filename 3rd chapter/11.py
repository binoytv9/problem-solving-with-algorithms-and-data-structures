"""	Write a program that can check an HTML document for proper opening and closing
tags	"""

import re
from stack import *

def htmlTagCheck(htmlContent):
	tagList = re.findall(r'<(/?)(\w+)>',htmlContent)
	tag_stack = Stack()
	for tag in tagList:
		if tag[0] == '':
			tag_stack.push(tag)
		else: # tag[0] == '/'
			if tag_stack.is_empty():
				return  False
			else:
				top_tag = tag_stack.pop()
				if top_tag[1] != tag[1]:
					return  False
	return True



html = """
<html>
	<head>
		<title>
			Example
		</title>
	</head>
	<body>
		<h1>Hello, world</h1>
	</body>
</html>
"""
print htmlTagCheck(html)
