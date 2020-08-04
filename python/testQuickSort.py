'''
Created on Jun 26, 2020

@author: charles newman
https://github.com/26point2Newms
'''
import unittest
import CNQuickSort

class Test(unittest.TestCase):

	def setUp(self):
		self.numbers = [54, 789, 1, 44, 789, 321, 852, 32456, 2, 88, 741, 258, 369, 951, 753]

	def testQuickSort(self):
		print("Before sort:")
		print(self.numbers)
		CNQuickSort.sort(self.numbers)
		print("After sort:")
		print(self.numbers)

		for i in range(len(self.numbers)-1):
			self.assertLessEqual(self.numbers[i], self.numbers[i+1])


if __name__ == "__main__":
	unittest.main()