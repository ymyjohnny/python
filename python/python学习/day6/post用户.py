#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-29
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import requests


def main():
    r = requests.post(
            "https://www.douban.com/login", 
             data = {'from_email':'ymy',
                              'from_password' :'123',
                              'source': 'index_nav'},
             headers = {
                        'referer'   : 'http://www.douban.com'},
                      
                  )




if __name__ == '__main__':
    main()