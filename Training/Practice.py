from functools import reduce
import time, random
import logging
from contextlib import contextmanager


### use dectorator

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'function {func.__name__} takes {end_time-start_time} seconds')
        return result

    return wrapper


def timeit2(logTime):
    def decorator1(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f'function {func.__name__} takes {end_time-start_time} seconds')
            return result

        if logTime:
            return wrapper
        return func

    return decorator1


@timeit2(logTime=True)
def fetch_url(url):
    time.sleep(random.randint(1, 1000) / 1000);
    return 200, 'OK'


@contextmanager
def myopenfile(file, mode):
    f = open(file, mode, encoding='utf8')
    yield f
    f.close()


if __name__ == "__main__":

    with(myopenfile('../README.md', 'r')) as f:
        content = f.read()
        #print(content)

    numbers = [1, 2, 3, 4, 5, 6, 7]
    n = reduce(lambda x, y: x if x < y else y, numbers, 10)
    print(n)
    fetch_url('http://bing.com')

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logging.warning("warn")
    logging.info("info")

    lst = [1, 2, 3, 4, 5]
    lst2 = [6, 7]
    nls = [i ** 2 for i in lst]  # 列表推导式
    print(nls)
    nls2 = list(map(lambda x: x ** 2, lst))
    print(nls2)
    nls3 = [x for x in lst if x % 2 == 0]
    print(nls3)

    nls4 = [x + y for x in lst for y in lst2]
    print(nls4)

    nls = [x + y for x in 'ab' for y in 'yz']
    print(nls)
    nls = [[x + y for x in 'ab'] for y in 'yz']
    print(nls)

    for i in [1, 2]:
        print('hello')
    else:
        print('nothing')
