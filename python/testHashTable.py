'''
Created on Aug 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''

import unittest
from CNHashTable import HashTable

class Test(unittest.TestCase):

	SIZE = 50

	def setUp(self):
		self.table = HashTable(self.SIZE)

	def tearDown(self):
		self.table = None
		pass

	def testHashKeyGeneration(self):
		key = self.table.hash("hello world")
		self.assertLess(key, self.SIZE)

		key = self.table.hash(0x736b831877d84f827ca24ceba37a6697)
		self.assertLess(key, self.SIZE)

		key = self.table.hash("Mr. Smith")
		self.assertLess(key, self.SIZE)

		key = self.table.hash(32767)
		self.assertLess(key, self.SIZE)

	def testSetAndGet(self):
		self.table.set(1234, "1234")
		self.table.set("Steinbeck", "The Grapes of Wrath")
		self.table.set(32767, "32767")
		self.table.set("Dostoyevsky", "The Brothers Karamozov")
		self.table.set(1, "1")
		self.table.set(987654321, "987654321")
		self.table.set("abcdefghijklmnopqrstuvwxyz", "abc")

		value = self.table.get(1234)
		self.assertEqual(value, "1234")
		value = self.table.get(987654321)
		self.assertEqual(value, "987654321")
		value = self.table.get("Dostoyevsky")
		self.assertEqual(value, "The Brothers Karamozov")
		value = self.table.get(987654321)
		self.assertEqual(value, "987654321")

		self.table.dump()

	def testSetAndRemove(self):
		self.table.set(1234, "1234")
		self.table.set("Steinbeck", "The Grapes of Wrath")
		self.table.set(32767, "32767")

		self.assertTrue(self.table.remove("Steinbeck"))
		self.assertFalse(self.table.remove("Steinbeck"))
		

if __name__ == "__main__":
	unittest.main()
