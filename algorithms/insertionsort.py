#!/usr/bin/env python
#--coding:utf-8--
import unittest
from testsortbase import algorithmTest

def sort(seq):
	for j in range(1, len(seq)):
		key = seq[j]
		i = j - 1
		while i >= 0 and seq[i] > key:
			seq[i + 1] = seq[i]
			i = i - 1
		seq[i + 1] = key
	return seq

class TestInsertionSort(algorithmTest):	
	def assertRange(self, seq):
		seqSorted = sort(seq)
		for x in range(len(seqSorted) - 1):
			self.assertTrue(seqSorted[x] <= seqSorted[x + 1])

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInsertionSort)
	unittest.TextTestRunner(verbosity=2).run(suite)