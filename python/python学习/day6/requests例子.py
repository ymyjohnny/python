#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import requests

r = requests.get('http://www.baidu.com/login', data = {'username': ' ymy' })
r.status_code

r.text

with open()

## cn.python-requests.org