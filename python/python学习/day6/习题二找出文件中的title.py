#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


from bs4 import BeautifulSoup


f = open('1643.html')
soup = BeautifulSoup(f.read())
#print soup

def get_urltitle(doc):
    
    title = doc.select('div')[4]
    print title
       


def main():
    get_urltitle(soup)

if __name__ == '__main__':
    main()