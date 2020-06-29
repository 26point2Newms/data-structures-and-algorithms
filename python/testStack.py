'''
Created on Jun 25, 2020

@author: charles newman
https://github.com/26point2Newms
'''
import unittest
from CNStack import Stack


class Test(unittest.TestCase):

	def setUp(self):
		self.stack = Stack()
		self.assertNotEqual(self.stack, None, "Stack object creation failed.")
		
		self.stack.push(5)
		self.stack.push("Five")
		self.stack.push('+')
		self.stack.push("a string")
		self.stack.push(32767)

	def tearDown(self):
		self.stack = None
		pass
	
	def testPush(self):
		self.stack.push("one more item")
		self.assertEqual(self.stack.count(), 6, "testPush method failed.")

	def testPop(self):
		item = self.stack.pop()
		self.assertEqual(item, 32767)
		self.assertEqual(self.stack.count(), 4, "testPop method failed.")
		
		item = self.stack.pop()
		self.assertEqual(item, "a string")
		self.assertEqual(self.stack.count(), 3, "testPop method failed.")
		
	def testPeek(self):
		item = self.stack.peek()
		self.assertEqual(item, 32767)
		
	def testEmpy(self):
		while self.stack.count() > 0:
			self.stack.pop()
		self.assertEqual(self.stack.count(), 0, "testPop method failed.")
		item = self.stack.pop()
		self.assertEqual(item, None)
		item = self.stack.peek()
		self.assertEqual(item, None)

if __name__ == "__main__":
	unittest.main()
