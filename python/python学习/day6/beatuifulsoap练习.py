#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


#找出chardet.html中的a标签中的url
#bs4需要另外安装 /home/ymy/python/uplooking/python-bs4_4.3.2-2_all.deb 包

from bs4 import BeautifulSoup

f = open("chardet.html")
soup = BeautifulSoup(f.read())

#print soup.find_all('p')

for link in soup.find_all('a'):
    print link.get('href')

f.close()