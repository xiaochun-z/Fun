#!/usr/bin/env python
#--coding:utf-8--

import requests
from bs4 import BeautifulSoup
from urllib import parse
from urllib.parse import urlparse
import html2text
import os
import re

SESSION = {
			'title':'御天邪神',
			'url':'http://i.258zw.com/wapbook-1852/'
		}
		
def crawl(url):
	try:
		payload = {}
		headers = {
		'HOST':urlparse(url).netloc,
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate, br',
		'Referer':url,
		'Connection':'keep-alive',
		'Cache-Control':'max-age=0'
		}
		r = requests.get(url, params=payload, headers = headers)
		content = r.content
		text = content.decode(r.encoding)

		encoding = requests.utils.get_encodings_from_content(text)
		if type(encoding) is list and len(encoding) > 0:
			#print(encoding)
			encoding = encoding[0]

		soup = BeautifulSoup(content.decode(encoding), 'lxml')
		return soup
	except Exception as ex:
		print(ex)
		print('retry {}'.format(url))
		return crawl(url)

	#print(soup.prettify())

def buildchapters(base_url, soup):
	chapters = getchapters(base_url, soup)
	nextp = getNextPage(base_url, soup)

	while nextp != None:
		soup = crawl(nextp)
		c = getchapters(base_url, soup)
		chapters += c

		nextp = getNextPage(base_url, soup)
		print(nextp)
	return chapters

def getchapters(base_url, soup):
	chapters = []
	for c in soup.select('.chapter'):
		#print(type(c))
		#print(dir(c))
		links = c.select('a')
		for l in links:
			chapters.append((l.text, parse.urljoin(base_url, l['href'])))

	return chapters

def getNextPage(base_url, soup):
	l = soup.find_all(text = '下一页')
	if len(l) > 0:
		return parse.urljoin(base_url,l[0].parent['href'])
	return None

def getChapterContent(title, url):
	soup = crawl(url)
	content = soup.select('#chapterContent')
	if type(content) is list and len(content) > 0:
		content = content[0].decode_contents(formatter="html")

	content = html2text.html2text(content)

	dir_path = os.path.dirname(os.path.realpath(__file__))
	dir_path = os.path.join(dir_path, SESSION['title'])
	if os.path.exists(dir_path) == False:
		os.mkdir(dir_path)

	file_path = os.path.join(dir_path, SESSION['title'] + '.md')
	content = cleanMess(content)
	print(title)
	with open(file_path, 'a') as f:
		f.write(content)

def cleanMess(content):
	# remove Ads
	cleaned = re.sub(r'[。](.+((com)|(net)))','',content)

	# remove space
	cleaned = re.sub(r'^( |[\s　])+$','',cleaned)
	cleaned = re.sub(r'^( |[\s　])+(\S+)','\n\\2',cleaned, 0, re.MULTILINE)
	cleaned = re.sub(r'|(\S+)( |[\s　])+$','\\1',cleaned,0, re.MULTILINE)

	# add # for chapter title
	cleaned = re.sub(r'^\s+(第.+章)','# \\1',cleaned)
	#print(cleaned)
	return cleaned

if __name__ == '__main__':
	#dir_path = os.path.dirname(os.path.realpath(__file__))
	#dir_path = os.path.join(dir_path, SESSION['title'])
	#file_path = os.path.join(dir_path, SESSION['title'] + '.md')
	#content = None
	#with open(file_path,'r') as f:
	#	content = f.read()
	#cleanMess(content)
	#getChapterContent('44', 'http://i.258zw.com/wapbook-1852-621648/')
	
	base_url = SESSION['url']
	soup = crawl(base_url)
	chapters = buildchapters(base_url, soup)
	for c in chapters:
		getChapterContent(c[0], c[1])