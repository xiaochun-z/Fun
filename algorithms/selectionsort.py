#!/usr/bin/env python
#--coding:utf-8--
import unittest
from testsortbase import algorithmTest

def sort(seq):
	n = len(seq)
	for j in range(n - 1):
		smallest = j
		for i in range(j + 1, n):
			if seq[i] < seq[smallest]:
				smallest = i
		if smallest != j:
			seq[j], seq[smallest] = seq[smallest], seq[j]
	return seq

class TestSelectionSort(algorithmTest):	
	def assertRange(self, seq):
		seqSorted = sort(seq)
		for x in range(len(seqSorted) - 1):
			self.assertTrue(seqSorted[x] <= seqSorted[x + 1])

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSelectionSort)
	unittest.TextTestRunner(verbosity=2).run(suite)