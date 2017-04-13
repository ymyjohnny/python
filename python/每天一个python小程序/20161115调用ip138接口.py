#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-11-15
@author:ymy
Copyright ymyjohnny@gmail.com
'''



import httplib2, urllib

params = urllib.urlencode({'ip':'9.8.8.8','datatype':'jsonp','callback':'find'})
url = 'http://api.ip138.com/query/?'+params
headers = {"token":"8594766483a2d65d76804906dd1a1c6a"}#token为示例
http = httplib2.Http()
response, content = http.request(url,'GET',headers=headers)
print(content)