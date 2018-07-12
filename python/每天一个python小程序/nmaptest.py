#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年3月6日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import nmap


host = '10.21.10.250'
ports = range(80,82)
print ports
nm = nmap.PortScanner()

#输出不同颜色
class INFO:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


for  port in ports:
    ret = nm.scan(host, str(port))
    state =  ret['scan'][host]['tcp'][int(port)]['state']
    if state =='open':
            print INFO.OKBLUE+'[*] '+host+ ' tcp/'+  str(port)+" "+state+INFO.ENDC
    else:
            print INFO.WARNING+'[*] '+host+ ' tcp/'+ str(port) +" "+state+INFO.ENDC
