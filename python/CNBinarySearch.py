'''
Created on Aug 4, 2020

@author: charles newman
https://github.com/26point2Newms
'''

class BinarySearch(object):
	'''
	Implementation of a binary search algorithm as a class
	so we can use recursion and not need to place the 
	searched list (array) and the value we're searching for
	on the stack for each recursive call.
	'''
	def __init__(self, lst, targetVal):
		self.lst = lst
		self.targetVal = targetVal
		self.indexFound = -1

	def search(self):
		'''
		Performs a binary search on a sorted array.
		Returns the index of the item or -1 if not found
		'''
		self.__quickSearch(0, len(self.lst)-1 )
		return self.indexFound

	def __quickSearch(self, low, high):
		'''
		Recursive binary search implementation. If this was not 
		a class we would need to either make the list we searching
		and the target value we're searching for global to avoid
		placing them on the stack for each recursion.

		Arguments:
		low  : starting index to search
		high : ending index to search

		Return value:
		The index of the target value we're searching for or -1 if not
		found.
		''' 
		if (low > high):
			return -1	# we didn't find it
		mid = int((low + high)/ 2)
		if (self.targetVal == self.lst[mid]):
			self.indexFound = mid
		elif (self.targetVal < self.lst[mid]):
			self.__quickSearch(low, mid-1)
		else:
			self.__quickSearch(mid+1, high)
