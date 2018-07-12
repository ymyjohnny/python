#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年2月28日
@author:ymy
Copyright ymyjohnny@gmail.com
'''
import urllib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT   lalalalalalala)'
headers = { 'User-Agent' : user_agent }
url = 'http://www.adsame.com'
data = ""
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
