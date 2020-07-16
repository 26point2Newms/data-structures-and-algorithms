'''
Created on July 15, 2020

@author: charles newman
https://github.com/26point2Newms

'''
import unittest
from CNLRUCache import LRUCache

class Test(unittest.TestCase):

    def setUp(self):
        self.cache = LRUCache(3)

    def testPutAndGet(self):
        failedMsg = "testPutAndGet method failed."

        self.cache.put("A", "abc")
        self.cache.put("B", "bcd")

        item = self.cache.get("A")
        self.assertEqual(item, "abc", failedMsg)

        item = self.cache.get("X")
        self.assertEqual(item, -1, failedMsg)

        self.cache.put("C", "cde")
        self.cache.put("D", "def")
        self.cache.put("E", "efg")

        item = self.cache.get("A")
        # "A" should no longer be cached because we've exceeded our capacity
        self.assertEqual(item, -1, failedMsg)

        item = self.cache.get("C")
        self.assertEqual(item, "cde", failedMsg)

        self.cache.put("A", "abc")
        item = self.cache.get("A")
        self.assertEqual(item, "abc", failedMsg)
        

if __name__ == "__main__":
	unittest.main()
