'''
Created on Jun 25, 2020

@author: charles newman
https://github.com/26point2Newms
'''

class Stack:
	'''
	Implementation of a LIFO (Last In, First Out Stack in python 3.
	'''
	def __init__(self):
		'''
		Constructor
		'''
		self.items = []
		
	def push(self, item):
		'''
		Push an item onto the top of the stack.
		'''
		self.items.append(item)

	def pop(self):
		'''
		Pop the top-most item off the stack (also removes it from the stack).
		'''
		item = None
		if len(self.items) > 0:
			item = self.items.pop()
		return item

	def count(self):
		'''
		Returns the number of items in the stack.
		'''
		return len(self.items)

	def peek(self):
		'''
		Returns the top-most item from the stack without removing it.
		'''
		item = None
		stackSize = len(self.items)
		if stackSize > 0:
			item = self.items[stackSize - 1]
		return item
