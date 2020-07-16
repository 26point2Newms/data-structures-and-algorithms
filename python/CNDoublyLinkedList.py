'''
Created on Jun 29, 2020

@author: charles newman
https://github.com/26point2Newms
'''

from CNNode import Node
from CNLinkedList import LinkedList

class DoublyLinkedList(LinkedList):
	'''
	Implementation of a Doubly Linked List (inherits from LinkedList)
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self.tail = None
		LinkedList.__init__(self)
		
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
			newNode.prev = currentNode
			self.tail = newNode

	def insertFront(self, newNode):
		'''
		Inserts a new node at the front (head) of the list.
		'''
		if (self.head == None):
			self.head = newNode
		else:
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode
	
	def remove(self, node):
		'''
		Removes the specified node from the list and updates the next and previous pointers.
		'''
		if (node == self.tail):
			self.tail = node.prev
			self.tail.next = None
		elif (node == self.head):
			self.head = node.next
			self.head.prev = None
		else:
			currentNode = self.head
			prevNode = None
				
			while (currentNode != None):
				if (node == currentNode):
					break
				prevNode = currentNode
				currentNode = currentNode.next
		
			prevNode.next = node.next
			node.next.prev = prevNode
			
		node.next = None
		node.prev = None
