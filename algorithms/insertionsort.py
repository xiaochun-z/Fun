#!/usr/bin/env python
#--coding:utf-8--
import unittest

def sort(seq):
	for j in range(1, len(seq)):
		key = seq[j]
		i = j - 1
		while i >= 0 and seq[i] > key:
			seq[i + 1] = seq[i]
			i = i - 1
		seq[i + 1] = key
	return seq

class TestInsertionSort(unittest.TestCase):
	def test_sort_1(self):
		seq = [1,3,2,4,6,5]
		self.assertRange(seq)

	def test_sort_2(self):
		seq = [1,3,3,3,5,6]
		self.assertRange(seq)

	def test_sort_3(self):
		seq = [5,4,3,2,1]
		self.assertRange(seq)

	def test_sort_4(self):
		seq = [1,20,18,5,30]
		self.assertRange(seq)
	
	def test_sort_5(self):
		seq = [1]
		self.assertRange(seq)

	def test_sort_6(self):
		seq = []
		self.assertRange(seq)

	def test_sort_7(self):
		seq = [3,2]
		self.assertRange(seq)

	def assertRange(self, seq):
		seqSorted = sort(seq)
		for x in range(len(seqSorted) - 1):
			self.assertTrue(seqSorted[x] <= seqSorted[x + 1])

if __name__ == '__main__':
	unittest.main()