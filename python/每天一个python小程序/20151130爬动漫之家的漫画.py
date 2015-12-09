#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-30
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import requests,sys
from bs4 import BeautifulSoup
from os import path
import re

def download(url):
     r = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'
                                       })
     return BeautifulSoup(r.content)
 
def parse_index(url):
     doc = download(url)
     title = doc.select('div  h1')[0].get_text().encode('utf-8')
     for i in doc.select('div  ul li a '):
         if title not in  i.encode('utf-8'):
             continue
         #print i['href'],i['title']
         pagetitle = i['title']
         pageurl =  url+'/'+i['href'].split('/')[2]
         picture = download(pageurl)
         f = open( '%s.txt' % title, 'w')
         #print path.join(path.dirname(url) , i['href'])
         #print i['href']
         
         print  pagetitle,pageurl
         
def main():
    parse_index(sys.argv[1])

if __name__ == '__main__':
    main()
    