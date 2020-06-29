'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''
from CNStack import Stack

class Queue(Stack):
	'''
	Implementation of a FIFO (First In, First Out) Queue.
	Inherits from Stack (CNStack.py).
	'''
	def pop(self):
		raise NotImplementedError
	
	def push(self, item):
		raise NotImplementedError
	
	def insert(self, item):
		'''
		Insert an item at the end of the queue.
		'''
		self.items.append(item)
	
	def remove(self):
		'''
		Remove the item at the front of the queue.
		'''
		item = None
		if len(self.items) > 0:
			item = self.items.pop(0)
		return item

	def peek(self):
		'''
		Returns the item at the front of the queue without removing it.
		'''
		item = None
		queueSize = len(self.items)
		if queueSize > 0:
			item = self.items[0]
		return item
	