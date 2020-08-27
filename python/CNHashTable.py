'''
Created on Aug 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''

from CNNode import Node
from CNLinkedList import LinkedList
from hashlib import md5

import logging

class Bucket(object):
	'''
	A Bucket for the hash table. Each bucket will contain the original key and value.
	We need to store the original (un-hashed) key to support hash table collisions.
	'''
	def __init__(self, key, value):
		self.key = key	# The un-hashed key
		self.value = value

class HashTable(object):
	'''
	Implementation of a hash table with a fixed size (capacity) that deals
	with key collisions using chaining (a linked list).
	'''

	DEFAULT_CAPACITY = 32

	def __init__(self, capacity = DEFAULT_CAPACITY):
		'''
		The constructor
		'''
		self.capacity = capacity
		self.hashTable = []

		# Each item in the list is a linked list to support hash key collisions
		for _ in range(0, self.capacity):
			self.hashTable.append(LinkedList())

	def hash(self, key):
		'''
		This method creates a unique (hopefully) number from the key, which
		can be any data type. Hasing by it's very nature has the potential to 
		create collisions, meaning two or more different keys can generate the same hash value.
		The capacity of the hash table and the hashing algorithm go a long way to avoid
		collisions. In this case, we'll use the md5 hash from the python hashlib 
		since the builtin __hash__() function in python will create a different 
		hash for a different process, which would be a problem if you wanted to
		persist the table or use this function across different processes.
		'''
		numKey = 0

		# Generate a hexidecimal version of the key (such as 736b831877d84f827ca24ceba37a6697)
		hexKey = md5(str(key).encode('utf-8')).hexdigest()

		# Now convert each character into an integer
		for c in list(hexKey):
			numKey += ord(c)

		# Now use modulo to ensure our numeric key is within our capacity
		return numKey % self.capacity
		

	def set(self, key, value):
		'''
		Takes the key, value pair and adds it to the hash table. To support collisions,
		each entry (or bucket) in the hash table is a linked list and we'll store
		the original key with the value so we can distinquish between key collisions and
		unique value updates for a key we've already added.
		'''

		# Create the hash key and get the linked list at that location
		keyHash = self.hash(key)
		linkedList = self.hashTable[keyHash]

		# First we need to see if the key, value pair is there and update if so
		#	Note we store the original (un-hashed) key along with the value so
		#	we can determine which is which if we have a hash key collision
		currentNode = linkedList.head
		while (currentNode != None):
			bucket = currentNode.info
			if bucket.key == key:
				# This is an update
				bucket.value = value
				currentNode.info = bucket
				break
			currentNode = currentNode.next

		# Otherwise, insert the (original un-hashed) key, value pair into the linked list
		if currentNode == None:
			linkedList.insert(Node(Bucket(key, value)))

	def get(self, key):
		'''
		Returns the value associated with the key or None if not found.
		'''

		returnVal = None

		# Generate the hash key from the supplied key and get the linked list at 
		#	that location
		keyHash = self.hash(key)
		linkedList = self.hashTable[keyHash]

		# Iterate over the linked list and look for the node with the original key
		currentNode = linkedList.head
		while (currentNode != None):
			bucket = currentNode.info
			if bucket.key == key:
				returnVal = bucket.value
				break
			currentNode = currentNode.next

		return returnVal

	def remove(self, key):
		'''
		Removes the entry from the hash table specified by the key.
		Returns True if found and removed, otherwise False.
		'''

		returnVal = False

		# Generate the hash key from the supplied key and get the linked list at 
		#	that location
		keyHash = self.hash(key)
		linkedList = self.hashTable[keyHash]

		# Iterate over the linked list and look for the node with the original key
		currentNode = linkedList.head
		while (currentNode != None):
			bucket = currentNode.info
			if bucket.key == key:
				linkedList.remove(currentNode)
				returnVal = True
				break
			currentNode = currentNode.next

		return returnVal

	def dump(self):
		''' 
		This method simply dumps the hash table to the console so 
		you can verify the contents look exactly the way you expect and
		you can count and see the collisions if there were any.
		'''
		logging.getLogger().setLevel(logging.DEBUG)

		collisionCount = 0

		for i in range(0, len(self.hashTable)):
			linkedList = self.hashTable[i]
			currentNode = linkedList.head
			currentCollisionCount = 0

			while (currentNode != None):
				bucket = currentNode.info
				logging.debug("hashTable[" + str(i) + "]: key="+str(bucket.key)+", value="+str(bucket.value))
				currentNode = currentNode.next

				if currentNode != None:
					currentCollisionCount += 1

			collisionCount += currentCollisionCount
			i += 1

		logging.debug("Collisions Counted: " + str(collisionCount))






		



