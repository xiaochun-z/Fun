#!/usr/bin/env python
# --coding:utf-8--

import requests
from bs4 import BeautifulSoup
from urllib import parse
from urllib.parse import urlparse
import html2text
import os
import re
import json

queue_file = 'queue'
finished_file = 'finished'

SESSION = {}

task_queue = set()
task_check = set()

finished_queue = set()
finished_check = set()


def crawl(url):
    try:
        payload = {}
        headers = {
            'HOST': urlparse(url).netloc,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referrer': url,
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }
        r = requests.get(url, params=payload, headers=headers, timeout=5)
        content = r.content
        text = content.decode(r.encoding)

        encoding = requests.utils.get_encodings_from_content(text)
        if type(encoding) is list and len(encoding) > 0:
            # print(encoding)
            encoding = encoding[0]

        soup = BeautifulSoup(content.decode(encoding), 'lxml')
        return soup
    except Exception as ex:
        print(ex)
        print('retry {}'.format(url))
        return crawl(url)

        # print(soup.prettify())


def buildchapters(base_url, soup):
    getchapters(base_url, soup)
    lastp = base_url
    nextp = getNextPage(base_url, soup)
    if nextp != None:
        lastp = nextp

    while nextp != None:
        soup = crawl(nextp)
        getchapters(base_url, soup)

        nextp = getNextPage(base_url, soup)
        if nextp != None:
            lastp = nextp
        print(nextp)

    SESSION['last_page_url'] = lastp
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_f = os.path.join(dir_path, 'task.json')
    with open(json_f, 'w') as f:
        json.dump(SESSION, f, ensure_ascii=False)


def addChapterToQueue(chapter):
    if (chapter[2] in task_check) == False and (chapter[2] in finished_check) == False:
        task_queue.add(chapter)
        task_check.add(chapter[2])


def getchapters(base_url, soup):
    for c in soup.select('.chapter'):
        links = c.select('a')
        for l in links:
            order = len(finished_check) + len(task_check) + 1
            addChapterToQueue((order, l.text, parse.urljoin(base_url, l['href'])))


def getNextPage(base_url, soup):
    l = soup.find_all(text='下一页')
    if len(l) > 0:
        return parse.urljoin(base_url, l[0].parent['href'])
    return None


def getChapterContent(chapter):
    title, url = chapter[1], chapter[2]
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


def file_to_set(file, queue_set=True):
    r = set()
    with open(file, 'r') as f:
        i = 0
        for l in f:
            l = l.replace('\r', '')
            l = l.replace('\n', '')
            chapter = l.split('∆')
            if len(chapter) != 2:
                continue
            if queue_set:
                r.add((i, chapter[0], chapter[1]))
            else:
                r.add(chapter[1])
            i += 1
    return r


def set_to_file(file, chapter_set):
    with open(file, 'w+') as f:
        for l in sorted(chapter_set, key=lambda k: int(k[0])):
            f.write('{}∆{}\r\n'.format(l[1], l[2]))


def cleanMess(content):
    # remove Ads
    cleaned = re.sub(r'[。](.+((com)|(net)))', '', content)

    # remove space
    cleaned = re.sub(r'^( |[\s　])+$', '', cleaned)
    cleaned = re.sub(r'^( |[\s　])+(\S+)', '\n\\2', cleaned, 0, re.MULTILINE)
    cleaned = re.sub(r'|(\S+)( |[\s　])+$', '\\1', cleaned, 0, re.MULTILINE)

    # add # for chapter title
    cleaned = re.sub(r'^\s+(第.+章)', '# \\1', cleaned)
    # print(cleaned)
    return cleaned


def create_new_file(path):
    with open(path, 'w') as f:
        f.write('')


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_f = os.path.join(dir_path, 'task.json')
    with open(json_f, 'r') as f:
        SESSION = json.load(f)

    dir_path = os.path.join(dir_path, SESSION['title'])
    if os.path.isdir(dir_path) == False:
        os.mkdir(dir_path)

    q_file = os.path.join(dir_path, queue_file)
    f_file = os.path.join(dir_path, finished_file)

    if os.path.exists(q_file) == False:
        create_new_file(q_file)

    if os.path.exists(f_file) == False:
        create_new_file(f_file)

    task_queue = file_to_set(q_file)
    finished_queue = file_to_set(f_file)
    task_check = file_to_set(q_file, False)
    finished_check = file_to_set(f_file, False)

    base_url = SESSION['base_url'] if len(SESSION['last_page_url']) == 0 else SESSION['last_page_url']
    soup = crawl(base_url)
    buildchapters(base_url, soup)
    sortedList = sorted(task_queue, key=lambda k: int(k[0]))
    while sortedList:
        c = sortedList.pop(0)
        getChapterContent(c)
        finished_queue.add(c)
        set_to_file(q_file, sortedList)
        set_to_file(f_file, sorted(finished_queue, key=lambda k: int(k[0])))
