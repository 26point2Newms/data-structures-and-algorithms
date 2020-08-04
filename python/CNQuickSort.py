'''
Created on Aug 3, 2020

@author: charles newman
https://github.com/26point2Newms
'''

def sort(lst):
	__quick(lst, 0, len(lst) - 1)

def __quick(lst, lb, ub):
	'''
	Recursive sort method.

	Arguments:
	lst : the list or array to sort
	lb	: the lower bound of the partition to sort
	ub	: the upper bound of the partition to sort
	'''

	if (lb >= ub):
		return
	
	pIndex = __partition(lst, lb, ub)

	__quick(lst, lb, pIndex - 1)

	__quick(lst, pIndex + 1, ub)

def __partition(lst, lb, ub):
	'''
	This function uses a pivot value, can be the lower bound,
	or the upper bound (see comments below). It places the 
	pivot value at its correct position in the sorted list by
	placing all values smaller than the pivot value to the
	left of the pivot value and all values greatter than the 
	pivot value to the right of the pivot value.

	Arguments:
	lst : the list or array to partition
	lb	: the lower bound of the partition
	ub	: the upper bound of the partition

	Returns:
	The partitioning index to use on subsequent calls
	'''
	# This is the pivot value, an area where we can experiment, such 
	#	as using the median of lst[lb], lst[ub], and the middle, lst[(lb+ub)/2].
	#	Or we can use lst[lb] or lst[up]
	# Pick one and comment the other one out.
	# pivot = lst[lb]	# Using the lower bound as the pivot
	pivot = lst[ub]	# Using the upper bound as the pivot
	
	i = lb - 1	# this is index of the smaller element

	for j in range(lb, ub):
		# Is the current element smaller or equal to the the pivot?
		if lst[j] <= pivot:
			# Increment the index of the smaller element
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
	lst[i+1], lst[ub] = lst[ub], lst[i+1]
	return (i + 1)

