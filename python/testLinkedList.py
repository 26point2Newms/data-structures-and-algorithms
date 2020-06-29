'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms

'''
import unittest
from CNLinkedList import LinkedList
from CNNode import Node


class Test(unittest.TestCase):


	def setUp(self):
		self.linkedList = LinkedList()
		self.linkedList.insertInfo("item one")
		self.linkedList.insert(Node("item two"))
		self.linkedList.insertInfo("item three")
		self.linkedList.insert(Node("item four"))


	def tearDown(self):
		self.linkedList = None
		pass


	def testPrint(self):
		print("\n  -------- start list ---------  ")
		currentNode = self.linkedList.head
		while (currentNode != None):
			print(currentNode.info)
			currentNode = currentNode.next
		print("^ -------- end of list --------- ^\n")
		pass
	
	def testRemove(self):
		currentNode = self.linkedList.head
		while (currentNode != None):
			if (currentNode.info == "item three"):
				self.linkedList.remove(currentNode)
				break;
			currentNode = currentNode.next
		self.testPrint()
		
		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item one", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item two", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item four", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemove method failed.")
		
	def testRemoveHead(self):
		currentNode = self.linkedList.head
		self.linkedList.remove(currentNode)
		
		self.testPrint()
		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item two", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item three", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item four", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemoveHead method failed.")
		
	def testRemoveLastNode(self):
		currentNode = self.linkedList.head
		while (currentNode != None):
			if (currentNode.info == "item four"):
				self.linkedList.remove(currentNode)
				break;
			currentNode = currentNode.next
		self.testPrint()
		
		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item one", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item two", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item three", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemove method failed.")


if __name__ == "__main__":
	unittest.main()