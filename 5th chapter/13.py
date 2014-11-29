"""	Implement the merge_sort function without using the slice operator.	"""


def mergeSort(a_list, start=0, stop=None):
	if stop == None:
		stop = len(a_list)
	if stop - start > 1:
		mid = (start + stop) // 2
	
		mergeSort(a_list,start,mid)
		mergeSort(a_list,mid,stop)

		j = mid
		i = start
		n_list = []
		while i < mid and j < stop:
			if a_list[i] < a_list[j]:
				n_list.append(a_list[i])
				i += 1
			else:
				n_list.append(a_list[j])
				j += 1

		while i < mid :
				n_list.append(a_list[i])
				i += 1
		
		while j < stop :
				n_list.append(a_list[j])
				j += 1
		a_list[start:stop] = n_list

	
a_list = [54,26,93,17,77,31,44,55,20]
print 'before mergeSort\n\t',a_list
mergeSort(a_list)
print 'after mergeSort\n\t',a_list
