#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''

#删除目录下不需要保存的文件。(保存：每个月第一天的，每周第一天的，7天以内的)
#执行方法：python 删除目录下不需要保存的文件.py -l INFO /home/ymy/python/

import datetime
import os
import logging
import sys,getopt

def getfiles(base):
    #print os.listdir(base)
    #result = []
    for filename in os.listdir(base):
        filepath = os.path.join(base, filename)
        #print filepath
        st = os.stat(filepath)
        #print st
        dt = datetime.datetime.fromtimestamp(st. st_mtime)
        #print dt.day
        #print filepath , dt
        #print  filepath, st, dt
        #形成list
        yield filepath,st,dt
        
        
def filter_date(source):
    now = datetime.datetime.now()
    for filepath, st, dt in source:
        if dt.day == 1:
            logging.info('%s is ok' % filepath)
            continue
        if dt.weekday == 0:
            logging.info('%s is ok' % filepath)
            continue
        if (now - dt).days <= 7:
            logging.info('%s is ok' % filepath)
            continue
        #print filepath,dt
        yield filepath
        

        
def main():
    optlist, args = getopt.getopt(sys.argv[1:], 'l:h')
    # l:h   l:表示l后面有参数  h后面没有:表示h后面不跟参数
    print optlist
    print args
    optdict = dict(optlist)
    print optdict
    if '-h' in optdict:
        print main.__doc__
        return

    if '-l' in optdict:
        logging.basicConfig(level=getattr(logging, optdict['-l']))
        
#############以上为打印日志，-l和-h参数##########
    print sys.argv[3:]
    for base in args: 
      source = getfiles(base)
      source = filter_date(source)
      for filepath in source:
            #print 123
            logging.info('%s is deleted.' % filepath)
            # shutil.rmtree(filepath)
    
if __name__ == '__main__':
    main()   
    