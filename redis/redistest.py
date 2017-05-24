#!/usr/bin/env python
#--coding:utf-8--

import redis

def redis_set():
    r = redis.StrictRedis(host='192.168.88.3')
    r.set('greetings', 'hello world')
    if r.exists('count') == False:
        r.set('count', 0)


def redis_hello():
    r = redis.StrictRedis(host='192.168.88.3')
    greetings = r.get('greetings')
    r.incr('count')
    count = r.get('count')

    print('{}:\t{}'.format(greetings, count))


if __name__ == '__main__':
    redis_set()
    redis_hello()