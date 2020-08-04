'''
Created on Aug 3, 2020

@author: charles newman
https://github.com/26point2Newms

'''
import unittest
from CNBinaryTree import BinaryTree

class Test(unittest.TestCase):

	def setUp(self):
		self.tree = BinaryTree()

	def tearDown(self):
		self.tree = None
		pass

	def testInsert(self):
		errorMsg = "testInsert method failed."

		self.tree.insert(15)
		self.assertEqual(self.tree.size, 1, errorMsg)
		self.tree.insert(7)
		self.assertEqual(self.tree.size, 2, errorMsg)
		self.tree.insert(25)
		self.assertEqual(self.tree.size, 3, errorMsg)

	def testFind(self):
		errorMsg = "testFind method failed"

		item = self.tree.find(15)
		self.assertEqual(item, None, errorMsg)

		self.tree.insert(77)
		self.tree.insert(7)
		self.tree.insert(32)
		self.tree.insert(9)
		self.tree.insert(45)
		self.tree.insert(16)

		item = self.tree.find(9)
		self.assertEqual(item, 9, errorMsg)
		
	def testTraverse(self):
		self.tree.insert(10)
		self.tree.insert(7)
		self.tree.insert(102)
		self.tree.insert(322)
		self.tree.insert(9)
		self.tree.insert(45)
		self.tree.insert(16)

		self.tree.traverse(self.printNode)


	def printNode(self, info):
		print(str(info) + ", ")

if __name__ == "__main__":
	unittest.main()
