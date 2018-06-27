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

## algorithms
An algorithm is any well-deﬁned computational procedure that takes some value, or set of values, as input and produces some value, or set of values, as output. An algorithm is thus a sequence of computational steps that transform the input into the output. 
* [insertion sort(插入排序)](http://1few.com/algorithm-insertion-sort/)
* [selection sort(选择排序)](http://1few.com/algorithm-selection-sort/)
* [Binary search(二分查找)](http://1few.com/algorithm-binary-search/)
* [merge sort(归并排序)](http://1few.com/algorithm-merge-sort/)

## 其他内容
* [redis测试](http://1few.com/install-redis-on-centos/)
* mysql测试
* [简单Python爬虫--爬小说:Spider](http://1few.com/python-crawler-v1/)
* [intelliJ IDEA + Spring boot + freemarker + mybatis项目搭建](http://1few.com/spring-boot-freemarker-mybatis-for-beginner)
* [小说章节自动划分](chapter-splitter/CharpterDetector.py)，为了在Sigil里做出有章节的小说，使用Python来自动分割章节和生成目录。
效果
![epub目录效果](chapter-splitter/screenshot.jpg "某本网络小说")