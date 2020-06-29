'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''

class Node(object):
	'''
	Node class to support a Linked List and a Doubly Linked List
	'''

	def __init__(self, info, nextNode=None):
		'''
		Constructor
		'''
		self.info = info
		self.next = nextNode
		self.prev = None
