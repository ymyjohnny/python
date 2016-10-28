#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


#找出bs文档中制定代码段
#bs4需要另外安装 /home/ymy/python/uplooking/python-bs4_4.3.2-2_all.deb 包

from bs4 import BeautifulSoup

f = open('beautifulsoup-doc.html')
soup = BeautifulSoup(f.read())

#class_ 代表区分
for i in soup.find_all('div',class_="highlight-python"):
    print i.get_text()




