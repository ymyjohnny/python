#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''
import sys
import requests
from bs4 import BeautifulSoup
from os import path
import time

def download(url):
    r = requests.get(
                    url, 
                    headers = {
                     'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'
                     })
    return BeautifulSoup(r.content)
    
def  parse_index(url):
    doc = download(url)
    #print doc
    #select 可以逐层查找，比如  doc.select('body div')就是查body下的div层
    title = doc.select('div#title')[0].get_text()
    #print title
    f = open( '%s.txt' % title, 'w')
    for i in doc.select('td.ccss a'):
        pagetitle =  i.get_text()
        pageurl = path.join(path.dirname(url), i['href'])
        print pageurl ,pagetitle
        #抓取各url的正文
        pagecontent = download(pageurl).select('div#content')[0].get_text()
        f.write(pagetitle.encode('utf-8') + '\n')
        f.write(pagecontent.encode('utf-8') + '\n')

def main():
    #输入pageindexurl
    parse_index(sys.argv[1])
    
    

if __name__ == '__main__':
    main()
    

