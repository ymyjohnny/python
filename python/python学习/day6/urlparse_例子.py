#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import urllib
from urlparse import urlparse

def main():
    url = 'http://www.baidu.com#urlparse.urlparse '
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


if __name__ == '__main__':
    main()