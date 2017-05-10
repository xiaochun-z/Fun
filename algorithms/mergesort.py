#!/usr/bin/env python
#--coding:utf-8--
import math
import unittest
from testsortbase import algorithmTest

def merge(left, right):
	result = []
	n, m = 0, 0
	while n < len(left) and m < len(right):
		if left[n] <= right[m]:
			result.append(left[n])
			n += 1
		else:
			result.append(right[m])
			m += 1
	
	result += left[n:]
	result += right[m:]
	return result


def sort(seq):
	if len(seq) <= 1:
		return seq

	middle = len(seq) // 2
	left = sort(seq[:middle])
	right = sort(seq[middle:])
	return merge(left, right)

class TestMergeSort(algorithmTest):	
	def assertRange(self, seq):
		seqSorted = sort(seq)
		for x in range(len(seqSorted) - 1):
			self.assertTrue(seqSorted[x] <= seqSorted[x + 1])

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestMergeSort)
	unittest.TextTestRunner(verbosity=2).run(suite)
