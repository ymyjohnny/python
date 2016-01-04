#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import os,sys


def ip_addr_filter(ipaddr):
    ipaddr = sys.argv[1]
    source = os.popen("whois %s'" % ipaddr).read()
    for i in source:
        if i.splitlines().startswith('descr'):
            print i
            
def main():
    ipaddr = sys.argv[1]
    ip_addr_filter(ipaddr)

if __name__ == '__main__':
    main()