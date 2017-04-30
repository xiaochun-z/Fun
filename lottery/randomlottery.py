# /usr/local/bin/python
# coding=utf-8

from lottery import generator,printer

if __name__ == "__main__":
	red = 5
	g = generator(red)
	p = printer(red)
	print("今天，你应该买这几注彩票：")
	for i in range(5):
		ball = g.generateBalls()
		print(p.format(ball))
