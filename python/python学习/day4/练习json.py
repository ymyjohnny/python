#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


import json
import marshal

config = {
          'user' : 'ymy' ,
          'pass'  : 'test123',                 
          }
f = open('config.json', 'w')
json.dump(config, f)
 
f.close()

#f = open('config.json' , 'w')
#marshal.dump(config, f)
# f = open('config.json' )
# config = marshal.load(f)
# marshal.load
# f.close()
# print config['user']
# print config



