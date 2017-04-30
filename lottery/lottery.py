# /usr/local/bin/python
# coding=utf-8

from random import *

class printer:
	def __init__(self, red):
		self.red = red

	def print_list(self, itemlist, i):
		print("第{}期开奖号码： {}\n".format(i, self.format(itemlist)))

	def print_win(self, n, itemlist):
		print("\r恭喜，你买了 {} 期彩票: {}.\n共计花了 {} 元.\n  共计用了 {:.2f} 年。\r".format(n, self.format(itemlist), n*2, n/156))
	
	def format(self, balls):
		return "{} + {}".format(balls[:self.red], balls[self.red:])

class lottery:
	def __init__(self, printer, balls, red):
		self.balls = sort(balls[0:red]) + sort(balls[red:])
		self.printer = printer
		self.red = red
		self.g = generator(red)

	def getBalls(self):
		return self.balls;

	def generateBalls(self):
		return self.g.generateBalls()

	def draw(self, i = 0):
		llist = self.generateBalls()
		self.printer.print_list(llist, i)
		k = self.compare_ball(llist, self.balls)

		if(k < self.red):
			return k

		k += self.compare_ball(llist, self.balls, False)
		
		return k

	def compare_ball(self, items, compare_list, red = True):
		if red:
			return self.__compare_items(items[:self.red], compare_list[:self.red])
		else:
			return self.__compare_items(items[self.red:], compare_list[self.red:])

	def __compare_items(self, items, compare_list):
		k = 0
		for x in items:
			if x in compare_list:
				k+=1
			else:
				continue
		return k

class generator:
	def __init__(self, red = 5):
		self.red = 5

	def generateBalls(self):
		return self.__generateRed() + self.__generateBlue()

	def __generateRed(self):
		return sort(self.__generate(5, 1, 35))

	def __generateBlue(self):
		return sort(self.__generate(2, 1, 12))

	def __generate(self, length, minNum, maxNum):
		randomlist = []
		for x in range(length):
			while(True):
				n = randint(minNum,maxNum)
				if n not in randomlist:
					randomlist.append(n)
					break
		return randomlist

def sort(seq):
	for n in range(1, len(seq)):
		item = seq[n]
		hole = n
		while hole > 0 and seq[hole - 1] > item:
			seq[hole] = seq[hole - 1]
			hole = hole - 1
		seq[hole] = item
	return seq

		
if __name__ == "__main__":
	balls = [3,4,12,16,28,5,12]
	red = 5
	p = printer(red)
	l = lottery(p, balls, red)
	n = 1;
	while(l.draw(n) < 7):
		n += 1
	
	p.print_win(n, l.getBalls())