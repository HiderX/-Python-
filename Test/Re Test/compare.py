# -*- coding: utf-8 -*-

"""
@Datetime: 2019/3/13
@Author: Zhang Yafei
"""
import functools
import re
import sys
import time

import requests
from bs4 import BeautifulSoup as bs
from lxml.html import fromstring
from pyquery import PyQuery as pq


def timeit(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fun(*args, **kwargs)
        print('运行时间为%.6f' % (time.time() - start_time))
        return res

    return wrapper


@timeit  # time1 = timeit(time)
def time1(n):
    return [i * 2 for i in range(n)]


# ################# start request #################
url = "https://www.taobao.com/"
html = requests.get(url).text
num = 10000
print('\n==== Python version: %s =====' % sys.version)
print('\n==== Total trials: %s =====' % num)


@timeit
def bs4_test():
    soup = bs(html, 'lxml')
    for x in range(num):
        paragraphs = soup.findAll('p')
    print('bs4 total time:')


@timeit
def pq_test():
    d = pq(html)
    for x in range(num):
        paragraphs = d('p')
    print('pq total time:')


@timeit
def lxml_css():
    tree = fromstring(html)
    for x in range(num):
        paragraphs = tree.cssselect('p')
    print('lxml (cssselect) total time:')


@timeit
def lxml_xpath():
    tree = fromstring(html)
    for x in range(num):
        paragraphs = tree.xpath('.//p')
    print('lxml (xpath) total time:')


@timeit
def re_test():
    for x in range(num):
        paragraphs = re.findall('<[p ]>.*?</p>', html)
    print('regex total time:')


if __name__ == '__main__':
    bs4_test()
    pq_test()
    lxml_css()
    lxml_xpath()
    re_test()