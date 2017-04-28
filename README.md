# Fun
fun programing, some interesting programs

## lottery
a program to test how luck you are, it simulates buying lottery, in China, it calls 大乐透, if you match all the number, you will get 10,000,000 CNY.
let's figure out how long will it take to win the biggest prize.
大乐透模拟，选定一注号码，连续投注，每期都买，看看需要多少年你才能中奖。
要自己选注，修改balls变量，前五个球是红球，后两个是蓝球，我选的号是 3,4,12,16,28 + 5,12。
```python
if __name__ == "__main__":
	balls = [3,4,12,16,28,5,12]
	red = 5
	p = printer(red)
	l = lottery(p, balls, red)
	n = 1;
	while(l.draw(n) < 7):
		n += 1
	
	p.print_win(n, l.getBalls())
```
![screenshot](http://i67.tinypic.com/2ngh8wi.png)

参见文章：[你能中1000万吗](http://1few.com/fun-python-lottery)

