# /usr/local/bin/python
# coding=utf-8

import unittest
from lottery import *
class nullprinter:
	def __init__(self, red):
		pass

	def print_list(self, itemlist):
		pass

	def print_win(self, n, itemlist):
		pass
	
	def format(self, balls):
		return ''

class TestLottery(unittest.TestCase):
	def setUp(self):
		self.balls = [3,4,12,16,28,5,12]
		red = 5
		p = nullprinter(red)
		self.lottery = lottery(p, self.balls, red)

	def test_compare_red_ball_should_return_5(self):
		ball = [3,4,12,16,28,5,12]
		k = self.lottery.compare_ball(self.balls, ball)
		self.assertEqual(k, 5)

	def test_compare_red_ball_should_return_4(self):
		ball = [3,4,12,13,28,5,12]
		k = self.lottery.compare_ball(self.balls, ball)
		self.assertEqual(k, 4)

	def test_compare_red_ball_should_return_0(self):
		ball = [2, 1, 5, 6, 7, 3, 11]
		k = self.lottery.compare_ball(self.balls, ball)
		self.assertEqual(k, 0)

	def test_compare_red_ball_should_return_2(self):
		ball = [28, 29, 3, 2, 1, 5, 12]
		k = self.lottery.compare_ball(self.balls, ball)
		self.assertEqual(k, 2)

	def test_compare_all_ball_should_return_7(self):
		ball = [3,4,12,16,28,5,12]
		k = self.lottery.compare_ball(self.balls, ball) + self.lottery.compare_ball(self.balls, ball, False)
		self.assertEqual(k, 7)

	def test_compare_blue_ball_should_return_2(self):
		ball = [3,4,12,16,28,5,12]
		k = self.lottery.compare_ball(self.balls, ball, False)
		self.assertEqual(k, 2)

	def test_generateBalls(self):
		length = len(self.lottery.generateBalls())
		self.assertTrue(len, 7)

if __name__ == '__main__':
	unittest.main()
