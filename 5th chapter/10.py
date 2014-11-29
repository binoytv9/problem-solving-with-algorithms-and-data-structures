"""	A bubble sort can be modified to "bubble" in both directions. The first pass moves
"up" the list, and the second pass moves "down." This alternating pattern continues
until no more passes are necessary.	"""


def bubble_up_down(a_list):
	k=1
	stop = False
	forward = True
	while k <= len(a_list) and  not stop:
		stop = True
		if forward:
			print 'forward pass'
			i = k/2
			while i < (len(a_list) - (k/2 + 1)):
				if a_list[i] > a_list[i+1]:
					a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
					stop = False
				i += 1
			forward = False
		else:
			print 'backward pass'
			j = i-1
			while j > k/2 - 1:
				if a_list[j] < a_list[j-1]:
					a_list[j],a_list[j-1] = a_list[j-1],a_list[j]
					stop = False
				j -= 1
			forward = True
		k += 1
		print a_list
	print '\n\nsorted list is...\n\t',
	print a_list,'\n\n'


a_list = [54,26,93,17,77,31,44,55,20]

print '\n\noriginal list is...\n\t',
print a_list,'\n\n'

bubble_up_down(a_list)
