'''
Created on Aug 3, 2020

@author: charles newman
https://github.com/26point2Newms
'''

class TreeNode(object):
	'''
	Node class to support a Binary Tree data structure
	'''
	def __init__(self, info, parent=None):
		'''
		Constructor
		'''
		self.info = info
		self.left = None
		self.right = None
		self.parent = parent
	