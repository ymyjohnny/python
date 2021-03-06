#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-9
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import difflib,sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except:
    print 'please enter diff.py text1 text2'
    sys.exit()
    
def readline(filename):
    f = open(filename,'r')
    text = f.read().splitlines()
    f.close()
    return text

text1_line = readline(sys.argv[1])
text2_line = readline(sys.argv[2])

d = difflib.HtmlDiff()
filename = textfile1+'-'+textfile2+'.'+'html'
f1 = open(filename,'w')
diff = d.make_file(text1_line,text2_line)
f1.write(diff)
f1.close

