#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


#import ConfigParser
from ConfigParser import SafeConfigParser

cfg = SafeConfigParser()
cfg.read('config.ini')

print cfg.options('sec')

print cfg.get('sec', 'a')
