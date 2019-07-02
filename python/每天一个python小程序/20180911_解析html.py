#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年9月11日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import BeautifulSoup
import urllib2 
from bs4 import BeautifulSoup
from distutils.filelist import findall
 
def process_spark_ui(port):
    data_list = []
    page = urllib2.urlopen('http://192.168.32.170:%s/jobs/' % port) 
    contents = page.read() 
    #print(contents)
    soup = BeautifulSoup(contents,"html.parser")
    for tag in soup.find_all('tr'):  
    #print tag
    #print '================================================'
        tds = tag.find_all('td')
        data_list.append({
                      'id':tds[0].contents[0],
                      'Duration':tds[3].contents[0],
                      })
#print(data_list)

    for i in data_list:
        print i
    
def main():
    port = int(raw_input('portid:\n'))
    process_spark_ui(port)

if __name__ == '__main__':
    main()
    
    
