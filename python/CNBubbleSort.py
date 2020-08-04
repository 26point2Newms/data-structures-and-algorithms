'''
Created on Aug 3, 2020

@author: charles newman
https://github.com/26point2Newms
'''

def bubbleSort(lst):
	'''
	Implementation of a bubble sort. Probably the most 
	inefficient sorting algorithm at O(n^2).

	Arguments:
	lst : An array of numbers.
	num : Number of elements to sort, may be less than 
		the number of elements in the array to sort.
	'''
	hold = 0
	passCount = 0
	switched = True
	num = len(lst)

	if num <= 0:
		return

	while (passCount < num -1 and switched == True):
		# Outer loop controls the number of passes
		switched = False    # Initially no interchanges have been made on this pass

		j = 0
		while (j < (num - passCount - 1)):
			if (lst[j] > lst[j+1]):
				# elements out of order, an interchange is necessary
				switched = True
				hold = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = hold
			j += 1
				
		passCount += 1

