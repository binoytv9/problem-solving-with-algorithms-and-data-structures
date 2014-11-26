"""	Implement the median-of-three method for selecting a pivot value as a modification to quick_sort .	"""


def quick_sort(a_list):
	quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
	if first < last:
		split_point = partition(a_list, first, last)
		quick_sort_helper(a_list, first, split_point - 1)
		quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
	mid = (first+last) // 2
	pivot_value,median = return_median(a_list,first,mid,last)

	a_list[first],a_list[median] = a_list[median],a_list[first]
	left_mark = first + 1
	right_mark = last
	done = False
	while not done:
		while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
			left_mark = left_mark + 1
		while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
			right_mark = right_mark - 1
		if right_mark < left_mark:
			done = True
		else:
			a_list[left_mark],a_list[right_mark] =	a_list[right_mark],a_list[left_mark]

	a_list[first],a_list[right_mark] = a_list[right_mark],a_list[first]

	return right_mark

def return_median(lst,a,b,c):
	if (lst[a] >= lst[b] and lst[a] <= lst[c]) or (lst[a] <= lst[b] and lst[a] >= lst[c]):
		return lst[a],a
	elif (lst[b] >= lst[a] and lst[b] <= lst[c]) or (lst[b] <= lst[a] and lst[b] >= lst[c]):
		return lst[b],b
	else:
		return lst[c],c


if __name__ == '__main__':
	a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(a_list)
	print(a_list)
