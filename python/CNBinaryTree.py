'''
Created on Aug 3, 2020

@author: charles newman
https://github.com/26point2Newms
'''

from CNTreeNode import TreeNode

class BinaryTree(object):
	'''
	Implementation of a binary tree data structure.
	'''

	def __init__(self, info=None):
		'''
		Constructor

		Arguments:
		info (optional) : the first data or info item to be added to 
				the new tree, this becomes the data of the
				root node of the tree.
		'''
		self.root = None
		self.size = 0

		if info != None:
			self.root = TreeNode(info)
			self.size = 1
		
	def insert(self, info):
		'''
		Inserts info into the tree. 

		Arguments:
		info : the data or info item we will use to create a
				new node and insert it into its proper place
				in the tree.
		'''
		if self.root != None:
			self.__insert(info, self.root)
		else:
			self.root = TreeNode(info)
		self.size += 1

	def __insert(self, info, currentNode):
		'''
		Recursive method to insert a new node into 
		the tree containing the info supplied.

		Arguments:
		info : the data or info item we will use to create a
				new node and insert it into its proper place
				in the tree.
		'''
		if info < currentNode.info:
			if currentNode.left != None:
				self.__insert(info, currentNode.left)
			else:
				currentNode.left = TreeNode(info, currentNode)
		else:
			if currentNode.right != None:
				self.__insert(info, currentNode.right)
			else:
				currentNode.right = TreeNode(info, currentNode)

	def find(self, info, currentNode=None):
		'''
		Recursive method to find a specific node in the tree.

		Arguments:
		info : the data or info item we are looking for.
		'''
		foundNode = None
		returnVal = None

		if self.root != None:
			foundNode = self.__find(info, self.root)

		if foundNode != None:
			returnVal = foundNode.info

		return returnVal

	def __find(self, info, currentNode):
		if currentNode == None or currentNode.info == info:
			return currentNode
		elif info < currentNode.info:
			return self.__find(info, currentNode.left)
		else:
			return self.__find(info, currentNode.right)

	def traverse(self, callback):
		'''
		Traverses the tree in ascending order and calls
		the callback function for each node.
		For example, if you inserted random numbers into
		the tree, the callback function will be called in
		ascending order. If you were to print the info in
		the callback you would see a sorted list.

		Arguments:
		callback : A function that is called back on each
			node's value for every node in the tree.
		'''
		self.__traverse(self.root, callback)

	def __traverse(self, node, callback):
		if node == None:
			return
		self.__traverse(node.left, callback)
		callback(node.info)
		self.__traverse(node.right, callback)



