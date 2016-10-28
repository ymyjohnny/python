#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


#test.domain/add?a=1&b=2
#算出1加到10

import urllib
import urlparse

l = range(1,11)
for i in range(1,10): print 'http://test.domain/add?' + urllib.urlencode({'a': sum(l[:i]), 'b' : l[i]})