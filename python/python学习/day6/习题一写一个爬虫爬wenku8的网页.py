#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import requests
import sys
from bs4 import BeautifulSoup
from os import path


def download(url):
    r = requests.get(url, headers = {
                              'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'
    })
    return BeautifulSoup(r.content)

def parse_index(url):
    doc = download(url)
    title = doc.select('div#title')[0].get_text()
    fo = open('%s.txt'  % title ,'w')
    for i in doc.select('td.ccss a' ):
        page_title = i.get_text()
        pageurl = path.join(path.dirname(url), i['href'])
        print  '%s %s '   % (pageurl , page_title)
        page_content = download(url).select('div#content')[0].get_text()
        fo.write(page_title.encode('utf-8') + '\n')
        fo.write(page_content.encode('utf-8') + '\n')
        
     
    
def main():
# f = open('1643.html')
# soup = BeautifulSoup(f.read())
    parse_index(sys.argv[1])

if __name__ == '__main__':
    main()
    
    