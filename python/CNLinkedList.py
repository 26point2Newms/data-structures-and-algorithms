'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''
from CNNode import Node

class LinkedList(object):
	'''
	Implementation of a Linked List.
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self.head = None
	
	def insertInfo(self, info):
		'''
		Takes the info, creates a node, and inserts at the end of the list.
		'''
		newNode = Node(info)
		self.insert(newNode)

	def insert(self, newNode):
		'''
		Inserts a new node at the end of the list.
		'''
		if (self.head == None):
			self.head = newNode
		else:
			currentNode = self.head
			while (currentNode.next != None):
				currentNode = currentNode.next
			currentNode.next = newNode
			
	def remove(self, node):
		'''
		Removes the specified node from the list and updates the next pointer.
		'''
		if (node == self.head):
			self.head = node.next
		else:
			currentNode = self.head
			prevNode = None
					
			while (currentNode != None):
				if (node == currentNode):
					break
				prevNode = currentNode
				currentNode = currentNode.next
			
			prevNode.next = node.next
			
		node.next = None
		
