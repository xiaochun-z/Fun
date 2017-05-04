#!/usr/bin/env python
#--coding:utf-8--
import unittest

'''
loop search
'''
def search(seq, v, low, high):
	while low <= high:
		mid = (low + high) // 2
		if v == seq[mid]:
			return mid
		elif v > seq[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return None

'''
recursive search
'''
def search2(seq, v, low , high):
	if low > high:
		return None
	mid = (low + high) // 2
	if v == seq[mid]:
		return mid
	elif v > seq[mid]:
		return search2(seq, v, mid + 1, high)
	else:
		return search2(seq, v, low, mid - 1)

class TestSearch(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestSearch, self).__init__(*args, **kwargs)
		self.seq = [1,1.4,2,3,4,5,6,7,8,9,10]

	def test_search_should_return_2(self):
		v = 2
		result = search(self.seq, v, 0, len(self.seq))
		self.assertEqual(result, 2)

	def test_search_should_return_10(self):
		v = 10
		result = search(self.seq, v, 0, len(self.seq))
		self.assertEqual(result, 10)

	def test_search_should_return_0(self):
		v = 1
		result = search(self.seq, v, 0, len(self.seq))
		self.assertEqual(result, 0)

	def test_search2_should_return_2(self):
		v = 2
		result = search2(self.seq, v, 0, len(self.seq))
		self.assertEqual(result, 2)

	def test_search2_should_return_10(self):
		v = 10
		result = search2(self.seq, v, 0, len(self.seq))
		self.assertEqual(result, 10)

	def test_search2_should_return_0(self):
		v = 1
		result = search2(self.seq, v, 0, len(self.seq))
		self.assertEqual(result, 0)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
	unittest.TextTestRunner(verbosity=2).run(suite)