'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''
import unittest
from CNQueue import Queue

class Test(unittest.TestCase):

	def setUp(self):
		self.queue = Queue()
		self.assertNotEqual(self.queue, None, "Queue object creation failed.")
		
		self.queue.insert(5)
		self.queue.insert("Five")
		self.queue.insert('+')
		self.queue.insert("a string")
		self.queue.insert(32767)


	def tearDown(self):
		self.queue = None
		pass

	def testInsert(self):
		self.queue.insert("yet another item")
		self.assertEqual(self.queue.count(), 6, "testInsert failed.")

	def testRemove(self):
		item = self.queue.remove()
		self.assertEqual(item, 5, "restRemove failed.")
		
	def testPeek(self):
		item = self.queue.peek()
		self.assertEqual(item, 5)
		


if __name__ == "__main__":
	unittest.main()
