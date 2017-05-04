#!/usr/bin/env python
#--coding:utf-8--
import unittest

class algorithmTest(unittest.TestCase):
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
		pass