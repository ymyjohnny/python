#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2015-11-23
@author: Shell.Xu
@copyright: 2015, Shell.Xu <shell909090@gmail.com>
@license: cc
'''
import urllib
from urlparse import urlparse

def main():
    url = 'https://docs.python.org/2/library/urlparse.html#urlparse.urlparse'
    u = urlparse(url)
    print u
    print 'host:', u.netloc
    print 'path:', u.path
    print 'fragment:', u.fragment

    form = {
        'username': 'shell',
        'password': 'abc'}
    print urllib.urlencode(form)

    content = urllib.urlopen(url).read()
    print len(content)

if __name__ == '__main__': main()

