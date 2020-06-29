'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms

'''
import unittest
from CNDoublyLinkedList import DoublyLinkedList
from CNNode import Node

class Test(unittest.TestCase):


	def setUp(self):
		self.linkedList = DoublyLinkedList()
		self.linkedList.insertInfo("item 1")
		self.linkedList.insert(Node("item 2"))
		self.linkedList.insertInfo("item 3")
		self.linkedList.insert(Node("item 4"))
		self.linkedList.insert(Node("item 5"))

	def tearDown(self):
		self.linkedList = None
		pass


	def testPrint(self, msg="testPrint"):
		print("\n*** Called from test method: " + msg)
		print("  -------- start list ---------  ")
		currentNode = self.linkedList.head
		while (currentNode != None):
			print(currentNode.info)
			currentNode = currentNode.next
		print("^ -------- end of list --------- ^\n")
		pass

	def testPrintReverse(self, msg="testPrintReverse"):
		print("\n*** Called from test method: " + msg)
		print("REVERSE PRINT:")
		print("  -------- end of list ---------  ")
		currentNode = self.linkedList.tail
		while (currentNode != None):
			print(currentNode.info)
			currentNode = currentNode.prev
		print("^ -------- start of list --------- ^\n")
		pass
	
	def testRemove(self):
		currentNode = self.linkedList.head
		while (currentNode != None):
			if (currentNode.info == "item 3"):
				self.linkedList.remove(currentNode)
				break;
			currentNode = currentNode.next
		self.testPrint("testRemove")
		self.testPrintReverse("testRemove")
		
		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item 1", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 5", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemove method failed.")
		
		currentNode = self.linkedList.tail
		self.assertEqual(currentNode.info, "item 5", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 1", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode, None, "testRemove method failed.")
		
		
	def testRemoveHead(self):
		currentNode = self.linkedList.head
		self.linkedList.remove(currentNode)
		
		self.testPrint("testRemoveHead")
		self.testPrintReverse("testRemoveHead")
		
		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 3", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 5", "testRemoveHead method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemove method failed.")

		currentNode = self.linkedList.tail
		self.assertEqual(currentNode.info, "item 5", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 3", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 2", "testRemoveHead method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode, None, "testRemove method failed.")
		
		
	def testRemoveLastNode(self):
		currentNode = self.linkedList.head
		while (currentNode != None):
			if (currentNode.info == "item 5"):
				self.linkedList.remove(currentNode)
				break;
			currentNode = currentNode.next
		self.testPrint("testRemoveLastNode")
		self.testPrintReverse("testRemoveLastNode")
		
		
		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item 1", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 3", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemove method failed.")

		currentNode = self.linkedList.tail
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 3", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 1", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode, None, "testRemove method failed.")
		
		
	def testRemoveTail(self):
		currentNode = self.linkedList.tail
		self.linkedList.remove(currentNode)
		self.testPrint("testRemoveTail")
		self.testPrintReverse("testRemoveTail")

		currentNode = self.linkedList.head
		self.assertEqual(currentNode.info, "item 1", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 3", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.next
		self.assertEqual(currentNode, None, "testRemove method failed.")

		currentNode = self.linkedList.tail
		self.assertEqual(currentNode.info, "item 4", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 3", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 2", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode.info, "item 1", "testRemove method failed.")
		currentNode = currentNode.prev
		self.assertEqual(currentNode, None, "testRemove method failed.")
		

if __name__ == "__main__":
	unittest.main()