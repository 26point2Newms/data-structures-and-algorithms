'''
Created on Aug 4, 2020

@author: charles newman
https://github.com/26point2Newms
'''
import unittest
import CNQuickSort
from CNBinarySearch import BinarySearch

class Test(unittest.TestCase):

	def setUp(self):
		self.numbers = [54, 789, 1, 44, 789, 321, 852, 32456, 2, 88, 741, 258, 369, 951, 753]

	def testBinarySearch(self):
		# First we need to sort the array
		CNQuickSort.sort(self.numbers)
		# Now let's search for this value
		targetVal = 741
		binSearch = BinarySearch(self.numbers, targetVal)

		print("searching for the value: " + str(targetVal))
		print("in this array: ")
		print(self.numbers)

		index = binSearch.search()
		print("Found value at index = " + str(index) + " value = " + str(self.numbers[index]))
		self.assertEqual(self.numbers[index], targetVal)

if __name__ == "__main__":
	unittest.main()
