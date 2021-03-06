#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''

import unittest
import hashlib
import subprocess    


#验证md5是否正确
ALGO = 'md5'
def get_hash(filepath):
    #print filepath
    h = getattr(hashlib, ALGO)()
    fi = open(filepath, 'rb')
    #print fi.read()
    #with open(filepath, 'rb') as fi:
    h.update(fi.read())
    return h.hexdigest()
#print get_hash('/home/ymy/121.txt')
    

class TestDateFilter(unittest.TestCase):

    def test_md5(self):
        source =  (subprocess.check_output(["md5sum","/home/ymy/121.txt"]))
        
        source1 =  source.split()[1]
        #source2 = source.split()[0]
        #print source
        #print get_hash('/home/ymy/121.txt')
        self.assertEqual(get_hash(source1),source.split()[0] )

if __name__ == '__main__':
    unittest.main()
